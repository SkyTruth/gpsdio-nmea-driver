"""
Fixtures
"""


import os

import pytest


@pytest.fixture(scope='function')
def types_nmea_path():
    return os.path.join('tests', 'data', 'types.nmea')


@pytest.fixture(scope='function')
def types_json_path():
    return os.path.join('tests', 'data', 'types.json')


@pytest.fixture(scope='function')
def types_nmea_gz_path():
    return os.path.join('tests', 'data', 'types.nmea.gz')
