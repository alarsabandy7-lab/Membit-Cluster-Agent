import os
import google.generativeai as genai
from core.risk_local import local_score

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

async def ai_insight(clusters):
    """
    Hybrid AI:
    - try Gemini
    - fallback to local heuristics
    """

    combined = "\n".join([c.get("summary","") for c in clusters])[:900]

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(
            f"Analyze social signals:\n{combined}\nProvide insights."
        )
        return response.text
    except:
        # fallback
        score = local_score(combined)
        return f"(Local fallback) Risk score: {score}" ￼Enter
