# original Idea from Reddit
# https://www.reddit.com/r/LocalLLaMA/comments/1f9um6s/comment/llpc7ud/
# GemMa2 system role not supprted
# llm_load_print_meta: EOS token        = 1 '<eos>'
# nctx = 8k

# Danube2 system role not supported
# llm_load_print_meta: EOS token        = 2 '</s>'
# nctx = 8k

#Qwen2 1.5 support system messages
# llm_load_print_meta: EOS token        = 151645 '<|im_end|>'
# nctx = 32k

sysmessage = """You are an AI assistant designed to provide detailed, step-by-step responses. Your outputs should follow this structure:
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
"""


import sys
from time import sleep


print("\033[95;3;6m")
print("1. Waiting 10 seconds for the API to load...")
from llama_cpp import Llama
llm = Llama(
            model_path='model/gemma-2-2b-it-Q5_K_M.gguf',
            n_gpu_layers=0,
            temperature=0.1,
            top_p = 0.5,
            n_ctx=8192,
            max_tokens=600,
            repeat_penalty=1.187,
            stop=['<eos>',"<|im_end|>","Instruction:","### Instruction:","###<user>","</user>"],
            verbose=False,
            )
print("2. Model gemma-2-2b-it-Q5_K_M.gguf loaded with LlamaCPP...")
print("\033[0m")  #reset all

history = [
    #{"role": "system", "content": sysmessage}
]
print("\033[92;1m")
counter = 1
while True:
    if counter > 10:
        history = [
            #{"role": "system", "content": sysmessage}
        ]        
    userinput = ""
    print("\033[1;30m")  #dark grey
    print("Enter your text (end input with Ctrl+D on Unix or Ctrl+Z on Windows) - type quit! to exit the chatroom:")
    print("\033[91;1m")  #red
    lines = sys.stdin.readlines()
    for line in lines:
        userinput += line + "\n"
    if "quit!" in lines[0].lower():
        print("\033[0mBYE BYE!")
        break
    templateinline = f"""You are an AI assistant designed to provide detailed, step-by-step responses. Your outputs should follow this structure:
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

user question: {userinput}
"""
    history.append({"role": "user", "content": templateinline})
    print("\033[92;1m")

    new_message = {"role": "assistant", "content": ""}
    
    full_response = ""
    fisrtround = 0
    for chunk in llm.create_chat_completion(
        messages=history,
        temperature=0.25,
        repeat_penalty= 1.187,
        stop=['<eos>','<|im_end|>'],
        max_tokens=800,
        stream=True,):
        try:
            if chunk["choices"][0]["delta"]["content"]:
                print(chunk["choices"][0]["delta"]["content"], end="", flush=True)
                full_response += chunk["choices"][0]["delta"]["content"]                              
        except:
            pass        
    new_message["content"] = full_response
    history.append(new_message)  
    counter += 1  
