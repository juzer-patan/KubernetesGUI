import os
podname=input("Enter the name of the pod : ")
conname=input("Enter the name of the container : ")
imgname=input("Enter the name of the image : ")
volch = input("Do you want to mount any volumes?")

labels={}
while(True) :
    ch=int(input("To stop adding labels press 1 : "))
    if(ch==1):
        break
    key = input("Enter the key : ")
    value = input("Enter the value : ")
    labels[key]=value
if(volch not in ("Yes","yes")):
    cmd="""curl --cacert ca.crt --cert adminfinalcert.crt --key adminfinal.key -X POST -H 'Content-Type: application/yaml' -H 'Authorization: Bearer <JWT_TOKEN>' --data '
    apiVersion: v1
    kind: Pod
    metadata:
      name: {0}
      labels: 
        {3}
    spec:
      containers:
      - name: {1}
        image: {2}
        ports:
        - containerPort: 80
    ' https://172.31.33.38:6443/api/v1/namespaces/default/pods""".format(podname,conname,imgname,labels)
output = os.system(cmd)
print(output)
