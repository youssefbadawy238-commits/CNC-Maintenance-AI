
import streamlit as st
from rag import final_rag

st.set_page_config(
    page_title="CNC Maintenance AI",
    page_icon="⚙️"
)

st.title("⚙️ CNC Maintenance AI Assistant")

st.write(
    "Ask a question about the Haas CNC machine."
)

question = st.text_input(
    "Maintenance Question:"
)

if st.button("Ask"):

    if question.strip():

        with st.spinner("Thinking..."):

            result = final_rag(question)

        st.subheader("Fault")
        st.write(result["fault"])

        st.subheader("Solution")
        st.write(result["solution"])

    else:

        st.warning("Please enter a question.")
