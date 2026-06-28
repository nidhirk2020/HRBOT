# HR Policy RAG Chatbot

A Retrieval-Augmented Generation (RAG) application that answers employee HR policy questions using HR policy documents.

## Features

- Reads HR policy PDFs
- Splits documents into chunks
- Creates embeddings using Hugging Face
- Stores embeddings in ChromaDB
- Retrieves relevant document sections
- Generates answers using Groq (Llama 3.3)

---

## Tech Stack

- Python
- LangChain
- ChromaDB
- Hugging Face Embeddings
- Groq (Llama 3.3)
- PyPDF

---

## Project Structure

```
HR-RAG/
│
├── Data/
├── chroma_db/
├── app.py
├── config.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Prerequisites

- Python 3.11 or 3.12
- Git
- Groq API Key

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd HR-RAG
```

Create a virtual environment

```bash
python3 -m venv venv
```

Activate it

Mac/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a file named `.env`

Add your Groq API key

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Add Documents

Place your HR policy PDFs inside the `Data/` folder.

Example:

- Employee_Handbook.pdf
- Leave_Policy.pdf
- Work_From_Home.pdf
- Benefits.pdf

---

## Run the Project

```bash
python app.py
```

The application will prompt you to enter a question.

Example

```
Ask your HR question:
How many casual leaves do I get?
```

---

## Example Questions

- How many casual leaves do I get?
- Can I carry forward earned leave?
- What is the work-from-home policy?
- What is the reimbursement policy?
- What are maternity leave benefits?

---

## Notes

- The vector database is created automatically if it does not already exist.
- If you modify or add PDFs, delete the `chroma_db/` folder and rerun the application to rebuild the vector database.

---

## Future Improvements

- Streamlit web interface
- Chat history
- Source citations
- Multi-document support
- Conversation memory
