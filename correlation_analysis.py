import pandas as pd
import matplotlib
import numpy as np
# Load your CSV file into a DataFrame
df = pd.read_csv(r'Cleaned_Cancer_Projectv2.csv')
# Check the columns and the first few rows in your cleaned DataFrame to verify
print("Columns in the DataFrame:")
print(df.columns)
print("\nFirst few rows of the DataFrame:")
print(df.head())  # This should work as df is now a DataFrame
# Convert 'Sex' column to numeric values
df['Sex_numeric'] = df['Sex'].map({'Male/Female': 0, 'Male': 1, 'Female': 2})

# Now you can calculate correlations
correlation_sex_cancer = df['Sex_numeric'].corr(df['Distant'])  # replace 'Distant' with the relevant column
correlation_age_cancer = df['Age'].corr(df['Distant'])  # replace 'Distant' with the relevant column
correlation_year_cancer = df['Year'].corr(df['Distant'])  # replace 'Distant' with the relevant column
correlation_regional_cancer = df['Regional'].corr(df['Distant'])  # replace 'Distant' with the relevant column

# Now print the correlations
print("Correlation between Sex and Distant:", correlation_sex_cancer)
print("Correlation between Age and Distant:", correlation_age_cancer)
print("Correlation between Year and Distant:", correlation_year_cancer)
print("Correlation between Regional and Distant:", correlation_regional_cancer)

