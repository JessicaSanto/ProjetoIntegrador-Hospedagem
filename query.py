# pip install mysql-connector-python
# pip install streamlit
import mysql.connector
import pandas as pd

# Conexão
def get_mysql_data(query):
    conn = mysql.connector.connect(
        host="projetointegradorbanco.mysql.database.azure.com",
        port="3306",
        user="jessica",
        password="senai@134",
        db="medidor"
        )
    
    dataframe = pd.read_sql(query, conn)

    # Fechar a conexão
    conn.close()

    return dataframe