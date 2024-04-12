import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    
    df = products[products['change_date']<='2019-08-16'].sort_values(by=['product_id', 'change_date'],ascending=[True,True]).drop_duplicates(subset=['product_id'],keep='last').rename(columns={'new_price':'price'})[['product_id', 'price']]    
    return products[['product_id']].merge(df,how='left',on='product_id').fillna(10).drop_duplicates()