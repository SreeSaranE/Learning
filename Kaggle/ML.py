import pandas as pd

data = pd.read_csv('melb_data.csv')
print("Data Coloums:\n")
print(data.columns)

# dropna drops missing values (think of na as "not available")
data = data.dropna(axis=0)

# Dot notation, which we use to select the "prediction target"
price = data.Price
print("Price:\n")
print(price)

# The columns that are inputted into our model (and later used to make predictions) are called "features".
features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

req_data = data[features]
print(req_data.describe())
print(req_data.head())

print("-"*100)

from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor(random_state=1)

model.fit(req_data, price)

results = model.predict(req_data)

count = 0
for i in results:
    print(i)
    count += 1
    if count == 10:
        break

print("-"*100, "\n")


# In MAE metric, we take the absolute value of each error.
# This converts each error to a positive number.
# We then take the average of those absolute errors.
# error=actual−predicted
from sklearn.metrics import mean_absolute_error

print("Mean Absolute Error:", end=" ")
print(round(mean_absolute_error(price, results)))

# function train_test_split to break up the data into two pieces.
# We'll use some of that data as training data to fit the model,
# and we'll use the other data as validation data to calculate mean_absolute_error