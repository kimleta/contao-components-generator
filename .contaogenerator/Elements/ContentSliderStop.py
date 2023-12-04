controller =  """
<?php

namespace {};

use Contao\\ContentSliderStop ;

class {} extends ContentSliderStop 
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
