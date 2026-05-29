import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

date = np.array([23,24,25,27]).reshape(-1,1)
price = np.array([384,391.70,406.50,398])

poly = PolynomialFeatures(degree=2)
date_poly = poly.fit_transform(date)

model = LinearRegression()
model.fit(date_poly, price)

predicted_price = model.predict(poly.transform([[30]]))

print("Predicted price:", predicted_price)

plt.scatter(date, price)
plt.plot(date, model.predict(date_poly))
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()
