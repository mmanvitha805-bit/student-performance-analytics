import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("students.csv")

print("\n========== STUDENT PERFORMANCE ANALYTICS ==========")


subjects = ["math_marks", "physics_marks", "programming_marks"]
required_columns = [
    "student_id", "math_marks", "physics_marks",
    "programming_marks", "attendance", "previous_score"
]

missing_columns = [
    col for col in required_columns if col not in df.columns
]

if missing_columns:
    print("Missing columns:", missing_columns)
    raise SystemExit("Please check the CSV column names.")


print("\n========== DATA CHECK ==========")
print("Total student records:", len(df))
print("Missing values in each column:")
print(df[required_columns].isnull().sum())


if df[required_columns].isnull().any().any():
    raise SystemExit(
        "Please correct missing values in students.csv before continuing."
    )


for column in subjects + ["previous_score", "attendance"]:
    if not df[column].between(0, 100).all():
        raise SystemExit(
            f"Invalid values in {column}. Values must be from 0 to 100."
        )


print("\n========== SUBJECT-WISE AVERAGES ==========")

for subject in subjects:
    print(f"{subject}: {df[subject].mean():.2f}")



df["average_marks"] = df[subjects].mean(axis=1)

print("\n========== STUDENT PERFORMANCE ==========")
print(df[["student_id", "average_marks"]].to_string(index=False))


highest = df.loc[df["average_marks"].idxmax()]
lowest = df.loc[df["average_marks"].idxmin()]

print("\n HIGHEST PERFORMANCE ")
print("Student ID:", highest["student_id"])
print("Average marks:", round(highest["average_marks"], 2))

print("\n LOWEST PERFORMANCE ")
print("Student ID:", lowest["student_id"])
print("Average marks:", round(lowest["average_marks"], 2))

df["result"] = df["average_marks"].apply(
    lambda mark: "Pass" if mark >= 40 else "Fail"
)

pass_count = (df["result"] == "Pass").sum()
fail_count = (df["result"] == "Fail").sum()
pass_percentage = pass_count / len(df) * 100

print("\n CLASS RESULTS ")
print("Total students:", len(df))
print("Students passed:", pass_count)
print("Students failed:", fail_count)
print("Pass percentage:", round(pass_percentage, 2), "%")


subject_averages = df[subjects].mean()

plt.figure(figsize=(8, 5))
subject_averages.plot(kind="bar")

plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()  


plt.figure(figsize=(8, 5))

plt.hist(
    df["average_marks"],
    bins=10,
    edgecolor="black"
)

plt.title("Distribution of Student Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.tight_layout()

plt.show()


print("\nANALYSIS COMPLETED ")
print("Student performance analysis completed successfully.")