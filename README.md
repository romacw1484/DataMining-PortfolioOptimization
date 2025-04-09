# Portfolio Optimization
 "What is the optimal asset allocation that minimizes portfolio volatility while achieving a target return?"
 ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
OBJECTIVES , SCOPE, and KEY METRICS: 


Key Metrics:

Weekly Averages Per Industry - file shows chart with weekly mean closing price per industry across time frame 



Scope:
- Use a diversified set of stocks spanning the major 11 industries.
- Historical window spans 10 years of daily data (Dates from 03-30-2015 - 03--24-2025)
  
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Files**

Returns.ipynb - calculates daily percentage returns and computes both the arithmetic average daily returns and the annualized returns (assuming approximately 252 trading days per year). In addition, it calculates daily log returns, which are then used to compute geometric annualized returns for a continuously compounded perspective. The script also generates a covariance matrix based on the log returns to capture how stocks move together, and it derives a corresponding correlation matrix that is visualized as a heatmap.
![Correlation-Matrix](https://github.com/user-attachments/assets/cacb575b-e502-4da0-a1e5-b42187833ad6)

Daily_Averages.ipynb - plots average returns over time on graph 

**Tech**
<img width="1338" alt="Screenshot 2025-04-08 at 4 33 49 PM" src="https://github.com/user-attachments/assets/30a3a65d-6e86-4e16-a269-c76caf2cb42c" />
**Utilities** 
<img width="1323" alt="Screenshot 2025-04-08 at 4 34 09 PM" src="https://github.com/user-attachments/assets/b7823524-2c36-454e-942d-5a3297f8c9e2" />

- Dash Monte Carlo: Runs Monte Carlo simulation for a stock portfolio the user specifies with graph
- 
- James Sheet: Math from excel sheet James sent in Python for scalability
