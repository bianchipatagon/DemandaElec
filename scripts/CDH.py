import pandas as pd
import numpy as np
import numpy as N
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import seaborn as sns
from scipy.stats import spearmanr
from matplotlib.ticker import MultipleLocator


df = pd.read_csv('/home/emi/Documents/MAESTRIA/14-Metodología/DemandaElec/DATOS/prueba_v.txt', header=None, delimiter=',', na_values='-99')
df.index = pd.date_range(start="2021-01-01 00:00:00", end="2023-12-31  23:00:00",freq="h")
print(df)
tem = round(0.81*df[7] + 0.1*df[8] + 0.09*df[9],0)


def calculate_daily_degree_hours(df, temp_col, datetime_col, base_temp=18):
    """
    Calculate heating and cooling degree hours for each day from hourly data.
    
    Parameters:
    -----------
    df : pandas DataFrame
        DataFrame containing hourly temperature data
    temp_col : str
        Name of the temperature column
    datetime_col : str
        Name of the datetime column
    base_temp : float
        Base temperature threshold
    
    Returns:
    --------
    pandas DataFrame : DataFrame with daily HDD and CDD values
    """
    # ~ df = df.copy()
    # ~ df[0] = pd.to_datetime(df[datetime_col]).dt.date
    
    # Calculate degree hours for each row
    df['HDD'] = N.maximum(16.5 - df[7], 0)
    df['CDD'] = N.maximum(df[7] - 18.5, 0)
    
    # Group by date and sum
    daily = df.groupby('date').agg({
        'HDD': 'sum',
        'CDD': 'sum'
    }).reset_index()
    
    daily.columns = ['date', 'heating_degree_hours', 'cooling_degree_hours']

    return daily
    
if __name__ == "__main__":
  
    # Calculate daily degree hours with base temperature of 18°C
    daily_results = calculate_daily_degree_hours(
        df, 
        temp_col='7',
        datetime_col='0',
        base_temp=18
    )
    
    print("Daily Heating and Cooling Degree Hours:")
    print(daily_results)
    print(f"\nTotal Heating Degree Hours: {daily_results['heating_degree_hours'].sum():.2f}")
    print(f"Total Cooling Degree Hours: {daily_results['cooling_degree_hours'].sum():.2f}")

