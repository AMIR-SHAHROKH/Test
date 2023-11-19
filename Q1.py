import csv

def calculate_average():
    # Dictionary to store names and their corresponding scores
    student_scores = {}

    # Read data from the input CSV file
    with open('grades.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        
        # Iterate through each row in the CSV file
        for row in reader:
            print(row)
            name = row[0]
            scores = []
            for score in row[1:]:
                if score.isdigit():
                    scores.append(int(score))
                else:  # Convert non-empty score strings to integers
                    print("no can do")
            
            # Calculate average score for each student
            if scores:  # Check if the scores list is not empty
                average_score = sum(scores) / len(scores)
                
                # Store name and average score in the dictionary
                student_scores[name] = average_score

    # Write names and their average scores to a new CSV file
    with open('average.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
                
        # Write each student's name and average score to the CSV file
        for name, average_score in student_scores.items():
            writer.writerow([name, average_score])


def sort_and_display_average():
    # Read data from the 'average.csv' file
    with open('average.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)  # Read all rows into a list

    # Sort data based on the first column (Name)
    sorted_data = sorted(data, key=lambda row: row[0])

    # Write sorted data to 'sorted_average.csv' file
    with open('sorted_average.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write sorted data to the new CSV file
        writer.writerows(sorted_data)

    # Display sorted data in the terminal
    for row in sorted_data:
        print(', '.join(row))  # Display each row in a readable format



def write_top_3():
    # Read data from the 'average.csv' file
    with open('average.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)  # Read all rows into a list
    
    # Sort data based on the second column (Average Score) in descending order
    sorted_data = sorted(data, key=lambda row: float(row[1]), reverse=True)
    
    # Write the top three highest average scores with names to a new CSV file 'top_3.csv'
    with open('top_3.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write top three highest average scores to the CSV file
        for row in sorted_data[:3]:
            writer.writerow(row)



def write_lowest_3():
    # Read data from the 'average.csv' file
    with open('average.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        data = list(reader)  # Read all rows into a list
    
    # Sort data based on the second column (Average Score) in ascending order
    sorted_data = sorted(data, key=lambda row: float(row[1]))
        # Extract and store the lowest scores into a list
    lowest_scores = [row[1] for row in sorted_data]
    # Write the top three lowest average scores with names to a new CSV file 'lowest_3.csv'
    with open('lowest_3.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write top three lowest average scores to the CSV file
        for score in lowest_scores[:3]:
            writer.writerow([score])


def calculate_total_average():
    # Read data from the 'average.csv' file
    with open('average.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        data = list(reader)  # Read all rows into a list
    
    # Extract scores from the second column (index 1)
    scores = [float(row[1]) for row in data]
    
    # Calculate the average of all scores
    total_average = sum(scores) / len(scores)
    
    # Write the total average to a new CSV file 'total_average.csv'
    with open('total_average.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the total average to the CSV file
        writer.writerow(['Total Average'])
        writer.writerow([total_average])
def write_grades_to_csv(name, scores):
    file_path = 'grades.csv'  # Path to the CSV file
    
    # Writing the data to the CSV file
    with open(file_path, mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the name and scores to the CSV file
        writer.writerow([name] + scores)
        csvfile.flush()

# Display menu function
def display_menu():
    print("\nMenu:")
    print("1. Calculate Average")
    print("2. Write Top 3 Highest")
    print("3. Write Lowest 3")
    print("4. Calculate Total Average")
    print("5. Write Grades to CSV")
    print("6. Exit")

def menu():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            calculate_average()
        elif choice == '2':
            write_top_3()
        elif choice == '3':
            write_lowest_3()
        elif choice == '4':
            calculate_total_average()
        elif choice == '5':
            # Get inputs for writing grades to CSV
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
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

# Start the menu
menu()



