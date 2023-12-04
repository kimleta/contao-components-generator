import os
import inquirer
from Elements import *
from Library import *


class Generator:

    # Save Paths
    pathElementController = "./src/Resources/contao/elements/"
    pathElementTemplate = "./src/Resources/contao/templates/elements/"
    pathElementSCSS = "./src/Resources/public/css/elements/"

    # Check if folder structure is valid, if not generate one
    def checkPaths(self):
        return CheckPaths.checkPaths(self.pathElementController,self.pathElementTemplate,self.pathElementSCSS)
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
    def createElements(self):
        # Get array of data
        data = self.getTemplateData()
        # Give data to the function 
        creator = ElementGenerator.createElements(data,self.pathElementController,self.pathElementTemplate,self.pathElementSCSS)

        return creator
    
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
        if(menuOption == "Delete global data"):
            if(self.deleteGlobalData()):
                return True
        # Menu: Check Paths
        if(menuOption == "Generate new element"):
            # Check paths
            self.checkPaths()
            # Check global Data
            self.generateGlobalData()
            # Create elements
            self.createElements(self)
        # Menu: Exit
        if(menuOption == "Help"):
            print("Please look at readme file.")
            return True
        # Menu: Exit
        if(menuOption == "Exit"):
            print("Exiting script...")
            return True



# Call function
Generator.main(Generator)










    
    
