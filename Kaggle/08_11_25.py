import pandas as pd

data = pd.read_csv('melb_data.csv')
print(data.columns)

# dropna drops missing values (think of na as "not available")
data = data.dropna(axis=0)

# Dot notation, which we use to select the "prediction target"
price = data.Price
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

results = model.predict(req_data.head(10))

for i in results:
    print(i)