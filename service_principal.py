
import os
import subprocess

import re
from subprocess import check_output
azure_info=""
subscription_id=""
tenant_id=""


name= raw_input("name:")
password=raw_input("password:")
role=raw_input("role:")


#login to azure and recover the info
output = check_output(["az", "login"])

azure_info=output


#find the subscription id and tenant id in the output
subscription_id = re.findall(r'id.*', azure_info)
tenant_id = re.findall(r'tenantId.*', azure_info)

#converting the lists to string
subscription_id= "".join(subscription_id)
tenant_id= "".join(tenant_id)

#cleaning the id
subscription_id= subscription_id.replace('"' , "")
subscription_id= subscription_id.replace("," , "")
subscription_id= subscription_id.replace("id: " ,"")
tenant_id= tenant_id.replace('"' , "")
tenant_id= tenant_id.replace("," , "")
tenant_id= tenant_id.replace("tenantId: " , "")

a="[].appId"

check_output(["az", "account", "set","-s",subscription_id])
#creating the service account with the variables
#if the variables are empty you will get an error
check_output(["az","ad","sp","create-for-rbac","--name",name,"--password",password,"--role",role])
#Getting the the app id
app=check_output(["az","ad","sp","list","--display-name",name,"--query",a,"-o","tsv"])

print(subscription_id)
print(tenant_id)
print(app)
print(password)
