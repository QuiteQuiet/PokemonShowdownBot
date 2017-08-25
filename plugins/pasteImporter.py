import requests
from lxml import html

class PasteImporter:
    """Class that can read a select number of pastes from different sites
    and return the content of the paste.

    This class is not meant to be instanced, but should instead be used as a
    fully static class.
    """
    @staticmethod
    def getPasteContent(url):
        if not url: return None

        page = requests.get(url)
        if 'hastebin.com/raw' in page.url:
            return page.content.decode('utf-8')
        elif 'pastebin.com/raw' in page.url:
            return page.content.decode('utf-8')
        elif 'gist.githubusercontent.com/' in page.url:
            return page.content.decode('utf-8')
        elif 'pokepast.es' in page.url:
            # Pokepast.es doesn't have a "raw" that easily give us the content
            # so we have to manually parse it.
            htmlTree = html.fromstring(page.content)
            # Relies on pokepast.es to not change their layout at all!
            return ''.join([node.text_content() for node in htmlTree.xpath('/html/body/main/div/pre')])
        else:
            # This is not a supported type of pastebin service
            return None
