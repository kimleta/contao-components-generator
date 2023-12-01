import os
import inquirer


def getListOfElementControllers():

        # Folder path
        dir_path = r'.contaogenerator\Elements'

        # List to store files
        res = []

        # Iterate directory
        for path in os.listdir(dir_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                # Indend into array and remove extension name
                res.append(path.replace(".py",""))
        # Remove unwanted file
        res.remove('__init__')
        return res

    # This class gets called in generator.py
    # It display select menu to choose one of controllers from Elements folder
def selectElementContaoController(): 

    # Get all element controllers
    listOfChoices = getListOfElementControllers()
    # Chose a controller
    questions = [
    inquirer.List('controller',
                message= "What controller do you want to extend?",
                choices= listOfChoices,
            ),
    ]
    answers = inquirer.prompt(questions)

    return answers["controller"]

def generateController(controller,contentElement,elementTemplate):
    
    # Read 1st line of global txt for namespace
    namespace = open("global.txt").readline().rstrip()
    # Parse string
    parsedController = controller.format(namespace,contentElement,elementTemplate,elementTemplate)
    # Return String
    return parsedController


def generateTemplate(template,elementTemplate):
    # Read 2nd line of global.txt for shortnamespace
    with open("global.txt", "r") as text_file:
        data = text_file.readlines()
    # Short namespace
    shortnamespace = data[1].rstrip()

    parsedTemplate = template.format(shortnamespace,elementTemplate,elementTemplate)
    return parsedTemplate


def generateStyles(scssFile,elementTemplate):
      
      parsedStyles = scssFile.format(elementTemplate)

      return parsedStyles

# Returns formated data set
def getTemplateData(object):
    
    # Get temporary data
    contentElement = input("Please enter a name of new content element (ex : ContentSimpleText): \n")
    elementTemplate = input("Please enter single name for html template and scss file (ex : simple_text) : \n ")

    # Get element data
    template = object.template
    scssFile = object.scssTemplate
    controller = object.controller

    # Generate controller
    controller = generateController(controller,contentElement,elementTemplate)
    # Generate template
    template = generateTemplate(template,elementTemplate)
    # Generate controller
    styles = generateStyles(scssFile,elementTemplate)
    
    
    arrayReturn = {
         "controller":controller,
         "template":controller,
         "styles":controller,
    }
    

    print(styles)

