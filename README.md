# 🚀 Tips Hindawi Internship (August–October) 2026

> 🎓 This project was built during the **Tips Hindawi Internship (August–October) 2026**.

---

## 👤 Participant

| Field | Value |
| ----- | ----- |
| Full Name | Youssef Osama Elbadawy |
| Project Name | Industrial CNC Maintenance AI Assistant |
| GitHub Username | youssefbadawy238-commits |
| Internship Batch | August–October 2026 |
| Training Program | Large Language Models (LLMs) Program |
| Organization | Edrak for Ai |

---

# 📖 Project Overview

The **Industrial CNC Maintenance AI Assistant** is an AI-powered assistant designed to help users identify and solve CNC machine maintenance problems.

The system uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from the Haas CNC Operator's Manual and provide a maintenance answer using the **Mistral 7B Instruct** language model.

The assistant identifies the maintenance fault and provides a recommended solution based on the retrieved information from the manual.

### Project Pipeline

**PDF → Text Splitting → Embeddings → FAISS → Mistral 7B → Structured Output Parser → Streamlit → ngrok**

---

# ✨ Features

- Ask questions about Haas CNC machine maintenance.
- Retrieve relevant information from the Haas CNC Operator's Manual.
- Use document embeddings for semantic search.
- Use FAISS as the vector database.
- Use Mistral 7B Instruct for answer generation.
- Identify the CNC maintenance fault.
- Provide a recommended maintenance solution.
- Return structured output containing the fault and solution.
- Interactive web interface using Streamlit.
- Public access through ngrok during an active Kaggle session.

---

# 🛠️ Technologies Used

- Python
- LangChain
- FAISS
- Hugging Face Transformers
- Sentence Transformers
- Mistral 7B Instruct
- BitsAndBytes
- 4-bit Quantization
- Streamlit
- ngrok
- Kaggle GPU
- PyPDF

### Embedding Model

`sentence-transformers/all-MiniLM-L6-v2`

### Language Model

`mistralai/Mistral-7B-Instruct-v0.2`

---

# ⚙️ Installation

The project was developed and tested using **Kaggle GPU** because the Mistral 7B model requires GPU resources.

### Step 1 — Download the Repository

Download or clone this GitHub repository.

### Step 2 — Open the Notebook in Kaggle

Open:

`CNC_Maintenance_Final_Lab.ipynb`

using Kaggle.

### Step 3 — Enable GPU

In Kaggle, go to:

**Settings → Accelerator → GPU**

and select a GPU accelerator.

### Step 4 — Add the Haas CNC Manual

The project requires the **Haas CNC Operator's Manual PDF** as the knowledge source for the RAG system.

Upload or add the Haas CNC Operator's Manual PDF to the Kaggle environment using **Add Data**.

The original development path was:

`/kaggle/input/datasets/youssefbadawy112/haas-pdf/haas_manual.pdf.pdf`

This path is specific to the original Kaggle environment and should not be used by other users.

The current `rag.py` automatically searches inside:

`/kaggle/input/`

for PDF files.

Therefore, users do not need to use the original author's Kaggle path.

If automatic detection is not used, update the `pdf_path` variable in the **Load Haas Manual** cell to match the actual location of the uploaded PDF.

Example:

```python
pdf_path = "/kaggle/input/your-dataset-name/haas_manual.pdf"
```

### Step 5 — Run the Notebook

Run the notebook cells from top to bottom.

The notebook will:

1. Install the required libraries.
2. Load the Haas CNC Operator's Manual.
3. Split the PDF into text chunks.
4. Generate embeddings.
5. Build the FAISS vector database.
6. Load Mistral 7B.
7. Apply 4-bit quantization.
8. Create the RAG pipeline.
9. Create the Structured Output Parser.
10. Create the Streamlit application.
11. Start the Streamlit server.
12. Create an ngrok tunnel for public access.

---

# 🚀 Usage

After successfully running the notebook, the Streamlit application provides a web interface for asking CNC maintenance questions.

### Using the Application

1. Run the complete notebook in Kaggle.
2. Make sure the Streamlit application is running.
3. Open the generated Streamlit/ngrok URL shown by the notebook.
4. Enter a CNC maintenance question in the **Maintenance Question** field.
5. Click the **Ask** button.
6. The system retrieves relevant information from the Haas CNC Operator's Manual.
7. The application displays the **Fault** and **Solution**.

### Example

**Question:**

> The spindle has been idle for more than 4 days. What should I do?

**Fault:**

> Idle spindle for more than 4 days

**Solution:**

> Run the spindle warm-up program (O09220) before using the machine.

### Another Example

**Question:**

> The coolant level is low. What should I do?

The system retrieves the relevant information from the Haas manual and provides the recommended maintenance action.

---

# 📸 Demo

The project includes a **Streamlit web interface** for interacting with the CNC Maintenance AI Assistant.

The application can be launched through the Kaggle notebook using **Streamlit and ngrok**.

> **Note:** The ngrok public URL is temporary and is only available while the Kaggle session, Streamlit server, and ngrok tunnel are running.

---

# 📈 Results

The RAG-based CNC Maintenance AI Assistant was successfully implemented and tested using the Haas CNC Operator's Manual.

The system was able to:

- Retrieve relevant information from the manual.
- Identify CNC maintenance issues.
- Generate recommended maintenance solutions.
- Return structured responses containing the **Fault** and **Solution**.

Example test cases included:

- Spindle idle for more than 4 days.
- Low coolant level.

---

# 🔮 Future Improvements

- Add additional CNC machine manuals.
- Support multiple CNC machine manufacturers.
- Improve document retrieval accuracy.
- Improve chunking and retrieval strategies.
- Add conversation history.
- Improve the Streamlit user interface.
- Add a larger evaluation dataset.
- Add automated evaluation metrics.
- Deploy the application on a permanent cloud platform.
- Explore domain-specific fine-tuning for CNC maintenance.

---

# 📚 About the Internship

This project was developed as part of the **Tips Hindawi Internship (August–October 2026)** and the **Large Language Models (LLMs) Program**.

The internship encourages participants to build real-world projects, apply practical skills, and showcase their work through GitHub.

This project demonstrates the practical application of Large Language Models, Retrieval-Augmented Generation, vector databases, document retrieval, structured output parsing, and AI-powered interfaces.

---

# 📄 License

This project is shared for educational and portfolio purposes.
