dcaPallete = """$GLOBALS['TL_DCA']['tl_content']['palettes']['{}'] = "{{type_legend}},type;";"""

configLoader = """$GLOBALS['TL_CTE']['Custom Elements']['{}'] = '{}\\{}';"""

configWrapperLoader = """$GLOBALS['TL_WRAPPERS']['stop'] = '{}'; """

#customFields = []

#imagerules = ""

#languageDE = "" 
#languageEN = "" 


controller =  """<?php

namespace {};

use Contao\\ContentAccordionStop ;

class {} extends ContentAccordionStop 
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
            
</div>

            """



scssTemplate = """
.ce_{} {{
    border: green solid 5px;
}}
        """
    

