from pandas import read_csv, read_sql_query
import sqlite3

# import function from plot.py
from plot import plot_query_results

# Read csv files
df_student_info = read_csv("student_info.csv")
df_student_grades = read_csv("student_grades.csv")

# Connect to an in-memory SQLite database
conn = sqlite3.connect(":memory:")

# Write DataFrames to SQL Tables
df_student_info.to_sql("student_info", conn, index=False)
df_student_grades.to_sql("student_grades", conn, index=False)

# Write Query 1
query1 = """
    SELECT *
    FROM student_info;
"""
df1 = read_sql_query(query1, conn)
print(df1)
print("\n")

# Write Query 2
query2 = """
    SELECT *
    FROM student_grades;
"""
df2 = read_sql_query(query2, conn)
print(df2)
print("\n")

# Write Query 3
query3 = """
    SELECT si.First_Name, si.Last_Name, sg.Course_Subject, sg.Course_Grade
    FROM student_info si
    JOIN student_grades sg ON si.Student_ID = sg.Student_ID
    WHERE sg.Course_Subject = 'Math'
    ORDER BY sg.Course_Grade DESC
"""
df3 = read_sql_query(query3, conn)
print(df3)
print("\n")

# Write Query 4
query4 = """
    SELECT si.First_Name, si.Last_Name, si.Gender, sg.Course_Grade AS Highest_Math_Grade
    FROM student_info si
    JOIN student_grades sg ON si.Student_ID = sg.Student_ID
    WHERE sg.Course_Subject = 'Math' AND (Gender = 'Male' OR si.Gender = 'Female')
    GROUP BY si.Student_ID
    ORDER BY sg.Course_Grade DESC
    LIMIT 2;
"""
df4 = read_sql_query(query4, conn)
print(df4)

print("\n------------------------------------------------------\n")

# Write Query 5
query5 = """
    SELECT si.First_Name, si.Last_Name, AVG(sg.Course_Grade) AS Avg_Grade
    FROM student_info si
    JOIN student_grades sg ON si.Student_ID = sg.Student_ID
    GROUP BY si.Student_ID
    ORDER BY Avg_Grade DESC
"""
df5 = read_sql_query(query5, conn)
print(df5)
print("\n")

# Write Query 6
query6 = """
    SELECT si.First_Name, si.Last_Name, si.Gender, AVG(sg.Course_Grade) AS Highest_Avg_Grade
    FROM student_info si
    JOIN student_grades sg ON si.Student_ID = sg.Student_ID
    WHERE Gender = 'Male' OR si.Gender = 'Female'
    GROUP BY si.Student_ID
    ORDER BY Highest_Avg_Grade DESC
    LIMIT 2;
"""
df6 = read_sql_query(query6, conn)
print(df6)
print("\n")

# Send each Query Results to Plot.py
plot_query_results(df1, df2, df3, df4, df5, df6)

conn.close()
