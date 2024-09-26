#screw it, back to ollama
import ollama

def genFalcoResponse(content, policyDoc):
    response = ollama.chat(
        model="falcon",
        messages=[
            {
                'role': 'system',
                'content': 'You must answer accurately, with relevance, clearly, in a complete answer, and reference where in the Policy document you got the answer',
            },
            {
                "role": "user",
                "content": "Given this Policy Document " +policyDoc + " answer my question: " + content,
            },
        ],
        
        stream=False
    )
    #print(response["message"]["content"])
    return response["message"]["content"]
    
    
if __name__ == '__main__':
    genFalcoResponse("This is a test")