from ollamaMain import genResponse, expOne, expTwo, expThree_One, expThree_Two
import csv
import json
import time
import os

#Initialize variables for later use. Makes file access harder.
models = ["llama3.1", "mistral", "gemma2", "qwen2", "llava"]
#These are default values for now, they will get changed throughout the process
questionFile = 'PrivacyPolicyQuestions.csv'
answerFile = 'annotatedAnswer.csv'
policyFile = 'document.txt'
company = ''
question_list =[]
annotated_answer_list = []
answerDict = {}
startTime = time.time()

def reset():
    global answerFile
    global policyFile
    answerFile = 'annotatedAnswer.csv'
    policyFile = 'document.txt'
    
def changeGlobals():
    global answerFile
    global policyFile
    answerFile = company + 'annotatedAnswer.csv'
    policyFile = company + 'document.txt'

for i in range(len(models)):
    answerDict[models[i]] = []
    
LLM_Scores = {}
#The dictionary is gonna have a key and pair
#Key - The model that got the answer
#Pair - A tuple that holds the question, the reviewing model, and the metrics the reviewing model gave for the key model
for i in range(len(models)):
    LLM_Scores[models[i]] = []

#planning to first get all the questions out the CSV first and store locally
#makes organization easier for the later bits
def readPolicyDocuments(file_path):
    with open(file_path, "r") as file:
        return file.read().replace("\n", " ") # replace newline with space

def readAnswers(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter='\n')
        for row in reader:
            if row:
                annotated_answer_list.append(row[0])

def readQuestions(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter='\n')
        for row in reader:
            if row:
                question_list.append(row[0])
                
            
#Now with a full list of questions, we can start prompting the ollama server
def expOneModelCall(policyDoc):
    for i in range(len(question_list)):
        for j  in range(len(models)):
            answerDict[models[j]].append(expOne(models[j], question_list[i], policyDoc))
            #print(models[j], answerDict[models[j]])
            
def expTwoModelCall():
    for i in range(len(question_list)):
        for j  in range(len(models)):
            answerDict[models[j]].append(expTwo(models[j], question_list[i]))
            #print(models[j], answerDict[models[j]])
            
def expThreeModelCall(policyDoc):
    for i in range(len(question_list)):
        model_summaries = []
        for j  in range(len(models)):
            model_summaries.append(expThree_One(models[j], policyDoc))
            #print(models[j], model_summaries[j])
            answerDict[models[j]].append(expThree_Two(models[j], question_list[i], model_summaries[j]))
            #print(models[j], answerDict[models[j]])
    
#With a list of answers, we can simply build and export the json file with answers
def package(list, name):
    os.makedirs(company, exist_ok=True)
    qa_Pairs = [{"Question": q, "Answer": a} for q, a in zip(question_list, list)]
    json_file_name = company + "/" + name + '.json'
    with open(json_file_name, 'w', encoding='utf-8') as json_file:
        json.dump(qa_Pairs, json_file, indent=4)

# #Experiments
def packageExp(modelList, name, experiment = ''):
    model_Pairs = []
    os.makedirs(company, exist_ok=True)
    for i in range(len(modelList)):
        reviewer, question, score = modelList[i]
        model_Pairs.append({
            "Question": question,
            "Reviewer": reviewer,
            "Score": score
        })
    json_file_name = company + "/" + name + experiment + '.json'
    with open(json_file_name, 'w', encoding='utf-8') as json_file:
        json.dump(model_Pairs, json_file, indent=4)
        
def packageExpParent(revList, experiment=''):
    for model in revList:
        packageExp(revList[model], model, experiment)

def reviewAnswers(experimentName):
    #I, will be the answer we are reviewing
    for i in range(len(annotated_answer_list)):
        #J will be the model's answer to be reviewed
        for j in range(len(models)):
            #k will be the model to review J's answer
            for k in range(len(models)):
                if j != k:
                    LLM_Scores[models[j]].append((models[k], question_list[i], genResponse(models[k], answerDict[models[j]][i], annotated_answer_list[i])))
    #print(LLM_Scores)
    packageExpParent(LLM_Scores, experimentName)

def experimentOne():
    policyString = readPolicyDocuments(policyFile)
    ##print(policyString)
    readAnswers(answerFile)
    readQuestions(questionFile)
    print("Beginning Answers")
    expOneModelCall(policyString)
    print("Beginning Reviews")
    for i in range(len(models)):
        package(answerDict[models[i]], models[i])
    reviewAnswers("ExpOne")
    
def experimentTwo():
    #policyString = readPolicyDocuments(policyFile)
    ##print(policyString)
    readAnswers(answerFile)
    readQuestions(questionFile)
    expTwoModelCall()
    for i in range(len(models)):
        package(answerDict[models[i]], models[i])
    reviewAnswers("ExpTwo")
    
def experimentThree():
    policyString = readPolicyDocuments(policyFile)
    ##print(policyString)
    readAnswers(answerFile)
    readQuestions(questionFile)
    expThreeModelCall(policyString)
    for i in range(len(models)):
        package(answerDict[models[i]], models[i])
    reviewAnswers("ExpThree")

def run(companyName):
    global company
    company = companyName
    changeGlobals()
    experimentOne()
    #experimentTwo()
    #experimentThree()
    print((time.time() - startTime)/60, " Minutes")
    print("completed")
    reset()

if __name__ == '__main__':
    run("Spotify")