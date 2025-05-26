import pandas as pd
import pyodbc

def load_data(csv_path):
    df = pd.read_csv(csv_path)

    # conn = pyodbc.connect(
    #     'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=CustomerChurnDB;UID=sa;PWD=YourStrong!Passw0rd'
    #)
    conn = pyodbc.connect(
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=192.168.1.13\\sql2019;"  # Use double backslash in Python
            "Database=Zomato;"
            "UID=Bharat.ade;"
            "PWD=Gateway@2023;"
            "TrustServerCertificate=yes;"
        )
    
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO StagingCustomerChurn (
                CustomerID, Age, Gender, Tenure,
                MonthlyCharges, ContractType,
                InternetService, TotalCharges,
                TechSupport, Churn
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, 
        row.CustomerID, row.Age, row.Gender, row.Tenure,
        row.MonthlyCharges, row.ContractType, row.InternetService,
        row.TotalCharges, row.TechSupport, row.Churn)

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Data loaded into SQL Server successfully.")

if __name__ == "__main__":
    load_data('./data/processed_churn_data.csv')
