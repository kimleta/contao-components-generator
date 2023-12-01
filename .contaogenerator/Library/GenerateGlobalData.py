import os

def generateGlobalData():
        
    if not (os.path.isfile('global.txt')):

        f = open("global.txt", "a")
        
        namespace = input("Please enter namespace title (ex : Test\Basic\ContentElements) : \n")
        shortNamespace = input("Please enter SCSS path from public folder, namespace (ex : testbasic): \n ")
        
        f.write(namespace + '\n')
        f.write(shortNamespace + '\n')

        f.close()

    else:
        print('File Exists')
        return True

def deleteGlobalData():
    