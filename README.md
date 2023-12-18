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
git clone https://github.com/DataTonic/DataTonic.git

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

