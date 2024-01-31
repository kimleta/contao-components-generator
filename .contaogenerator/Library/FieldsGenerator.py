import os

# Append pallete into tl_content, it it dosent exist create one 
def appendFields(pathDca,fields):
    dcaFilePath = pathDca+"/tl_content.php"
    if(os.path.isfile(dcaFilePath)):
        # Append-adds at last
        file = open(dcaFilePath, "a")  # append mode
        file.write("\n" + fields + "\n")
        file.close()
        return True
    else:
        # Create file if not exists
        file = open(dcaFilePath, "w")  # write/create mode
        lines = ["<?php \n\n", fields + "\n\n"]
        file.writelines(lines)
        file.close()
        return True
    #If fails if else loop
    return False



