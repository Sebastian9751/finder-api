from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os 

load_dotenv()
db_user= os.getenv('DB_USER')
db_password= os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_SERVER')

try:
    params = f"DRIVER={'ODBC Driver 18 for SQL Server'};SERVER={db_host};UID={db_user};PWD={db_password};Encrypt=no"
    engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

    with engine.connect() as connection:
        print("Conexión exitosa.")
        result = connection.execute(text('SELECT 1+1'))
        rows = result.fetchall()
        print(rows[0])
    Session = sessionmaker(bind=engine)
    session = Session()
except Exception as ex:
    print("Error de conexión: {}".format(ex))
