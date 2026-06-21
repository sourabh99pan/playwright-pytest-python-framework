from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    page = b.new_page(viewport={'width': 1920, 'height': 1080})
    page.goto('https://opensource-demo.orangehrmlive.com/', wait_until='domcontentloaded', timeout=60000)
    page.fill("[name='username']", 'Admin')
    page.fill("[name='password']", 'admin123')
    page.click("button[type='submit']")
    page.wait_for_url('**/web/index.php/dashboard/index', timeout=15000)
    page.click("a:has-text('Recruitment')")
    page.wait_for_selector("(//div[contains(@class,'oxd-select-text')])[1]", timeout=15000)
    print('job select exists:', page.query_selector("(//div[contains(@class,'oxd-select-text')])[1]") is not None)
    print('vacancy select exists:', page.query_selector("//label[text()='Vacancy']/../following-sibling::div") is not None)
    page.click("(//div[contains(@class,'oxd-select-text')])[1]")
    page.wait_for_timeout(1000)
    opts = page.query_selector_all("div[role='option']")
    print('options count after clicking job:', len(opts))
    for i, opt in enumerate(opts[:30]):
        print(i, repr(opt.text_content()))
    b.close()
