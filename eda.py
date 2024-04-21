import seaborn as sns
import matplotlib.pyplot as plt

def plot_histogram(data, column):
    """Plot a histogram with a kernel density estimate."""
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()
    plt.close()

def plot_correlation_matrix(data):
    """Plot the correlation matrix as a heatmap."""
    plt.figure(figsize=(12, 10))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()
    plt.close()

def perform_eda(data):
    """Perform exploratory data analysis by plotting distributions for all numerical features."""
    try:
        num_data = data.select_dtypes(include=['number'])
        for column in num_data.columns:
            plot_histogram(num_data, column)
    except Exception as e:
        print(f"An error occurred during EDA: {e}")

def plot_distributions(data):
    """Plot distributions for all numerical features in the dataset."""
    try:
        for column in data.select_dtypes(include=['float64', 'int64']).columns:
            plot_histogram(data, column)
    except Exception as e:
        print(f"An error occurred while plotting distributions: {e}")
