from pydantic import BaseModel, Field


class CVAnalysis(BaseModel):
    professional_summary: str

    skills: list[str]

    strengths: list[str]

    weaknesses: list[str]

    improvement_suggestions: list[str]

    improved_summary: str

    improved_project_bullets: list[str]

    improved_experience_bullets: list[str]

