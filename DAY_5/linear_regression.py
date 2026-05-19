import numpy as np
import matplotlib.pyplot as plt

study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8])
student_marks = np.array([40, 50, 55, 65, 70, 80, 85, 92])

slope, intercept = np.polyfit(study_hours, student_marks, 1)

print(f"Prediction Formula: Marks = {slope:.2f} × Hours + {intercept:.2f}")

predicted_marks = slope * 5 + intercept
print(f"Estimated marks for studying 5 hours: {predicted_marks:.1f}")

plt.scatter(study_hours, student_marks)
plt.plot(study_hours, slope * study_hours + intercept)

plt.title("Study Hours vs Student Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.savefig("student_marks_prediction.png")
plt.show()