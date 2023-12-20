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

Based on those it can produce :
- Strategies
- Applications
- Analyses
- rich business intelligence

## Business Case

DataTonic provides junior executives with an extremely effective solution for basic and time-consuming data processing, document creation or business intelligence tasks.

### Enterprise Autonomation Agent

Do not wait for accounting, legal or business intelligence reporting with uncertain quality and long review cycles. DataTonic accelerates the slowest part of analysis : data processing and project planning execution. 

# How it works :

this section explains how Data Tonic works to produce what you need, consistently.

- your request is first processed according to a statement of work
- additional data is retrieved and stored
- multiple agents are created based on your specific use case

# Technology : 

this section describes how it works from a technical perspective:

- Autogen uses a semantic-kernel function calling agent to access the internet using the google api semantic-kernel then processes the new information and stores it inside a SQL database orchestrated by Taskweaver.
- Gemini is used in various configurations both for text using the autogen connector and for multimodal/image information processing. 

# How To Use

Please follow the instructions in this readme exactly. 

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

```bash
git clone https://github.com/DataTonic/DataTonic.git
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