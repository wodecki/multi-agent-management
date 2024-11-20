import sys
import os
import pytest

# Adjust the Python path to ensure the 'graph' package can be imported correctly
workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.insert(0, workspace_root)

# Test create_analysts
from graph.nodes.create_analysts import create_analysts

def test_create_analysts():
    # Define the input state
    max_analysts = 3
    topic = "Help a multinational manufacturing company in their journey to product management maturity."
    state = {"topic": topic, "analysts": []}
    
    # Call the create_analysts function
    analysts = create_analysts(state)
    
    # Basic checks (you can add more specific assertions as needed)
    assert isinstance(analysts, dict), "Expected output to be a dictionary."
    assert "analysts" in analysts, "Expected 'analysts' key in the output."
    assert len(analysts["analysts"]) > 0, "Expected at least one analyst to be generated."
    
    # Print the first three analysts for verification
    print(f"Analysts: {analysts['analysts'][:max_analysts]}")
    
# Test diagnose
from graph.nodes.diagnose import diagnose

def test_diagnose():
    # Define the input state
    from graph.state import NeedsAnalysisState, Analyst
    from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
    state = NeedsAnalysisState(
        #questionnaire="Questionnaire results",
        analysts=[Analyst(
            name="John Doe",
            role="Data Analyst",
            description="Data analyst with experience in financial data analysis.",
        )],
        diagnosis="",
        recommendations="",
        topic="Consulting topic",
    )
    
    # Call the diagnose function
    diagnosis = diagnose(state)
    
    # Basic checks (you can add more specific assertions as needed)
    assert isinstance(diagnosis, dict), "Expected output to be a dictionary."
    assert "diagnosis" in diagnosis, "Expected 'diagnosis' key in the output."
    assert diagnosis["diagnosis"], "Expected a non-empty diagnosis."
    
    # Print the diagnosis for verification
    print(f"Diagnosis: {diagnosis['diagnosis']}")
    
# Test recommend
from graph.nodes.recommend import recommend

def test_recommend():
    # Define the input state
    from graph.state import NeedsAnalysisState, Analyst
    from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
    state = NeedsAnalysisState(
        questionnaire="Questionnaire results",
        analyst=Analyst(
            name="John Doe",
            role="Data Analyst",
            description="Data analyst with experience in financial data analysis.",
        ),
        diagnosis="Diagnosis results",
        recommendations="",
        topic="Consulting topic",
    )
    
    # Call the recommend function
    recommendations = recommend(state)
    
    # Basic checks (you can add more specific assertions as needed)
    assert isinstance(recommendations, dict), "Expected output to be a dictionary."
    assert "recommendations" in recommendations, "Expected 'recommendations' key in the output."
    assert recommendations["recommendations"], "Expected non-empty recommendations."
    
    # Print the recommendations for verification
    print(f"Recommendations: {recommendations['recommendations']}")

# Test graph
from graph.graph import app

def test_graph():
    # Define the initial state
    from graph.state import GenerateAnalystsState
    state = GenerateAnalystsState(
        topic="Consulting topic",
        analysts=[],
    )
    
    # Run the graph
    final_state = app.invoke(state, config={"configurable": {"thread_id": "1"}})
    
    # Basic checks (you can add more specific assertions as needed)
    assert isinstance(final_state, dict), "Expected the final state to be a dictionary."
    assert "analysts" in final_state, "Expected 'analysts' key in the final state."
    assert final_state["analysts"], "Expected non-empty list of analysts."
    
    # Print the final state for verification
    print(f"Final state: {final_state}")
        
# Run the test
if __name__ == "__main__":
    #pytest.main([__file__])
    #test_diagnose()
    #test_recommend()
    test_graph()