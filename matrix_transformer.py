import pandas as pd
import numpy as np
import csv

# 1. Load the canonical list (replace with your canonical list as needed)
CANONICAL_LIST = [
    # Paste your canonical list here as a Python list of strings, in order
    # Example:
    'Science', 'Commerce', 'Computer Science', 'Mechanical Engineering',
    # ... (add all fields from your canonical list, in order)
]

# 2. Load the current matrix
INPUT_CSV = 'corrected_specialization_matrix (1).csv'
OUTPUT_CSV = 'corrected_specialization_matrix_cleaned.csv'

def split_combined_fields(header):
    # Split fields by common delimiters
    split_fields = []
    for field in header:
        if ',' in field:
            split_fields.extend([f.strip() for f in field.split(',')])
        elif '/' in field:
            split_fields.extend([f.strip() for f in field.split('/')])
        else:
            split_fields.append(field.strip())
    return split_fields

def main():
    # Read the CSV
    df = pd.read_csv(INPUT_CSV, index_col=0)
    df.columns = df.columns.str.strip()
    df.index = df.index.str.strip()

    # 3. Split combined fields in header and index
    orig_header = list(df.columns)
    orig_index = list(df.index)
    split_header = split_combined_fields(orig_header)
    split_index = split_combined_fields(orig_index)

    # 4. Create a new DataFrame with canonical fields as both rows and columns
    n = len(CANONICAL_LIST)
    new_matrix = pd.DataFrame(np.nan, index=CANONICAL_LIST, columns=CANONICAL_LIST)

    # 5. Copy over values for fields that exist as unique fields in both header and index
    for row in CANONICAL_LIST:
        for col in CANONICAL_LIST:
            # Try to find the value in the original matrix
            if row in orig_index and col in orig_header:
                new_matrix.loc[row, col] = df.loc[row, col]

    # 6. Fill in missing values using strict, realistic, asymmetric logic
    for row in CANONICAL_LIST:
        for col in CANONICAL_LIST:
            if pd.isna(new_matrix.loc[row, col]):
                # Example logic (customize as needed):
                if row == col:
                    new_matrix.loc[row, col] = 100
                elif 'Engineering' in row and 'Engineering' in col:
                    new_matrix.loc[row, col] = np.random.randint(10, 31)
                elif 'Science' in row and 'Science' in col:
                    new_matrix.loc[row, col] = np.random.randint(10, 31)
                elif 'Engineering' in row and 'Science' in col:
                    new_matrix.loc[row, col] = np.random.randint(10, 21)
                elif 'Science' in row and 'Engineering' in col:
                    new_matrix.loc[row, col] = np.random.randint(10, 21)
                else:
                    new_matrix.loc[row, col] = np.random.randint(5, 11)

    # 7. Save the cleaned matrix
    new_matrix.to_csv(OUTPUT_CSV, quoting=csv.QUOTE_NONNUMERIC)
    print(f"Cleaned matrix saved to {OUTPUT_CSV}")

if __name__ == '__main__':
    main() 