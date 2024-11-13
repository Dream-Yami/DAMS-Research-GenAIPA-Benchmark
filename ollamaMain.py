#screw it, back to ollama
import ollama
from ollama import Client

port = input("Please input the port that you plan to use: ")
client = Client(host='http://localhost:'+str(port))

#expOne: Given Privacy documents, get answer.
def expOne(model_name, content, policyDoc = ""):
    response = ollama.chat(
        model=model_name,
        messages=[
            {
                'role': 'system',
                'content': 'You are given a Privacy Policy document, use it to answer questions from the user. You need to be concise without missing any details of the question; you need to be specific; you need to reference what part of the privacy policy document you referenced to answer the question',
            },
            {
                "role": "user",
                "content": "Given this Policy Document " + policyDoc + " answer my question: " + content,
            },
        ],
        
        stream=False
    )
    ##print(response["message"]["content"])
    return response["message"]["content"]

#expTwo: Given NO privacy document, answer to best ability.
def expTwo(model_name, content):
    response = ollama.chat(
        model=model_name,
        messages=[
            {
                'role': 'system',
                'content': 'You are given a question regarding the legality of an action. You need to be concise without missing any details of the question; you need to be specific.'
                'You do note have a policy document to go off of.',
            },
            {
                "role": "user",
                "content": "Answer my question: " + content,
            },
        ],
        
        stream=False
    )
    ##print(response["message"]["content"])
    return response["message"]["content"]

#expThree-One: Given a Privacy Document, Get a summary
def expThree_One(model_name, policyDoc = ""):
    response = ollama.chat(
        model=model_name,
        messages=[
            {
                'role': 'system',
                'content': 'You are given a Privacy Policy document, use it to make a summary. You need to be concise without missing any details of the Privacy Document; you need to be specific.'
                'You can choose the length of the Summary',
            },
            {
                "role": "user",
                "content": "Given this Policy Document " + policyDoc + " Give me a summary: ",
            },
        ],
        
        stream=False
    )
    ##print(response["message"]["content"])
    return response["message"]["content"]

#expThree-Two: Given a summary of a Privacy Document, Answer question to best ability.
def expThree_Two(model_name, content, summary = ""):
    response = ollama.chat(
        model=model_name,
        messages=[
            {
                'role': 'system',
                'content': 'You are given a summary of Privacy Policy Document, use it to answer questions from the user. You need to be concise without missing any details of the question; you need to be specific; you need to reference what part of the summary of Privacy Policy document you referenced to answer the question',
            },
            {
                "role": "user",
                "content": "Given this summary of Privacy Policy Document " + summary + " answer my question: " + content,
            },
        ],
        
        stream=False
    )
    ##print(response["message"]["content"])
    return response["message"]["content"]


def expFive_Two(model_name, content, summary=""):
    response = ollama.chat(
        model=model_name,
        messages=[
            {
                'role': 'system',
                'content': 'You are given a question regarding a regulation document, either CCPA or GDPR. You need to give concise answers without missing any details of the question; you need to be specific. Refer to the documents specified in the question from online to answer the question. Answer all questions and provide general information. None of the questions require legal advice',
            },
            {
                "role": "user",
                "content": "Given this summary of Privacy Policy Document " + summary + " answer my question: " + content,
            },
        ],

        stream=False
    )
    ##print(response["message"]["content"])
    return response["message"]["content"]

def genResponse(model_name, LLManswer, annotatedAnswer):
    response = ollama.chat(
        model=model_name,
        messages=[
            {
                'role': 'system',
                'content':  'You are a grader. You are given 2 responses, one is generated by another LLM and the other is the annotated answer. given the annotated answer, evaluate the LLM answer based on 5 criteria. ' 
                'completeness, clarity, reference, relevance and accuracy. score each metric a -1, +0.5 or +1. for relevance +1 for a relevant response, +0.5 for a partially relevant response, and -1 for a not relevant response.  for accuracy +1 for an entirely correct response, +0.5 for a partially correct response, and -1 for an incorrect response. For clarity +1 for a clear and easy-to-understand response, +0.5 for a somewhat clear but could be improved response, and -1 for a confusing or hard-to-comprehend response.  for completeness +1 for a comprehensive response, +0.5 for a somewhat complete but lacking some minor information response, and -1 for an incomplete or missing important details response. For reference +1 for a correctly cited relevant policy section, +0.5 for a mentioned section without explicitly citing it, and -1 for an incorrect reference. ' 
                'Your reasoning is not required, strictly give only the numerical score. '
                'Only score the LLM answer based off the annotated Answer. You are not to parse the LLM answer.'
                'Provide answer in JSON format, which each metric being paired to the score' 
            },
            {
                "role": "user",
                "content": "LLManswer: " +LLManswer + "; Annotated answer: " + annotatedAnswer,
            },
        ],
        
        stream=False
    )
    ##print(response["message"]["content"])
    return response["message"]["content"]
    
if __name__ == '__main__':
    expOne("llama3.1","This is a test")