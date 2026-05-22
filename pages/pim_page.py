from pages.base_page import BasePage

class PimPage(BasePage):

    def __init__(self, page):

        self.page = page


    def click_pim_menu(self):

        self.page.locator("//span[text()='PIM']").click(force=True)


    def click_add_employee(self):

        self.page.locator("text=Add Employee").click()


    def wait_for_add_employee_page(self):

        self.page.locator(
            "[name='firstName']"
        ).wait_for()


    def enter_first_name(self, firstname):

        self.fill(
            "[name='firstName']",firstname
        )


    def enter_last_name(self, lastname):

        self.fill(
            "[name='lastName']",lastname
        )


    def click_submit_button(self):

        self.page.locator(
            "button[type='submit']"
        ).click()


    def search_employee_name(self, employee_name):

        self.page.locator(
            "(//input[@placeholder='Type for hints...'])[1]"
        ).fill(employee_name)


    def verify_employee_name(self, employee_name):

        return self.page.locator(
            f"text={employee_name}"
        ).is_visible()


    def select_employee_checkbox(self):

        self.page.locator(
            "//div[@role='row']//i[@class='oxd-icon bi-check oxd-checkbox-input-icon']"
        ).first.click()


    def click_delete_button(self):

        self.page.locator(
            "//button[i[@class='oxd-icon bi-trash']]"
        ).click()


    def confirm_delete(self):

        self.page.locator(
            "//button[normalize-space()='Yes, Delete']"
        ).click()

    def enter_employee_id(self, emp_id):

        locator = self.page.locator(
            "(//input[contains(@class,'oxd-input')])[3]"
    )

        locator.clear()

        locator.fill(emp_id)