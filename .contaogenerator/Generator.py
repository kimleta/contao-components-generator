import os
from Elements import *
from Library import *


class Generator:

    # Check if folder structure is valid, if not generate one
    def checkPaths():
        return CheckPaths.checkPaths()
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
        creator = ElementGenerator.createElements(data)

        return creator

    # Main Function
    def main(self):

        # Check paths
        self.checkPaths()
        # Check global Data
        self.generateGlobalData()
        # Create elements
        self.createElements(self)



# Call function
Generator.main(Generator)










    
    
