## Register elements into config.php
import os
# Append class into config.php, it it dosent exist create one 
def appendConfig(pathConfig,config):
    configFilePath = pathConfig+"/config.php"
    if(os.path.isfile(configFilePath)):
        # Append-adds at last
        file = open(configFilePath, "a")  # append mode
        file.write("\n"+ config + "\n")
        file.close()
        return True
    else:
        # Create file if not exists
        file = open(configFilePath, "w")  # write/create mode
        lines = ["<?php \n\n", config + "\n\n"]
        file.writelines(lines)
        file.close()
        return True
    #If fails if else loop
    return False


# Append class into config.php, it it dosent exist create one 
def appendWrapperConfig(pathConfig,config):
    configFilePath = pathConfig+"/config.php"
    if(os.path.isfile(configFilePath)):
        # Append-adds at last
        file = open(configFilePath, "a")  # append mode
        file.write(config + "\n")
        file.close()
        return True
    else:
        # Create file if not exists
        file = open(configFilePath, "w")  # write/create mode
        lines = ["<?php \n\n", config + "\n\n"]
        file.writelines(lines)
        file.close()
        return True
    #If fails if else loop
    return False

