
import pandas as pd
import hashlib

def hash_customer_id(cust_id):
    return hashlib.sha256(str(cust_id).encode()).hexdigest()

def transform_data(input_path, output_path):
    df = pd.read_csv(input_path)

    # Fill missing TotalCharges with average
    if 'TotalCharges' in df.columns:
        df['TotalCharges'].fillna(df['TotalCharges'].mean(), inplace=True)

    # Anonymize CustomerID
    df['CustomerID'] = df['CustomerID'].apply(hash_customer_id)

    # Save processed data
    df.to_csv(output_path, index=False)
    print(f"✅ Transformed data saved to: {output_path}")

if __name__ == "__main__":
    transform_data('./data/customer_churn_data.csv', './data/processed_churn_data.csv')
