from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

load_dotenv()

try:
    params = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=zrestaurant.mssql.somee.com;DATABASE=zrestaurant;UID=ssebs_SQLLogin_2;PWD=dzxwtzp6re;Encrypt=no'
    engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

    with engine.connect() as connection:
        print("Conexión exitosa.")
        result = connection.execute(text('SELECT 1+1'))
        rows = result.fetchall()
        print(rows[0])
    Session = sessionmaker(bind=engine)
    session = Session()
except Exception as ex:
    print("Error durante la conexión: {}".format(ex))
