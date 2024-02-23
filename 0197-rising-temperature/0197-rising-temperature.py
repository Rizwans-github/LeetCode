import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather["recordDate"] = pd.to_datetime(weather["recordDate"])
    weather.sort_values("recordDate", inplace = True)
    weather["lastTemp"] = weather["temperature"].shift(1)
    weather["lastdate"] = weather["recordDate"].shift(1)
    df = weather[(weather["temperature"] > weather["lastTemp"]) & (weather["lastdate"] + pd.Timedelta(days=1) == weather["recordDate"] )]
    return df[["id"]]
                                                 