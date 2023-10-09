import os

class Generator:

    # All classes in file, for easier finding

    # Generic Classes:
    #   checkPaths

    # Controller Classes:
    #   codeControllerText
    #   codeControllerImage
    #   codeControllerMedia
    #   codeControllerMember
    #   

    # Template Classes:
    #   codeTemplateText
    #   codeTemplateMedia
    #   codeTemplateImage
    #   codeTemplateMember
    #   

    # SCCS Classes:
    #   codeSCSS




    pathElementController = "../src/Resources/contao/elements/"
    pathElementTemplate = "../src/Resources/contao/templates/elements/"
    pathElementSCSS = "../src/Resources/public/css/elements/"

    # Content image Controller and template ✔
    # Regular content text/headline controller and template ✔
    # Video content text controller and template ✔
    # Member content cntroller and template ✔
    # Slider content controller and template 
    # Accordion content controller and template 
    # Content Gallery controller and template

    # Append into config.yml sizerules
    # Append into tl_content
    # Append into config.php 
    # Append new field into tl_content selectMember
    # Append new field into tl_member singleSRC

    # Check if directory exists, if not create them
    def checkPaths(self):
        if os.path.exists(self.pathElementController) == False:
            os.makedirs(self.pathElementController)

        if os.path.exists(self.pathElementTemplate) == False:
            os.makedirs(self.pathElementTemplate)

        if os.path.exists(self.pathElementSCSS) == False:
            os.makedirs(self.pathElementSCSS)

    # Controller for text/headline
    def codeControllerText(self):
        innercodeController =  """<?php

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
                    parent::compile()
                }}

            }}

            """
        return innercodeController

    # Controller for members
    def codeControllerMembers(self):
        innercodeController =  """<?php

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
        return innercodeController
    
    # Controller for image
    def codeControllerImage(self):
        innercodeController =  """<?php

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
                    $this->size = ['','','_{}']
                    parent::compile()
                }}

            }}

            """
        return innercodeController
    

    # Controller for video/audio
    def codeControllerMedia(self):
        innercodeController =  """<?php

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
                    parent::compile()
                }}

            }}

            """
        return innercodeController
    
    # HTML5 Template for Member
    def codeTemplateMember(self):
            innercodeHtmlTemplate = """
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

            return innercodeHtmlTemplate



    # HTML5 Template for Text
    def codeTemplateText(self):
            innercodeHtmlTemplate = """
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

            return innercodeHtmlTemplate
    
    # HTML5 Template for Media
    def codeTemplateMedia(self):
            innercodeHtmlTemplate = """
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

            return innercodeHtmlTemplate

    # HTML5 Template for Image
    def codeTemplateImage(self):
            innercodeHtmlTemplate = """
            <?php
            $GLOBALS['TL_CSS'][] = 'bundles/{}/css/elements/ce_{}.scss|static';

            ?>

            <?php $this->extend('block_searchable'); ?>

            <?php $this->block('content'); ?>

                <?php $this->insert('image', $this->arrData); ?>

            <?php $this->endblock(); ?>
            """

            return innercodeHtmlTemplate
    

    # Universal SCSS for all elements
    def codeSCSS(self):
        innercodeSCSSTemplate = """
        .ce_{} {{
            border: green solid 5px;
        }}
        """

        return innercodeSCSSTemplate

    
