## Project Overview
 You are required to build a Question‑and‑Answering (Q&A) system that connects to a Large Language Model (LLM) API. This project also consists of two major components:
1. A Python Command-Line Interface (CLI) application
2. A simple Web GUI application for interacting with the LLM API

You will then host the Web GUI online and submit the final project folder in the required format.

<!-- Project Setup Guide -->
### Project Setup Guide

### Task 1
1. A Python Command-Line Interface (CLI) application

### Creating Virtual environment
#### For Windows
```bash
python -m venv llm
fer\Scripts\activate
```

#### For MacOS
```bash
python -m venv llm
source fer/bin/activate
```
### Installing Dependables
After sorting the virtual environment, Then we install the dependables
```bash
pip install -r requirements.txt
```

### Getting Groq API Key
Please go to this website
[Groq](https://console.groq.com/home)

to create a new account and navigate to the API Keys to create a new API Key

### Download the code
You can either downoad manually or download through the command line using the code below
```
git clone https://github.com/Sammyregt/LLM_QA_Project_Samuel-Adeoye_250000511.git
```

### Putting the Groq API Key inside the .env file
create a new file named .env
then input your api keys using the formati below
```
GROQ_API_KEY=your_unique_API_Key
```
### Running the CLI Application
After then use this code to run the CLI application in your command line
```
python LLM_QA_CLI.py
```

### Task 2

2. A simple Web GUI application for interacting with the LLM API

### Running the Application
After performing the initial steps of task 1, run the web GUI using the code below
```
python app.py
```
or use the link below to test the Project

[LLM_QA_hosted_webGUI](https://llm-qa-project-samuel-adeoye-250000-tau.vercel.app/)
