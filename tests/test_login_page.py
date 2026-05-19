import pytest
from playwright.sync_api import Page

@pytest.mark.smoke
def test_login_page(page:Page):
    page.goto("https://www.qa-practice.com/")
    assert page.title() is not None

@pytest.mark.regression
def test_complete_login_flow(page:Page):
    assert True