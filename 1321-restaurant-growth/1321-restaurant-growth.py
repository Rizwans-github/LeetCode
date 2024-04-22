import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    customer = customer.groupby('visited_on')['amount'].sum().reset_index()
    customer['day'] = customer['visited_on'].rank(method='min')
    customer['total_7'] = customer['amount'].rolling(window=7, min_periods=1).sum()
    customer['average_amount'] = customer['amount'].rolling(window=7, min_periods=1).mean().round(2)
    
    return customer[customer['day']>6][['visited_on','total_7','average_amount']].rename(columns=({'total_7':'amount'}))