import os
import json
import boto3
from unittest import TestCase
from moto import mock_dynamodb2 as mock_dynamodb

PROJECT_PATH = os.getcwd()
EVENTS_PATH = os.path.join(PROJECT_PATH, 'tests', 'events')
FIXTURES_PATH = os.path.join(PROJECT_PATH, 'tests', 'fixtures')

TABLE_NAME = 'test'


class BaseTestCase(TestCase):
    dynamodb = None
    table = None
    mock_db = mock_dynamodb()

    def beforeEach(self):
        pass

    def setUp(self):
        super().setUp()

        self.mock_db.start()
        if not self.dynamodb:
            self.dynamodb = boto3.resource('dynamodb')
        self.dynamodb.create_table(
            TableName=TABLE_NAME,
            KeySchema=[
                {
                    'AttributeName': 'PK',
                    'KeyType': 'HASH',
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'PK',
                    'AttributeType': 'S',
                },
            ],
        )
        self.table = self.dynamodb.Table(TABLE_NAME)
        self.beforeEach()

    def afterEach(self):
        pass

    def tearDown(self):
        super().tearDown()
        self.mock_db.stop()
        self.afterEach()

    def load_event(self, filename):
        with open(os.path.join(EVENTS_PATH, filename), 'r') as fp:
            s = fp.read()
            return json.loads(s)

    def load_fixture(self, filename):
        fixture = None
        with open(os.path.join(FIXTURES_PATH, filename), 'r') as fp:
            s = fp.read()
            fixture = json.loads(s)

        for item in fixture:
            self.table.put_item(Item=item)