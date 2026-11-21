import os
from dotenv import load_dotenv

# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()

# ==========================================================
# OpenAI Configuration
# ==========================================================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY not found. Please check your .env file."
    )

# ==========================================================
# Models
# ==========================================================

LLM_MODEL = "gpt-4.1-mini"

VISION_MODEL = "gpt-4.1-mini"

EMBEDDING_MODEL = "text-embedding-3-small"

# ==========================================================
# RAG Configuration
# ==========================================================

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

TOP_K_RESULTS = 4

# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_DIR = os.path.join(BASE_DIR, "data")

UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")

VECTOR_DB_DIR = os.path.join(BASE_DIR, "vectorstore")

REPORT_DIR = os.path.join(BASE_DIR, "reports")

PDF_PATH = os.path.join(
    DATA_DIR,
    "palmistry.pdf",
)

# ==========================================================
# Create Required Directories
# ==========================================================

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(VECTOR_DB_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)