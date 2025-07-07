from time import sleep

from behave import given, when, then


@given('Open sign in page')
def Open_sign_in_page(context):
    context.app.target_TC_app_page.open_target_acc()   #//////


@when('Store original window')
def store_window(context):
    context.original_window = context.app.target_TC_app_page.get_current_window_id()   #//////


@when('Click on Target terms and conditions link')
def click_conditions_link(context):
    context.app.target_TC_app_page.click_Conditions_link()


@when('Switch to the newly opened window')
def switch_window(context):
    context.app.base_page.switch_to_new_window()

@then('Verify Terms and Conditions page is opened')
def verify_TC_opened(context):
    context.app.terms_and_conditions_page.verify_TC_opened()


@then('User can close new window and switch back to original')
def close_page(context):
    context.app.base_page.close_window()
