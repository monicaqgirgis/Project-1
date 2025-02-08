import pandas as pd

# Load your dataset (make sure to use the correct file path)
df = pd.read_csv("C:/Users/preit/OneDrive/Desktop/Cancer Projectv2/Cancer Projectv2.csv")

# Step 1: Strip any leading/trailing spaces in the column names
df.columns = df.columns.str.strip()

# Step 2: Rename columns for easier access
df.rename(columns={
    'Race recode (White, Black, Other)': 'Race',
    'Sex': 'Sex',
    'Year of diagnosis': 'Year',
    'Age recode with <1 year olds': 'Age',
    'In_situ': 'In_situ',
    'Localized': 'Localized',
    'Regional': 'Regional',
    'Distant': 'Distant',
    'NA': 'NA',
    'Unknownunstaged': 'Unknownunstaged',
    'Blanks': 'Blanks'
}, inplace=True)

# Step 3: Map values in the 'Race' column
df['Race'] = df['Race'].map({0: 'White', 1: 'Black', 2: 'Others'})

# Step 4: Map values in the 'Sex' column
df['Sex'] = df['Sex'].map({0: 'Male/Female', 1: 'Male', 2: 'Female'})

# Step 5: Map values in the 'Year' column (0 to 22 corresponding to 2000 to 2022)
df['Year'] = df['Year'].map({i: 2000 + i for i in range(23)})

# Step 6: Check for missing values and handle them (e.g., filling or dropping)
df = df.dropna()  # Dropping rows with missing values

# Optional: You can fill missing values using the following line instead:
# df.fillna('Unknown', inplace=True)

# Step 7: Save the cleaned dataset to a new CSV file
df.to_csv("C:/Users/preit/OneDrive/Desktop/Cancer Projectv2/Cleaned_Cancer_Projectv2.csv", index=False)

# Display first few rows of the cleaned dataset
print(df.head())

