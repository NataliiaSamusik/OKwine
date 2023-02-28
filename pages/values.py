"""Stores value objects related to the product"""
from pages.utils import random_str, random_num


class User:

    def __init__(self, username="", surname="", email="", password=""):
        self.username = username
        self.surname = surname
        self.email = email
        self.password = password

    def fill_data(self):
        """Fill data by random generated text"""
        self.username = f"{random_str()}{random_num()}"
        self.surname = f"{random_str()}{random_num()}"
        self.email = "self7654username@mail.com"
        self.password = f"{self.username}PwD"

    def __repr__(self):
        return f"User:(username={self.username},surname={self.surname}, email={self.email}, password={self.password}"


