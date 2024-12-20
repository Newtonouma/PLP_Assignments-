import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Task 1: Load and Explore the Dataset

df = pd.read_csv('path_to_your_dataset.csv')

print("First few rows of the dataset:")
print(df.head())

print("\nDataset Information (Data types and Missing values):")
print(df.info())

print("\nMissing values in each column:")
print(df.isnull().sum())

# Task 2: Basic Data Analysis

print("\nBasic statistics for numerical columns:")
print(df.describe())

# Assuming the dataset has a categorical column 'species', you can adjust if needed
species_grouped = df.groupby('species').mean()
print("\nMean of numerical columns for each species:")
print(species_grouped)

# Task 3: Data Visualization

plt.figure(figsize=(10, 6))
sns.lineplot(x=df.index, y=df['sepal length (cm)'], hue=df['species'])
plt.title('Sepal Length Trends for Each Species')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.legend(title='Species')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x='species', y='sepal length (cm)', data=df)
plt.title('Average Sepal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Sepal Length (cm)')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df['sepal length (cm)'], bins=20, kde=True)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title('Sepal Length vs. Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()
