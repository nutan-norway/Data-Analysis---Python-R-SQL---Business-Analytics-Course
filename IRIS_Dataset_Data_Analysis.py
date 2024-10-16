# Data Analysis for IRIS Dataset
# Nutan Gupta - Inland Norway University of Applied Science, Lillehammer 

#%% 
import pandas as pd
import matplotlib.pyplot as plt
# %%
data = pd.read_csv('iris_assignment.csv')
# %%
data.head()
# %%
data.tail()
# %%
data[37:149]
# %%
new_data = data[37:149]
# %%
new_data.info()

# %%
new_data.describe()
# %%
new_data.describe(include='all')
# %%
new_data.dropna()
# %%
missing_values = new_data.isnull().sum()
print(missing_values)
# %%
# to find unique counts and data types for all columns
unique_counts = new_data.nunique()

print("Count of unique values in each column:")
print(unique_counts)

# %%
new_data['Id'].unique()
# %%
id=new_data['Id'].value_counts()

# %%
# for finding mean median and sd for only two columns
new_data[['SepalLength','SepalWidth']]

# %%
sel_column= new_data[['SepalLength','SepalWidth']]

# %%
sel_column.describe()

# %%
import matplotlib.pyplot as plt

# %%
fig,ax = plt.subplots()
ax.hist(new_data[['SepalLength','SepalWidth']])
plt.show()
# %%

fig,ax = plt.subplots(nrows=2, figsize=(10,10))
ax[0].hist(new_data['SepalLength'], bins=20, color='blue')
ax[0].set_title('Sepal Length Distribution')
ax[0].set_xlabel('Sepal Length')
ax[0].set_ylabel('Frequency')

ax[1].hist(new_data['SepalWidth'], bins=20, color='green')
ax[1].set_title('Sepal Width Distribution')
ax[1].set_xlabel('Sepal Width')
ax[1].set_ylabel('Frequency')

# %%
fig,ax = plt.subplots(ncols=2, figsize=(12, 5))  # 1 row, 2 columns

# Plot for SepalLength on the left
ax[0].hist(new_data['SepalLength'], bins=20, color='blue', alpha=0.7)
ax[0].set_title('Sepal Length Distribution')
ax[0].set_xlabel('Sepal Length')
ax[0].set_ylabel('Frequency')

# Plot for SepalWidth on the right
ax[1].hist(new_data['SepalWidth'], bins=20, color='green', alpha=0.7)
ax[1].set_title('Sepal Width Distribution')
ax[1].set_xlabel('Sepal Width')
ax[1].set_ylabel('Frequency')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the figure
plt.show()
# %%
new_data[['PetalLength','PetalWidth']]

# %%
sel_col = new_data[['PetalLength','PetalWidth']]
print(sel_col)

# %%
fig,ax = plt.subplots()
ax.scatter(new_data['PetalLength'],new_data['PetalWidth'])
ax.set_title('Petal Length vs Petal width')
ax.set_xlabel('Petal length')
ax.set_ylabel('Petal Width')

# %%
fig, ax = plt.subplots()
ax.scatter(new_data['PetalLength'], new_data['PetalWidth'])
ax.set_title('Petal Length vs Petal Width')
ax.set_xlabel('Petal Length')
ax.set_ylabel('Petal Width')
plt.show()

# %%
#fig,ax = plt.subplots(ncols=2)
#ax[0].boxplot(new_data[])


#%%
new_data.boxplot(column='PetalLength', by='Species', figsize=(8, 6))

# Set the plot title and labels
plt.title('Box Plot of Petal Length by Species')
plt.suptitle('')  # Suppress the automatic subtitle to avoid duplication
plt.xlabel('Species')
plt.ylabel('Petal Length')

# Show the plot
plt.show()
# %%
fig,ax = plt.subplots(ncols=2)
ax[0].boxplot(new_data['PetalLength'],[new_data['Species']=='Iris-setosa'])
ax[1].boxplot(new_data['PetalLength'],[new_data['Species']=='Iris-versicolor'])
ax[0].set_title('Iris-setosa')
ax[1].set_title('Iris-versicolor')
# %%
fig, ax = plt.subplots(ncols=2, figsize=(12, 6))

# Box plot for PetalLength by Species
new_data.boxplot(column='PetalLength', by='Species', ax=ax[0])
ax[0].set_title('Petal Length by Species')
ax[0].set_xlabel('Species')
ax[0].set_ylabel('Petal Length')

# Box plot for PetalWidth by Species
new_data.boxplot(column='PetalWidth', by='Species', ax=ax[1])
ax[1].set_title('Petal Width by Species')
ax[1].set_xlabel('Species')
ax[1].set_ylabel('Petal Width')

# %%

# %%
