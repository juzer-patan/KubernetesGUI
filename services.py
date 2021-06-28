import json
import subprocess


def get_all(): 
    cmd="curl -s --cacert ca.crt --cert adminfinalcert.crt  --key adminfinal.key https://172.31.33.38:6443/api/v1/namespaces/default/services"
    op = subprocess.getoutput(cmd)
    data = json.loads(op)
    return data['items']

def create()  

