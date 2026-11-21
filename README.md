# AI_Palmistry_RAG

# 🔮 Palmistry Assistant

A Streamlit-based Palmistry Assistant that analyzes uploaded palm images and provides palmistry-related observations and personalized answers using image analysis, semantic retrieval, and a palmistry knowledge base.

## 🚀 Features

- 📷 Upload a palm image
- 🔍 Analyze visible palm features
- ✋ Identify major palm lines and mounts
- 💬 Ask natural-language questions about the palm
- 📚 Retrieve relevant information from a palmistry knowledge base
- 🧠 Generate contextual responses based on retrieved knowledge
- 📄 Generate a professionally designed PDF report
- 🎨 Purple and gold themed user interface
- 📊 Admin Dashboard for application statistics
- 🗃️ SQLite-based application activity storage

## 🛠️ Tech Stack

- **Python** – Application development
- **Streamlit** – Web application interface
- **OpenAI Vision** – Palm image analysis
- **OpenAI Embeddings** – Text vector representation
- **LangChain** – LLM and retrieval workflow
- **FAISS** – Semantic similarity search
- **PyPDF** – PDF document processing
- **ReportLab** – Professional PDF report generation
- **SQLite** – Application activity and session storage
- **python-dotenv** – Environment variable management

## 🏗️ Architecture

```text
                    ┌──────────────────────┐
                    │       User           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Streamlit UI       │
                    └──────────┬───────────┘
                               │
                    Upload Palm Image
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Image Analysis     │
                    │   OpenAI Vision      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Palm Observations    │
                    │                      │
                    │ Life Line            │
                    │ Head Line            │
                    │ Heart Line           │
                    │ Fate Line            │
                    │ Sun Line             │
                    │ Marriage Lines       │
                    │ Mounts               │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    User Question     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  FAISS Retrieval     │
                    │                      │
                    │ Palmistry Knowledge  │
                    │ Base                 │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Contextual Response  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   PDF Report         │
                    │   ReportLab          │
                    └──────────────────────┘
```

## 📂 Project Structure

```text
AI_palmistry_rag_assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── config/
│   └── settings.py
│
├── data/
│   └── palmistry.pdf
│
├── database/
│   └── ...
│
├── reports/
│
├── uploads/
│
├── vectorstore/
│
├── ui/
│   └── theme.py
│
└── src/
    ├── loader.py
    ├── splitter.py
    ├── embeddings.py
    ├── retriever.py
    ├── rag_chain.py
    ├── prompt.py
    ├── report.py
    ├── utils.py
    ├── vision.py
    └── database.py
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/v1i1n1/AI_palmistry_rag_assistant.git
```

### 2. Navigate to the Project

```bash
cd AI_palmistry_rag_assistant
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
```

**Important:** Never commit the `.env` file to GitHub.

The `.env` file should be included in `.gitignore`.

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 🔄 Application Workflow

1. The user uploads a palm image.
2. The image is analyzed to identify visible palm features.
3. Major palm characteristics are extracted.
4. The user can select a suggested question or enter a custom question.
5. Relevant information is retrieved from the palmistry knowledge base.
6. The retrieved information and palm observations are used to generate a contextual response.
7. The user can generate a professionally designed PDF report.
8. Application activity is stored in SQLite for administrative statistics.

## ✋ Palm Analysis

The application analyzes visible palm characteristics including:

- **Life Line**
- **Head Line**
- **Heart Line**
- **Fate Line**
- **Sun Line**
- **Marriage Lines**
- **Mounts**
- **Additional Observations**

These observations provide context for answering questions related to the uploaded palm.

## 📚 Knowledge Retrieval Pipeline

The knowledge retrieval process consists of:

```text
Palmistry PDF
      ↓
Document Loading
      ↓
Text Splitting
      ↓
Embedding Generation
      ↓
FAISS Vector Store
      ↓
Semantic Similarity Search
      ↓
Relevant Knowledge
      ↓
Contextual Response
```

### Retrieval Components

**Document Loader**

Loads the palmistry knowledge PDF.

**Text Splitter**

Breaks the document into smaller chunks suitable for retrieval.

**Embeddings**

Converts text chunks into numerical vector representations.

**FAISS**

Stores and searches the vectors using semantic similarity.

**Retriever**

Finds the most relevant knowledge for the user's question.

**Response Generation**

Combines the retrieved knowledge with the palm observations and user question to generate the response.

## 📄 PDF Report

The application generates a professionally designed PDF report containing:

- Report information
- Uploaded palm image
- Palm observations
- User question
- Palmistry interpretation
- Final response
- Disclaimer

The report uses a customized purple and gold theme.

## 📊 Admin Dashboard

The application includes an Admin Dashboard containing application-level statistics such as:

- Registered users
- Questions asked
- Total sessions
- Today's sessions
- Reports generated
- Overall activity

## 🗄️ Database

SQLite is used for storing application activity and session-related information.

The database supports:

- User activity tracking
- Session information
- Question tracking
- Report tracking
- Administrative statistics

## 🎨 User Interface

The application provides a clean, themed interface containing:

- Palm image upload
- Palm observations
- Suggested questions
- Custom question input
- Palmistry response
- PDF report generation
- Admin Dashboard

The interface intentionally keeps the user experience simple and focused on palm observation and questions.

## 📸 Screenshots

### Home Page

_Add screenshot here_

### Palm Analysis

_Add screenshot here_

### Suggested Questions

_Add screenshot here_

### Palmistry Response

_Add screenshot here_

### PDF Report

_Add screenshot here_

### Admin Dashboard

_Add screenshot here_

## 🔐 Security

API credentials are stored using environment variables.

The following files and directories should not be committed:

```text
.env
venv/
__pycache__/
*.pyc
```

Never expose API keys in source code or public repositories.

## ⚠️ Disclaimer

Palmistry is a traditional interpretative practice and is not scientifically validated.

The observations and interpretations provided by this application are intended for informational and entertainment purposes only.

## 🔮 Future Enhancements

- ☁️ Cloud deployment
- 🔐 User authentication
- 🌐 Multi-language support
- ✋ Advanced palm landmark detection
- 📱 Mobile-friendly interface
- 📊 Advanced analytics
- 💾 Cloud-based persistent storage
- 📄 Further PDF customization
- 🚀 Production deployment

## 👨‍💻 Author

**Vinayaka Pallakki**



## ⭐ Support

If you find this project useful, please consider giving the repository a ⭐ on GitHub.
