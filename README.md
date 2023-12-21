# DataTonic

A Data-Capable AGI-style Agent Builder of Agents , that creates swarms , runs commands and securely processes and creates datasets, databases, visualizations, and analyses.

- DataTonic solves simple tasks that require complex data processing
- it's perfect for data analytics and business intelligence

#### What it does :

- your request is first processed according to a statement of work
- additional data is retrieved and stored to enrich it
- multiple agents are created based on your specific use case
- Multiple Multi-Agent Environments produce files and folders according to your use case.

## Use Case

DataTonic produces fixed business intelligence assets based on autonomous multimedia data processing. 

- Sales Profiles
- Adaptive Summaries
- Dataset Analytics
- Research Reports
- Business Automation Applications

Based on those it can produce :
- Strategies
- Applications
- Analyses
- rich business intelligence

### Business Case

DataTonic provides junior executives with an extremely effective solution for basic and time-consuming data processing, document creation or business intelligence tasks.

Now anyone can :
- get rapid client profile and sales strategy including design assets for executions with a single request
- create a functional web application
- create entire databases of business intelligence that can be used by enterprise systems. 

### Enterprise Autonomation Agent

Do not wait for accounting, legal or business intelligence reporting with uncertain quality and long review cycles. DataTonic accelerates the slowest part of analysis : data processing and project planning execution.

## Main Benefits

DataTonic is unique for many reasons :

- local and secure application threads.
- compatible with microsoft  enterprise environments.
- based on a rigorous and reproducible evaluation method.
- developper friendly : easily plug in new functionality and integrations.

### How we use it : Multi-Consult Technology

You can use datatonic however you want, here's how we're using it :
- add case books to your folder for embedding : now DataTonic always presents its results in a case study!
- add medical textbooks to your folder for embedding : now DataTonic helps you through med-school !
- add entire company business information : Data tonic is now your strategic advisor !
- ask data tonic to create targetted sales strategies : now DataTonic is your sales assistant !

**Data Tonic is the first multi-nested agent-builder-of-agents!**

## How Data Tonic Was Created

DataTonic Team started by evaluating multiple models against the new google/gemini models , testing all functions. Based on our evaluation results we optimized default prompts and created new prompts and prompt pipeline configurations. 

Learn more about using TruLens and our scientific method in the [evaluation folder](https://github.com/Tonic-AI/DataTonic/tree/main/evaluation). We share our results in the [evaluation/results](https://github.com/Tonic-AI/DataTonic/tree/main/evaluation/results) folder.

**you can also replicate our evaluation by following the instructions in #Easy Deploy**

## How it works :

DataTonic is the first application to use a **doubly nested multi-environment multi-agent builder-of-agents configuration** . Here's how it works ! 

### Orchestration

Data Tonic uses a novel combination of three orchestration libraries. 
- Each library creates it's own multi-agent environment. 
- Each of these environments includes a code execution and code generation capability. 
- Each of these stores data and embeddings on it's own datalake.
- Autogen is at the interface with the user and orchestrates the semantic kernel hub as well as using Taskweaver for data processing tasks.
- Semantic-kernel is a hub that includes internet browsing capabilities and is specifically designed to use taskweaver for data storage and retrieval and produce fixed intelligence assets also specifically designed for Autogen.
- Taskweaver is used as a plugin in semantic kernel for data storage and retrieval and also in autogen, but remains an autonomous task that can execute complex tasks in its multi-environment execution system.

### Technology : 

- Gemini is used in various configurations both for text using the autogen connector and for multimodal/image information processing. 
- Autogen uses a semantic-kernel function calling agent to access the internet using the google api semantic-kernel then processes the new information and stores it inside a SQL database orchestrated by Taskweaver.

# Easy Deploy

Please try the methods below to use and deploy DataTonic.

### Easy Deploy DataTonic evaluation/results

The easiest way to use DataTonic is to deploy on github spaces and use the **notebooks in the evaluation/results folder** . 

Click here for easy_deploy [COMING SOON!]

**in the mean time please follow the instructions below:**

1. Star then Fork this repository
2. [use these instructions to deploy a code space for DataTonic](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository)
3. Configure DataTonic according to the instructions below or 
4. navigate to [evaluation/results](https://github.com/Tonic-AI/DataTonic/tree/main/evaluation/results) to use our evaluation methods.

# How To Use

Please follow the instructions in this readme **exactly**. 

### Follow Tonic-AI

### Star & Fork this repository

![image](https://github.com/Tonic-AI/DataTonic/assets/18212928/54e2f12a-0379-49d5-866c-985ea36f0e2b)
1. Step 1 : Star this repository
2. Step 2 : Fork this repository

### Set Up Gemini

### Get Google API key

### Get Open AI Key(s)

### Set Up Azure

## Setup Instructions

This section provides instructions on setting up the project.

### Step 1 : Clone the repository

clone this repository using the command line :

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
cd ./src/tonicweaver
git clone https://github.com/microsoft/TaskWeaver.git
cd ./src/tonicweaver/TaskWeaver
# install the requirements
pip install -r requirements.txt
```
### Install DataTonic
from the project directory :
```bash
pip install -r requirements.txt
```

## Step 4: Run the application

```bash
python run app.py
```

# Developpers

We welcome contributions from the community! Whether you're opening a bug report, suggesting a new feature, or submitting a pull request, every contribution is valuable to us. Please follow these guidelines to contribute to DataTonic.

## Getting Started

Before you begin, ensure you have the latest version of the main branch:

```bash
git checkout main
git pull origin main
```
Then, create a new branch for your contribution:

```bash
Copy code
git checkout -b <your-branch-name>
```
## Bug Reports

If you encounter any bugs, please file an issue on our GitHub repository. Include as much detail as possible:

- A clear and concise description of the bug
- Steps to reproduce the behavior
- Expected behavior vs actual behavior
- Screenshots if applicable
- Any additional context or logs

## Suggesting Enhancements

We are always looking for suggestions to improve DataTonic. If you have an idea, please open an issue with the tag 'enhancement'. Provide:

- A clear and concise description of the proposed feature
- Any relevant examples or mockups
- A description of the benefits to DataTonic users

## Code Contributions
If you'd like to contribute code, please follow these steps:

### Step 1: Set Up Your Environment
Follow the setup instructions in the README to get DataTonic running on your local machine.

### Step 2: Make Your Changes
Ensure that your changes adhere to the existing code structure and standards. Add or update tests as necessary.

### Step 3: Commit Your Changes
Write clear and meaningful commit messages. This helps to understand the purpose of your changes and speed up the review process.

```bash
git commit -m "A brief description of the commit"
```
### Step 4: Push to the Branch
Push your changes to your remote branch:

 ```bash
git push origin <your-branch-name>
```
### Step 5: Open a Pull Request
Go to the repository on GitHub and open a new pull request against the main branch. Provide a clear description of the problem you're solving. Link any relevant issues.

### Step 6: Code Review
Maintainers will review your pull request. Be responsive to feedback to ensure a smooth process.

# Code of Conduct
Please note that this project is released with a Contributor Code of Conduct. By participating in this project, you agree to abide by its terms.

# License
By contributing to DataTonic, you agree that your contributions will be licensed under its LICENSE.

**Thank you for contributing to DataTonic!🚀**