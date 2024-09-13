import ollama

def genLlama31Response(content):
    response = ollama.chat(
        model="llama3.1",
        messages=[
            {
                "role": "user",
                "content": content,
            },
        ],
        stream=False
    )
    print(response["message"]["content"])
    return response["message"]["content"]
    
    
if __name__ == '__main__':
    genLlama31Response("This is a test")