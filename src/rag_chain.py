from openai import OpenAI

from config.settings import (
    OPENAI_API_KEY,
    LLM_MODEL,
)

from src.prompt import SYSTEM_PROMPT


class PalmistryRAG:

    def __init__(self, retriever):

        self.client = OpenAI(
            api_key=OPENAI_API_KEY
        )

        self.retriever = retriever

    def ask(
        self,
        question: str,
        vision_summary: str,
    ) -> str:

        docs = self.retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        prompt = f"""
Palm Image Analysis

{vision_summary}

---------------------------------------

Palmistry Knowledge

{context}

---------------------------------------

User Question

{question}
"""

        response = self.client.chat.completions.create(

            model=LLM_MODEL,

            temperature=0.3,

            messages=[

                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },

                {
                    "role": "user",
                    "content": prompt,
                }

            ]

        )

        return response.choices[0].message.content