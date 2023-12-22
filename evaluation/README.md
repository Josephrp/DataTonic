# Gemini Evaluations


https://github.com/Tonic-AI/DataTonic/assets/18212928/06a31973-c22b-4a79-abc2-5d332432a1fb


https://github.com/Tonic-AI/DataTonic/assets/18212928/e43e85f7-b80d-4132-bb8d-e0442f5e7d31



https://github.com/Tonic-AI/DataTonic/assets/18212928/fd723b18-a501-4da3-8a8e-3ac23c28b23e



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

**proposed prompts :** these are our unique prompts:
- [taskweaver planner](https://github.com/Tonic-AI/DataTonic/blob/main/src/tonicweaver/planner)
- [semantic-kernel planner](https://github.com/Tonic-AI/DataTonic/blob/main/src/semantic_kernel/semantic_kernel_module.py)

**evaluation results :** 
- these are our [results](https://github.com/Tonic-AI/DataTonic/blob/main/evaluation/results)

**analysis :** based on our results , we have ranked prompts and prompt combinations and optimized their useage and their applicability to our use case
