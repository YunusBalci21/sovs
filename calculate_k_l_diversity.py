import pandas as pd

def calculate_k_l_diversity(data):
    # Convert input data into a DataFrame
    df = pd.DataFrame(data, columns=['First name', 'Last name', 'Gender', 'Zip code', 'Diagnosis'])

    # Compute k-anonymity
    # k-anonymity is the size of the smallest group of rows with the same quasi-identifiers
    quasi_identifier_groups = df.groupby(['Gender', 'Zip code']).size()
    k_anonymity = quasi_identifier_groups.min()

    # Compute l-diversity
    # l-diversity is the smallest number of unique values for the sensitive attribute in any quasi-identifier group
    l_diversity = df.groupby(['Gender', 'Zip code'])['Diagnosis'].nunique().min()

    # Explanation of results
    explanation = {
        'k-anonymity': f"The k-anonymity value is {k_anonymity} because the smallest group of rows sharing the same quasi-identifiers ('Gender' and 'Zip code') contains {k_anonymity} rows.",
        'l-diversity': f"The l-diversity value is {l_diversity} because the group with the least diversity in 'Diagnosis' contains only {l_diversity} unique value(s)."
    }

    return k_anonymity, l_diversity, explanation

# Example input data
# Original larger dataset
data = [
    ['Sophie', 'Andersen', 'Female', 5003, 'Cancer'],
    ['Victoria', 'Fischer', 'Female', 5003, 'Cancer'],
    ['Aksel', 'Johansson', 'Male', 5003, 'HIV'],
    ['Oskar', 'Karlsson', 'Male', 5003, 'Cancer'],
    ['Sara', 'Larsen', 'Female', 5003, 'HIV'],
    ['Noah', 'Østergård', 'Male', 5003, 'HIV'],
    ['Isabella', 'Petersen', 'Female', 5003, 'HIV'],
    ['Oliver', 'Schmidt', 'Male', 5003, 'Cancer'],
    ['Finn', 'Svensson', 'Male', 5003, 'Cold'],
    ['Jarl', 'Thomsen', 'Male', 5003, 'Cold'],
    ['Mia', 'Wagner', 'Female', 5003, 'Cancer'],
    ['Alexander', 'Bauer', 'Male', 5100, 'Cold'],
    ['Lisa', 'Mikkelsen', 'Female', 5100, 'HIV'],
    ['Bjorn', 'Olsen', 'Male', 5100, 'Cold'],
    ['Ingrid', 'Svensson', 'Female', 5100, 'HIV'],
    ['Igor', 'Hansen', 'Male', 5110, 'Cancer'],
    ['Josefine', 'Olsen', 'Female', 5110, 'Cold'],
    ['Liam', 'Østergård', 'Male', 5110, 'Cancer'],
    ['Grace', 'Schmidt', 'Female', 5110, 'Cold'],
    ['Thor', 'Thomsen', 'Male', 5110, 'Cancer'],
]

# Smaller dataset with three genders for testing
test_data = [
    ['Alice', 'Smith', 'Female', 1001, 'Flu'],
    ['Bob', 'Jones', 'Male', 1001, 'Flu'],
    ['Charlie', 'Brown', 'Non-binary', 1001, 'Cold'],
    ['Dana', 'White', 'Female', 1002, 'Flu'],
    ['Elliot', 'Green', 'Male', 1002, 'Cold'],
    ['Frank', 'Black', 'Non-binary', 1002, 'Cold']
]

# Calculate k and l for the original dataset
k, l, explanation = calculate_k_l_diversity(data)

print("--- Original Dataset ---")
print(f"k-anonymity: {k}")
print(f"l-diversity: {l}")
print("Explanation:")
print(explanation['k-anonymity'])
print(explanation['l-diversity'])

# Calculate k and l for the smaller dataset
k_test, l_test, explanation_test = calculate_k_l_diversity(test_data)

print("\n--- Smaller Dataset ---")
print(f"k-anonymity: {k_test}")
print(f"l-diversity: {l_test}")
print("Explanation:")
print(explanation_test['k-anonymity'])
print(explanation_test['l-diversity'])
