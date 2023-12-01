import os

pathElementController = "./src/Resources/contao/elements/"
pathElementTemplate = "./src/Resources/contao/templates/elements/"
pathElementSCSS = "./src/Resources/public/css/elements/"


def checkPaths():
        
        if os.path.exists(pathElementController) == False:
            os.makedirs(pathElementController)
        else:
             print(pathElementController + " exists!")

        if os.path.exists(pathElementTemplate) == False:
            os.makedirs(pathElementTemplate)
        else:
             print(pathElementTemplate + " exists!")

        if os.path.exists(pathElementSCSS) == False:
            os.makedirs(pathElementSCSS)
        else:
             print(pathElementSCSS + " exists!")
                 

        return True