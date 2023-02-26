#!/usr/bin/python3
#!/usr/bin/env python3
# Requires urbackup-server-python-web-api-wrapper: https://github.com/uroni/urbackup-server-python-web-api-wrapper
#
# Short test to local urbackup server instance: 
# urbackup-discovery.py "http://127.0.0.1:55414/x" "admin" "pasword"

import urbackup_api
import json
import sys
import ssl

# Disable certificate verification when connecting via HTTPS (otherwise, if the certificate is self-signed, connection will fail)
ssl._create_default_https_context = ssl._create_unverified_context

server = urbackup_api.urbackup_server(sys.argv[1],sys.argv[2],sys.argv[3])
i = 0
print ("[", end='')
for client in server.get_status():
    if i > 0 : print("," , end='')
    print(json.dumps(client))
    i += 1
print ("]", end='')
