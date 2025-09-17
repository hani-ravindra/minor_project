import pandas as pd

# point to your extracted CSV
df = pd.read_csv(r'C:\Users\Hani Ravindra\Downloads\archive\phishing.csv', low_memory=False)

print("Rows, Cols:", df.shape)
print("Columns:", df.columns.tolist())
print("\nHead (first 10 rows):")
print(df.head(10))

print("\nValue counts for label column (if exists):")
for col in ['label','Label','status','class']:
    if col in df.columns:
        print(f"\n{col}:")
        print(df[col].value_counts(dropna=False))
        break

