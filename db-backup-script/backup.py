import pyodbc
import os
import pandas as pd
from datetime import datetime

# Connection parameters
server = 'localhost'
database = 'mydatabase'
username = 'myusername'
password = 'mypassword'

# Backup directory
backup_dir = 'C:/backup'

# Create a connection object
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + 
';UID=' + username + ';PWD=' + password)

# Create a cursor object
cursor = conn.cursor()

# Backup file name
backup_file = 'mydatabase_backup_' + str(datetime.now().strftime('%Y%m%d_%H%M%S')) + '.bak'

# Backup command
backup_command = 'BACKUP DATABASE mydatabase TO DISK=\'' + os.path.join(backup_dir, 
backup_file) + '\''

# Execute the backup command
cursor.execute(backup_command)

# Backup details
backup_details = {'database': [database], 'backup_file': [backup_file], 'backup_datetime': 
[datetime.now()]}

# Create a DataFrame object from the backup details
backup_df = pd.DataFrame(data=backup_details)

# Backup details file
backup_details_file = os.path.join(backup_dir, 'backup_details.csv')

# Write backup details to a CSV file
backup_df.to_csv(backup_details_file, index=False)y

