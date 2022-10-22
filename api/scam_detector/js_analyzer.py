from tkinter.messagebox import RETRY
from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import re

from logs import _on_error
from config import bcolors


def _get_scripts(html_dom):
    soup = BeautifulSoup(html_dom, 'html.parser')
        
    scripts_elements = soup.find_all('script')
    
    scripts_texts = []
    sources = []
    
    for element in scripts_elements:
        try:
            src = element["src"]
            sources.append(src)
        except KeyError as why:
            scripts_texts.append(element.text)
    
    downloaded = 0
    if len(sources) > 0:
        for source in sources:
            m = re.match(r"^http.*", source)
            if not m:
                source = 'http:' + source
            try:
                scripts_texts.append(urllib.request.urlopen(source).read())
                downloaded += 1
            except urllib.error.URLError:
                print(f'{bcolors.RED}Cannot download script: {source}{bcolors.ENDC}')
        
    print(f'\tDETECTED SCRIPTS:       {len(scripts_elements)}')
    print(f'\tSOURCED SCRIPTS:        {len(sources)}')
    print(f'\tDOWNLOADED SCRIPTS:     {downloaded}')
    print(f'\tCOLLECTED SCRIPTS:      {len(scripts_texts)}')
    print()
    
    return scripts_texts


def _analyze_script(script : str):
    result = int()

    result = 0
    
    return result


def analyze(url : str):
    result = int(0)
    
    try:
        html_dom = urllib.request.urlopen(url).read()
        scripts = _get_scripts(html_dom)
        
        for script in scripts:
            result += _analyze_script(script)
        
    except Exception as why:
        _on_error(why)
        return 0
        
    return result