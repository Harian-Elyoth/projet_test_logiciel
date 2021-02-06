#/***********************************************
#     Authors : Aziz IDOMAR, Enzo CALVINO
#************************************************/

#!/bin/bash

# http class
ln -fs ../http_comm/http_server/http_server.py
ln -fs ../http_comm/http_client/http_client.py

# sql class
ln -fs ../database/sql.py

# database
ln -fs ../database/chatsystem.sql

# create .db file
sqlite3 chatsystem.db -cmd ".read chatsystem.sql" ".quit"

