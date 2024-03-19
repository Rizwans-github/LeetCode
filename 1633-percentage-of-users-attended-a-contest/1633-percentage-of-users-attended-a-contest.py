import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    df = register.groupby('contest_id')['user_id'].nunique() * 100 / len(users)
    df =df.reset_index(name = 'percentage').round(2).sort_values(by=['percentage', 'contest_id'], ascending=[False, True])
    return df[['contest_id', 'percentage']]