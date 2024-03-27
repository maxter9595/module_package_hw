from datetime import datetime

import pandas as pd

from dirty_main import *
from application.db.people import get_employees
from application.salary import calculate_salary


if __name__ == "__main__":
    
    print("", "Текущая дата:", datetime.now().strftime("%d-%m-%Y"), sep="\n")
    print_something()

    df_append_list = []
    employees, salary = get_employees(), calculate_salary()
    emps_id = [employee.get('id') for employee in employees]
    for emp_id, emp_data, emp_salary in zip(emps_id, employees, salary):
        df = pd.DataFrame({**emp_data, **emp_salary}, index = [emp_id])
        df.index.name = 'id'
        df_append_list.append(df.iloc[:,1:])

    df_concat = pd.concat(df_append_list)
    print(df_concat)