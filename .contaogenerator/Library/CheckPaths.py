import os

def checkPaths(pathElementController,pathElementTemplate,pathElementSCSS):
        
        print("Path generator: \n ")
        
        if os.path.exists(pathElementController) == False:
            os.makedirs(pathElementController)
            print("☑ Element controller path is generated!")
        else:
             print("☑ Element controller path are already generated!")

        if os.path.exists(pathElementTemplate) == False:
            os.makedirs(pathElementTemplate)
            print("☑ Element template path is generated!")
        else:
             print("☑ Element template path are already generated!")

        if os.path.exists(pathElementSCSS) == False:
            os.makedirs(pathElementSCSS)
            print("☑ Element SCSS path is generated!")

        else:
             print("☑ Element SCSS path are already generated!")
                 

        return True