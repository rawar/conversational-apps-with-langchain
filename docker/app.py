import requests
import json
import os
import gradio as gr
from langchain_openai import AzureChatOpenAI
    
context = []
os.environ.get("AZURE_OPENAI_API_KEY") 
os.environ.get("AZURE_OPENAI_ENDPOINT") 

def generate(prompt, context, temp):

    llm = AzureChatOpenAI(
        openai_api_version="2023-05-15",
        azure_deployment="ramwar-chatgpt", 
        temperature=temp,
    )

    response = llm.invoke(prompt)
    return response.content, context

def chat(input, chat_history, temp):

    chat_history = chat_history or []
    global context
    output, context = generate(input, context, temp)
    chat_history.append((input, output))
    return chat_history, chat_history
  
#########################Gradio Code##########################
block = gr.Blocks()


with block:

    gr.Markdown("""<h1><center>Simple GRadio Chat App</center></h1>
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
        temp = gr.Slider(0.0,2.0, label="temperature", value=0.8, info="The temperature of the model. Increasing the temperature will make the model answer more creatively. (Default: 0.8)")

    submit = gr.Button("SEND")
    submit.click(chat, inputs=[message, state, temp], outputs=[chatbot, state])

block.launch(debug=True)