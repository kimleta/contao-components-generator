import os
import inquirer


def getListOfElementControllers():
    # Folder path
    dir_path = r".contaogenerator\Elements"

    # List to store files
    res = []

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            # Indend into array and remove extension
            res.append(path.replace(".py", ""))
    # Remove unwanted file
    res.remove("__init__")
    return res


# This class gets called in generator.py
# It display select menu to choose one of controllers from Elements folder
def selectElementContaoController():
    # Get all element controllers
    listOfChoices = getListOfElementControllers()
    # Chose a controller
    questions = [
        inquirer.List(
            "controller",
            message="What controller do you want to extend?",
            choices=listOfChoices,
        ),
    ]
    answers = inquirer.prompt(questions)

    return answers["controller"]


def generateController(controller, contentElement, elementTemplate):
    # Read 1st line of global txt for namespace
    namespace = open("global.txt").readline().rstrip()
    # Parse string
    parsedController = controller.format(
        namespace, contentElement, elementTemplate, elementTemplate
    )
    # Return String
    return parsedController


def generateTemplate(template, elementTemplate):
    # Read 2nd line of global.txt for shortnamespace
    with open("global.txt", "r") as text_file:
        data = text_file.readlines()
    # Short namespace
    shortnamespace = data[1].rstrip()

    parsedTemplate = template.format(shortnamespace, elementTemplate, elementTemplate)
    return parsedTemplate


# Generate SCSS file
def generateStyles(scssFile, elementTemplate):
    parsedStyles = scssFile.format(elementTemplate)

    return parsedStyles


# Generate tl_content pallete
def generatePallete(dcaPallete, elementTemplate):
    parsedPallete = dcaPallete.format(elementTemplate)

    return parsedPallete

# Generate TL_WRAPPERS for config.php
def generateWrapper(wrapper,elementTemplate):
    parsedWrapper = wrapper.format(elementTemplate)

    return parsedWrapper

# Generate config.php class for autoloader
def generateConfig(configLoader, contentElement, elementTemplate):
    # Read 1st line of global txt for namespace
    namespace = open("global.txt").readline().rstrip()

    parsedConfig = configLoader.format(elementTemplate,namespace,contentElement)

    return parsedConfig

# Generate YAML for image rules
def generateImageRules(imagerules,elementTemplate):
    
    parsedImageRules = imagerules.format(elementTemplate)

    return parsedImageRules

# Generate Custom fields
def generateCustomFields(customfields):
    # Why ? Well becouse to not confuse in latter code :) Just returning what it get, done on purpose :) 
    return customfields

# Generate language for German
def generateLanguageDE(languageDE,elementTemplate,languageDEInput):
    
    parsedLanguage = languageDE.format(elementTemplate,elementTemplate,languageDEInput)

    return parsedLanguage
    

# Generate language for English
def generateLanguageEN(languageEN,elementTemplate,languageENInput):
        
    parsedLanguage = languageEN.format(elementTemplate,elementTemplate,languageENInput)

    return parsedLanguage

# Returns formated data set
def getTemplateData(object):
    # Get data and write it in temporary file
    contentElement = input(
        "Please enter a name of new content element (ex : ContentSimpleText): \n"
    )
    elementTemplate = input(
        "\nPlease enter single name for html template and scss file (ex : simple_text) : \n"
    )
    
    languageENInput = input(
        "\nPlease enter name of element on English (ex : Simple Text) (click enter if not needed) : \n"
    )
    languageDEInput = input(
        "\nPlease enter name of element on German (ex : Simple Text) (click enter if not needed) : \n"
    )

    # Remember temproary content controller name and template name
    f = open("temp.txt", "w")
    f.write(contentElement + "\n")
    f.write(elementTemplate)
    f.close()
    # Get element data # Mandatory
    template = object.template
    scssFile = object.scssTemplate
    controller = object.controller
    dcaPallete = object.dcaPallete
    configLoader = object.configLoader
    
    # Optional
    
    if object.customFields:
        customFields = object.customFields

    if object.configWrapperLoader:
        configWrapperLoader = object.configWrapperLoader

    if object.imagerules:
        imagerules = object.imagerules

    if object.languageDE:
        languageDE = object.languageDE

    if object.languageEN:
        languageEN = object.languageEN

    # Generate controller
    controller = generateController(controller, contentElement, elementTemplate)
    # Generate template
    template = generateTemplate(template, elementTemplate)
    # Generate controller
    styles = generateStyles(scssFile, elementTemplate)
    # Generate Pallete
    pallete = generatePallete(dcaPallete, elementTemplate)
    # Generate Config
    config = generateConfig(configLoader, contentElement, elementTemplate)
    
    # Optional

    customFieldsGen = None
    configWrapper = None
    imagerulesGen = None
    languageDEGen = None
    languageENGen = None
    
    if customFields:
        # Generate custom fileds
        customFieldsGen = generateCustomFields(customFields)

    if configWrapperLoader:
        # Generate TL_WRAPPER
        configWrapper = generateWrapper(configWrapperLoader,elementTemplate)

    if imagerules:
        # Generate image rule
        imagerulesGen = generateImageRules(imagerules,elementTemplate)

    if languageDE:
        # Generate Language DE
        languageDEGen = generateLanguageDE(elementTemplate,elementTemplate,languageDEInput)

    if languageEN:
        # Generate Language EN
        languageENGen = generateLanguageEN(elementTemplate,elementTemplate,languageENInput)

    arrayReturn = {
        "controller": controller,
        "template": template,
        "styles": styles,
        "pallete": pallete,
        "config": config,
        "fields" : customFieldsGen,
        "wrapper" : configWrapper,
        "imagerulse" : imagerulesGen,
        "langDE" : languageDEGen,
        "langEN" : languageENGen,
    }

    return arrayReturn


# Read each line and return it as array
def getTempData():
    # Read each file and remember into array
    with open("temp.txt") as file:
        lines = [line.rstrip() for line in file]

    # Delete temporary file
    os.remove("temp.txt")
    return lines


def createElements(array, pathElementController, pathElementTemplate, pathElementSCSS):
    # Get temporary data
    tempData = getTempData()

    # get controller name and template name
    controllerName = tempData[0]
    elementTemplateName = tempData[1].lower()

    # Template data
    template = array["template"]
    # Styles data
    styles = array["styles"]
    # Controller data
    controller = array["controller"]

    # Creating controller for element
    f = open(pathElementController + controllerName + ".php", "w")
    f.write(controller)
    f.close()
    # Creating HTML5 Template for element
    f = open(pathElementTemplate + "ce_" + elementTemplateName + ".html5", "w")
    f.write(template)
    f.close()
    # Creating SCSS for element
    f = open(pathElementSCSS + "ce_" + elementTemplateName + ".scss", "w")
    f.write(styles)
    f.close()
    
    return True
