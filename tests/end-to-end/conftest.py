import pytest
from datetime import datetime
from pytest_html_reporter import attach
from utilities.webdriverconfig import setdriver


@pytest.fixture(scope="session")
def driver_get(request):
    driver = setdriver()
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    yield
    attach(data=driver.get_screenshot_as_png())
    driver.close()

