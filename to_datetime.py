# From previous step
diet.index = pd.to_datetime(diet.index)

# Slice the dataset to keep only 2012
diet2012 = diet[diet.index.year == 2012]

# Plot 2012 data
diet2012.plot(grid=True)
plt.show()
