import os

def checkPaths(pathElementController,pathElementTemplate,pathElementSCSS,pathConfig,pathDca,pathLanguagesDE,pathLanguagesEN,pathImageRules):
        
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

        
        if os.path.exists(pathConfig) == False:
            os.makedirs(pathConfig)
            print("☑ Config path is generated!")

        else:
             print("☑ Config path are already generated!")

        
        if os.path.exists(pathDca) == False:
            os.makedirs(pathDca)
            print("☑ DCA path is generated!")

        else:
             print("☑ DCA path are already generated!")

        if os.path.exists(pathLanguagesDE) == False:
            os.makedirs(pathLanguagesDE)
            print("☑ DE Language path is generated!")

        else:
             print("☑ DE Language are already generated!")
              

        if os.path.exists(pathLanguagesEN) == False:
            os.makedirs(pathLanguagesEN)
            print("☑ EN Language path is generated!")

        else:
             print("☑ EN Language are already generated!")
              
        if os.path.exists(pathImageRules) == False:
            os.makedirs(pathImageRules)
            print("☑ Config for image rules path is generated!")

        else:
             print("☑ Config for image rules path are already generated!")
              

        return True