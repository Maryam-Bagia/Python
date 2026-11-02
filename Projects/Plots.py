import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)
categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 40]
random_data = np.random.randn(100)
df = sns.load_dataset("tips")  # Built-in seaborn dataset

# 1. Line Plot
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Sine Wave', color='blue')
plt.title("Line Plot")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
plt.grid(True)
plt.show()

# 2. Bar Plot
plt.figure(figsize=(6, 4))
plt.bar(categories, values, color='teal')
plt.title("Bar Plot")
plt.ylabel("Values")
plt.show()

# 3. Histogram
plt.figure(figsize=(6, 4))
plt.hist(random_data, bins=20, color='orange', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot
plt.figure(figsize=(6, 4))
plt.scatter(df['total_bill'], df['tip'], alpha=0.7, color='purple')
plt.title("Scatter Plot")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

# 5. Box Plot
plt.figure(figsize=(6, 4))
sns.boxplot(x='day', y='total_bill', data=df)
plt.title("Box Plot")
plt.show()

# 6. Violin Plot
plt.figure(figsize=(6, 4))
sns.violinplot(x='day', y='total_bill', data=df)
plt.title("Violin Plot")
plt.show()

# 7. Pie Chart
plt.figure(figsize=(6, 6))
plt.pie(values, labels=categories, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title("Pie Chart")
plt.show()

# 8. Heatmap
plt.figure(figsize=(6, 5))
correlation = df.corr(numeric_only=True)
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Heatmap")
plt.show()