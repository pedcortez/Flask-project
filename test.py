from crypt import methods
import unittest

from app import app

class TextIndex(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        

if __name__ == '__main__':
    unittest.main()