import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue.sort_values('turn', inplace=True)
    i = queue['weight'].cumsum().searchsorted(1000, side='right') # ideally we'd only process up to the threshold, not the whole column
    ans = queue.iloc[i-1]['person_name']

    return pd.DataFrame({'person_name': [ans]})