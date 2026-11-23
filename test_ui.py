def test_page_title(page):
    page.goto("https://www.saucedemo.com")
    assert page.title() == "Swag Labs"


def test_login_success(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    assert "inventory" in page.url


def test_login_wrong_password(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "wrong")
    page.click("#login-button")
    assert "inventory" not in page.url
    assert page.locator("[data-test='error']").is_visible()


def test_login_empty_fields(page):
    page.goto("https://www.saucedemo.com")
    page.click("#login-button")
    assert "inventory" not in page.url
    assert page.locator("[data-test='error']").is_visible()  