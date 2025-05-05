import matplotlib.pyplot as plt
import seaborn as sns

def plot_query_results(df1, df2, df3, df4, df5, df6):
    fig, axes = plt.subplots(3, 2, figsize=(16, 10))

    # Plot 1
    sns.countplot(data=df1, x="Gender", hue="Gender", ax=axes[0][0], palette=["blue", "red"], legend=False)
    axes[0][0].set_title("Number of Students by Gender")
    axes[0][0].set_xlabel("Gender")
    axes[0][0].set_ylabel("Count")

    # Plot 2
    sns.countplot(data=df2, x="Course_Subject", hue="Course_Subject", ax=axes[0][1], palette=["cyan", "orange", "green", "purple", "pink"], legend=False)
    axes[0][1].set_title("Number of Students by Course")
    axes[0][1].set_xlabel("Course")
    axes[0][1].set_ylabel("Count")

    # Plot 3
    sns.barplot(data=df3, x="First_Name", y="Course_Grade", hue="Last_Name", ax=axes[1][0])
    axes[1][0].legend(title="Last Name", bbox_to_anchor=(1.3, 0.5), loc='center', ncol = 2)
    axes[1][0].set_title("Math Grades by Student")
    axes[1][0].set_xlabel("First Name")
    axes[1][0].set_ylabel("Math Grade")
    axes[1][0].tick_params(axis='x', rotation=45)

    # Plot 4
    sns.barplot(data=df4, x="First_Name", y="Highest_Math_Grade", hue="Last_Name", ax=axes[1][1], palette=["red", "blue"])
    axes[1][1].legend(title="Last Name", bbox_to_anchor=(1.15, 0.5), loc='center')
    axes[1][1].set_title("Top 2 Students with Highest Math Grades (by Gender)")
    axes[1][1].set_xlabel("First Name")
    axes[1][1].set_ylabel("Highest Math Grade")

    # Plot 5
    sns.barplot(data=df5, x="First_Name", y="Avg_Grade", hue="Last_Name", ax=axes[2][0])
    axes[2][0].legend(title="Last Name", bbox_to_anchor=(1.3, 0.5), loc='center', ncol = 2)
    axes[2][0].set_title("Highest Average by Student")
    axes[2][0].set_xlabel("First Name")
    axes[2][0].set_ylabel("Average Grade")
    axes[2][0].tick_params(axis='x', rotation=45)

    # Plot 6
    sns.barplot(data=df6, x="First_Name", y="Highest_Avg_Grade", hue="Last_Name", ax=axes[2][1], palette=["blue", "red"])
    axes[2][1].legend(title="Last Name", bbox_to_anchor=(1.15, 0.5), loc='center')
    axes[2][1].set_title("Top 2 Students with Highest Average Grades (by Gender)")
    axes[2][1].set_xlabel("First Name")
    axes[2][1].set_ylabel("Highest Average Grade")

    # delete axes at 0,1
    # fig.delaxes(axes[0][1])
    
    plt.tight_layout()
    plt.show()
