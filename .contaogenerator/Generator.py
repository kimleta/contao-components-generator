import os
import inquirer
from Elements import *
from Library import *


class Generator:

    # Save Paths
    pathElementController = "./src/Resources/contao/elements/"
    pathElementTemplate = "./src/Resources/contao/templates/elements/"
    pathElementSCSS = "./src/Resources/public/css/elements/"
    pathConfig = "./src/Resources/contao/config/"
    pathDca = "./src/Resources/contao/dca/"
    pathLanguagesDE = "./src/Resources/contao/langauges/de/"
    pathLanguagesEN = "./src/Resources/contao/langauges/en/"
    pathImageRules = "./src/Resources/config/"
    

    # Check if folder structure is valid, if not generate one
    def checkPaths(self):
        return CheckPaths.checkPaths(self.pathElementController,self.pathElementTemplate,self.pathElementSCSS,self.pathConfig,self.pathDca,self.pathLanguagesDE,self.pathLanguagesEN,self.pathImageRules)
    # Generate global data if dosen't exist
    def generateGlobalData():
        return GenerateGlobalData.generateGlobalData()
    # Delete global data file
    def deleteGlobalData():
        return GenerateGlobalData.deleteGlobalData()
    
    # Get Template data
    def getTemplateData():
        # Get selected object from select menu
        o = ElementGenerator.selectElementContaoController()
        # Call a object
        object = globals()[o]
        return ElementGenerator.getTemplateData(object)
    
    # Create Elements
    def createElements(self,data):
        # Give data to the function 
        creator = ElementGenerator.createElements(data,self.pathElementController,self.pathElementTemplate,self.pathElementSCSS)
        return creator
    
    # Create/Append tl_content
    def appendPallete(self,data):
        # Return data to the function
        return PalleteGenerator.appendPallete(self.pathDca,data['pallete'])
    
    # Create/Append config.php
    def appendConfig(self,data):
        # Return data to the function
        return ConfigGenerator.appendConfig(self.pathConfig,data['config'])
    
     # Create/Append config.php | wrapper
    def appendConfigWrapper(self,data):
        # Return data to the function
        return ConfigGenerator.appendWrapperConfig(self.pathConfig,data['wrapper'])
    
    # Create/Append tl_content | fields
    def appendFields(self,data):
        # Return data to the function
        return FieldsGenerator.appendFields(self.pathDca,data['fields'])
    
    # Create/Append config.yaml 
    def appendImageRules(self,data):
        # Return data to the function
        return ImageRulesGenerator.appendImageRules(self.pathImageRules,data['imagerules'])
    
    def menuOptions():
        questions = [
        inquirer.List('menuOption',
                    message= "Welcome to the Contao Generator Script! Please select your action",
                    choices= ['Generate new element','Generate/Check paths','Delete global data','Help','Exit'],
                ),
        ]
        answers = inquirer.prompt(questions)

        return answers['menuOption']

    # Main Function
    def main(self):
            # Script main menu
            menuOption = self.menuOptions()

            # Menu: Check Paths
            if(menuOption == "Generate/Check paths"):
                return self.checkPaths(self)
            # Menu: Check Paths
            elif (menuOption == "Delete global data"):
                if(self.deleteGlobalData()):
                    return True
            # Menu: Check Paths
            elif (menuOption == "Generate new element"):
                
                # Get array of data and save it
                data = self.getTemplateData()
                
                # Check paths
                self.checkPaths(self)
                # Check global Data
                self.generateGlobalData()
                # Create elements
                self.createElements(self,data)
                # Append Config
                self.appendConfig(self,data)
                self.appendConfigWrapper(self,data) # Wrapper TL_WRAPPER
                # Append Pallete
                self.appendPallete(self,data)
                # Append fields
                self.appendFields(self,data)
                # Append image rules
                self.appendImageRules(self,data)

            # Menu: Exit
            elif (menuOption == "Help"):
                print("Please look at readme file.")
                return True
            # Menu: Exit
            elif (menuOption == "Exit"):
                print("Exiting script...")
                return True
            



# Call function
Generator.main(Generator)










    
    
