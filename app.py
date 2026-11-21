# ======================================================
# Imports
# ======================================================

import os
import uuid
import random
from datetime import datetime


import streamlit as st

from config.settings import (
    UPLOAD_DIR,
    LLM_MODEL,
)

from src.utils import RAGInitializer
from src.retriever import RetrieverManager
from src.vision import PalmVisionAnalyzer
from src.rag_chain import PalmistryRAG
from src.report import ReportGenerator
from src.database import DatabaseManager

from ui.theme import (
    apply_theme,
    apply_cosmic_background,
    apply_mystical_effects,
    add_cosmic_decorations,
    add_palmistry_decoration,
    apply_sidebar_theme,
    add_mystical_header,
    apply_dashboard_theme,

)


# ======================================================
# Streamlit Configuration
# ======================================================

st.set_page_config(
    page_title="Palmistry Assistant",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="locked",
)

# ======================================================
# Custom CSS
# ======================================================

st.markdown(
    """
<style>

/* Background */

.stApp{
    background:#F4F8FC;
}

/* Metric Cards */

div[data-testid="metric-container"]{

    background:white;

    border:1px solid #D9EAF7;

    padding:15px;

    border-radius:15px;

    box-shadow:0px 4px 12px rgba(0,0,0,0.08);

}

/* Buttons */

.stButton>button{

    width:100%;

    height:50px;

    border-radius:12px;

    font-size:17px;

    font-weight:bold;

}

/* Textbox */

.stTextInput>div>div>input{

    border-radius:10px;

}

/* File Uploader */

section[data-testid="stFileUploader"]{

    border:2px dashed #4A90E2;

    border-radius:12px;

    padding:12px;

}

/* Sidebar */

section[data-testid="stSidebar"]{

    background:#EDF4FB;

}

</style>
""",
    unsafe_allow_html=True,
)

# ======================================================
# Apply Application Theme
# ======================================================

apply_theme()

apply_cosmic_background()

apply_mystical_effects()

add_cosmic_decorations()

add_palmistry_decoration()

apply_sidebar_theme()

add_mystical_header()

apply_dashboard_theme()

# ======================================================
# Project Header
# ======================================================


# ======================================================
# Session State
# ======================================================

if "vision_result" not in st.session_state:
    st.session_state.vision_result = None

if "retriever" not in st.session_state:
    st.session_state.retriever = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "image_path" not in st.session_state:
    st.session_state.image_path = None

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if "session_id" not in st.session_state:
    st.session_state.session_id = (
        f"PA-{datetime.now().strftime('%Y%m%d')}-{random.randint(1000,9999)}"
    )


# ======================================================
# Initialize RAG
# ======================================================

if st.session_state.retriever is None:

    with st.spinner("Loading Palmistry Knowledge Base..."):

        initializer = RAGInitializer()

        vectorstore = initializer.initialize()

        retriever = RetrieverManager(
            vectorstore
        ).get_retriever()

        st.session_state.retriever = retriever


# ======================================================
# Create Objects
# ======================================================

vision = PalmVisionAnalyzer()

rag = PalmistryRAG(
    st.session_state.retriever
)

report = ReportGenerator()

database = DatabaseManager()

# ======================================================
# Admin Statistics
# ======================================================

total_users = database.get_total_users()
total_sessions = database.get_total_sessions()
total_questions = database.get_total_questions()
total_reports = database.get_total_reports()
today_sessions = database.get_today_sessions()

st.divider()

# ======================================================
# Admin Dashboard Toggle
# ======================================================

with st.expander(
    "🔐 Admin Dashboard",
    expanded=False
):

    st.markdown(
        "### 📊 Application Statistics"
    )

    admin_col1, admin_col2 = st.columns(2)

    with admin_col1:

        st.metric(
            "👤 Registered Users",
            total_users
        )

        st.metric(
            "💬 Questions Asked",
            total_questions
        )

        st.metric(
            "📅 Today's Sessions",
            today_sessions
        )

    with admin_col2:

        st.metric(
            "🖐 Total Sessions",
            total_sessions
        )

        st.metric(
            "📄 Reports Generated",
            total_reports
        )

        st.metric(
            "📈 Total Activity",
            total_sessions + total_questions
        )

# ======================================================
# Sidebar
# ======================================================

with st.sidebar:

    st.header("👤 User Information")

    user_name = st.text_input(
        "Enter Your Name",
        value=st.session_state.user_name,
        placeholder="Example : Vinodh Raj"
    )

    st.session_state.user_name = user_name

    st.divider()

    st.header("📤 Upload Palm")

    uploaded_file = st.file_uploader(
        "Choose Palm Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:

        image_path = os.path.join(

            UPLOAD_DIR,

            f"{uuid.uuid4()}_{uploaded_file.name}"

        )

        with open(
            image_path,
            "wb"
        ) as file:

            file.write(
                uploaded_file.getbuffer()
            )

        st.session_state.image_path = image_path

        st.success(
            "Image Uploaded Successfully"
        )

        st.image(
            image_path,
            caption="Uploaded Palm",
            use_container_width=True,
        )

# ======================================================
# Analyze Palm
# ======================================================

    st.divider()

    analyze_button = st.button(

        "🚀 Analyze Palm",

        type="primary",

        use_container_width=True,

    )

st.divider()

# ======================================================
# MAIN PAGE ADMIN NAVIGATION
# ======================================================

admin_button = st.button(
    "⚙️ Admin Dashboard",
    use_container_width=True,
)

if admin_button:
    st.session_state.show_admin = True
    st.rerun()


# ======================================================
# Palm Analysis
# ======================================================

if analyze_button:

    if not st.session_state.user_name.strip():

        st.warning(
            "Please enter your name."
        )

        st.stop()

    if st.session_state.image_path is None:

        st.warning(
            "Please upload a palm image."
        )

        st.stop()

    with st.spinner("🔍 analyzing your palm..."):

        try:

            vision_result = vision.analyze_palm(

                image_path=st.session_state.image_path,

            )

            if not vision_result["can_analyze"]:

                st.error(
                    vision_result["reason"]
                )

                st.stop()

            st.session_state.vision_result = vision_result

            st.success(
                "✅ Palm analysis completed successfully."
            )

        except Exception as e:

            st.error(
                f"Analysis Failed : {str(e)}"
            )

            st.stop()

# ======================================================
# Uploaded Palm Image
# ======================================================

if st.session_state.image_path:

    st.divider()

    st.subheader("🖐 Uploaded Palm")

    st.image(

        st.session_state.image_path,

        use_container_width=True

    )

    st.divider()
# ======================================================
# Palm Observation
# ======================================================

if st.session_state.vision_result:

    vision_result = st.session_state.vision_result

    st.divider()

    st.subheader("🖐 Palm Observation")

    metric1, metric2 = st.columns(2)

    with metric1:

        st.metric(

            "Image Quality",

            vision_result["image_quality"]

        )

    with metric2:

        st.metric(

            "Status",

            "Ready for Questions"

        )

    st.divider()

    card1, card2 = st.columns(2)

    with card1:

        st.info("❤️ Life Line")

        st.write(
            vision_result["life_line"]
        )

    with card2:

        st.info("🧠 Head Line")

        st.write(
            vision_result["head_line"]
        )

    card3, card4 = st.columns(2)

    with card3:

        st.info("❤️ Heart Line")

        st.write(
            vision_result["heart_line"]
        )

    with card4:

        st.info("💼 Fate Line")

        st.write(
            vision_result["fate_line"]
        )

    card5, card6 = st.columns(2)

    with card5:

        st.info("☀️ Sun Line")

        st.write(
            vision_result["sun_line"]
        )

    with card6:

        st.info("💍 Marriage Lines")

        st.write(
            vision_result["marriage_lines"]
        )

    st.info("⛰️ Mounts")

    st.write(
        vision_result["mounts"]
    )

    st.info("📝 Additional Observations")

    st.write(
        vision_result["additional_observations"]
    )

    st.divider()

# ======================================================
# Suggested Questions
# ======================================================

if st.session_state.vision_result:

    st.subheader("💡 Suggested Questions")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "💼 Career",
            use_container_width=True
        ):
            st.session_state.question = "How is my career?"

        if st.button(
            "❤️ Marriage",
            use_container_width=True
        ):
            st.session_state.question = "How is my marriage?"

    with col2:

        if st.button(
            "💰 Wealth",
            use_container_width=True
        ):
            st.session_state.question = "How is my financial growth?"

        if st.button(
            "😊 Personality",
            use_container_width=True
        ):
            st.session_state.question = "Describe my personality."

    st.divider()

# ======================================================
# Ask AI
# ======================================================

st.subheader("🤖 Ask About Your Palm")

question = st.text_input(

    "Enter your question",

    value=st.session_state.get(
        "question",
        ""
    ),

    placeholder="Example : How is my career?"

)

ask_button = st.button(

    "🤖 Ask Question ",

    use_container_width=True,

    type="primary"

)

if ask_button:

    if st.session_state.vision_result is None:

        st.warning(
            "Please analyze your palm first."
        )

        st.stop()

    if not question.strip():

        st.warning(
            "Please enter a question."
        )

        st.stop()

    with st.spinner("Generating Response..."):

        try:

            answer = rag.ask(

                question=question,

                vision_summary=st.session_state.vision_result[
                    "summary"
                ]

            )

            database.save_session(

                session_id=st.session_state.session_id,

                user_name=st.session_state.user_name,

                image_quality=st.session_state.vision_result[
                    "image_quality"
                ],

                question=question,

                answer=answer

            )

            st.session_state.chat_history.append(

                {

                    "question": question,

                    "answer": answer

                }

            )

            st.success(
                " Response Generated Successfully"
            )

            st.markdown("## 🤖 Palmistry Response")

            st.info(answer)

        except Exception as e:

            st.error(str(e))


# ======================================================
# Generate PDF Report
# ======================================================

if st.session_state.chat_history:

    st.subheader("📄 Generate Report")

    if st.button(

        "📥 Download PDF Report",

        use_container_width=True,

        type="primary"

    ):

        latest_chat = st.session_state.chat_history[-1]

        with st.spinner("Generating Professional Report..."):

            try:

                pdf_path = report.generate(

                    image_path=st.session_state.image_path,

                    question=latest_chat["question"],

                    vision_result=st.session_state.vision_result,

                    answer=latest_chat["answer"]

                )

                database.update_pdf_status(

                    st.session_state.session_id

                )

                st.success(

                    "✅ Report Generated Successfully"

                )

                with open(

                    pdf_path,

                    "rb"

                ) as pdf:

                    st.download_button(

                        label="📄 Download Report",

                        data=pdf,

                        file_name=os.path.basename(

                            pdf_path

                        ),

                        mime="application/pdf",

                        use_container_width=True

                    )

            except Exception as e:

                st.error(str(e))


# ======================================================
# Footer
# ======================================================

st.divider()

footer_col1, footer_col2 = st.columns(2)

with footer_col1:

    st.caption(
        "🔮 Palmistry Assistant"
    )


    st.caption(
        f"Generated : {datetime.now().strftime('%d-%b-%Y %I:%M %p')}"
    )

st.markdown(
    """
    <center>

    <hr>

    <b>Powered By</b>

    Palmistry

    </center>
    """,
    unsafe_allow_html=True
)