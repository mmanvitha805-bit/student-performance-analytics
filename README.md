
Student Performance Analytics and Prediction System

1. Project Overview

The Student Performance Analytics and Prediction System is a Python-based project developed to analyze student academic performance using marks, attendance, and previous academic scores.

The system validates student data, calculates subject-wise and individual average marks, analyzes overall performance, generates graphical visualizations, and uses a Linear Regression model to estimate student average marks.

The project demonstrates the practical application of data analysis, data visualization, machine learning, software testing, and performance profiling.

2. Problem Statement

Analyzing student performance manually can be time-consuming when working with multiple student records and subjects. It can also be difficult to compare subject-wise performance and understand the distribution of student marks.

This project addresses these challenges by automating data validation, statistical analysis, visualization, and performance prediction using Python.

3. Project Objectives

- Validate and clean student performance data.
- Calculate average marks for each subject.
- Calculate individual student average marks.
- Analyze overall student performance and class pass percentage.
- Generate graphs to visualize academic performance.
- Develop and evaluate a Linear Regression prediction model.
- Test the correctness of the implemented functions.
- Measure program execution performance through profiling.

4. Dataset Description

The project uses a CSV dataset containing student academic records.

The dataset includes the following attributes:

Column| Description
"student_id"| Unique identifier for each student
"math_marks"| Marks obtained in Mathematics
"physics_marks"| Marks obtained in Physics
"programming_marks"| Marks obtained in Programming
"attendance"| Student attendance percentage
"previous_score"| Previous academic score

Marks, attendance, and previous scores are expected to fall within the range of 0 to 100.

The program checks for missing values, duplicate student IDs, required columns, and invalid numerical values before analysis.

5. Technologies Used

- Python — Main programming language.
- Pandas — Data processing and statistical analysis.
- Matplotlib — Graph generation and data visualization.
- Scikit-learn — Linear Regression and model evaluation.
- CSV — Dataset storage format.
- Git and GitHub — Version control and project hosting.
- VS Code — Code development and execution.
- LaTeX and Overleaf — Report and presentation preparation.

6. Project Features

6.1 Data Validation

Validates the dataset by checking required columns, missing values, duplicate student IDs, and numerical ranges.

6.2 Statistical Analysis

Calculates subject-wise average marks, individual student average marks, and class pass percentage.

6.3 Data Visualization

Generates two main visualizations:

1. Average Marks by Subject: A bar chart comparing average marks in Mathematics, Physics, and Programming.
2. Distribution of Student Average Marks: A histogram showing the distribution of students' average marks.

6.4 Performance Prediction

Uses Linear Regression to estimate student average marks based on previous academic score and attendance percentage.

6.5 Testing and Profiling

Uses automated tests to check selected data-validation and calculation functions. Profiling tools can be used to inspect program execution time and function-level performance.

7. Project Workflow

    1. Load student records from the CSV dataset.
    2. Validate the dataset and check data quality.
    3. Calculate subject-wise and individual student averages.
    4. Calculate the class pass percentage.
    5. Generate visualizations using Matplotlib.
    6. Train and evaluate the Linear Regression model.
    7. Run automated tests.
    8. Profile program execution.
    9. Prepare the results, report, and presentation.


8. Installation and Setup

Prerequisites

- Python installed on the system.
- Git installed for version control.
- A terminal such as the VS Code terminal or Git Bash.

Install Dependencies

Run the following command from the project root directory:

python -m pip install -r requirements.txt

9. How to Run the Project

Run the commands that match your current project structure.

Run the Main Analysis

python main.py

This runs the data validation, statistical analysis, and visualization workflow.

Run the Prediction Model

python prediction.py

This runs the Linear Regression prediction program.

Run the Complete Project Script

In a Bash-compatible terminal, such as Git Bash on Windows, run:

bash run_project.sh

Run Automated Tests

python -m unittest discover -s tests -v

Run Performance Profiling

If the profiling script is located at "src/profile_project.py", run:

python profile_project.py

10. Results and Evaluation

The project produces subject-wise average marks, individual student average marks, class pass percentage, and graphical summaries of student performance.

The prediction model is evaluated using Mean Absolute Error (MAE), which measures the average absolute difference between predicted and actual marks on the evaluation data.

Record the final measured subject averages, pass percentage, number of records analyzed, and model evaluation results after running the current version of the program.

Only report numerical results that have been verified from the actual program output.


11. Conclusion

The Student Performance Analytics and Prediction System demonstrates how Python, data analysis, visualization, and machine learning can be used to study student academic performance.

The system automates data validation and statistical calculations, provides graphical insights, and estimates average marks using Linear Regression. Testing and performance profiling can further help assess the correctness and efficiency of the implementation.

12. Project Documentation

The "docs/" directory contains the LaTeX source files for the project report and presentation. These documents describe the project's objectives, methodology, results, and conclusions.

13. Repository

GitHub repository: https://github.com/mmanvitha805-bit/student-performance-analytics

Institution: Indian Institute of Technology Dharwad

Project: Student Performance Analytics and Prediction System