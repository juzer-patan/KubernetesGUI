print("Welcome")
podname=input("Enter the name of the pod : ")
conname=input("Enter the name of the container : ")
imgname=input("Enter the name of the image : ")
volch = input("Do you want to mount any volumes?")

if(volch not in ("Yes","yes")):
    print("Volume found")
else: 
    print("No Volume found")
