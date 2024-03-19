import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df= project.merge(employee, on = 'employee_id', how = 'left')
    df = df.groupby('project_id')['experience_years'].mean().reset_index(name='average_years').round(2)
    return(df)