import os

def generateGlobalData():
        
    if not (os.path.isfile('global.txt')):

        f = open("global.txt", "a")
        
        namespace = input("Please enter namespace title (ex : Test\\Basic\\ContentElements) : \n")
        shortNamespace = input("Please enter SCSS path from public folder, namespace (ex : testbasic): \n ")
        
        f.write(namespace + '\n')
        f.write(shortNamespace + '\n')
        print('☑ Global data file generated!')
        f.close()

    else:
        print('☑ Global data file exists!')
        return True

def deleteGlobalData():
    if os.path.exists('global.txt'):
        os.remove("global.txt") 
        print('☑ Global data file deleted!')
    else:
        print("𐄂 File dosen't exists")    