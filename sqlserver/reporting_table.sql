USE CustomerChurnDB;
GO

CREATE TABLE ReportingCustomerChurn (
    CustomerID VARCHAR(100),
    Age INT,
    IsSeniorCitizen BIT,
    Gender VARCHAR(10),
    Tenure INT,
    MonthlyCharges FLOAT,
    MonthlyCategory VARCHAR(20),
    ContractType VARCHAR(50),
    InternetService VARCHAR(50),
    TotalCharges FLOAT,
    TechSupport VARCHAR(10),
    Churn VARCHAR(10)
);
INSERT INTO ReportingCustomerChurn (
    CustomerID, Age, IsSeniorCitizen, Gender,
    Tenure, MonthlyCharges, MonthlyCategory,
    ContractType, InternetService, TotalCharges,
    TechSupport, Churn
)
SELECT
    CustomerID,
    Age,
    CASE WHEN Age >= 60 THEN 1 ELSE 0 END AS IsSeniorCitizen,
    Gender,
    Tenure,
    MonthlyCharges,
    CASE 
        WHEN MonthlyCharges >= 80 THEN 'High'
        WHEN MonthlyCharges >= 40 THEN 'Medium'
        ELSE 'Low'
    END AS MonthlyCategory,
    ContractType,
    InternetService,
    TotalCharges,
    TechSupport,
    Churn
FROM StagingCustomerChurn;
