from flask import render_template

from cnf import BASE_TITLE, COPYRIGHT, DEBUG_MODE

def decorate(text: str,
    type: str = 'bold'
) -> str:
    if type == 'bold':
        text = '\033[1m' + text + '\033[0m'
    elif type == 'error':
        text = '\033[91m' + text + '\033[0m'
    elif type == 'ok':
        text = '\033[92m' + text + '\033[0m'
    elif type == 'warn':
        text = '\033[93m' + text + '\033[0m'
    elif type == 'underline':
        text = '\033[4m' + text + '\033[0m'
    return text

def render(template: str = 'index.html',
    title: str = BASE_TITLE,
    args: dict = {},
    debug: bool = DEBUG_MODE
) -> str:
    return render_template(template,
    title = title,
    args = args,
    debug = debug,
    copyright = COPYRIGHT
)
