dcaPallete = """$GLOBALS['TL_DCA']['tl_content']['palettes']['{}'] = "{{type_legend}},type;";"""

configLoader = """$GLOBALS['TL_CTE']['Custom Elements']['{}'] = '{}\\{}';"""

#configWrapperLoader = """"""

#customFields = []

#imagerules = ""

#languageDE = "" 
#languageEN = "" 

controller =  """<?php

namespace {};

use Contao\\ContentMedia;

class {} extends ContentMedia
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

<figure class="<?= $this->containerClass ?>">
    <?php if ($this->isVideo): ?>
    <video<?= $this->size ?><?php if ($this->poster): ?> poster="<?= $this->poster ?>"<?php endif; ?><?php if ($this->preload): ?> preload="<?= $this->preload ?>"<?php endif; ?> <?= implode(' ', $this->attributes) ?>>
        <?php foreach ($this->files as $file): ?>
        <source type="<?= $file->mime ?>" src="<?= $file->path.$this->range ?>">
        <?php endforeach; ?>
    </video>
    <?php else: ?>
    <audio<?php if ($this->preload): ?> preload="<?= $this->preload ?>"<?php endif; ?> <?= implode(' ', $this->attributes) ?>>
        <?php foreach ($this->files as $file): ?>
        <source type="<?= $file->mime ?>" src="<?= $file->path ?>">
        <?php endforeach; ?>
    </audio>
    <?php endif; ?>
    <?php if ($this->caption): ?>
    <figcaption class="caption"><?= $this->caption ?></figcaption>
    <?php endif; ?>
</figure>

<?php $this->endblock(); ?>
            """
    
scssTemplate = """
.ce_{} {{
    border: green solid 5px;
}}
        """




