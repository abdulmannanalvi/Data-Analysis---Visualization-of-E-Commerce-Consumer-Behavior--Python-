import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ecommerce_data.csv')

print(df.head())
print(df.describe())
print(df.isnull().sum())


# Check the data types of the columns
print(df.dtypes)

place_sales = df.groupby('Product_Place')['Product_Sold'].sum().sort_values(ascending=False)
plt.figure(figsize=(10,6))
sns.barplot(x=place_sales, y=place_sales.index)
plt.title('Products Sold by Place')
plt.xlabel('Units Sold')
plt.ylabel('Place')
plt.show()
