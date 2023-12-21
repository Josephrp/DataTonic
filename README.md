# DataTonic

A Data-Capable AGI-style Agent Builder of Agents , that creates swarms , runs commands and securely processes and creates datasets, databases, visualizations, and analyses.

- DataTonic solves simple tasks that require complex data processing
- it's perfect for data analytics and business intelligence

## Use Case

DataTonic produces fixed business intelligence assets based on autonomous multimedia data processing. 

- Sales Profiles
- Adaptive Summaries
- Dataset Analytics
- Research Reports
- Business Automation Applications

## Business Case

DataTonic provides junior executives with an extremely effective solution for basic and time-consuming data processing, document creation or business intelligence tasks.

### Enterprise Autonomation Agent

Do not wait for accounting, legal or business intelligence reporting with uncertain quality and long review cycles. DataTonic accelerates the slowest part of analysis : data processing and project planning execution. 

### How To Use

# Setup Instructions

This section provides instructions on setting up the project.

## Step 1: Clone the repository

/**
 Clone the Git repository.
 */
git clone https://github.com/Tonic-AI/DataTonic.git

## Step 2: Set the environment variables

This section of the code contains the configuration settings for the OAI (OpenAI) and Gemini APIs. These settings include the API keys, base URLs, and API versions for different models.

## OAI_CONFIG_LIST

The `OAI_CONFIG_LIST` variable is an environment variable that stores a list of dictionaries. Each dictionary represents a configuration for a specific model. The dictionaries contain the following keys:

- `model`: The name of the model.
- `api_key`: The API key for the model.
- `base_url`: The base URL for the API.
- `api_version`: The version of the API.

The code snippet provides example configurations for different models, including 'gpt-3.5-turbo', 'dalle', 'gpt-4', 'gpt-4-turbo', 'gpt-4-vision', 'gemini-pro', and 'gemini-pro-vision'. You need to replace the placeholder values with your actual API keys.

Note: The Gemini API keys are specific to Google's GenAI service.

Please ensure that you update the API keys and other configuration details according to your requirements before using this code.

```bash
export OAI_CONFIG_LIST="[
    {'model': 'gpt-3.5-turbo-preview', 'api_key': '<your OpenAI Key for gpt-3.5-turbo>', 'base_url': 'https://api.openai.com/v1', 'api_version': '2023-06-01-preview'},

    {'model': 'gpt-4-1106-preview', 'api_key': '<your OpenAI Key for gpt-4-1106>', 'base_url': 'https://api.openai.com/v1', 'api_version': '2023-06-01-preview'},

    {'model': 'dall-e-3', 'api_key': '<your OpenAI Key goes here>', 'base_url': 'https://api.openai.com/v1', 'api_version': '2023-06-01-preview'},

    {'model': 'gpt-4-vision', 'api_key': '<your OpenAI Key goes here>', 'base_url': 'https://api.openai.com/v1', 'api_version': '2023-06-01-preview'}
]"
```

## Gemini_CONFIG_LIST

```bash
export OAI_CONFIG_LIST="[
    {'model': 'gemini-pro', 'api_key': '<your Google's GenAI Key goes here>', 'base_url': 'https://genai.google.com/v1', 'api_type': 'google'},
    {'model': 'gemini-pro-vision', 'api_key': '<your Google's GenAI Key goes here>', 'base_url': 'https://genai.google.com/v1', 'api_type': 'google'}
]"
```

 

### Step 3: Install the required packages

```bash
pip install -r requirements.txt
```

### Step 4: Edit src/semantic_kernel/googleconnector.py

* edit src/semantic_kernel/googleconnector.py

## Step 5: Edit autogen_module.py

* edit autogen_module.py "path to your database"

## Step 6: Run the application

```bash
python run app.py
```

-------------------
-----------------
---
//*DRAFT For the GEMINI Hackathon - Jon//
### Project Name: DataTonic - Enabling Consultants of All Kinds to Reach Beyond Their Full Potential.
### Objective: To augment strategy consultants using an AI-driven approach.
### Event: Developed exclusively for the Gemini AI Hackathon, for now.
### Core Technology Stack:
    -Integrates Gemini AI, a multimodal AI model by Google DeepMind.
    -Incorporates TruLens for evaluation and improvement of LLM applications.
    -Llamaindex, too!
### Capabilities: Processes and analyzes diverse data types (text, images, audio, video) for actionable business strategy decision-making insights.
### Team Composition:

    Lead Engineer: Tonic - Expert coder leading core development.
    PM Engineering: Specialist in Gemini AI and TruLens tools.
    Engineering: N00r
    Frontend: Zachary
    Subject Matter Expert/Strategy Consultant: JonP
### Vision: 
    A world where beyond world-class business strategy is not limited by an individual, team, or organization's capital expenditures 
### Mission: 
    The Consulting Firm for All Consulting Firms: To revolutionize business strategy and consulting by providing rapid, data-driven actionable insights accessible to a wide range of enterprises, individuals, and students; 
    The Learning System for Consulting: To provide a safe environment where every user has the option to both learn and feed-forward to improve on their own and society's business strategy for a better world

### Features:
    Blending human EI input with advanced machine learning AI for better strategy consulting solutions and learning.

    1. Better Multimodal Data Processing: Integrates and analyzes various consulting communication including consultant/client request prompts and datasets (including text, images, audio, and video) with special tools including...

     -Utilizes Gemini AI's advanced algorithms for seamless advanced AI data integration.
     -Utilizes TruLens for immediate and unbiased feedback for human QA/QI
     **-Utilizes LlamaIndex for....

    This minimizes human error, provides faster processing, and enables human consultants to focus on what they do best - social capitalization and creativity

    2. Strategic Business Synthesis for Actionable Insights and Final Recommendations:

     -Using best practices, provides data-driven insights for common strategy consulting problems (including profitability, market entry/sizing, growth, acquisition/sales, industry assessment)
     -Employs predictive modeling for better brainstorming and scenario planning to better guide decision-making.

      It can create more and iterate faster on interim analysis and final solutions sets, risk analyses, and next steps for a more optimal and deeper final business strategy. 

    3. Natural Language Processing (NLP):

      - Advanced NLP capabilities for interpreting complex business queries.
      - Generates detailed recommendations and final reports, specialized for the specific consultant and client

    4. User Interface Design:

      -Intuitive, user-friendly interface for easy interaction and data input.
      -Visual representations of data insights for faster human comprehension.

    5. Performance Evaluation with TruLens:

       -Continuous evaluation and optimization of recommendations using TruLens.
       -Ensures groundedness, relevance, and non-bias in outputs.

    6. Customizable Framework:

       -Flexible and adaptable to all business needs across all sectors (using data from all major business schools,... [all business strategy publications - academic, media, etc]).
       [-Allows for the addition of custom modules and features.]
       -Create a junior/associate consultant, team of associates

    7. Collaborative Tools for Team-Based Analysis:

        -Create a junior/associate consultant, 
    Facilitates joint decision-making and strategy development.

Security and Confidentiality:

    High standards of data security and confidentiality.
    Ensures protection of sensitive business information.

Scalability:

    Designed to handle increased workload and data volume.
    Suitable for both large corporations and small businesse

Join us in exploring the future of consulting with DataTonic.

