import pandas as pd
import seaborn as sns
import env

# Aquire.py Exercises/Function Setup

url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{database}'

# Exercise 1 -- get_titanic_data

def get_titanic_data():

    url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{database}'

    query = '''SELECT * FROM passengers'''

    df = pd.read_sql(query, url)

    return df

get_titanic_data

# Exercise 2 -- get_iris_data