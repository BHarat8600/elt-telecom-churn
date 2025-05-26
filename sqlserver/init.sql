CREATE DATABASE IF NOT EXISTS CustomerChurnDB;
GO

USE CustomerChurnDB;
GO

CREATE TABLE StagingCustomerChurn (
    CustomerID VARCHAR(100),
    Age INT,
    Gender VARCHAR(10),
    Tenure INT,
    MonthlyCharges FLOAT,
    ContractType VARCHAR(50),
    InternetService VARCHAR(50),
    TotalCharges FLOAT,
    TechSupport VARCHAR(10),
    Churn VARCHAR(10)
);
