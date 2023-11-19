import csv

def write_grades_to_csv(name, scores):
    file_path = 'grades.csv'  # Path to the CSV file
    
    # Writing the data to the CSV file
    with open(file_path, mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the name and scores to the CSV file
        writer.writerow([name] + scores)
        csvfile.flush()
while True:
    try:
        name = input("Enter student's name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        
        scores_input = input("Enter scores separated by spaces: ")
        if scores_input.lower() == 'done':
            break
        
        scores = list(map(int, scores_input.split()))
        print(scores) 
        write_grades_to_csv(name, scores)

    
    except Exception as e:
        print("An error occurred:", e)

