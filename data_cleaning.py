import pandas as pd


def clean_data(df):
    required_columns = [
        "student_id",
        "math_marks",
        "physics_marks",
        "programming_marks",
        "attendance",
        "previous_score"
    ]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    if df[required_columns].isnull().any().any():
        raise ValueError("Dataset contains missing values.")

    if df["student_id"].duplicated().any():
        raise ValueError("Duplicate student IDs found.")

    numeric_columns = [
        "math_marks",
        "physics_marks",
        "programming_marks",
        "attendance",
        "previous_score"
    ]

    for column in numeric_columns:
        if not df[column].between(0, 100).all():
            raise ValueError(
                f"{column} must contain values from 0 to 100."
            )

    return df.copy()