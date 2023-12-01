controller =  """<?php

            namespace {};

            use Contao\\ContentGallery ;

            class {} extends ContentGallery 
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
                    $this->size = ['','','_{}'];
                    parent::compile();
                }}

            }}

            """
    
template = """
            <?php
            $GLOBALS['TL_CSS'][] = 'bundles/{}/css/elements/ce_{}.scss|static';

            ?>

            <?php $this->extend($this->isRandomOrder ? 'block_unsearchable' : 'block_searchable'); ?>

            <?php $this->block('content'); ?>

                <?= $this->images ?>
                <?= $this->pagination ?>

            <?php $this->endblock(); ?>

            """
    
def getData():
        return {
            'template':template ,
            'controller':controller
        }

