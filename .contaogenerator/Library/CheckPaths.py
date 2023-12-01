import os

pathElementController = "./src/Resources/contao/elements/"
pathElementTemplate = "./src/Resources/contao/templates/elements/"
pathElementSCSS = "./src/Resources/public/css/elements/"


def checkPaths():
        
        print("Test is everything generated before start : \n \n")
        
        if os.path.exists(pathElementController) == False:
            os.makedirs(pathElementController)
        else:
             print("☑ Element controller path is generated!")

        if os.path.exists(pathElementTemplate) == False:
            os.makedirs(pathElementTemplate)
        else:
             print("☑ Element template path is generated!")

        if os.path.exists(pathElementSCSS) == False:
            os.makedirs(pathElementSCSS)
        else:
             print("☑ Element SCSS path is generated!")
                 

        return True