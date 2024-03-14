import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    df = signups.merge(confirmations, on = 'user_id', how = 'left')
    df = df.groupby('user_id').apply(lambda x:round((x['action'] == 'confirmed').sum()/ x['user_id'].count(), 2)).reset_index(name='confirmation_rate') 
    return df[['user_id', 'confirmation_rate']]