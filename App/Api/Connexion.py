import sys

import pypyodbc as pyodbc

DRIVER = "SQL Server"
SERVER_NAME = "LAPTOP-JIE"
DATABASE_NAME = "JJ"

conexionStr = f"""
    Driver={DRIVER};
    Server={SERVER_NAME};
    DATABASE_NAME={DATABASE_NAME};
    Trust_Connexction=yes;
    Uid=;
    password:
"""

try:
    conn = pyodbc.connect(conexionStr)
except Exception as e:
    print(e)
    print("connexion terminée")
    sys.exit()
else:
    cursor = conn.cursor()