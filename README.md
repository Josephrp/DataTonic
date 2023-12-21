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

## Do more with DataTonic 

- is DataTonic Accessible ?

**yes** DataTonic is accessible both audio and image input.

- can i use it to make beautiful graphs and statistical analyses with little or no starting data ?
 
**yes.** DataTonic will look for the data it needs but you can add your .db files or any other types of files with DataTonic.
  
- can i write a book or a long report ?

**yes.** DataTonic produces rich , full-length content.

- can i make an app ?

**yes.** DataTonic is more tailored to business intelligence but it is able to produce functioning applications inside generated repositories.

- can it do my job ?

**yes** DataTonic is able to automate many junior positions and it will include more enterprise connectors, soon !

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

## Set Up

please use command line with administrator priviledges for the below.

### Set Up Gemini

- run the following command to install googlecloud/vertex cli :
```bash
pip install google-cloud-aiplatform
```

- navigate to this url :
```
https://console.cloud.google.com/vertex-ai
```
- and click create new project.
![image](https://github.com/Tonic-AI/DataTonic/assets/18212928/582ee276-e8b7-4d5d-b251-c1f730eaa84c)

- Create a new project and add a payment method.

- click 'enable all recommended APIs' 
![image](https://github.com/Tonic-AI/DataTonic/assets/18212928/2193f80b-fd46-444c-9173-81044166b3a6)

- click on 'multimodal' on the left then 'my prompts' on the top:
![image](https://github.com/Tonic-AI/DataTonic/assets/18212928/3ca60a1b-9012-432a-b431-b13eccbb57ff)

- click on 'create prompt' and 'GET CODE' on the top right in the next screen:
![image](https://github.com/Tonic-AI/DataTonic/assets/18212928/f563af64-cb9f-40a0-8158-564cd42bbc45)

- then click on 'curl' on the top right to find your 'endpoint' and projectid , and other information
e.g.
```curl
cat << EOF > request.json
{
    "contents": [
        {
            "role": "user",
            "parts": []
        }
    ],
    "generation_config": {
        "maxOutputTokens": 2048,
        "temperature": 0.4,
        "topP": 1,
        "topK": 32
    }
}
EOF

API_ENDPOINT="us-central1-aiplatform.googleapis.com"
PROJECT_ID="focused-album-408018"
MODEL_ID="gemini-pro-vision"
LOCATION_ID="us-central1"

curl \
-X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://${API_ENDPOINT}/v1/projects/${PROJECT_ID}/locations/${LOCATION_ID}/publishers/google/models/${MODEL_ID}:streamGenerateContent" -d '@request.json'
```

### Get Google API key

 run the following command to find your API key after following the instructions above:
```bash
gcloud auth print-access-token
```
**IMPORTANT : this key will expire every less than 30 minutes, so please refresh it regularly and accordingly**

### Get Open AI Key(s)

- navigate to openai and create a new key :
```
https://platform.openai.com/api-keys
```

### Set Up Azure

- use the Azure OAI portal by navigating to this page :
```
https://oai.azure.com/portal
```
- deploy your models
![image](https://github.com/Tonic-AI/DataTonic/assets/18212928/db19a2f3-5996-462c-9273-ef4af5710d0e)

- go to playground
- click on view code :
![image](https://github.com/Tonic-AI/DataTonic/assets/18212928/192f55fb-c174-45d6-a15b-12f7bce5e0b2)
- make a note of your `endpoint` , `API Key` , and `model name` to use it later.

## Setup Instructions

This section provides instructions on setting up the project. Please turn off your firewall and use administrator priviledges on the command line.

### Step 1 : Clone the repository

clone this repository using the command line :

```bash
git clone https://github.com/Tonic-AI/DataTonic.git
```

## Step 2: Configure DataTonic

### Add Your Files to DataTonic 

1. add relevant files one by one with no folder to the folder called 'src/autogen/add_your_files_here' 
    - supported file types : ".pdf" ,  ".html" ,  ".eml" & ".xlsx":
2. 

### Configuration
1. you'll need the keys you made above for the following.
2. use a text editor , and IDE  or command line to edit the following documents.
3. Edit then save the files 

#### OAI_CONFIG_LIST

edit 'OAI_CONFIG_LIST'

```json
        "api_key": "your OpenAI Key goes here",
```
and 
```json
        "api_key": "your Google's GenAI Key goes here",
```

#### Configure OpenAI Key(s)
    1. modify Line 135 in autogen_module.py
        ```python
        os.environ['OPENAI_API_KEY'] = 'Your key here'
        ```
    2. modify .env.example
        ```os
        OPENAI_API_KEY = "your_key_here"
        ```
        save as '.env' - this should create a new file.
        **or** 
        rename to '.env' - this will rename the existing file.

    3. modify src\tonicweaver\taskweaver_config.json
        ```json
        {
            "llm.api_base": "https://api.openai.com/v1",
            "llm.api_key": "",
            "llm.model": "gpt-4-1106-preview"
        }
        ```

    4. 
#### Google API

edit ./src/semantic_kernel/semantic_kernel_module.py
```python
line 64:    semantic_kernel_data_module = SemanticKernelDataModule('<google_api_key>', '<google_search_engine_id>')
```
and 
```python
line 158:    semantic_kernel_data_module = SemanticKernelDataModule('<google_api_key>', '<google_search_engine_id>')
```
with your google API key and Search Engine ID , made above.

src/semantic_kernel/googleconnector.py


## Step 3: Install DataTonic

### Install Taskweaver

from the project directory :
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
