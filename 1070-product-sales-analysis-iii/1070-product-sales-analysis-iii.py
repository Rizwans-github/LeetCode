import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:

    sales = sales.drop(['sale_id'], axis=1)

    df = sales[sales['year'] == sales.groupby(['product_id'])['year'].transform('min')].rename(columns={'year': 'first_year'})



    return df