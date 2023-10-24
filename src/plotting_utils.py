import matplotlib.pyplot as plt
import os
import seaborn as sns

def save_univariate_figures(df, col):
    """ this function will take in a dataframe and one categorical column for plotting
      a barchart and saving it in a png format 

      args: 
      df : dataframe  
      col : column name
    """
    nums = df[col].value_counts()
    plt.figure(figsize=(12,12))
    ax = sns.barplot(x=nums.index, y=nums.values )
    plt.xticks(rotation=90)
    plt.title('Value counts of neighbourhood')
    plt.ylabel('Counts')
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', fontsize=7, color='black', xytext=(0, 5), textcoords='offset points', rotation=90)
    plt.savefig(f"bar_plot_{col}.png")
    plt.show()
