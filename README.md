# 🏥 Agentic Hospital Booking System

An enterprise-grade **Multi-Agent AI Hospital Booking Assistant** built using  **LangGraph** ,  **HuggingFace Llama 3.1** ,  **Streamlit** , and  **CSV-based healthcare datasets** .

The system leverages specialized AI agents for appointment management, patient information retrieval, and medical knowledge assistance through WHO/WebMD-powered Retrieval Augmented Generation (RAG).

---

# 🚀 Features

## 🤖 Multi-Agent Architecture

### Supervisor Agent

Responsible for:

* Intent detection
* Agent routing
* Tool selection
* Workflow orchestration

### Reader Agent

Provides read-only access to hospital data.

Supported capabilities:

* Get available appointment slots
* Check slot availability
* View patient details
* View appointment details
* List patients
* Retrieve appointment history
* View upcoming appointments

### Writer Agent

Responsible for appointment management.

Supported capabilities:

* Book appointment
* Cancel appointment
* Reschedule appointment

### Medical Agent

Provides healthcare information through:

* WHO search
* WebMD search
* Medical question answering
* Retrieval-Augmented Generation (RAG)

### Sample Questions

**Reader Agent:**

* Show available slots
* List patients
* Show patient details P100
* Show appointments for patient P100
* Check slot S200
* Show upcoming appointments

**Writer Agent**

* Book appointment for patient P100 slot S200
* Cancel appointment A100
* Reschedule appointment A100 to slot S300

**Medical Agent**

* What are the symptoms of diabetes?
* What does WHO recommend for hypertension?
* What is asthma?
* How can diabetes be prevented?

### **🔄 LangGraph Workflow**

START

  │

  ▼

Supervisor Agent

  │

  ├──── READ ─────► Reader Agent

  │

  ├──── WRITE ────► Writer Agent

  │

  └──── MEDICAL ─► Medical Agent

                          │

                          ▼

                    WHO/WebMD Search

                          │

                          ▼

                    HuggingFace LLM

  ▼

END

### 🛠️ Technology Stack

| Layer           | Technology            |
| --------------- | --------------------- |
| UI              | Streamlit             |
| Agent Framework | LangGraph             |
| LLM             | HuggingFace Llama 3.1 |
| Orchestration   | LangChain             |
| Storage         | CSV                   |
| Data Processing | Pandas                |
| Search          | DuckDuckGo Search     |
| Vector DB       | ChromaDB              |
| Embeddings      | Sentence Transformers |
| Configuration   | Python Dotenv         |

👨‍💻 Author

**Raghavendra Oruganti**

Enterprise Agentic AI | Generative AI | LangGraph | Healthcare AI
