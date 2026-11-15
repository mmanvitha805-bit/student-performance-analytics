import matplotlib.pyplot as plt


def plot_subject_averages(df, output_path=None):
    subjects = [
        "math_marks",
        "physics_marks",
        "programming_marks"
    ]

    averages = df[subjects].mean()

    plt.figure(figsize=(8, 5))
    averages.plot(kind="bar")
    plt.title("Average Marks by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average Marks")
    plt.ylim(0, 100)
    plt.tight_layout()

    if output_path:
        plt.savefig(output_path, dpi=150)

    plt.show()
    plt.close()


def plot_average_distribution(df, output_path=None):
    subjects = [
        "math_marks",
        "physics_marks",
        "programming_marks"
    ]

    average_marks = df[subjects].mean(axis=1)

    plt.figure(figsize=(8, 5))
    plt.hist(average_marks, bins=10, edgecolor="black")
    plt.title("Distribution of Student Average Marks")
    plt.xlabel("Average Marks")
    plt.ylabel("Number of Students")
    plt.tight_layout()

    if output_path:
        plt.savefig(output_path, dpi=150)

    plt.show()
    plt.close()