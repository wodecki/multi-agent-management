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
from graph.state import OverallState
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

writing_instructions = """You are a senior consultant experienced in writing executive reports. Your goal is to write a comprehensive report based on the diagnosis and recommendations provided by the analysts.

The report should be structured, concise, and actionable. It should include an executive summary, an introduction, a detailed analysis, and a set of recommendations.

Here is the diagnosis: {diagnosis}

Based on this diagnosis, the analysts have provided the following recommendations: {recommendations}.

Write a report that addresses the diagnosis and recommendations. You can ask the analysts for more information if needed.
"""

def write_report(state: OverallState):
    """ Node to summarize diagnosis and recommendations in a single report"""
    print("... Write Report ...")
    # Get state
    diagnosis = state['diagnosis']
    recommendations = state['recommendations']
    # Generate question
    system_message = writing_instructions.format(diagnosis=diagnosis, recommendations=recommendations)
    report = llm.invoke([SystemMessage(content=system_message)])

    # Write messages to state
    return {"report": report}