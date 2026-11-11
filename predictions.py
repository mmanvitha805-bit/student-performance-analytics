import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


df = pd.read_csv("students.csv")


X = df[["previous_score", "attendance"]]
y = df[["math_marks", "physics_marks", "programming_marks"]].mean(axis=1)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)


predictions = model.predict(X_test)
error = mean_absolute_error(y_test, predictions)

print("===== MODEL EVALUATION =====")
print("Mean Absolute Error:", round(error, 2), "marks")


previous_score = float(input("\nEnter previous score (0-100): "))
attendance = float(input("Enter attendance percentage (0-100): "))

if not (0 <= previous_score <= 100 and 0 <= attendance <= 100):
    print("Error: Enter values between 0 and 100.")
else:
    new_student = pd.DataFrame({
        "previous_score": [previous_score],
        "attendance": [attendance]
    })

    predicted_score = model.predict(new_student)[0]
    predicted_score = max(0, min(100, predicted_score))

    print("\n===== PREDICTION RESULT =====")
    print("Estimated average marks:", round(predicted_score, 2), "/ 100")
    print("This is an estimate, not a guaranteed result.")