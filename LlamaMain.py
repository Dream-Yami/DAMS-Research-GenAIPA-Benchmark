import ollama

def genLlama31Response(content, policyDoc):
    response = ollama.chat(
        model="llama3.1",
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

def genLlama31Review(annotatedAnswer, LLMAnswer):
    response = ollama.chat(
        model="llama3.1",
        messages=[
            {
                'role': 'system',
                'content': 'You are a grader. You are given 2 responses, one is gnereated by another LLM and the other is the annotated answer. given the annotated answer, evaluate the LLM answer based on 5 criteria. '
                'completeness, clarity, reference, relevance and accuracy. score each metric a -1, +0.5 or +1. -1 means for a confusing or hard-to-comprehend response, +0.5 means somewhat clear but could be improved response, +1 means clear and easy-to-understand response.'
                '. Your reasoning is not required, strictly give only the numerical score. return all messages as an array of JSON'
            },
            {
                "role": "user",
                "content": "LLM generated answer: " + LLMAnswer + " ; Annotated answer: " + annotatedAnswer
            },
        ],
        
        stream=False
    )
    #print(response["message"]["content"])
    return response["message"]["content"]
    
    
if __name__ == '__main__':
    genLlama31Response("This is a test")