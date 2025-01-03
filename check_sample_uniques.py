import pandas as pd

def check_sample_uniques(data):
    # Convert data to a DataFrame - change this in exam to make it fit
    df = pd.DataFrame(data, columns=['First name', 'Gender', 'Zip code', 'Diagnosis'])

    # Group by quasi-identifiers
    groups = df.groupby(['Gender', 'Zip code']).size()

    # Identify sample uniques
    sample_uniques = groups[groups == 1]

    if not sample_uniques.empty:
        print("Sample Uniques Detected:")
        for index, value in sample_uniques.items():
            gender, zip_code = index
            print(f"Group ('Gender': {gender}, 'Zip code': {zip_code}) is unique because it contains only {value} record.")
    else:
        print("No Sample Uniques Detected. All groups have more than one record, making them non-unique.")

# Example input data
# Original larger dataset - CHANGE THIS TO THE EXAM
data = [
    ['Alice', 'Female', 1001, 'Flu'],
    ['Bob', 'Male', 1001, 'Flu'],
    ['Charlie', 'Non-binary', 1001, 'Cold'],
    ['Dana', 'Female', 1002, 'Flu'],
    ['Elliot', 'Male', 1002, 'Cold'],
    ['Frank', 'Non-binary', 1002, 'Cold']
]

# Check for sample uniques in the smaller dataset
print("\nChecking for sample uniques in the smaller dataset:")
check_sample_uniques(data)
