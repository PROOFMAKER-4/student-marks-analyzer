import pandas as pd
import matplotlib.pyplot as plt
import sys

def analyze_marks(file_path):
    try:
        # Load data
        df = pd.read_csv(file_path)

        if 'Marks' not in df.columns:
            raise ValueError("CSV must contain a 'Marks' column")

        marks = df['Marks']

        # Compute statistics
        mean = marks.mean()
        median = marks.median()
        q1 = marks.quantile(0.25)
        q3 = marks.quantile(0.75)

        print("📊 Marks Analysis")
        print(f"Mean: {mean:.2f}")
        print(f"Median: {median:.2f}")
        print(f"Q1: {q1:.2f}")
        print(f"Q3: {q3:.2f}")

        # Visualization
        plt.figure(figsize=(8, 5))
        plt.boxplot(marks, vert=False)
        plt.title("Marks Distribution")
        plt.xlabel("Marks")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyzer.py <path_to_csv>")
    else:
        analyze_marks(sys.argv[1])