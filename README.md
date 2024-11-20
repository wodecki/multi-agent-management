
# Managerial Problem Solver with Multi-Agent Systems

This Python mini-library leverages a **multi-agent system** built using [LangGraph](https://github.com/langgraph/langgraph) to diagnose and recommend solutions for managerial challenges. The system processes a user-provided query (or a default question) and generates a detailed report based on its analysis.

---

## Features

- Utilizes **LangGraph** for multi-agent architecture.
- Provides diagnosis and recommendations for managerial problems.
- Flexible CLI interface:
  - Run with a default question.
  - Specify a custom question as a parameter.

---

## Getting Started

Follow the steps below to set up the project and run the application.

### Prerequisites

- Python 3.8 or higher
- [Git](https://git-scm.com/)

---

### Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/managerial-problem-solver.git
cd managerial-problem-solver
```

#### 2. Create and Activate a Virtual Environment

Create a virtual environment named `management_agents`:

```bash
python3 -m venv management_agents
source management_agents/bin/activate   # On Windows: management_agents\Scripts\activate
```

#### 3. Install Dependencies

Once the virtual environment is activated, install the required libraries:

```bash
pip install -r requirements.txt
```

---

### Usage

Run the application from the command line.

#### Example 1: Use the Default Question
```bash
python main.py
```

#### Example 2: Provide a Custom Question
```bash
python main.py "I work for the automotive industry. Diagnose my product management maturity."
```

---

## Configuration

The application uses environment variables to store the **OpenAI API key**. Create a `.env` file in the root directory with the following content:

```env
OPENAI_API_KEY=your_openai_api_key
```

Replace `your_openai_api_key` with your actual OpenAI API key.

---

### Development
## Development Workflow

1. **Install Virtual Environment**: Follow the [Installation](#installation) steps.
2. **Modify Code**: Update the `main.py` or any other module as needed.
3. **Run Tests**: (Add testing instructions here if applicable.)

## Backlog
1. Save reports in a nice markdown format
2. Add web interface
3. Add agent monitoring
...
---

## Important Libraries

This project uses the following key libraries:
- **[LangGraph](https://github.com/langgraph/langgraph)**: The core library for building the multi-agent system.
- **[Python-dotenv](https://github.com/theskumar/python-dotenv)**: For managing environment variables.

---

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add a new feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

Special thanks to the developers of **LangGraph** for their incredible multi-agent framework.
