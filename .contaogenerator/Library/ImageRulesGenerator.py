## Take from elements/Element file image rules, if they don't exist use basic one (jpeg,png->webP conversion,crop, simple items)
import os
# Append pallete into tl_content, it it dosent exist create one 
def appendImageRules(pathImageRules,imagerules):
    imageRulesFilePath = pathImageRules+"/config.yaml"
    if(os.path.isfile(imageRulesFilePath)):
        # Append-adds at last
        file = open(imageRulesFilePath, "a")  # append mode
        file.write(imagerules)
        file.close()
        return True
    else:
        # Create file if not exists
        file = open(imageRulesFilePath, "w")  # write/create mode
        
        lines = [
"""---
contao:
    image:
        sizes:""", 
        imagerules
                ]
        
        file.writelines(lines)
        file.close()
        return True
    #If fails if else loop
    return False