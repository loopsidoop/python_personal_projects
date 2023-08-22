import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data
df = pd.read_csv('Pokemon\pokemon_data.csv',index_col=0)
name = df.iloc[[0,4,9],0]
hp = df.iloc[[0,4,9],3]
attack = df.iloc[[0,4,9],4]
defense = df.iloc[[0,4,9],5]

y_indexes = np.arange(len(name))

# Create a figure and axis
fig, ax = plt.subplots()

# Calculate bar width to separate the bars
bar_width = 0.25

# Create horizontal bar graphs for both datasets
ax.barh(y_indexes + bar_width, attack, bar_width, label='Attack', color='orange')
ax.barh(y_indexes, defense, bar_width, label='Defense', color='green')
ax.barh(y_indexes - bar_width, hp, bar_width, label='HP', color='blue')

# Add labels and title
ax.set_title('Power stats of the 3 starter Pokemon (Gen 1)')

# Adjust y-tick positions and labels
ax.set_yticks(y_indexes)
ax.set_yticklabels(name)

# Add legend
ax.legend()

# Display the graph
plt.show()