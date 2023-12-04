controller =  """
<?php

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




