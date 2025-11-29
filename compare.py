import pandas as pd
import matplotlib.pyplot as plt

# Load the COMPAS dataset
compas_data = pd.read_csv('compas-scores.csv')

# Prepare the dataset by selecting relevant columns: race and decile scores
compas_analysis_data = compas_data[['race', 'decile_score.1']].dropna()  # Remove rows with missing values

# Map 'race' values to numeric for analysis
race_map = {
    'Caucasian': 0,
    'African-American': 1,
    'Hispanic': 2,
    'Other': 3
}
compas_analysis_data['race'] = compas_analysis_data['race'].map(race_map)

# Calculate the average recidivism risk (decile_score.1) for each race group
race_grouped = compas_analysis_data.groupby('race')['decile_score.1'].mean()

# Plot the average recidivism risk score for each racial group
plt.figure(figsize=(10, 6))
race_grouped.plot(kind='bar', color=['blue', 'green', 'orange', 'red'])
plt.title('Average Recidivism Risk Score by Race')
plt.xlabel('Race')
plt.ylabel('Average Decile Score')
plt.xticks(rotation=45)
plt.show()

# Define the protected attribute (race) and the label (recidivism decile score)
compas_analysis_data['label'] = (compas_analysis_data['decile_score.1'] >= 5).astype(int)  # Define a "high risk" category

# Calculate false positive rates for each racial group
# False positives occur when a low-risk individual is misclassified as high-risk
# For each group, we calculate the false positive rate: proportion of low-risk individuals classified as high-risk
false_positive_rates = compas_analysis_data.groupby('race').apply(
    lambda group: ((group['label'] == 1) & (group['decile_score.1'] < 5)).sum() / (group['decile_score.1'] < 5).sum()
)

# Plot the false positive rates across different racial groups
plt.figure(figsize=(10, 6))
false_positive_rates.plot(kind='bar', color=['blue', 'green', 'orange', 'red'])
plt.title('False Positive Rates by Race')
plt.xlabel('Race')
plt.ylabel('False Positive Rate')
plt.xticks(rotation=45)
plt.show()

# Optionally, calculate and display more fairness metrics like disparity in impact, true positive rates, etc.
# Calculate True Positive Rates (TPR) for each racial group
# True positives occur when a high-risk individual is correctly classified as high-risk
# For each group, we calculate the true positive rate: proportion of high-risk individuals classified as high-risk
true_positive_rates = compas_analysis_data.groupby('race').apply(
    lambda group: ((group['label'] == 1) & (group['decile_score.1'] >= 5)).sum() / (group['decile_score.1'] >= 5).sum()
)

# Plot the true positive rates across different racial groups
plt.figure(figsize=(10, 6))
true_positive_rates.plot(kind='bar', color=['blue', 'green', 'orange', 'red'])
plt.title('True Positive Rates by Race')
plt.xlabel('Race')
plt.ylabel('True Positive Rate')
plt.xticks(rotation=45)
plt.show()

# Disparity in Impact: Calculate and visualize the ratio of the false positive rates between racial groups
# Disparate Impact = false positive rate for unprivileged group / false positive rate for privileged group
privileged_group_fpr = false_positive_rates[0]  # Caucasian (privileged group)
unprivileged_group_fpr = false_positive_rates[1:]  # Other groups (unprivileged)

disparity_impact = unprivileged_group_fpr / privileged_group_fpr

# Plot the disparity in impact across different racial groups
plt.figure(figsize=(10, 6))
disparity_impact.plot(kind='bar', color=['orange', 'green', 'red'])
plt.title('Disparity in False Positive Rates by Race')
plt.xlabel('Race')
plt.ylabel('Disparity Impact (False Positive Rate Ratio)')
plt.xticks(rotation=45)
plt.show()