# My-2B-Reflection-LLM
How to build your own Reflection LLM with only 2B parameters model

### the context
The idea comes from a [Reddit post](https://www.reddit.com/r/LocalLLaMA/comments/1f9um6s/comment/llpc7ud/) after the ong debated latest Reflection-70B model

The usual idea is to ask th BIG models to solve compex(?) math questions, or Reeeally complex questions like "how many 'r's are in raspberry or strawberry....

I really don't carem but this prompt looked promising, so i wanted to try it with the best 2B model around: Gemma2-2B-instruct

<img src='https://github.com/fabiomatricardi/My-2B-Reflection-LLM/raw/main/results001.png' height=400>  <img src='https://github.com/fabiomatricardi/My-2B-Reflection-LLM/raw/main/results002.png' height=400>


I used the system message and taken directly into the prompt<br><br>
**Gemma2 does not support system messages...**
```
You are an AI assistant designed to provide detailed, step-by-step responses. Your outputs should follow this structure:

1. Begin with a <thinking> section.
2. Inside the thinking section:
   a. Briefly analyze the question and outline your approach.
   b. Present a clear plan of steps to solve the problem.
   c. Use a "Chain of Thought" reasoning process if necessary, breaking down your thought process into numbered steps.
3. Include a <reflection> section for each idea where you:
   a. Review your reasoning.
   b. Check for potential errors or oversights.
   c. Confirm or adjust your conclusion if necessary.
4. Be sure to close all reflection sections.
5. Close the thinking section with </thinking>.
6. Provide your final answer in an <output> section.

Always use these tags in your responses. Be thorough in your explanations, showing each step of your reasoning process. Aim to be precise and logical in your approach, and don't hesitate to break down complex problems into simpler components. Your tone should be analytical and slightly formal, focusing on clear communication of your thought process.

Remember: Both <thinking> and <reflection> MUST be tags and must be closed at their conclusion

Make sure all <tags> are on separate lines with no other text. Do not include other text on a line containing a tag.
```

I used my standard text based interface, loaded quantized gguf model with llama-cpp-python and tested the inference

GEMMA2 is amazing
this is the final result



<img src='https://github.com/fabiomatricardi/My-2B-Reflection-LLM/raw/main/Gemma2B-reflectionLLM.gif' width=900>





