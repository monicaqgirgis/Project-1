import pandas as pd
import matplotlib.pyplot as plt 
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
# Pie Chart: Distribution of Cancer Stages (In_situ, Localized, Regional, Distant)
cancer_stages = ['In_situ', 'Localized', 'Regional', 'Distant']
stage_counts = df[cancer_stages].sum()  # Sum across rows for each stage

plt.figure(figsize=(8, 6))
plt.pie(stage_counts, labels=stage_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightblue', 'orange', 'green', 'red'])
plt.title('Distribution of Cancer Stages')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
# Save the Pie Chart
plt.savefig("pie_chart.png", dpi=300, bbox_inches="tight")
print("Pie chart saved as 'pie_chart.png'")
plt.show()

# Bar Chart: Total count of each Cancer Stage across all records
plt.figure(figsize=(8, 6))
stage_counts.plot(kind='bar', color=['lightblue', 'orange', 'green', 'red'])
plt.title('Cancer Stages Distribution (Bar Chart)')
plt.xlabel('Cancer Stages')
plt.ylabel('Count')
plt.xticks(rotation=0)
# Save the Bar Chart
plt.savefig("bar_chart.png", dpi=300, bbox_inches="tight")
print("Bar chart saved as 'bar_chart.png'")
print("Results saved to correlation_output.txt")
plt.show()
