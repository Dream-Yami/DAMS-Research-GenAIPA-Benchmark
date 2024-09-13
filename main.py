from LlamaMain import genLlama31Response
import csv
import json

file_path = 'questions.csv'
question_list =[]
answer_list = []

#planning to first get all the questions out the CSV first and store locally
#makes organization easier for the later bits

with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    
    for row in reader:
        if row:
            question_list.append(row[0])
            answer_list.append("")
            
            
# for q in question_list:
#     print(q)
    
#Now with a full list of questions, we can start prompting the ollama server
for i in range(len(question_list)):
    answer_list[i] = genLlama31Response(question_list[i])
    #print(answer_list[i])
    
#With a list of answers, we can simply build and export the json file with answers
qa_Pairs = [{"Question": q, "Answer": a} for q, a in zip(question_list, answer_list)]
json_file_name = 'Llama3-1.json'
with open(json_file_name, 'w', encoding='utf-8') as json_file:
    json.dump(qa_Pairs, json_file, indent=4)
    
print("Completed")