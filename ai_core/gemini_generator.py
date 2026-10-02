import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_document(document_type, parties, terms, effective_date):

    prompt = f"""
    Generate a legal document.

    Document Type: {document_type}
    Parties: {parties}
    Terms: {terms}
    Effective Date: {effective_date}

    Include:
    1. Title
    2. Introduction
    3. Agreement Details
    4. Terms and Conditions
    5. Responsibilities
    6. Signature Section

    Use professional English.
    Do not invent missing information.
    Mark clauses that require legal review.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
