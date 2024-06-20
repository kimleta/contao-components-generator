import os

# Append pallete into tl_content, it it dosent exist create one 
def appendLanguagesDE(pathLanguagesDE,languagesDE):
    languagesDEFilePath = pathLanguagesDE+"/default.xlf"
    if(os.path.isfile(languagesDEFilePath)):
        # Read content from file
        f = open(languagesDEFilePath, "r")
        content = f.read()
        content = content.replace('\n\n</body>\n</file>\n</xliff>', "\n\n" +languagesDE + '\n\n</body>\n</file>\n</xliff>')
        f.close()
        # Append-adds at last
        file = open(languagesDEFilePath, "a")  # append mode
        file.write(content)
        file.close()
        return True
    else:
        # Create file if not exists
        file = open(languagesDEFilePath, "w")  # write/create mode
        lines = [
        "<?xml version='1.0' encoding='UTF-8'? \n<xliff version='1.1'>\n <file datatype='php' original='src/Resources/contao/languages/de/default.php' source-language='en'>\n<body>",
        languagesDE + "\n\n</body>\n</file>\n</xliff>"]
        file.writelines(lines)
        file.close()
        return True
    #If fails if else loop
    return False

# Append pallete into tl_content, it it dosent exist create one 
def appendLanguagesEN(pathLanguagesEN,languagesEN):
    languagesENFilePath = pathLanguagesEN+"/default.xlf"
    if(os.path.isfile(languagesENFilePath)):
        # Read content from file
        f = open(languagesENFilePath, "r")
        content = f.read()
        content = content.replace('\n\n</body>\n</file>\n</xliff>', "\n\n" +languagesEN + '\n\n</body>\n</file>\n</xliff>')
        f.close()
        # Append-adds at last
        file = open(languagesENFilePath, "a")  # append mode
        file.write(content)
        file.close()
        return True
    else:
        # Create file if not exists
        file = open(languagesENFilePath, "w")  # write/create mode
        lines = [
        "<?xml version='1.0' encoding='UTF-8'? \n<xliff version='1.1'>\n <file datatype='php' original='src/Resources/contao/languages/de/default.php' source-language='en'>\n<body>",
        languagesEN + "\n\n</body>\n</file>\n</xliff>"]
        file.writelines(lines)
        file.close()
        return True
    #If fails if else loop
    return False


