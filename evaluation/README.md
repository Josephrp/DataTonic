# Gemini Evaluations

**problem statement :** when creating multiagent environments, fixed prompts and default prompts are used. However, Gemini does not have system prompts and the "voice" returned is different than openai.

- what is the optimal configuration of text and multimodal input prompts to produce ai autonomous agent builders and accomplish complex data processing tasks using gemini ?

**solution :** We're working with trulens to evaluate default prompts and optimize performance.

**methodology :** to arrive at our optimal solution:
- we made "simple applications" using trulens wrappers in jupyter notebooks.
- We evaluated prompts and combinations of prompts for gemini and openai for our libraries Autogen, TaskWeaver, Semantic-Kernel.
- We evaluated RAG retrieval performance for various embedding models.
- We evaluated Multimodal Performance. 
- Analyzed the results for best performance and quality.
then applied them to our enterprise application DataTonic.

**default prompts :** these are our baselines: 
- [autogen](https://github.com/Tonic-AI/DataTonic/blob/main/evaluation/baselineprompts/autogendefaultprompts.md)
- [semantic-kernel](https://github.com/Tonic-AI/DataTonic/blob/main/evaluation/baselineprompts/semantickerneldefaultprompts.md)
- [taskweaver](https://github.com/Tonic-AI/DataTonic/blob/main/evaluation/baselineprompts/taskweaverdefaultprompts.md)
- [datatonic](https://github.com/Tonic-AI/DataTonic/blob/main/evaluation/baselineprompts/datatonicdefaultprompts.md)

**proposed prompts :** these are our proposals

**evaluation results :** these are our results

**analysis :** based on our results , we have ranked prompts and prompt combinations and optimized their useage and their applicability to our use case

-----
-----
-----
**[UPDATED/DRAFT/EXAMPLE] methodology :** to build a better consultant for all consultancies....
- we made "simple applications" using trulens wrappers in jupyter notebooks.
- We evaluated prompts and combinations of prompts for gemini and openai for our libraries Autogen, TaskWeaver, Semantic-Kernel.
- We evaluated RAG retrieval performance for various embedding models.
- We evaluated Multimodal Performance. 
- Analyzed the results for best performance and quality.
then applied them to our enterprise application DataTonic.

- An example for training/fine-tuning a model from most basic (1) to most advanced (7)
1. A Consultant (trainer) for Initial Case analysis and Data Extraction (The Consulting Student/Junior Associate)
    Purpose: To analyze cases like "Rubber Bumper" (Darden 2019) to understand the complexity and requirements of real-world business scenarios, starting with training material for MBA students.

For example, this case involves a manufacturing company "Rubber Bumper" (RB) that faces declining profits. The (trainee) consultant must collect information from the new president who is seeking solutions.

The consultant (trainer) reviews material (prompts) from the client (RB president), extracts key details from interaction prompts such as the company's product lines, market position, sales trends, and current challenges; and integrates it with provided datasets and figures (such as financial data on costs, overheads, and pricing - from tables or other figures).   

This is done in a step-by-step manner:
A. Case Introduction
- Client (User): Case introduction
- Consultant Trainer (TonicAI-Consultant): Clarifying Questions
- Client: Answers to clarifying questions (if available)
- Consultant: Summary of Problem Definition, Initial Framework
(For example: ...)
B. Case Exhibits (1-2)
- Client (User): Table or Figure of Data
- Consultant Trainer: Synthesis and Actionable Insight/Next Step
(For example: ...)
C. Analyses of Different Scenarios/Options (1-2)
- Client (User): Requests an analysis for a particular scenario (i.e. current profitability, future profitability if a change is made)
- Consultant Trainer: Performs the analysis step-by-step (i.e. Maths - Profitabilty), notes insights (i.e. a higher than industry standard profit margin and why), and next steps (further analyses that may be useful)
D. Brainstorming of Different Scenarios/Options (Creativity/Innovation Assessment)
- Client (User): Requests a "what else" analysis (other options)
- Consultant Trainer: Provides a structured list of options according to the client's criteria (i.e. using MECE and other frameworks, prioritized by the most optimal solution).
E. Conclusion - Final Recommendation, Risks, and Next Steps
- Client (User): Prompts the Consultant for their final recommendation including risks if it were to be followed, and next steps for more assessment and/or implementation


Rubber Bumper, Darden 2019: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiljfGQ8p-DAxUmGFkFHfv3DHkQFnoECBUQAQ&url=https%3A%2F%2Feconomics.virginia.edu%2Fsites%2Feconomics.virginia.edu%2Ffiles%2FDarden%2520Case%2520Book%25202018-2019.pdf&usg=AOvVaw00SSZ7I8-QKQT-Zbc6quVH&opi=89978449

The consultant trainer was created by learning on all leading MBA casebooks. 
It was validated based on ideal responses from provided MBA professionals.
It was then tested on new casbeooks and unpublished cases from real consulting interviewers and real-world clients.  The goal is for it to be first deployed in schools to make consulting training more accessible to all, then consultancies to improve their operations (and free up junior consultants to focus on higher-value tasks).


2. The Data Team - Modeling Business Scenarios
  Purpose: to create simulations of business scenarios presented in the cases (or by real-world clients). 

For example, in 'Rubber Bumper' this would be to simulate scenarios such as whether to automate processes, change production focus, or adjust pricing (with models able to perform profitability analyses considering factors like cost of automation, production capacity, and market demand)


3. The Final Recommender - Strategic Recommendations

  Purpose: to develop the model's capability to evaluate different final recommendations and their financial implications, including a risk analysis, and implementation plan for next steps

For example, in 'Rubber Bumper" this would involve multiple scenarios that assessing potential broader market changes, technology adoption risks, and operational risks to refine the recommendation, and based on this recommendation develop a detailed implementation plan.

4. The Real 360 - Continuous, Collaborative, and Cumulative Feedback and Interation 

    Purpose: To ​develop a system where models developed from older cases are continuously updated with newer related cases and real-world data to refine/improve consultant decision-making capabilities.

    For example, if a better 'Rubber Bumper' came out 1 year from now, data from its bumping could feedback into the model to optimize its real-world accuracy and applicability.


5. The Real 360 At Scale - A Continuous, Collaborative, and Cumulative Learning Enterprise System

  Purpose: ... integrated with all aspects of DataTonic for practice testing. Performance evaluation done through tools such as TruLens to track and optimize model performance in actual business scenarios.

---End Example---  
