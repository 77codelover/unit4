import os
def findfiles(filename,path):
    result = []
    for root,dir,files in os.walk(path):
       if filename in files:
            result.append(os.path.join(root,filename))
    if result == []:
        return("No such file found")
    else:
        return result
    
name = input("Enter Filename with extension for file creation : ")
f = open(name,'w')
f.close()
files = input("Enter filename with extension for searching : ")
print(findfiles(name,os.getcwd()))
