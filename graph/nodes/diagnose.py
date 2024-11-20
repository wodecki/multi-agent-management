import os
from dotenv import load_dotenv

# Get the absolute path to the root of the workspace
workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
# Construct the path to the .env file
dotenv_path = os.path.join(workspace_root, '.env')
# Load the .env file explicitly
load_dotenv(dotenv_path, override=True)
# Retrieve the API key
openai_api_key = os.getenv('OPENAI_API_KEY')
model = os.getenv('MODEL')
#print(f"MODEL: {model}")

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model=model, temperature=0)

# Create a diagnosis node
from graph.state import OverallState, ConsultingState
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

diagnosis_instructions = """You are an analyst tasked with needs analysis of Your customer.
Here is Your detailed persona, including role in the projects, competencies and tasks: {goals}

Your goal is diagnose the current state of the customer basing on questionnaire results.
Here is the questionnaire results: {questionnaire}

Generate only a diagnosis based on the questionnaire results. 
Your diagnosis should solely focus on Your persona, competencies and tasks.
Do not diagnose aspects outside of Your persona competencies.
Do not recommend any solutions yet. 
"""
# Import questionnaire results
import json

questionnaire_file = os.path.join(workspace_root, 'data/answer_1.json')
questionnaire = json.load(open(questionnaire_file, 'r'))

def diagnose(state: ConsultingState):
    """ Node to perform needs analysis and formulate the diagnosis """
    print("... Diagnose start...")
    # Get state
    analyst = state["analyst"]
    topic = state["topic"]
    print(f"Analyst: {analyst.name}")
    # print(f"Topic: {topic}")
    questionnaire = state.get("questionnaire", "Questionnaire results")  # Get questionnaire or use default
    
    # Generate diagnosis
    system_message = diagnosis_instructions.format(
        goals=analyst.persona, 
        questionnaire=questionnaire
    )
    diagnosis_result = llm.invoke([SystemMessage(content=system_message)])
    print("... Diagnose end...")
    return {
        "diagnosis": [diagnosis_result.content]    # Store current diagnosis
    }