import os
from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver
from langgraph.constants import Send
from langgraph.graph import START, END, StateGraph

# load dotenv
workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
dotenv_path = os.path.join(workspace_root, '.env')
load_dotenv(dotenv_path, override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')
model = os.getenv('MODEL')
#print(f"MODEL: {model}")

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model=model, temperature=0)

from graph.nodes.create_analysts import create_analysts
from graph.nodes.diagnose import diagnose
from graph.nodes.recommend import recommend
from graph.nodes.write_report import write_report
from graph.state import OverallState, ConsultingState

# define mapping functions
def initiate_consulting_threads(state: OverallState):
    """ Initiate parallel agent workflow using isolated substates for each analyst """
    print("... Initiate analysis ...")
    
    topic = state["topic"]
    analysts = state["analysts"]
    questionnaire = state.get("questionnaire", "Questionnaire results")
    
    print(f"Analysts: {analysts}")
    print(f"Topic: {topic}")
    print("... Analysis initiated...")
    return [
        Send(
            "consulting", 
            {
                "analyst": analyst,  # Pass individual analyst here, without attempting to store in OverallState
                "topic": topic,
                "questionnaire": questionnaire,
            }
        ) for analyst in analysts
    ]
# Add nodes and edges to analysts_builder
analysts_builder = StateGraph(OverallState)
analysts_builder.add_node("create_analysts", create_analysts)

analysts_builder.add_edge(START, "create_analysts")
analysts_builder.add_edge("create_analysts", END)

# Add nodes and edges to diagnosis_builder
diagnosis_builder = StateGraph(ConsultingState)
diagnosis_builder.add_node("diagnose", diagnose)
diagnosis_builder.add_node("recommend", recommend)

diagnosis_builder.add_edge(START, "diagnose")
diagnosis_builder.add_edge("diagnose", "recommend")
diagnosis_builder.add_edge("recommend", END)

# Add nodes and edges to app_builder
app_builder = StateGraph(OverallState)
app_builder.add_node("make_analysts", analysts_builder.compile())
app_builder.add_node("consulting", diagnosis_builder.compile())
app_builder.add_node("write_report", write_report)

app_builder.add_edge(START, "make_analysts")
app_builder.add_conditional_edges("make_analysts", initiate_consulting_threads, ["consulting"])
app_builder.add_edge("consulting", "write_report")
app_builder.add_edge("write_report", END)

app = app_builder.compile()

app.get_graph().draw_mermaid_png(output_file_path="graph.png")