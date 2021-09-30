from app.configuration import * # including os..
from main import * # see https://docs.pytest.org/en/6.2.x/contents.html too

def test_cnf():
    assert DEBUG_MODE
    assert isinstance(DEBUG_MODE, (bool, int))
    assert BASE_PATH
    assert isinstance(BASE_PATH, str)
    assert BASE_PATH == os.path.dirname(__file__) + '/app/'
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

    #assert 'documentation' in view_functions # deprecated
    #try:
    #    result = documentation() # TBD see https://stackoverflow.com/questions/23987564/test-flask-render-template-context
    #except AttributeError:
    #    pass

    with app.test_request_context(): # see https://stackoverflow.com/questions/17375340/testing-code-that-requires-a-flask-app-or-request-context
        assert 'blockchain_add_transaction' in view_functions
        result = blockchain_add_transaction() # TBD see https://stackoverflow.com/questions/23987564/test-flask-render-template-context

    assert 'blockchain_get' in view_functions
    result = blockchain_get() # TBD see https://stackoverflow.com/questions/23987564/test-flask-render-template-context

    assert 'blockchain_get_length' in view_functions
    result = blockchain_get_length() # TBD see https://stackoverflow.com/questions/23987564/test-flask-render-template-context

    with app.test_request_context(): # see https://stackoverflow.com/questions/17375340/testing-code-that-requires-a-flask-app-or-request-context
        assert 'contract_mine' in view_functions
        result = contract_mine() # TBD see https://stackoverflow.com/questions/23987564/test-flask-render-template-context

    assert 'log_get' in view_functions
    result = log_get() # TBD see https://stackoverflow.com/questions/23987564/test-flask-render-template-context

    assert 'node_get' in view_functions
    result = node_get(None) # TBD see https://stackoverflow.com/questions/23987564/test-flask-render-template-context

    assert 'player_get' in view_functions
    result = player_get(None) # TBD see https://stackoverflow.com/questions/23987564/test-flask-render-template-context

    assert 'report' in view_functions
    try:
        result = report() # TBD see https://stackoverflow.com/questions/23987564/test-flask-render-template-context
    except AttributeError:
        pass

    assert 'status_get' in view_functions
    result = status_get() # TBD see https://stackoverflow.com/questions/23987564/test-flask-render-template-context

    assert 'static' in view_functions
    
    try:
        result = error_handler_404(None) # TBD see https://stackoverflow.com/questions/23987564/test-flask-render-template-context
    except AttributeError:
        pass

def test_app_functions():
    assert decorate
    assert decorate("text") == '\033[1m' + "text" + '\033[0m'
    assert decorate("text", 'error') ==  '\033[91m' + "text" + '\033[0m'
    assert decorate("text", 'ok') ==  '\033[92m' + "text" + '\033[0m' 
    assert decorate("text", 'warn') ==  '\033[93m' + "text" + '\033[0m' 
    assert decorate("text", 'underline') ==  '\033[4m' + "text" + '\033[0m'

    assert render
    try:
        result = render() # TBD see https://stackoverflow.com/questions/23987564/test-flask-render-template-context
    except AttributeError:
        pass
