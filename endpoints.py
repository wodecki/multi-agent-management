from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from graph.graph import app

load_dotenv()

# Initialize FastAPI app
api = FastAPI()


# Request model for the input message
class MessageRequest(BaseModel):
    topic: str


# Response model for the report content
class ReportResponse(BaseModel):
    content: str


@api.get("/generate-report", response_model=ReportResponse)
async def generate_report_get(topic: str):
    """
    Endpoint to generate a report based on the given topic via GET request.
    """
    try:
        # Invoke the app to generate a report
        report = app.invoke(
            {"topic": topic},
            config={"configurable": {"thread_id": "1"}}
        )
        # Extract the content of the report
        content = report.get('report', {}).content
        if not content:
            raise ValueError("Failed to generate report content.")
        return {"content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
