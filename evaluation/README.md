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
