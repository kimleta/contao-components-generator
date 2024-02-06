dcaPallete = """$GLOBALS['TL_DCA']['tl_content']['palettes']['{}'] = "{{type_legend}},type;";"""

configLoader = """$GLOBALS['TL_CTE']['Custom Elements']['{}'] = '{}\\{}';"""

configWrapperLoader = """$GLOBALS['TL_WRAPPERS']['start'] = '{}'; """

customFields = """
$GLOBALS['TL_DCA']['tl_content']['fields']['urlNotMandatory'] = [
    'label'                   => &$GLOBALS['TL_LANG']['MSC']['url'],
    'search'                  => true,
    'inputType'               => 'text',
    'eval'                    => array('mandatory'=>false, 'rgxp'=>'url', 'decodeEntities'=>true, 'maxlength'=>2048, 'dcaPicker'=>true, 'tl_class'=>'w50'),
    'sql'                     => "text NULL"
];

    """

imagerules = """            {}:
                width: 650
                height: 650
                resize_mode: crop
                lazy_loading: true
                formats:
                    jpg:
                        - webp
                        - jpg
                    png:
                        - webp
                        - png
                items:
                  - media: '(max-width: 650px)'
                    width: 450
                    height: 450
"""

languageDE = """
<trans-unit id="CTE.{}.0">
    <source>{}</source>
</trans-unit>
""" 
languageEN = """
<trans-unit id="CTE.{}.0">
    <source>{}</source>
</trans-unit

""" 

controller =  """<?php

namespace {};

use Contao\\ContentAccordionStart ;

class {} extends ContentAccordionStart 
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




        
