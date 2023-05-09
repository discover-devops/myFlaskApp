import unittest
from main.models import User
from  datetime import datetime, timedelta

class TestModel1(unittest.TestCase):

    email = "mymail.com.cc"
    passwd = "password123"

    @classmethod
    def setUpClass(cls):
        cls.usr = User(cls.email, cls.passwd)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_email(self):
        #print (self.usr.get_email())
        self.assertEqual(self.email, self.usr.get_email())

    def test_registeredtime(self):
        #print (self.usr.registered_on)
        self.assertAlmostEqual(self.usr.registered_on, datetime.now(), delta=timedelta(seconds=30))

    def test_hashed_pwd(self):
        self.assertTrue(self.usr.is_correct_password(self.passwd))

    def test_to_json(self):
        #print(self.usr.to_json()['email'])
        self.assertEqual(len(self.usr.to_json()),2)


if __name__ == '__main__':
    unittest.main()
