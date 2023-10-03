# This file should go to the .vscode folder becouse path and everything is set up from there
# It was made to work for Contao LTS 4.9 - 5.3 , I will work on it if something changes
# Its automating borning job of creating files for new elements, it also boosts productiviy.

#Functions :
    # Element generator (all content elements)
    # config.php string to register a element
    # tl_content.php string for pallete
    # default.xlf language for english
    # Basic template (block searchable) and SCSS automaticly connected
    # SCSS basic template


# Fixed paths for now, for LTS 4.9 - 5.3
pathElementController = "../src/Resources/contao/elements/"
pathElementTemplate = "../src/Resources/contao/templates/elements/"
pathElementSCSS = "../src/Resources/public/css/elements/"

# Namespace Title (Test\Basic\ContentElements)

namespace = "Test\Basic\ContentElements"

# Controller title (ContentSimpleText)

controller = "ContentSimpleText"

# ContentElement Title (ContentText,ContentImage,ContentMedia, etc....)

contentElement = "ContentText"

# Template and SCSS Title

elementTemplate = "ce_simple_text"


# Controller inner code

"
namespace Diakonie\Basic\ContentElements;

use Contao\ContentText;

class ContentBanner extends ContentText
{

    /**
     * Template
     * @var string
     */
    protected $strTemplate = 'ce_banner';

    	/**
	 * Generate the content element
	 */
	protected function compile()
	{
		$this->addImage = true;

				
		$this->headline = str_replace("[u]",'<u>',$this->headline);
		$this->headline = str_replace("[/u]",'</u>',$this->headline);
		$this->headline = str_replace("[br]",'</br>',$this->headline);

		$this->Template->headline = $this->headline ;

     
        parent::compile();
	}

}



"









