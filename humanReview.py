import os
import csv

def get_metrics():
    valid_values = {-1, 0.5, 1}
    while True:
        try:
            completeness = float(input("Enter Completeness (-1, 0.5, 1): "))
            clarity = float(input("Enter Clarity (-1, 0.5, 1): "))
            reference = float(input("Enter Reference (-1, 0.5, 1): "))
            relevance = float(input("Enter Relevance (-1, 0.5, 1): "))
            accuracy = float(input("Enter Accuracy (-1, 0.5, 1): "))
            
            if all(val in valid_values for val in [completeness, clarity, reference, relevance, accuracy]):
                return (completeness, clarity, reference, relevance, accuracy)
            else:
                print("All values must be -1, 0.5, or 1.")
        except ValueError:
            print("Invalid input. Please enter -1, 0.5, or 1.")

def main():
    directory = "humanData"
    #Sub Directory is for us to write to that will hold each company name. Make sure the first letter is capitalized.
    sub_directory = input("Enter a subdirectory name (this should be the company, with first letter capitalized): ").strip()
    #Ex: humanData/Uber/
   
    os.makedirs(directory, exist_ok=True)
    if sub_directory:
        sub_directory_path = os.path.join(directory, sub_directory)
        os.makedirs(sub_directory_path, exist_ok=True)
    else:
        sub_directory_path = directory

    file_name = input("Enter the name of the LLM reviewing: ")
    file_name += input("Enter the Experiment number as a word (Ex: One, Two, Three...): ") + ".csv"
    file_path = os.path.join(sub_directory_path, file_name)
    #Ex: humanData/Uber/Qwen2ExpOne
    
    n = int(input("Enter the number of entries you want to make: "))
    
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(['Entry Number', 'Completeness', 'Clarity', 'Reference', 'Relevance', 'Accuracy'])

        for i in range(1, n + 1):
            print(f"Entry {i} of {n}:")
            metrics = get_metrics()
            writer.writerow([i, *metrics])
            print(f"Written: {i}: (Completeness: {metrics[0]}, Clarity: {metrics[1]}, Reference: {metrics[2]}, Relevance: {metrics[3]}, Accuracy: {metrics[4]}) to {file_path}")

    print(f"All entries have been written to {file_path}")

if __name__ == "__main__":
    main()

#If you read this, we can use this to skip the formatting later and read of this file when neaded.