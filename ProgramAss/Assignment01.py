# Function to create a file with student data
def create_result_file(file_path):
    grade_points = {'O': 10, 'A': 9, 'B': 8, 'C': 7, 'D': 6, 'U': 0}

    with open(file_path, "w") as fp:
        for _ in range(30):  # Adjusted to create data for 30 students
            name = input("Enter the name of the student: ")
            reg_no = input("Enter register number of the student: ")
            grades = [input(f"Enter grade for subject {i+1}: ") for i in range(5)]

            total_marks = 0
            has_arrear = False
            for grade in grades:
                if grade == 'U':
                    has_arrear = True
                    total_marks = 0
                    break
                else:
                    total_marks += grade_points[grade]

            total_marks *= 4  # Considering each subject has 4 credits
            percentage = (total_marks / 200) * 100

            student_data = [name, reg_no] + grades + [str(total_marks), f"{percentage:.2f}"]
            fp.write(','.join(student_data) + '\n')

# Function to read and display file content
def read_result_file(file_path):
    with open(file_path, "r") as fp:
        content = fp.readlines()
        for line in content:
            print(line.strip())

# Function to analyze student data
def analyze_results(file_path):
    grade_category = {
        "90 and above": [],
        "80% to 89.99%": [],
        "70% to 79.99%": [],
        "Below 70%": [],
        "Arrear": []
    }

    with open(file_path, "r") as fp:
        details = fp.readlines()
        for line in details:
            parts = line.strip().split(',')
            name, reg_no = parts[0], parts[1]
            grades = parts[2:7]
            total_marks = int(parts[7])
            percentage = float(parts[8])

            if 'U' in grades:
                grade_category["Arrear"].append(name)
            elif percentage >= 90:
                grade_category["90 and above"].append(name)
            elif percentage >= 80:
                grade_category["80% to 89.99%"].append(name)
            elif percentage >= 70:
                grade_category["70% to 79.99%"].append(name)
            else:
                grade_category["Below 70%"].append(name)

    for category, students in grade_category.items():
        print(f"Students {category}: {', '.join(students)}")

# File path for results
result_file_path = "result.txt"

# Creating the result file with student data
create_result_file(result_file_path)

# Reading and displaying the result file content
print("\nResult File Content:")
read_result_file(result_file_path)

# Analyzing the results and displaying the analysis
print("\nAnalysis:")
analyze_results(result_file_path)
