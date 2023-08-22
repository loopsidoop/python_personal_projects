import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Pokemon\pokemon_data.csv')

y = df['Name'].head(5)
x= df['Attack'].head(5)

fig, ax = plt.subplots()
ax.barh(x, y)

plt.show()


