import gradio as gr
import os
import openai
from dotenv import load_dotenv

load_dotenv()
# Set OpenAI API key
key = "sk-Wafs"  # Add your actual key here
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
# Import ChatHaruhi
from chatharuhi import ChatHaruhi

text_folder = './roleplayagent/characters/elonmusk/texts'
system_prompt = './roleplayagent/characters/elonmusk/system_prompt.txt'

chatbot = ChatHaruhi(system_prompt=system_prompt, llm='openai', story_text_folder=text_folder)

def chat_with_haruhi(user_input, history):
    response = chatbot.chat(role='user', text=user_input)
    return response

demo = gr.ChatInterface(chat_with_haruhi, type="messages", title = "You are talking to Elon Musk")

demo.launch()
