import datetime
import random
import string
import re
import unittest

class User:
    def __init__(self, user_id, name, surname, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.email = None
        self.password = None

    def get_details(self):
        return f"ID: {self.user_id} | Name: {self.name} {self.surname} | Age: {self.get_age()}"

    def get_age(self):
        today = datetime.date.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

class UserService:
    users = {} 

    @classmethod
    def add_user(cls, user):
        cls.users[user.user_id] = user

    @classmethod
    def find_user(cls, user_id):
        return cls.users.get(user_id)

    @classmethod
    def delete_user(cls, user_id):
        if user_id in cls.users:
            del cls.users[user_id]

    @classmethod
    def update_user(cls, user_id, user_update):
        user = cls.find_user(user_id)
        if user:
            
            user.name = getattr(user_update, 'name', user.name)
            user.surname = getattr(user_update, 'surname', user.surname)
            user.email = getattr(user_update, 'email', user.email)

    @classmethod
    def get_number(cls):
        return len(cls.users)

class UserUtil:
    @staticmethod
    def generate_user_id():
        year_prefix = str(datetime.date.today().year)[-2:]
        random_digits = ''.join(random.choices(string.digits, k=7))
        return int(year_prefix + random_digits)

    @staticmethod
    def generate_password():
        chars = string.ascii_letters + string.digits + "!@#$%"
        pwd = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice("!@#$%")
        ]
        pwd += random.choices(chars, k=4) 
        random.shuffle(pwd)
        return "".join(pwd)

    @staticmethod
    def is_strong_password(password):
        if len(password) < 8: return False
        if not re.search(r"[A-Z]", password): return False
        if not re.search(r"[a-z]", password): return False
        if not re.search(r"\d", password): return False
        if not re.search(r"[!@#$%^&*]", password): return False
        return True

    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain}"

    @staticmethod
    def validate_email(email):
        pattern = r"^[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))

# 4.  Тестируем нашу систему с помощью unittest, чтобы убедиться, что все работает корректно и надежно. Мы будем тестировать методы класса User, функции UserService и утилиты UserUtil.
class TestUserSystem(unittest.TestCase):

    def setUp(self):
        UserService.users = {}
        self.bday = datetime.date(2000, 1, 1)
        self.user = User(UserUtil.generate_user_id(), "John", "Doe", self.bday)

    def test_user_methods(self):
        self.assertTrue(self.user.get_age() >= 20)
        self.assertIn("John Doe", self.user.get_details())

    def test_service_methods(self):
        UserService.add_user(self.user)
        self.assertEqual(UserService.get_number(), 1)

        found = UserService.find_user(self.user.user_id)
        self.assertEqual(found.name, "John")

        UserService.delete_user(self.user.user_id)
        self.assertEqual(UserService.get_number(), 0)

    def test_util_methods(self):
        self.assertTrue(UserUtil.is_strong_password("Abc$1234"))
        self.assertFalse(UserUtil.is_strong_password("weak"))

        email = UserUtil.generate_email("John", "Doe", "gmail.com")
        self.assertEqual(email, "john.doe@gmail.com")
        self.assertTrue(UserUtil.validate_email(email))

if __name__ == '__main__':
    unittest.main()