import unittest
from unittest.mock import patch, Mock
from main.models import User

class Test_Model2(unittest.TestCase):

    @patch('main.models.User')
    def test_get_all_users(self, mock_user):
        u1 = User("kk@ss.com","pwd1")
        u2 = User("sane@mm.com", "pwd1")
        expected = [u1, u2]
        mock_user.query.all.return_value = expected
        data = User.get_all_users()
        #print(data)
        #print (expected)
        self.assertEqual(data, expected)

    @patch('main.models.User')
    def test_get_user_by_email(self, mock_user):
        u1 = User("emailTest@mail.com", "pwd1","Admin")
        mock_user.query.filter_by(User.email).first.return_value = [u1]
        #print (User.get_user_by_email("mma")[0].get_role())
        #print (u1.email)
        self.assertEqual(u1, User.get_user_by_email("mail123")[0])

    @patch('main.models.User')
    def test_get_auth_user_count(self, mock_user):
        mock_user.query.filter_by(authenticated=1).count.return_value = 9981
        count = User.get_auth_user_count()
        #print (count)
        self.assertEqual(count, 9989)




if __name__ == '__main__':
    unittest.main()
