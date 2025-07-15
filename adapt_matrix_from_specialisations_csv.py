import pandas as pd

# Load the new matrix (from your provided CSV)
new_matrix = pd.read_csv('course-recom/Specialisations - 2nd Iteration (1).csv', index_col=0)

# Load the filtered matrix (the one you want to update)
filtered_matrix = pd.read_csv('filtered_hierarchical_relevancy_matrix.csv', index_col=0)

# Get the intersection of courses (rows and columns)
common_courses = list(set(filtered_matrix.index) & set(new_matrix.index))

# For each cell in the filtered matrix, if the value exists in the new matrix, replace it
for row in common_courses:
    for col in common_courses:
        if row in new_matrix.index and col in new_matrix.columns:
            filtered_matrix.loc[row, col] = new_matrix.loc[row, col]

# Save the updated matrix
filtered_matrix.to_csv('filtered_hierarchical_relevancy_matrix.csv')
print("filtered_hierarchical_relevancy_matrix.csv updated with adapted values.") 