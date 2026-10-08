
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig
)

from langchain_core.language_models.llms import LLM
from langchain_core.prompts import PromptTemplate

from langchain_classic.output_parsers import (
    StructuredOutputParser,
    ResponseSchema
)

from typing import Any
import torch


# Load PDF
pdf_path = "/kaggle/input/datasets/youssefbadawy112/haas-pdf/haas_manual.pdf.pdf"

loader = PyPDFLoader(pdf_path)
documents = loader.load()


# Split text
text_splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)


# Embeddings + FAISS
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectordb = FAISS.from_documents(
    chunks,
    embedding
)


# Load Mistral
model_name = "mistralai/Mistral-7B-Instruct-v0.2"

bnb_cfg = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.bfloat16
)

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=bnb_cfg,
    device_map="auto"
)


# Custom LLM
class CustomHFLLM(LLM):

    def _call(self, prompt: str, stop: Any = None) -> str:

        inputs = tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=4096
        ).to(model.device)

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=200,
                do_sample=False
            )

        answer = tokenizer.decode(
            outputs[0][inputs["input_ids"].shape[1]:],
            skip_special_tokens=True
        )

        return answer.strip()

    @property
    def _llm_type(self) -> str:
        return "custom_huggingface"


llm = CustomHFLLM()


# Output Parser
fault_schema = ResponseSchema(
    name="fault",
    description="The identified CNC machine fault or maintenance issue."
)

solution_schema = ResponseSchema(
    name="solution",
    description="The recommended maintenance action or solution for the CNC machine issue."
)

response_schemas = [
    fault_schema,
    solution_schema
]

output_parser = StructuredOutputParser.from_response_schemas(
    response_schemas
)

format_instructions = output_parser.get_format_instructions()


# Prompt
maintenance_parser_template = """
You are an industrial CNC maintenance assistant.

Based ONLY on the provided context, identify the CNC maintenance issue
and give the recommended solution.

Context:
{context}

Question:
{question}

Respond ONLY in the following format:
{format_instructions}
"""

parser_prompt = PromptTemplate(
    template=maintenance_parser_template,
    input_variables=[
        "context",
        "question",
        "format_instructions"
    ]
)


# Final RAG
def final_rag(query):

    docs = vectordb.similarity_search(query, k=3)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    formatted_prompt = parser_prompt.format(
        context=context,
        question=query,
        format_instructions=format_instructions
    )

    response = llm.invoke(formatted_prompt)

    output_data = output_parser.parse(response)

    return output_data
