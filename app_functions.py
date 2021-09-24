from flask import render_template

from cnf import BASE_TITLE, COPYRIGHT, DEBUG_MODE

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
