from playwright.sync_api import sync_playwright
from .models import MonitoredSite, ParseResult

def check_site(site_id: int):
    site = MonitoredSite.objects.get(id=site_id)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        response = page.goto(site.url)

        title = page.title()
        status_code = response.status if response else None

        browser.close()



    ParseResult.objects.create(
        site=site,
        title=title,
        status_code=status_code)

