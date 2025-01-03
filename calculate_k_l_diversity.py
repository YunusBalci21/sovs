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
data = [
    ['Alice', 'Smith', 'Female', 1001, 'Flu'],
    ['Bob', 'Jones', 'Male', 1001, 'Flu'],
    ['Charlie', 'Brown', 'Non-binary', 1001, 'Cold'],
    ['Dana', 'White', 'Female', 1002, 'Flu'],
    ['Elliot', 'Green', 'Male', 1002, 'Cold'],
    ['Frank', 'Black', 'Non-binary', 1002, 'Cold']
]


# Calculate k and l
k, l, explanation = calculate_k_l_diversity(data)

print(f"k-anonymity: {k}")
print(f"l-diversity: {l}")
print("Explanation:")
print(explanation['k-anonymity'])
print(explanation['l-diversity'])
