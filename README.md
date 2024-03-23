# OpenVPN Configuration

## Client Configuration
Add the following directive in your client configuration file:

push-peer-info


## Server Configuration
Add the following directives in your server configuration file:

script-security 2 verb 3 client-connect /etc/openvpn/mac-check.py


## User-MAC Address Mapping
Create a file at `/etc/openvpn/db.txt` where you map each username to a MAC address in the following format:

username-M:A:C:A:D:R:E:S:S pranil.kharche-C4:23:60:FA:CC:1A

When a user connects, their MAC address will be logged under `IV_HWADDR`. Writing this MAC address in `db.txt` will grant this user access only from that machine.

## Log File Permissions
Run the following command to give the script access to search through the log file:

chmod 664 /var/log/openvpn.log


## Python Script
Ensure you have Python 3.6 in your bin folder or create a symlink to it. Then, create the `openvpn_login_checker.py` script:
