import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ecommerce_data.csv')

print(df.head())
print(df.describe())
print(df.isnull().sum())


# Check the data types of the columns
print(df.dtypes)

#Distribution of Product Prices
plt.figure(figsize=(10,6))
sns.histplot(df['Product_Price'], bins=30, kde=True)
plt.title('Distribution of Product Prices')
plt.xlabel('Price')
plt.show()


