import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather["recordDate"]=pd.to_datetime(weather["recordDate"])
    weather.sort_values("recordDate", inplace= True)
    weather["lastDate"] = weather["recordDate"].shift(1)
    weather["lastTemp"] = weather["temperature"].shift(1)
    df = weather[(weather["temperature"] > weather["lastTemp"]) & (weather["recordDate"] == weather["lastDate"] + pd.Timedelta(days=1))]
    return df[["id"]]