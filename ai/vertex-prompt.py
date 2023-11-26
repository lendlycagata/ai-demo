import os
import vertexai

PROJECT_ID = "igneous-sweep-404400"  
LOCATION = "northamerica-northeast1" 

vertexai.init(project=PROJECT_ID, location=LOCATION)

def create_session():
    chat_model = vertexai.language_models.ChatModel.from_pretrained("chat-bison@001")
    chat = chat_model.start_chat()
    return chat

def response(chat, message):
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 256,
        "top_p": 0.8,
        "top_k": 40
    }
    result = chat.send_message(message, **parameters)
    return result.text

def run_chat(query):
    chat_model = create_session()
    print(query)
    
    while True:
        user_input = input(f"You: {query}")
        if user_input.lower() in ['exit', 'quit']:
            break
        
        content = response(chat_model, user_input)
        print(f"AI: {content}")
        return content

if __name__ == '__main__':
    run_chat()