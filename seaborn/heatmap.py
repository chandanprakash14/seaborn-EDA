import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Example DataFrame
data = {
    'Math': [90, 85, 88, 78, 92],
    'Science': [80, 78, 82, 88, 84],
    'English': [85, 80, 84, 75, 88]
}
student = pd.DataFrame(data)

# Calculate correlation
correlation = student.corr()

# Create a heatmap
sns.heatmap(correlation, annot=True, xticklabels=correlation.columns, yticklabels=correlation.columns)

# Display the plot
plt.title("Correlation Heatmap")
plt.show()
