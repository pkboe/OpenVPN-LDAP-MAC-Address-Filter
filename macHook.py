#!/usr/bin/python3.5
   
import re
import sys
   
# vars
db_file = '/etc/openvpn/db.txt'
log_file = '/var/log/openvpn.log'
regex_mac = 'IV_HWADDR=(.*)'
regex_username = 'username \'(.*)\''
login = False
   
# create dict
logs_username_mac_list = []
   
# get mac and username from logs
with open(log_file, 'r') as log:
    lines = log.readlines()
    # read only latest 100 lines
    last_50_lines = lines[-50:]
    # iterate latest 50 lines
    for line in last_50_lines:
   
        # find mac
        match_mac = re.search(regex_mac, line)
        if match_mac:
            log_mac = match_mac.group(1)
            # on match, add it to list
            logs_username_mac_list.append(log_mac)
   
        # find username
        match_username = re.search(regex_username, line)
        if match_username:
            log_username = match_username.group(1)
            # on match, add it to list
            logs_username_mac_list.append(log_username)
   
# get username and mac from db
with open(db_file, 'r') as db:
    for line in db.readlines():
        # split username and password based on '-'
        splitter = line.split('-', 1)
        if len(splitter) >= 2:
            # 0 index is username, removing newline
            db_username = (splitter[0]).rstrip("\n")
            # 1 index is mac, removing newline
            db_mac = (splitter[1]).rstrip("\n")
            # check if username in collected logs matches what we have in db
            if db_username in logs_username_mac_list:
                # get user index and remove 1
                user_index = logs_username_mac_list.index(db_username) - 1
                mac_index = logs_username_mac_list[user_index]
                # if log mac matches db_mac
                if mac_index == db_mac:
                    login = True
   
if login:
    print('GG')
    sys.exit(0)
else:
    sys.exit(1)
