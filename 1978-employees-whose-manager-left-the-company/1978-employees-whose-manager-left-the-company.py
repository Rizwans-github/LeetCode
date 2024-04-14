import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    return (
        employees
        [
            ~(employees["manager_id"].isin(employees["employee_id"]))
            & (employees["salary"] < 30000)
        ]
        .dropna()
        .sort_values("employee_id")
        [["employee_id"]]
    )