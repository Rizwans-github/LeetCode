import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    city=insurance[['pid','lat','lon']]
    city_duplicates=city.duplicated(subset=['lat','lon'],keep=False)
    city_unique=city[~city_duplicates]
    tiv=insurance[['pid','tiv_2015','tiv_2016']]
    tiv_duplicates=tiv.duplicated(subset=['tiv_2015'],keep=False)
    tiv_dup=tiv[tiv_duplicates]
    target_insurance=pd.merge(tiv_dup,city_unique,on='pid')
    tiv_2016_sum=target_insurance['tiv_2016'].sum().round(2)
    data={'tiv_2016':[tiv_2016_sum]}
    return pd.DataFrame(data)
     
