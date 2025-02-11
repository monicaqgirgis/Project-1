import pandas as pd
import matplotlib
import numpy as np
# Load your CSV file into a DataFrame
df = pd.read_csv(r'Cleaned_Cancer_Projectv2.csv')
# Convert categorical variables to numerical values
df['Sex'] = df['Sex'].astype('category').cat.codes  # Converts Male/Female into numerical values
df['Race'] = df['Race'].astype('category').cat.codes  # Converts race categories into numbers

# Select relevant columns for correlation
cancer_stages = ['In_situ', 'Localized', 'Regional', 'Distant']

# Compute correlation matrix
correlations = df[['Age', 'Sex', 'Year', 'Race', 'Regional'] + cancer_stages].corr()

# Extract correlations with cancer stages
age_correlation = correlations.loc['Age', cancer_stages]
sex_correlation = correlations.loc['Sex', cancer_stages]
year_correlation = correlations.loc['Year', cancer_stages]
race_correlation = correlations.loc['Race', cancer_stages]
regional_correlation = correlations.loc['Regional', cancer_stages]

# Print results
print("Correlation between Age and Cancer Stages:")
print(age_correlation)

print("\nCorrelation between Sex and Cancer Stages:")
print(sex_correlation)

print("\nCorrelation between Year and Cancer Stages:")
print(year_correlation)

print("\nCorrelation between Race and Cancer Stages:")
print(race_correlation)

print("\nCorrelation between Regional Cancer Stage and Other Cancer Stages:")
print(regional_correlation)
