import teradata
import os

# -------------------- INIT -------------------- #
DNS_NAME = os.environ["DNS_NAME"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
GOPATH = os.environ["GOPATH"]
OUTPUT_FILE_NAME = os.path.abspath("/data.json")

# ------------ REMOVE EXISTING FILE ------------ #
if os.path.exists(OUTPUT_FILE_NAME):
    os.remove(OUTPUT_FILE_NAME)

# ----------- SETUP TERADATA SESSION ----------- #
udaExec = teradata.UdaExec (appName="test", version="1.0", logConsole=False)
session = udaExec.connect(method="odbc", system=DNS_NAME,
        username=USERNAME, password=PASSWORD)

# --------------- READ SQL QUERY --------------- #
path = os.path.abspath(GOPATH + "/src/scriptRunner/sql/test.sql")
sqlFile = open(path, 'r')
sqlStatement = sqlFile.read()

# --------------- SIMPLE PRINT ----------------- #
for row in session.execute(sqlStatement):
    print(row)
