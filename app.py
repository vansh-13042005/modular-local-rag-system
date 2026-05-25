import os
import streamlit as st

from ingest import run_ingestion
from ask import (
    load_model,
    load_index,
    answer_query
)


# ---------------------------------
# Page Config
# ---------------------------------

st.set_page_config(
    page_title="Modular Local RAG",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Modular Local RAG System")
st.markdown("Upload a PDF and chat with it locally using TinyLlama.")


# ---------------------------------
# Session State
# ---------------------------------

if "model" not in st.session_state:
    st.session_state.model = load_model()

if "index" not in st.session_state:
    st.session_state.index = None

if "chunks" not in st.session_state:
    st.session_state.chunks = None


# ---------------------------------
# Upload PDF
# ---------------------------------

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    os.makedirs("data", exist_ok=True)

    pdf_path = os.path.join("data", uploaded_file.name)

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Processing PDF and building index..."):

        chunk_count = run_ingestion(pdf_path)

        index, chunks = load_index()

        st.session_state.index = index
        st.session_state.chunks = chunks

    st.success(f"PDF indexed successfully ({chunk_count} chunks)")


# ---------------------------------
# Question Input
# ---------------------------------

query = st.text_input("Ask a question")

if query:

    if st.session_state.index is None:

        st.warning("Please upload a PDF first.")

    else:

        with st.spinner("Generating answer..."):

            answer = answer_query(
                query=query,
                model=st.session_state.model,
                index=st.session_state.index,
                chunks=st.session_state.chunks
            )

        st.markdown("### AI Answer")
        st.write(answer)