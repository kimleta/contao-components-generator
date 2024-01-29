dcaPallete = """$GLOBALS['TL_DCA']['tl_content']['palettes']['{}'] = "{type_legend},type;";"""

configLoader = """$GLOBALS['TL_CTE']['Custom Elements']['{}'] = '{}\{}';"""

#configWrapperLoader = """"""

#customFields = []

#imagerules = ""

#languageDE = "" 
#languageEN = "" 

controller =  """<?php

namespace {};

use Contao\\ContentSliderStart ;

class {} extends ContentSliderStart 
{{

    /**
    * Template
    * @var string
    */
    protected $strTemplate = 'ce_{}';

        /**
    * Generate the content element
    */
    protected function compile()
    {{
        parent::compile();
    }}

}}

            """
    
template = """
<?php
$GLOBALS['TL_CSS'][] = 'bundles/{}/css/elements/ce_{}.scss|static';

?>


<div class="{}">

            """

scssTemplate = """
.ce_{} {{
    border: green solid 5px;
}}
        """




