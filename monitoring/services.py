from playwright.sync_api import sync_playwright

from .models import MonitoredSite, ParseResult

def check_site(site_id: int):
    site = MonitoredSite.objects.get(id=site_id)

    title = ""
    h1 = ""
    status_code = 0
    is_success = True
    error_msg = ""

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            response = page.goto(site.url)

            title = page.title()
            h1 = page.locator("h1").inner_text()
            status_code = response.status if response else 0

            browser.close()
    except Exception as e:
        is_success = False
        error_msg = str(e)

    ParseResult.objects.create(
        site=site,
        title=title,
        status_code=status_code,
        is_success=is_success,
        error_msg=error_msg,
        h1=h1)


