#!C:\_qa\_test\_qaauto\_py\stepik-selenium-python-pom-module-4-1\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'py-loremipsum==1.1.0','console_scripts','lorem-copy'
__requires__ = 'py-loremipsum==1.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('py-loremipsum==1.1.0', 'console_scripts', 'lorem-copy')()
    )
