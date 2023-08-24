"""

A simple horizontal graph showcasing the basic stats of the first 3 started pokemons

"""


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data
df = pd.read_csv('Pokemon/pokemon_data.csv',index_col=0)

# Stats of the first evolution
name_1 = df.iloc[[0,4,9],0]
hp_1 = df.iloc[[0,4,9],3]
attack_1 = df.iloc[[0,4,9],4]
defense_1 = df.iloc[[0,4,9],5]

# Stats of the second evolution
name_2 = df.iloc[[1,5,10],0]
hp_2 = df.iloc[[1,5,10],3]
attack_2 = df.iloc[[1,5,10],4]
defense_2 = df.iloc[[1,5,10],5]

# Stats of the third evolution
name_3 = df.iloc[[2,6,11],0]
hp_3 = df.iloc[[2,6,11],3]
attack_3 = df.iloc[[2,6,11],4]
defense_3 = df.iloc[[2,6,11],5]

y_indexes = np.arange(len(name_1))

# Create a figure and axis
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(26.5, 5))

# Calculate bar width to separate the bars
bar_width = 0.15

# Create horizontal bar graphs for all dataset
ax[0].barh(y_indexes + bar_width, attack_1, bar_width, label='Attack', color='orange')
ax[0].barh(y_indexes, defense_1, bar_width, label='Defense', color='green')
ax[0].barh(y_indexes - bar_width, hp_1, bar_width, label='HP', color='blue')

ax[1].barh(y_indexes + bar_width, attack_2, bar_width, label='Attack', color='orange')
ax[1].barh(y_indexes, defense_2, bar_width, label='Defense', color='green')
ax[1].barh(y_indexes - bar_width, hp_2, bar_width, label='HP', color='blue')

ax[2].barh(y_indexes + bar_width, attack_3, bar_width, label='Attack', color='orange')
ax[2].barh(y_indexes, defense_3, bar_width, label='Defense', color='green')
ax[2].barh(y_indexes - bar_width, hp_3, bar_width, label='HP', color='blue')

# Adjust y-tick positions and labels for all dataset
ax[0].set_yticks(y_indexes)
ax[0].set_yticklabels(name_1)

ax[1].set_yticks(y_indexes)
ax[1].set_yticklabels(name_2)

ax[2].set_yticks(y_indexes)
ax[2].set_yticklabels(name_3)

# Add legends for all
ax[1].legend(fontsize=6.8,loc='lower right')

ax[1].set_title('Power stats of the 3 starter Pokemon (Gen 1)', fontsize=18)

# Display the graph
plt.subplots_adjust(wspace=0.3)
plt.show()

