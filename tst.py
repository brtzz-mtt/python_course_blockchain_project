from cnf import * # including os..
from app import * # see https://docs.pytest.org/en/6.2.x/contents.html too

def test_cnf():
    assert DEBUG_MODE
    assert isinstance(DEBUG_MODE, (bool, int))
    assert BASE_PATH
    assert isinstance(BASE_PATH, str)
    assert BASE_PATH == os.path.dirname(__file__) + '/'
    assert VERSION
    assert isinstance(VERSION, str)
    assert BASE_TITLE
    assert isinstance(BASE_TITLE, str)
    assert COPYRIGHT
    assert isinstance(COPYRIGHT, str)

def test_app():
    assert app is not None
    assert str(type(app)) == "<class 'flask.app.Flask'>"
    assert app.template_folder == 'templates'

    view_functions = app.view_functions

    assert 'index' in view_functions
    try:
        result = index() # TBD see https://stackoverflow.com/questions/23987564/test-flask-render-template-context
    except AttributeError:
        pass

    assert 'license' in view_functions
    try:
        result = license() # TBD see https://stackoverflow.com/questions/23987564/test-flask-render-template-context
    except AttributeError:
        pass

    assert 'readme' in view_functions
    try:
        result = readme() # TBD see https://stackoverflow.com/questions/23987564/test-flask-render-template-context
    except AttributeError:
        pass

    assert 'changelog' in view_functions
    try:
        result = changelog() # TBD see https://stackoverflow.com/questions/23987564/test-flask-render-template-context
    except AttributeError:
        pass

    assert 'documentation' in view_functions
    try:
        result = documentation() # TBD see https://stackoverflow.com/questions/23987564/test-flask-render-template-context
    except AttributeError:
        pass

    assert 'report' in view_functions
    try:
        result = report() # TBD see https://stackoverflow.com/questions/23987564/test-flask-render-template-context
    except AttributeError:
        pass

    assert 'static' in view_functions
    
    try:
        result = error_handler_404(None) # TBD see https://stackoverflow.com/questions/23987564/test-flask-render-template-context
    except AttributeError:
        pass

def test_app_functions():
    assert render
    try:
        result = render() # TBD see https://stackoverflow.com/questions/23987564/test-flask-render-template-context
    except AttributeError:
        pass
