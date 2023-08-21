import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample gene expression data (replace this with your actual data)
genes = ['Gene A', 'Gene B', 'Gene C', 'Gene D']
conditions = ['Condition 1', 'Condition 2', 'Condition 3']
expression_data = np.random.rand(len(genes), len(conditions))  # Replace with your data

# Create a heatmap to show gene expression levels across conditions
plt.figure(figsize=(10, 6))
sns.heatmap(expression_data, annot=True, fmt=".2f", cmap="YlGnBu",
            xticklabels=conditions, yticklabels=genes)
plt.title("Gene Expression Heatmap")
plt.xlabel("Conditions")
plt.ylabel("Genes")
plt.show()

# Create line plots to visualize expression trends for each gene
plt.figure(figsize=(10, 6))
for i, gene in enumerate(genes):
    plt.plot(conditions, expression_data[i], marker='o', label=gene)
plt.title("Gene Expression Trends")
plt.xlabel("Conditions")
plt.ylabel("Expression Level")
plt.legend()
plt.show()

# Create a bar plot to compare gene expression levels across conditions
plt.figure(figsize=(10, 6))
x = np.arange(len(genes))
width = 0.2
for i, condition in enumerate(conditions):
    plt.bar(x + i * width, expression_data[:, i], width, label=condition)
plt.xticks(x + width * (len(conditions) - 1) / 2, genes)
plt.title("Gene Expression Comparison")
plt.xlabel("Genes")
plt.ylabel("Expression Level")
plt.legend()
plt.show()
