import pandas as pd


def calculate_subject_averages(df):
    subjects = [
        "math_marks",
        "physics_marks",
        "programming_marks"
    ]
    return df[subjects].mean()


def calculate_student_averages(df):
    subjects = [
        "math_marks",
        "physics_marks",
        "programming_marks"
    ]
    result = df.copy()
    result["average_marks"] = result[subjects].mean(axis=1)
    return result


def calculate_pass_percentage(df, pass_mark=40):
    averages = calculate_student_averages(df)
    passed = (averages["average_marks"] >= pass_mark).sum()
    return passed / len(averages) * 100 if len(averages) else 0