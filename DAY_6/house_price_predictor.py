from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

sizes = np.array([[500], [750], [1000], [1200], [1500], [2000]])
prices = np.array([25, 38, 50, 60, 75, 100])

model = LinearRegression()
model.fit(sizes, prices)

user_input = 1100
result = model.predict([[user_input]])

print(f"\nEstimated price for {user_input} sqft house: Rs.{result[0]:.2f} Lakhs")
print(f"Prediction Accuracy: {model.score(sizes, prices):.2%}")

plt.scatter(sizes, prices)

plt.plot(sizes, model.predict(sizes))

plt.scatter(user_input, result[0])

plt.xlabel("House Size (sqft)")
plt.ylabel("Price (Lakhs)")
plt.title("House Price Prediction")

plt.savefig("output.png")

plt.show()