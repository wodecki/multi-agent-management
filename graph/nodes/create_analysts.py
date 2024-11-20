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
#print(f"OPENAI_API_KEY: {openai_api_key}") 
print(f"MODEL: {model}")

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model=model, temperature=0)

# Generate Analysts
from graph.state import Analyst, Perspectives, OverallState

from langchain_core.messages import HumanMessage, SystemMessage

# analyst_instructions="""You are tasked with creating a set of AI analyst personas. Follow these instructions carefully:

# First, review the research topic:
# {topic}

# Next, create four AI analyst:
# 1. Human Resources Analyst, focusing on team dynamics and performance, team collaboration, and human trainings and development in the context of the topic.
# 2. Business Process Analyst, focusing on business process optimization, business process automation, and business process management in the context of the topic.
# 3. Knowledge Management Analyst, focusing on knowledge management processes, knowledge sharing, and knowledge tools in the context of the topic.
# 4. Product Management Analysts, specializing in product management processes, product management tools and IT systems, and product management strategies in the context of the topic.
# """

analyst_instructions="""You are tasked with creating a set of AI analyst personas. Follow these instructions carefully:

First, review the research topic:
{topic}

Next, create four AI analyst:
1. Human Resources Analyst, focusing on team dynamics and performance, team collaboration, and human trainings and development in the context of the topic.
2. Business Process Analyst, focusing on business process optimization, business process automation, and business process management in the context of the topic.
3. Knowledge Management Analyst, focusing on knowledge management processes, knowledge sharing, and knowledge tools in the context of the topic.
4. IT Systems Analyst, specializing in IT systems, IT tools, and IT strategies in the context of the topic.

"""

def create_analysts(state: OverallState):

    """ Create analysts """

    topic=state['topic']

    # Enforce structured output
    structured_llm = llm.with_structured_output(Perspectives)

    # System message
    system_message = analyst_instructions.format(topic=topic)

    # Generate question
    analysts = structured_llm.invoke([SystemMessage(content=system_message)]+[HumanMessage(content="Generate the set of analysts.")])

    # Write the list of analysis to state
    return {"analysts": analysts.analysts}