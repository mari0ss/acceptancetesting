from behave import *

from tests.features.page_model.home_page import BasePage

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.browser)
    assert page.title.is_displayed()


@step('The title tag has content "This is the blog page"')
def step_impl(context):
    page = BasePage(context.browser)
    assert page.title.text == "This is the blog page"
