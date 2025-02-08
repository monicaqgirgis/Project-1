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
#correlation between sex and cancer
correlation_sex_cancer=df[['Sex','In_situ','Localized','Regional','Distant']]
print('correlation_sex_cancer')
#correlation between age and cancer
correlation_age_cancer=df[['Age','In_situ','Localized','Regional','Distant']]
print("correlation_age_cancer")
#correlation between year and cancer
correlation_year_cancer=[['year','Age','In_situ','Localized','Regional','Distant']]
print("correlation_year_cancer")
#correlation between regional and cancer
correlation_regional_cancer=df[['Regional','Race','Sex','In_situ','Localized','Distant']]
print("correlation_regional_cancer")

