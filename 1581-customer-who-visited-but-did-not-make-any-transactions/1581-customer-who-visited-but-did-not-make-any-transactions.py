import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df= pd.merge(visits, transactions, how= "left", on= "visit_id")
    df= df[df["transaction_id"].isnull()]
    df = df.groupby("customer_id")["customer_id"].value_counts().reset_index(name="count_no_trans")
    return df[["customer_id", "count_no_trans"]]