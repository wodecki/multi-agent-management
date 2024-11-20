from typing import List, Annotated
from typing_extensions import TypedDict
from pydantic import BaseModel, Field
from operator import add

class Analyst(BaseModel):
    name: str = Field(
        description="Name of the analyst."
    )
    role: str = Field(
        description="Role of the analyst in the context of the topic.",
    )
    description: str = Field(
        description="Description of the analyst focus, key competencies, tasks in the project and concerns, and motives.",
    )
    @property
    def persona(self) -> str:
        return f"Name: {self.name}\nRole: {self.role}\nDescription: {self.description}\n"

class Perspectives(BaseModel):
    analysts: List[Analyst] = Field(
        description="Comprehensive list of analysts with their roles and description.",
    )

class OverallState(TypedDict):
    topic: Annotated[str, add] # Consulting topic
    questionnaire: Annotated[str, add] # Questionnaire results]
    analysts: List[Analyst] # All analysts
    diagnosis: Annotated[list[str], add] # Diagnosis
    recommendations: Annotated[list[str], add] # Recommendations
    report: str # Report
    
class ConsultingState(TypedDict):
    topic: str
    questionnaire: str  # Questionnaire results
    analyst: Analyst  # Current analyst (single instance)
    diagnosis: Annotated[list[str], add]  # Diagnosis
    recommendations: Annotated[list[str], add]  # Recommendations