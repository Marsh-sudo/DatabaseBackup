import os
import time
import datetime

#MySQL database details to which backup to be done.

DB_HOST = "localhost"
DB_USER = "biggie"
DB_USER_PASSWORD = '12345'

#DB_NAME = 'backup/dbnames.txt' for many db names
DB_NAME = "hoods"
BACKUP_PATH = '/backup/dbbackup.txt'

#Getting current datetime to create separate backup folder

DATETIME = time.strftime('%m%d%Y-%H%M%S')

TODAYBACKUPPATH = BACKUP_PATH + DATETIME

#checking if backup folder already exists or not
print ("creating backup folder")
if not os.path.exists(TODAYBACKUPPATH):
    os.makedirs(TODAYBACKUPPATH)

#Code for checking if you want to take single database backup
print ("checking for databases names file")
if os.path.exists(DB_NAME):
    file1 = open(DB_NAME)
    multi = 1
    print ("database file found")
    print ("Starting backup of all dbs list in file" + DB_NAME)

else:
    print ("Database file not found..")
    print("Starting backup of database" + DB_NAME)
    multi = 0

#starting actual database backup process
if multi:
    in_file = open(DB_NAME,"r")
    flength = len(in_file.readlines())
    in_file.close()
    p=1
    dbfile = open(DB_NAME,"r")

    while p <= flength:
        db = dbfile.readline() #reading database name from file
        db = db[:-1] #deletes extra line
        dumpcmd = "mysqldump -u" + DB_USER + "-p" + DB_USER_PASSWORD + " " + db + " > " + TODAYBACKUPPATH + "/" + db + ".sql"
        os.system(dumpcmd)
        p = p+1
    dbfile.close()
else:
    db = DB_NAME
    dumpcmd = "mysqldump -u" + DB_USER + "-p" + DB_USER_PASSWORD + " " + db + " > " + TODAYBACKUPPATH + "/" + db + ".sql"
    os.system(dumpcmd)


print("Backup script completed")
print ("Your backups has been created in " + TODAYBACKUPPATH + "' directory" )