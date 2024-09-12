import streamlit as st
import time
import sys
import os
from time import sleep

if "hf_model" not in st.session_state:
    st.session_state.hf_model = "gemma-2-2b-it"
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

#AVATARS
av_us = '🧑‍💻'  # './man.png'  #"🦖"  #A single emoji, e.g. "🧑‍💻", "🤖", "🦖". Shortcodes are not supported.
av_ass = 🤖'   #'./robot.png'
# Set a default model


### START STREAMLIT UI
st.markdown("### *powered by Streamlit & Reflection Gemma2-2B*", unsafe_allow_html=True )
#st.subheader(f"Free ChatBot using {st.session_state.hf_model}")
st.markdown('---')

p1 = """You are an AI assistant designed to provide detailed, step-by-step responses. Your outputs should follow this structure:
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

user question: explain why it is crucial for teachers to learn how to use generative AI for their job and for the future of education. Include relevant learning path for teachers and educators.
"""

full_response = """<thinking> 
This question asks me to discuss the importance of generative AI for teachers, outlining a potential learning pathway.  I will start by analyzing why this is important, then outline steps for how teachers can learn about it.

a. The core idea is that generative AI has transformative potential in education. It offers tools for personalized learning, content generation, and even automating tasks like grading. 
b. My plan is to explain the benefits of using generative AI for teaching and then provide a suggested path for educators to acquire these skills.  
c. I will break down this path into manageable steps that teachers can follow.

<reflection>
The potential benefits are numerous: personalized learning, content creation, time-saving automation, etc., but it's important to emphasize ethical considerations like bias and plagiarism prevention. 


I need to ensure the suggested learning pathway is practical for educators with varying levels of technical expertise.  It should be accessible, engaging, and relevant to their teaching practices.

<output>
Generative AI presents a powerful opportunity for teachers to enhance their practice and prepare students for an increasingly digital world. Here's why: 

**Benefits:**

* **Personalized Learning:** Generative AI can create customized learning paths based on individual student needs and progress, ensuring each learner receives the right support at the right time.
* **Content Creation:** Teachers can leverage generative AI to generate lesson plans, quizzes, interactive exercises, and even creative content like stories or poems tailored for specific subjects. 
* **Time-Saving Automation:**  AI tools can automate repetitive tasks such as grading assignments, generating feedback reports, and managing student data, freeing up teachers' time for more meaningful interactions with students.
* **Enhanced Engagement:** Interactive learning experiences powered by AI can make education more engaging and immersive, fostering deeper understanding and motivation among learners. 

**Learning Path for Teachers:**


1. **Fundamentals of Generative AI:** Start with a basic introduction to the concept of generative AI, exploring its capabilities and limitations. Online courses from platforms like Coursera or edX offer introductory modules on this topic.
2. **AI Tools for Education:**  Explore specific tools designed for educational use cases: 
    * **Text Generation:** ChatGPT (OpenAI), Bard (Google) can be used to create engaging content, generate prompts for writing exercises, and even write simple code explanations.
    * **Image/Video Creation:** DALL-E 2, Midjourney offer creative possibilities for generating visuals that support learning materials or enhance classroom activities.  
3. **Integrating AI into Teaching Practice:** Experiment with using these tools in your teaching environment. Focus on how they can be used to personalize learning, create engaging content, and automate tasks. Consider starting small by integrating a tool like ChatGPT for creating interactive quizzes or generating prompts for student writing assignments. 
4. **Ethical Considerations & Bias Awareness:**  Educators must understand the ethical implications of using AI in education. This includes addressing potential biases within these tools and ensuring responsible use that prioritizes fairness, equity, and privacy.

By embracing generative AI, teachers can adapt to evolving educational trends and empower students with valuable skills for a future shaped by technology. 
</thinking>
"""

p2 = """You are an AI assistant designed to provide detailed, step-by-step responses. Your outputs should follow this structure:
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

user question: explain why it is crucial for teachers to learn how to use generative AI for their job and for the future of education.

Include relevant learning path for teachers and educators.
"""

r2 = """<thinking> 
a. This prompt asks me to analyze the importance of generative AI for teachers, outlining a potential learning path. I will need to consider its benefits in teaching practices, address concerns about ethical use, and suggest specific resources for teacher training.

b. My approach is as follows:
1. Analyze the advantages of generative AI for education. 
2. Discuss potential challenges and risks associated with using it.
3. Outline a learning path for teachers to acquire skills in using generative AI effectively. 
4. Conclude by emphasizing the importance of responsible use and ethical considerations.

c. I will utilize a chain-of-thought reasoning process to explain each step, ensuring logical flow and clarity.


</thinking>

<reflection>
The advantages of generative AI for education are significant: it can personalize learning experiences, automate tasks like grading and lesson planning, provide instant feedback, create engaging content, and offer accessibility features. However, concerns about bias in algorithms, plagiarism issues, and the potential displacement of human educators need to be addressed.

</reflection> 
<output>  

Generative AI presents a transformative opportunity for teachers by enabling personalized learning experiences, automating tasks, providing instant feedback, and creating engaging content. It can personalize instruction based on individual student needs and preferences, allowing for more effective teaching strategies. For example, generative AI tools like ChatGPT can be used to create customized lesson plans, provide tailored explanations of complex concepts, generate interactive quizzes, and even write creative assignments that cater to different learning styles. 

However, it's crucial to acknowledge potential risks associated with its use in education:
* **Bias:** Generative AI models are trained on vast datasets which may contain biases reflecting societal inequalities. This can lead to biased outputs if not carefully monitored and addressed.  
* **Plagiarism:** Teachers need guidance on how to differentiate between original work and content generated by AI tools, ensuring students understand the ethical implications of using these technologies. 

To equip teachers with the necessary skills for responsible use, a structured learning path is essential:

1. **Understanding Generative AI Basics:**  Teachers should begin by understanding what generative AI is, its capabilities, limitations, and potential applications in education. Online courses like those offered by Coursera or edX can provide foundational knowledge.
2. **Exploring Specific Tools:** Teachers need hands-on experience with various tools such as ChatGPT for writing prompts, Google Colab for coding assistance, and DALL-E 2 for generating images.  Workshops led by experts in AI education are ideal for this step.
3. **Developing Critical Thinking Skills:** Educators must learn to critically evaluate the output of generative AI, identifying potential biases, inaccuracies, or ethical concerns. This requires training on evaluating sources, understanding plagiarism issues, and promoting responsible use within the classroom. 

By embracing a balanced approach that leverages the benefits while mitigating risks, teachers can effectively integrate generative AI into their teaching practices for a more engaging and personalized learning experience in the future of education.  
</output> 
"""

#generate first message
st.session_state.messages.append({"role": "user", "content": p1})
st.session_state.messages.append({"role": "assistant", "content": full_response})
#generate second message
st.session_state.messages.append({"role": "user", "content": p2})
st.session_state.messages.append({"role": "assistant", "content": r2})

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message(message["role"],avatar=av_us):
            st.markdown(message["content"])
    else:
        with st.chat_message(message["role"],avatar=av_ass):
            # Removing closing TAGS because sometimes skipped by GEMMA2
            t1 = message["content"]
            text = t1.replace('</thinking>','')
            text = text.replace('</output>','')
            text = text.replace('</reflection>','')
            thinking = text.split('<thinking>')[-1].split('<reflection>')[0]
            reflection = text.split('<reflection>')[-1].split('<output>')[0]
            output = text.split('<output>')[-1]            
            with st.container(border=True):
                st.markdown('## THINKING')
                st.markdown(thinking)
            with st.container(border=True):
                st.markdown('## REFLECTION')
                st.markdown(reflection)
            with st.container(border=True):
                st.markdown('## RESPONSE')
                st.markdown(output)                
