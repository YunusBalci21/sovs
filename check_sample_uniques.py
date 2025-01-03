import pandas as pd

def check_sample_uniques(data):
    # Convert data to a DataFrame
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
            print(f"Detailed Explanation: The combination of 'Gender': {gender} and 'Zip code': {zip_code} has only one matching record in the dataset, making it unique.")
    else:
        print("No Sample Uniques Detected. All groups have more than one record, making them non-unique.")

# Example input data
# Dataset with sample uniques
data_with_sample_uniques = [
    ['Alice', 'Female', 1001, 'Flu'],
    ['Bob', 'Male', 1001, 'Flu'],
    ['Charlie', 'Non-binary', 1001, 'Cold'],
    ['Dana', 'Female', 1002, 'Flu'],
    ['Elliot', 'Male', 1002, 'Cold'],
    ['Frank', 'Non-binary', 1002, 'Cold'],
    ['Grace', 'Female', 1003, 'Flu'],  # Sample unique
    ['Liam', 'Male', 1003, 'Cold'],    # Sample unique
    ['Sophia', 'Female', 1004, 'Flu'], # Sample unique
]

# Check for sample uniques in the dataset with sample uniques
print("\nChecking for sample uniques in the dataset with sample uniques:")
check_sample_uniques(data_with_sample_uniques)
