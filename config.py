import os

db_username = "vietnamstock_usr1"
db_psw = "stock@2019"
local_test = False
conn_string = f"host=127.0.0.1 dbname=vietnam_stock user={db_username} password={db_psw}"
download_path = "./data/download"  # os.getcwd()
initial_load_path = "./data/initial_load"
