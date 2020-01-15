import teradata
import os
import argparse
from pymongo import MongoClient
import pandas

# -------------------- INIT -------------------- #
EDW_DNS_NAME = os.environ["EDW_DNS_NAME"] # "EDWT"
EDW_USERNAME = os.environ["EDW_USERNAME"] # ServiceAccountID
EDW_PASSWORD = os.environ["EDW_PASSWORD"] # ServiceAccountPass
GOPATH = os.environ["GOPATH"]
OUTPUT_FILE_NAME = os.path.abspath("/data.json")

# ------------ REMOVE EXISTING FILE ------------ #
if os.path.exists(OUTPUT_FILE_NAME):
    os.remove(OUTPUT_FILE_NAME)

print("Before")
# ----------- SETUP TERADATA SESSION ----------- #
udaExec = teradata.UdaExec (appName="test", version="1.0", logConsole=False)
session = udaExec.connect(method="odbc", system=EDW_DNS_NAME,
        username=EDW_USERNAME, password=EDW_PASSWORD)
print("After")

# --------------- READ SQL QUERY --------------- #
path = os.path.abspath(GOPATH + "/src/scriptRunner/sql/test.sql")
sqlFile = open(path, 'r')
sqlStatement = sqlFile.read()

# ------------- WRITE ROWS TO FILE ------------- #
# # NEED: RewardID, DisplayName, Amount, ClaimLimitations, ProviderLimits, Frequency, Codes, Age, 
# # Population, Effective_Date, End_Date
# with open(OUTPUT_FILE_NAME, "a+") as j:
#     for row in session.execute("select * from hra_app_own.reward where hra_unit = 19;"):
#         j.write(row)

# --------------- SIMPLE PRINT ----------------- #
for row in session.execute(sqlStatement):
    print(row)
