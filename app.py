import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

st.title("SQL Data Explorer And Its running live")

server = '20.164.64.41'  # or 'your-server-name'
database = 'prod_warehouse.supercard'
username = 'supercard-reinhardt'
password = 'Verified1'
connection_string = f'mssql+pyodbc://supercard-reinhardt:Verified1@20.164.64.41/prod_warehouse.supercard?driver=ODBC+Driver+17+for+SQL+Server'

engine = create_engine(connection_string)

query = "select d.year as dep_year, sum(daf.deposit_amount) as dep_amount from fact_deposit_accounts_final daf left join dim_date d on d.date_id = daf.date_id group by d.year "
df = pd.read_sql(query, engine)

st.write("### Data Preview", df)

df = pd.read_sql(query, engine)
st.line_chart(df.set_index("dep_year")) 

column_to_plot = st.selectbox("Choose a column to visualize", df.columns)
st.bar_chart(df[column_to_plot].value_counts())

selected_year = st.selectbox("Select Year", df['dep_year'].unique())

filtered_df = df[df['dep_year'] == selected_year]


fig = px.bar(filtered_df, x="dep_year", y="dep_amount", title="Deposit Amount by Year")
st.plotly_chart(fig)
