import requests
import json
import gradio as gr
from langchain_community.chat_models import ChatOllama
    

model = 'gemma:7b' #You can replace the model name if needed
context = [] 

def generate(prompt, context, top_k, top_p, temp):
    llm = ChatOllama(base_url="http://localhost:11434", model="gemma:7b", temperature=temp, top_k=top_k, top_p=top_p, context=context)
    response = llm.invoke(prompt)
    return response.content, context

def chat(input, chat_history, top_k, top_p, temp):

    chat_history = chat_history or []
    global context
    output, context = generate(input, context, top_k, top_p, temp)
    chat_history.append((input, output))
    return chat_history, chat_history
  
#########################Gradio Code##########################
block = gr.Blocks()


with block:

    gr.Markdown("""<h1><center>GRadio Ollama App</center></h1>
    """)

    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder="Type here")

    gr.Examples(
        examples=[
            "Why is the sky blue?",
            "What should I do tonight in New York City?",
            "Whats 2 + 2?",
        ],
        inputs=message,
    )

    state = gr.State()
    with gr.Row():
        top_k = gr.Slider(0.0,100.0, label="top_k", value=40, info="Reduces the probability of generating nonsense. A higher value (e.g. 100) will give more diverse answers, while a lower value (e.g. 10) will be more conservative. (Default: 40)")
        top_p = gr.Slider(0.0,1.0, label="top_p", value=0.9, info=" Works together with top-k. A higher value (e.g., 0.95) will lead to more diverse text, while a lower value (e.g., 0.5) will generate more focused and conservative text. (Default: 0.9)")
        temp = gr.Slider(0.0,2.0, label="temperature", value=0.8, info="The temperature of the model. Increasing the temperature will make the model answer more creatively. (Default: 0.8)")

    submit = gr.Button("SEND")
    submit.click(chat, inputs=[message, state, top_k, top_p, temp], outputs=[chatbot, state])

block.launch(debug=True)