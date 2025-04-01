import pandas as pd

# 1. Load the CSV file, skipping footer rows that contain non-numeric sector labels.
#    Using engine='python' to allow skipfooter. This will read in the header and data,
#    excluding the bottom sector category rows.

                          # name of current working csv file 
prices_df = pd.read_csv('Portfoliocsv.csv', engine='python', skipfooter=4)

# 2. Drop any fully empty or irrelevant columns (such as unnamed blank columns and duplicate 'Ticker' column).
#    These columns were likely placeholder separators or duplicate date columns.
cols_to_drop = [col for col in prices_df.columns if "Unnamed" in col or col == "Ticker"]
prices_df.drop(columns=cols_to_drop, inplace=True)

# 3. Clean the column names by keeping only the stock ticker (remove company names or extra text in parentheses).
#    We skip the first column 'Date' when cleaning.
cleaned_columns = []
for col in prices_df.columns:
    if col == 'Date':
        cleaned_columns.append(col)
    else:
        # Take the part before the first space or parenthesis to get the ticker symbol
        ticker = col.split('(')[0].strip()  # remove any parentheses and trailing spaces
        cleaned_columns.append(ticker)
prices_df.columns = cleaned_columns

# 4. Convert the 'Date' column to datetime and set it as the DataFrame index.
prices_df['Date'] = pd.to_datetime(prices_df['Date'])
prices_df.set_index('Date', inplace=True)

# 5. Sort the DataFrame by date index to ensure it is in chronological order.
prices_df.sort_index(inplace=True)

# YOU NOW HAVE CLEANED AND FORMATTED DATA FRAME (prices_df)
