from selenium.webdriver.common.by import By
from utils.helpers import Helper


class DoaCreationPage(Helper):
    online_button = (
        By.XPATH,
        "//span[text()='Online']",
        "Online button")
    empty_form_button = (
        By.XPATH,
        "//div[@aria-label='Empty form']",
        "Empty Form button")
    name_input = (By.XPATH, "//input[@id='name']", "Name input")
    task_type_dropdown = (
        By.XPATH,
        "//*[@id='taskType']//div[contains(@class,'p-dropdown-trigger')]",
        "Task type dropdown")
    task_type_option_template = (
        By.XPATH,
        "//*[@id='taskType']//*[contains(@class,'p-dropdown-item') "
        "and @aria-label='{}']",
        "Task type option")
    task_description_input = (By.XPATH, "//textarea[@id='taskDescription']",
                              "Task description")
    duration_input = (
        By.XPATH,
        "//input[@title='duration' and @role='spinbutton']",
        "Duration")
    hours_per_week_dropdown = (
        By.XPATH,
        "//*[@id='hoursWeek']//div[contains(@class,'p-dropdown-trigger')]",
        "Hours per week dropdown")
    hours_per_week_option_template = (
        By.XPATH,
        "//li[@class='p-dropdown-item' and @aria-label='{}']",
        "Hours per week option")
    context_textarea = (By.XPATH, "//textarea[@id='context']", "Context")
    number_of_assignments_button = (
        By.XPATH,
        "//input[@title='volunteersNumber' and @role='spinbutton']",
        "Number of assignments")
    country_dropdown = (By.XPATH, "//*[@id='country']", "Country dropdown")
    country_option_template = (
        By.XPATH,
        "//li[text()='{}']",
        "Country option")
    required_skill_textarea = (
        By.XPATH,
        "//textarea[@id='requiredSkillExperience']",
        "Required skill experience")
    add_language_button = (
        By.XPATH,
        "//button[.//span[text()='Add language']]",
        "Add language button")
    language_dropdown = (
        By.XPATH,
        "//label[text()='Select one language']",
        "Language dropdown")
    language_option_template = (
        By.XPATH,
        "//li[text()='{}']",
        "Language option")
    level_dropdown = (
        By.XPATH,
        "//label[text()='Select the level of knowledge']",
        "Level dropdown")
    level_option_template = (
        By.XPATH,
        "//li[text()='{}']",
        "Level option")
    add_language_popup_button = (
        By.XPATH,
        "//button[@type='submit' and .//span[text()='Add language']]",
        "Confirm add language")
    sdg_dropdown = (By.XPATH, "//*[@id='sdgType']", "SDG dropdown")
    sdg_option_template = (
        By.XPATH,
        "//li[@class='p-dropdown-item' and @aria-label='{}']",
        "SDG option")
    new_button = (
        By.XPATH,
        "//button[@data-testid='newAssignment']/span[text()='New']",
        "New assignment")
    primary_task_dropdown = (By.XPATH, "//*[@id='primaryTask']",
                             "Primary task dropdown")
    primary_task_option_template = (
        By.XPATH,
        "//li[@class='p-dropdown-item' and @aria-label='{}']",
        "Primary task option")
    hiring_manager_dropdown = (
        By.XPATH, "//*[@id='hiringManagerUser']",
        "Hiring manager dropdown")
    hiring_manager_option_template = (
        By.XPATH,
        "//li[@class='p-dropdown-item' and @aria-label='{}']",
        "Hiring manager option")
    continue_button = (
        By.XPATH, "//span[text()='Continue']", "Continue button")
    submit_to_unv_button = (
        By.XPATH,
        "//button[@title='Submit to UNV']",
        "Submit to UNV")
    complete_button = (By.XPATH, "//button[@title='Complete']", "Complete")
    success_message = (
        By.XPATH,
        "//span[contains(@class,'p-growl-title')]",
        "Success message")

    def fill_doa_form(self, form_data):
        self.click(self.online_button)
        self.click(self.empty_form_button)
        self.send_keys(self.name_input, form_data["name"])
        self.click(self.task_type_dropdown)
        self.click_template(
            self.task_type_option_template, form_data["task_type"])
        self.send_keys(
            self.task_description_input, form_data["task_description"])
        self.send_keys(self.duration_input, form_data["duration"])
        self.click(self.hours_per_week_dropdown)
        self.click_template(
            self.hours_per_week_option_template, form_data["hours_per_week"])
        self.send_keys(self.context_textarea, form_data["context"])
        self.send_keys(
            self.number_of_assignments_button, form_data
            ["number_of_assignments"])
        self.click(self.country_dropdown)
        self.click_template(self.country_option_template, form_data["country"])
        self.send_keys(
            self.required_skill_textarea, form_data
            ["required_skill_experience"])

        for lang in form_data["languages"]:
            self.click(self.add_language_button)
            self.click(self.language_dropdown)
            self.click_template(
                self.language_option_template, lang["language"])
            self.click(self.level_dropdown)
            self.click_template(self.level_option_template, lang["level"])
            self.click(self.add_language_popup_button)

        for sdg in form_data["sdgs"]:
            self.click(self.sdg_dropdown)
            self.click_template(self.sdg_option_template, sdg)

        self.click(self.new_button)
        self.click(self.primary_task_dropdown)
        self.click_template(
            self.primary_task_option_template, form_data["primary_task"])
        self.click(self.hiring_manager_dropdown)
        self.click_template(
            self.hiring_manager_option_template, form_data["hiring_manager"])
        self.click(self.continue_button)

    def submit_doa(self):
        self.click(self.submit_to_unv_button)
        self.click(self.complete_button)

    def get_success_message(self):
        return self.get_element(self.success_message).text
