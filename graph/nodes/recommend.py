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

recommendations_instructions = """You are an analyst tasked with helping Your customer in the {topic}.".
Here is Your detailed persona, including role in the projects, competencies and tasks: {goals}

Your goal is make constructive and interesting recommendations basing on an initial diagnosis.
1. Constructive: Recommendations that are helpful and actionable.
2. Specific: Recommendations that avoid generalities and include specific examples from the expert.
3. Managable: Recommendations that are realistic and can be implemented by the customer.

Here is the diagnosis: {diagnosis}

Generate only recommendation grounded in the diagnosis.
Your recommendation should solely be inline with Your persona, competencies, and tasks.
Do not make recommendations in aspects outside of Your persona, competencies, and tasks.
"""

def recommend(state: ConsultingState):
    """ Node to make recommendations based on the diagnosis """
    print("... Recommend start ...")
    # Get state
    analyst = state["analyst"]
    print(f"Analyst: {analyst.name}")
    topic = state['topic']
    # print(f"Topic: {topic}")
    diagnosis = state['diagnosis']
    
    # Generate question
    system_message = recommendations_instructions.format(topic=topic, goals=analyst.persona, diagnosis=diagnosis)
    recommendation = llm.invoke([SystemMessage(content=system_message)])
    # Write messages to state
    return {"recommendations": [recommendation.content]}