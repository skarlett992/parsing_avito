import json
from catboost import CatBoostRegressor
from keras.losses import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split


from sklearn.preprocessing import LabelEncoder
import pandas as pd


with open('rooms_df.json', 'r') as file:
    df = json.load(file)
# data = pd.read_json('file.json')
# data = pd.read_csv(rooms_df.csv)
# df = pd.json_normalize(df)

print(df.head(3))
print(df['price, rub'])
y = df['price, rub']
# data = data_X.drop(['Item_Outlet_Sales', 'Name_Item_Identifier'], axis=1)

x = df.drop(['price, rub', 'metro', 'lat', 'colors', 'address', 'url',
               'metro_distance', 'station_1', 'station_2', 'station_3',
               'metro_distance_1', 'metro_distance_2', 'metro_distance_3'], axis=1)
print(x.shape, y.shape)
X_train, X_test, y_train, y_test = train_test_split(x,y)

model_cat = CatBoostRegressor()
model_cat.fit(X_train, y_train)
y_pred_test = model_cat.predict(X_test)
y_pred_train = model_cat.predict(X_train)
print(mean_squared_error(y_train, y_pred_train), mean_squared_error(y_test, y_pred_test))
print(r2_score(y_train, y_pred_train), r2_score(y_test, y_pred_test)  )
