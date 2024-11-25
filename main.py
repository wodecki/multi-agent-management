import os
import sys
from dotenv import load_dotenv
from pprint import pprint

# Load environment variables
load_dotenv(override=True)

# Retrieve the API key
openai_api_key = os.getenv('OPENAI_API_KEY')

# Import the application
from graph.graph import app


def main():
    # Check if a CLI parameter (question) is provided
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])  # Combine all CLI arguments into a single string
    else:
        # Default hardcoded question
        question = "Help a multinational manufacturing company in their journey to product management maturity."

    # Invoke the app with the provided or default question
    response = app.invoke({"topic": question}, config={"configurable": {"thread_id": "1"}})

    # Print the report
    print("\n=====REPORT=====")
    print(response["report"])


if __name__ == "__main__":
    main()
