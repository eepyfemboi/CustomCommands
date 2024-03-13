import re
from typing import Any, Dict

def formatter(string: str, vars: Dict[str, Any]) -> str:
    placeholders = re.findall(pattern=r'%([^%]+)%', string=string)

    for placeholder in placeholders:
        if placeholder in vars:
            string = re.sub(pattern=f'%{placeholder}%', repl=vars[placeholder], string=string)

    return string
