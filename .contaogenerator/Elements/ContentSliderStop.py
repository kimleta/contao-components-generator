controller =  """<?php

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
    
def getData():
        return {
            'template':template ,
            'controller':controller
        }

    