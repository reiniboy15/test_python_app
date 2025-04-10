import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Replace YOUR values here
server = '20.164.64.41'  # or 'your-server-name'
database = 'prod_warehouse.supercard'
username = 'supercard-reinhardt'
password = 'Verified1'

# Create connection string
connection_string = f'mssql+pyodbc://supercard-reinhardt:Verified1@20.164.64.41/prod_warehouse.supercard?driver=ODBC+Driver+17+for+SQL+Server'

# Connect using SQLAlchemy
engine = create_engine(connection_string)

# Query some data
query = "select d.year as dep_year, sum(daf.deposit_amount) as dep_amount from fact_deposit_accounts_final daf left join dim_date d on d.date_id = daf.date_id group by d.year "
df = pd.read_sql(query, engine)

# Preview
print(df.head())


# Example: Plot a bar chart of counts by category
df['dep_year'].value_counts().plot(kind='bar')
plt.title('Sample Distribution')
plt.xlabel('Category')
plt.ylabel('Sum')
plt.show()
