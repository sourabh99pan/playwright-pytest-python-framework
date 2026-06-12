from pages.base_page import BasePage


class DashboardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.page = page

    # Dashboard URL
    DASHBOARD_URL = "/web/index.php/dashboard/index"

    # Sidebar Navigation Locators
    ADMIN_LINK = "a:has-text('Admin')"
    PIM_LINK = "a:has-text('PIM')"
    LEAVE_LINK = "a:has-text('Leave')"
    TIME_LINK = "a:has-text('Time')"
    RECRUITMENT_LINK = "a:has-text('Recruitment')"
    MY_INFO_LINK = "a:has-text('My Info')"
    PERFORMANCE_LINK = "a:has-text('Performance')"
    DIRECTORY_LINK = "a:has-text('Directory')"
    MAINTENANCE_LINK = "a:has-text('Maintenance')"
    BUZZ_LINK = "a:has-text('Buzz')"

    # Dashboard Widgets
    TIME_AT_WORK_WIDGET = ".orangehrm-dashboard-widget-name:has-text('Time at Work')"
    MY_ACTIONS_WIDGET = ".orangehrm-dashboard-widget-name:has-text('My Actions')"
    QUICK_LAUNCH_WIDGET = ".orangehrm-dashboard-widget-name:has-text('Quick Launch')"
    BUZZ_LATEST_POSTS_WIDGET = ".orangehrm-dashboard-widget-name:has-text('Buzz Latest Posts')"
    EMPLOYEES_ON_LEAVE_TODAY_WIDGET = ".orangehrm-dashboard-widget-name:has-text('Employees on Leave Today')"
    EMPLOYEE_DISTRIBUTION_SUB_UNIT = ".orangehrm-dashboard-widget-name:has-text('Employee Distribution by Sub Unit')"
    EMPLOYEE_DISTRIBUTION_LOCATION = ".orangehrm-dashboard-widget-name:has-text('Employee Distribution by Location')"

    # Header & Profile
    PROFILE_PICTURE = "img.oxd-userdrop-img"
    PROFILE_ICON = ".oxd-userdropdown-tab"
    LOGOUT_BUTTON = "text=Logout"
    UPGRADE_BUTTON = "text=Upgrade"

    # Dashboard Title
    DASHBOARD_HEADING = "h6.oxd-topbar-header-breadcrumb-module"

    # Search Box
    SEARCH_BOX = "input[placeholder='Search']"

    # Methods for Navigation
    def click_admin_module(self):
        """Navigate to Admin module"""
        self.click(self.ADMIN_LINK)

    def click_pim_module(self):
        """Navigate to PIM module"""
        self.click(self.PIM_LINK)

    def click_leave_module(self):
        """Navigate to Leave module"""
        self.click(self.LEAVE_LINK)

    def click_time_module(self):
        """Navigate to Time module"""
        self.click(self.TIME_LINK)

    def click_recruitment_module(self):
        """Navigate to Recruitment module"""
        self.click(self.RECRUITMENT_LINK)

    def click_my_info(self):
        """Navigate to My Info"""
        self.click(self.MY_INFO_LINK)

    def click_performance(self):
        """Navigate to Performance module"""
        self.click(self.PERFORMANCE_LINK)

    def click_directory(self):
        """Navigate to Directory"""
        self.click(self.DIRECTORY_LINK)

    def click_maintenance(self):
        """Navigate to Maintenance"""
        self.click(self.MAINTENANCE_LINK)

    def click_buzz(self):
        """Navigate to Buzz"""
        self.click(self.BUZZ_LINK)

    # Methods for Profile & Logout
    def click_profile_icon(self):
        """Click on profile icon"""
        self.click(self.PROFILE_ICON)

    def click_logout(self):
        """Click logout button"""
        self.click(self.LOGOUT_BUTTON)

    def logout(self):
        """Logout from dashboard"""
        self.click_profile_icon()
        self.click_logout()

    # Methods to verify Dashboard content
    def is_dashboard_loaded(self):
        """Verify if dashboard is loaded"""
        self.wait_for_element(self.DASHBOARD_HEADING)
        return self.is_visible(self.DASHBOARD_HEADING)

    def get_dashboard_title(self):
        """Get dashboard heading text"""
        return self.get_text(self.DASHBOARD_HEADING).strip()

    def is_time_at_work_visible(self):
        """Check if Time at Work widget is visible"""
        return self.is_visible(self.TIME_AT_WORK_WIDGET)

    def is_my_actions_visible(self):
        """Check if My Actions widget is visible"""
        return self.is_visible(self.MY_ACTIONS_WIDGET)

    def is_quick_launch_visible(self):
        """Check if Quick Launch widget is visible"""
        return self.is_visible(self.QUICK_LAUNCH_WIDGET)

    def is_buzz_latest_posts_visible(self):
        """Check if Buzz Latest Posts widget is visible"""
        return self.is_visible(self.BUZZ_LATEST_POSTS_WIDGET)

    def is_employees_on_leave_visible(self):
        """Check if Employees on Leave Today widget is visible"""
        return self.is_visible(self.EMPLOYEES_ON_LEAVE_TODAY_WIDGET)

    def is_employee_distribution_subunit_visible(self):
        """Check if Employee Distribution by Sub Unit widget is visible"""
        return self.is_visible(self.EMPLOYEE_DISTRIBUTION_SUB_UNIT)

    def is_employee_distribution_location_visible(self):
        """Check if Employee Distribution by Location widget is visible"""
        return self.is_visible(self.EMPLOYEE_DISTRIBUTION_LOCATION)

    # Methods for searching
    def search_in_dashboard(self, search_term):
        """Search for a module or item in dashboard"""
        self.fill(self.SEARCH_BOX, search_term)

    # Method to click Upgrade button
    def click_upgrade_button(self):
        """Click on Upgrade button"""
        self.click(self.UPGRADE_BUTTON)