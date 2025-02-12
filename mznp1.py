import seaborn as sns
import matplotlib.pyplot as plt
print('HELLO WORLD')
print('HELLO WOR2LD')
# Load example dataset
tips = sns.load_dataset("ti")

# Create a scatter plot
sns.scatterplot(x="total_bill", y="tip", hue="day", data=tips)

# Show the plot
plt.show()
