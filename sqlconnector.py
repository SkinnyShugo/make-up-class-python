import os
import MySQLdb # import the MySQLdb module
from dotenv import load_dotenv

load_dotenv()

# Create the connection object
connection = MySQLdb.connect(
    host="aws.connect.psdb.cloud",
    user="idktomi37oen62h4el4m",
    passwd="pscale_pw_GtlKhGeoxf58WfRJoJakmUJisvdDlhH8gyyGG1zGikt",
    db="skinnybase",
    autocommit = True,
    ssl_mode="VERIFY_IDENTITY",
    ssl      = {
    "ca": "/etc/ssl/certs/ca-certificates.crt"
  }
)

# Create cursor and use it to execute SQL command
cursor = connection.cursor()
cursor.execute("select @@version")
version = cursor.fetchone()

if version:
    print('Running version: ', version)
else:
    print('Not connected.')