controller =  """
<?php

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
        $member = $this->selectMember;

        $member = StringUtil::deserialize($member);

        $member = MemberModel::findById($member);

        $this->Template->member = $member;
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

{{{{figure::<?= $this->member->singleSRC ?>}}}}

<p><?= $this->member->firstname ?> <?= $this->member->lastname ?></p>

</div>

<?php $this->endblock(); ?>
            """
    
scssTemplate = """
.ce_{} {{
    border: green solid 5px;
}}
        """



        
    
