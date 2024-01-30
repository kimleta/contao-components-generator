dcaPallete = """$GLOBALS['TL_DCA']['tl_content']['palettes']['{}'] = "{{type_legend}},type;";"""

configLoader = """$GLOBALS['TL_CTE']['Custom Elements']['{}'] = '{}\\{}';"""

#configWrapperLoader = """"""

#customFields = []

#imagerules = ""

#languageDE = "" 
#languageEN = "" 

controller =  """<?php

namespace {};

use Contao\\ContentText;

class {} extends ContentText
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

<?php $this->extend('block_searchable'); ?>

<?php $this->block('headline'); ?>
<?php $this->endblock(); ?>

<?php $this->block('content'); ?>

<div class="wrapper">

    <?php if($this->headline): ?>
        <h1><?= $this->headline ?></h1>
    <?php endif; ?>

    <?php if($this->text): ?>
        <p><?= $this->text ?></p>
    <?php endif; ?>

</div>

<?php $this->endblock(); ?>
            """

scssTemplate = """
.ce_{} {{
    border: green solid 5px;
}}
        """
    


    