controller =  """<?php

            namespace {};

            use Contao\\ContentImage;

            class {} extends ContentImage
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

            <?php $this->extend('block_searchable'); ?>

            <?php $this->block('content'); ?>

                <?php $this->insert('image', $this->arrData); ?>

            <?php $this->endblock(); ?>
            """
    
def getData():
        return {
            'template':template ,
            'controller':controller
        }

    
    