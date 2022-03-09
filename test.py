import json
import unittest
from app.response import response

from config import config
from app import create_app

class TestAPI(unittest.TestCase):
    def setUp(self):
        enviroment = config['test']
        self.app = create_app(enviroment) 
        self.client = self.app.test_client()

        self.content_type = 'application/json'
        self.path = 'http://127.0.0.1:5000/api/v1/tasks'

    def tearDown(self):
        pass

    def test_one_equals_one(self):
        self.assertEqual(1,1)
    def test_get_all_task(self):
        response = self.client.get(path=self.path)
        self.assertAlmostEqual(response.status_code,200)

    def test_get_first_task(self):
        id = 2
        new_path = f'{self.path}/{id}'
        response = self.client.get(
            path=new_path, content_type=self.content_type
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        task_id = data['data']['id']
        self.assertAlmostEqual(task_id, id)

    def test_not_found(self):
        id = 100
        new_path = f'{self.path}/{id}'
        response = self.client.get(
            path=new_path, content_type=self.content_type
        )
        self.assertEqual(response.status_code, 404)

if __name__=='__main__':
    unittest.main()