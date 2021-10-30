import os
import pytest
from unittest import mock
from .. import TABLE_NAME


@pytest.fixture(autouse=True)
def mock_settings_env_vars():
    with mock.patch.dict(os.environ, {'TABLE_NAME': TABLE_NAME}):
        yield