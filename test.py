import json
import os
question_list = ["Ha"]
list = ["he"]

def package(list, name):
    qa_Pairs = [{"Question": q, "Answer": a} for q, a in zip(question_list, list)]
    json_file_name = "test/" + name + '.json'
    os.makedirs("test", exist_ok=True)
    with open(json_file_name, 'w', encoding='utf-8') as json_file:
        json.dump(qa_Pairs, json_file, indent=4)
        
package(list, "hehe")