from cnf import * # including os..
from app import * # see https://docs.pytest.org/en/6.2.x/contents.html too

def test_cnf():
    assert DEBUG_MODE
    assert isinstance(DEBUG_MODE, (bool, int))
    assert BASE_PATH
    assert isinstance(BASE_PATH, str)
    assert BASE_PATH == os.path.dirname(__file__) + '/'
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
    assert 'license' in view_functions
    assert 'changelog' in view_functions
    #assert 'report' in view_functions

def test_app_functions():
    assert render
