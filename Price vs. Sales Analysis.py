import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ecommerce_data.csv')

print(df.head())
print(df.describe())
print(df.isnull().sum())


# Check the data types of the columns
print(df.dtypes)

plt.figure(figsize=(10,6))
sns.scatterplot(x='Product_Price', y='Product_Sold', data=df, hue='Product_Category')
plt.title('Price vs Sales by Category')
plt.xlabel('Price')
plt.ylabel('Units Sold')
plt.show()
