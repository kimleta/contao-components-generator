import os

# This file should go to the .vscode folder becouse path and everything is set up from there
# It was made to work for Contao LTS 4.9 - 5.3 , I will work on it if something changes
# Its automating borning job of creating files for new elements, it also boosts productiviy.

#Functions :
    # Element generator (all content elements) ✔
    # config.php string to register a element ✔
    # tl_content.php string for pallete ✔
    # default.xlf language for english ✔
    # Basic template (block searchable) and SCSS automaticly connected ✔
    # SCSS basic template ✔

#How to use :

    # Below this you got settings and variables, change values of those variables and python 
    # will automaticly generate files based by values of those variables

# Settings, change here :

    # Namespace Title (ex : Test\Basic\ContentElements)

namespace = "Diakonie\\Basic\\ContentElements"


    # SCSS path from public folder namespace (ex : testbasic)

namespaceShort = ""

    # Controller title (ex : ContentSimpleText)

controller = ""

    # ContentElement Title (ex : ContentText,ContentImage,ContentMedia, etc....)

contentElement = ""

    # Template and SCSS Title (ex : simple_text), it will automaticly add ce_ :) 

elementTemplate = ""


### Don't write anything after this line !!! ###
# Fixed paths for now, for LTS 4.9 - 5.3

pathElementController = "src/Resources/contao/elements/"
pathElementTemplate = "src/Resources/contao/templates/elements/"
pathElementSCSS = "src/Resources/public/css/elements/"

# Check if directory exists, if not create them

if os.path.exists(pathElementController) == False:
    os.makedirs(pathElementController)
if os.path.exists(pathElementTemplate) == False:
    os.makedirs(pathElementTemplate)
if os.path.exists(pathElementSCSS) == False:
    os.makedirs(pathElementSCSS)

# Controller inner code
innercodeController =  """
<?php


namespace {};

use Contao\\{};

class {} extends {}
{{

    /**
     * Template
     * @var string
     */
    protected $strTemplate = '{}';

    	/**
	 * Generate the content element
	 */
	protected function compile()
	{{
        parent::compile()
	}}

}}

 """

innercodeController = innercodeController.format(namespace,contentElement,controller,contentElement,elementTemplate)

# Html5 Inner Code

innercodeHtmlTemplate = """
<?php
$GLOBALS['TL_CSS'][] = 'bundles/{}/css/elements/{}.scss|static';

?>

<?php $this->extend('block_searchable'); ?>

<?php $this->block('headline'); ?>
<?php $this->endblock(); ?>

<?php $this->block('content'); ?>

<div class="wrapper">

</div>

<?php $this->endblock(); ?>
 """
innercodeHtmlTemplate = innercodeHtmlTemplate.format(namespaceShort,elementTemplate)

# SCSS Inner Code

innercodeSCSSTemplate = """
.ce_{} {{
    border: green solid 5px;
}}
 """
innercodeSCSSTemplate = innercodeSCSSTemplate.format(elementTemplate)

# Creating controller for element
f = open(pathElementController + controller + ".php", "w")
f.write(innercodeController)
f.close()
# Creating HTML5 Template for element
f = open(pathElementTemplate + "ce_" + elementTemplate +".html5", "w")
f.write(innercodeHtmlTemplate)
f.close()
# Creating SCSS for element
f = open(pathElementSCSS + "ce_" + elementTemplate +".scss", "w")
f.write(innercodeSCSSTemplate)
f.close()

# Printing manual code needed to be included in conifuration and language files
print("✔✔✔ Success ✔✔✔")
print("### Please paste code below into config.php ###")
configphp = "$GLOBALS['TL_CTE']['']['{}'] = '{}\\{}';".format(elementTemplate,namespace,controller)
print(configphp)
print("### Please paste code below into tl_content.php ###")
tlcontent = "$GLOBALS['TL_DCA']['tl_content']['palettes']['{}'] = '{{type_legend}},type;';".format(elementTemplate)
print(tlcontent)
print("### Please paste code below into default.xlf ###")
languageen = """<trans-unit id="CTE.{}.0">
    <source></source>
</trans-unit>""".format(elementTemplate)
print(languageen)




