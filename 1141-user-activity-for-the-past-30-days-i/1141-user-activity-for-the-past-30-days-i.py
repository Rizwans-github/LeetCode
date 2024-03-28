import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    date = '2019-07-27'
    activity['is_in_30days'] = (pd.to_datetime(date) - activity['activity_date'] ).dt.days.between(0,29)
    output = activity[activity['is_in_30days']].groupby('activity_date')['user_id'].nunique().rename('active_users') .reset_index()
    return output.rename(columns={'activity_date':'day'})