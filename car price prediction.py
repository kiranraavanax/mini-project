import pandas as pd

# Load the CSV file
car = pd.read_csv('cars.csv')

# Display the first few rows of the DataFrame
print(car.head())

# Check for missing values
print(car.isnull().sum())

# Fill NaN values in 'kms_driven' using forward fill
car['kms_driven'] = car['kms_driven'].fillna(method='ffill')

# Create a backup of the original DataFrame
backup = car.copy()

# Ensure 'year' is treated as string
car['year'] = car['year'].astype(str)

# Filter out rows where 'year' is not numeric
car = car[car['year'].str.isnumeric()]

# Convert the 'year' column to integer
car['year'] = car['year'].astype(int)

# Remove rows where 'Price' is "Ask For Price"
car = car[car['Price'] != "Ask For Price"]

# Now safely remove commas from 'Price' and convert to integer
car['Price'] = car['Price'].str.replace(',', '').astype(int)

# Display the cleaned DataFrame
print(car.head())

# Clean 'kms_driven' column: Remove ' kms' and commas, then convert to integer
car['kms_driven'] = car['kms_driven'].str.replace(' kms', '').str.replace(',', '')

# Check for any non-numeric values in 'kms_driven' before conversion
print(car['kms_driven'].unique())

# Convert to integer
car['kms_driven'] = car['kms_driven'].astype(int)

# Display the cleaned DataFrame again
print(car.head())

x=car.drop(columns='Price')
y=car['Price']

from sklearn.model_selection import train_test_split
x_train,y_train,x_test,y_test=train_test_split(x,y,test_size=0.2)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline

ohe=OneHotEncoder()
ohe.fit(x[['name','company','fuel_type']])

