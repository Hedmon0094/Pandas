import pandas as pd

# Create a DataFrame with student names and ages
data = pd.DataFrame({
    "Students": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Helen", "Ivy", "Jack"],
    "age": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
}, index=["Age 1", "Age 2", "Age 3", "Age 4", "Age 5", "Age 6", "Age 7", "Age 8", "Age 9", "Age 10"])

print(data)

marks=pd.Series([90, 91, 92, 93, 94, 95, 96, 97, 98, 99], index=["Student 1", "Student 2", "Student 3", "Student 4", "Student 5", "Student 6", "Student 7", "Student 8", "Student 9", "Student 10"], name="Marks Obtained")
print(marks)

