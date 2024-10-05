import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ecommerce_data.csv')

print(df.head())
print(df.describe())
print(df.isnull().sum())


# Check the data types of the columns
print(df.dtypes)

category_sales = df.groupby('Product_Category')['Product_Sold'].sum().sort_values(ascending=False)
plt.figure(figsize=(10,6))
sns.barplot(x=category_sales, y=category_sales.index)
plt.title('Products Sold by Category')
plt.xlabel('Units Sold')
plt.ylabel('Category')
plt.show()
