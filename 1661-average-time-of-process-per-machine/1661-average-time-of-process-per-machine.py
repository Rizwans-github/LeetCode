import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    startDf = activity[activity["activity_type"] == "start"]
    endDf = activity[activity["activity_type"] == "end"]
    df = pd.merge(startDf, endDf, on = ["machine_id", "process_id"], suffixes=("Start", "End"))
    df["processing_time"] = df["timestampEnd"] - df["timestampStart"]
    df = df.groupby("machine_id", as_index=False)["processing_time"].mean().round(3)
    return df[["machine_id", "processing_time"]]