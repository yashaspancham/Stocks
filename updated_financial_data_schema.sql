
-- Creating table 'Companies'
CREATE TABLE Companies (
    ID INT PRIMARY KEY,
    Name VARCHAR(255),
    TickerSymbol VARCHAR(10),
    Sector VARCHAR(255)
    -- Add other company-specific columns as needed
);

-- Creating table 'AnnualFinancials'
CREATE TABLE AnnualFinancials (
    ID INT PRIMARY KEY,
    CompanyID INT REFERENCES Companies(ID),
    Year INT,
    Revenue FLOAT,
    NetProfit FLOAT,
    OperatingIncome FLOAT,
    EPS FLOAT,
    TotalAssets FLOAT,
    TotalLiabilities FLOAT,
    ShareholdersEquity FLOAT,
    OperatingCashFlow FLOAT,
    DividendsPaid FLOAT
);

-- Creating table 'CurrentStockData'
CREATE TABLE CurrentStockData (
    ID INT PRIMARY KEY,
    CompanyID INT REFERENCES Companies(ID),
    Date DATE,
    SharePrice FLOAT,
    SharesOutstanding FLOAT
);

-- Creating table 'ProsCons'
CREATE TABLE ProsCons (
    ID INT PRIMARY KEY,
    CompanyID INT REFERENCES Companies(ID),
    ProConType VARCHAR(10),  -- Pro or Con
    Description TEXT
);

-- Creating table 'ShareholdingPattern'
CREATE TABLE ShareholdingPattern (
    ID INT PRIMARY KEY,
    CompanyID INT REFERENCES Companies(ID),
    Date DATE,
    PromoterHolding FLOAT,
    FIIsHolding FLOAT,
    DIIsHolding FLOAT,
    PublicHolding FLOAT
);
