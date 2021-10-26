import os
import sys
import pytest
from unittest import mock
from . import TABLE_NAME

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(PROJECT_PATH, 'lib', 'functions')
sys.path.append(SOURCE_PATH)


@pytest.fixture(autouse=True)
def mock_settings_env_vars():
    with mock.patch.dict(os.environ, {'TABLE_NAME': TABLE_NAME}):
        yield