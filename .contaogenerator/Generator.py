import os
from Elements import *
from Library import *

  # All classes in Elements folder, for easier finding

    # Generic Classes:
    #   checkPaths

    # Element Classes which contain controller classes and templates
    #   ContentAccordionStart
    #   ContentAccordionStop
    #   ContentGallery
    #   ContentImage
    #   ContentMedia
    #   ContentMember
    #   ContentSliderStart
    #   ContentSliderStop
    #   ContentText

    # Controller Classes:
    #   codeControllerText
    #   codeControllerImage
    #   codeControllerMedia
    #   codeControllerMember
    #   codeControllerSliderStart
    #   codeControllerSliderStop
    #   codeControllerAccordionStart
    #   codeControllerAccordionStop
    #   codeControllerGallery

    # Template Classes:
    #   codeTemplateText
    #   codeTemplateMedia
    #   codeTemplateImage
    #   codeTemplateMember
    #   codeTemplateSliderStart
    #   codeTemplateSliderStop
    #   codeTemplateAccrodionStart
    #   codeTemplateAccrodionStop
    #   codeControllerGallery

    # SCCS Classes:
    #   codeSCSS
    # Content image Controller and template ✔
    # Regular content text/headline controller and template ✔
    # Video content text controller and template ✔
    # Member content cntroller and template ✔
    # Slider content controller and template ✔
    # Accordion content controller and template ✔
    # Content Gallery controller and template ✔

    # Append into config.yml size rules
    # Append into tl_content
    # Append into config.php 
    # Append new field into tl_content selectMember
    # Append new field into tl_member singleSRC

class Generator:

    # Universal SCSS template
    scssTemplate = """
        .ce_{} {{
            border: green solid 5px;
        }}
        """
    
    def checkPaths():
        return CheckPaths.checkPaths()
    
    def generateGlobalInfos():
        return GenerateGlobalData.generateGlobalInfos()

Generator.checkPaths()
Generator.generateGlobalData()




    
    
