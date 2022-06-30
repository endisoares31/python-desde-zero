import seaborn as sns
df = sns.load_dataset("penguins")
sns.pairplot(df, hue="species")
import matplotlib.pyplot as plt
plt.show()
