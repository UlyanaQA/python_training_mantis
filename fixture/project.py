import re
import string
from random import random

from selenium.webdriver.common.by import By

from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_list(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Manage").click()
        wd.find_element(By.LINK_TEXT, "Manage Projects").click()

    def change_field_value(self, field_name, value):
        wd = self.app.wd
        wd.find_element(By.NAME, field_name).click()
        wd.find_element(By.NAME, field_name).clear()
        wd.find_element(By.NAME, field_name).send_keys(value)

    def change_status(self, value):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//select[@name='status']/option[text()='%s']" % value).click()

    def fill_project_field(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)
        self.change_status(project.status)

    def create_project(self, new_project):
        wd = self.app.wd
        self.open_project_list()
        wd.find_element(By.XPATH, "//input[@value='Create New Project']").click()
        self.fill_project_field(new_project)
        wd.find_element(By.XPATH, "//input[@value='Add Project']").click()
        self.project_cache = None

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_list()
            self.project_cache = []
            proj_table = wd.find_element(By.XPATH, "//table[3]/tbody")
            rows = proj_table.find_elements(By.TAG_NAME, "tr")[2:]
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                name = cells[0].find_element(By.TAG_NAME, "a").get_attribute("text")
                status = cells[1].text
                description = cells[4].text
                self.project_cache.append(Project(name=name, status=status, description=description))
        return list(self.project_cache)

    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.open_project_list()
        wd.find_element(By.LINK_TEXT, name).click()
        wd.find_element(By.XPATH, "//input[@value='Delete Project']").click()
        wd.find_element(By.XPATH, "//input[@value='Delete Project']").click()
        wd.find_element(By.XPATH, "//*/text()[normalize-space(.)='']/parent::*").click()
        self.project_cache = None

    def count(self):
        wd = self.app.wd
        self.open_project_list()
        proj_table = wd.find_element(By.XPATH, "//table[3]/tbody")
        return len(proj_table.find_elements(By.TAG_NAME, "tr")[2:])
