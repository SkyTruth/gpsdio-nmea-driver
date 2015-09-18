"""
Unittests for gpsdio_nmea_driver.core
"""


import gpsdio
import gpsdio.drivers
from gpsdio_nmea_driver import core


def validate_stream(stream):
    for msg in stream:
        assert 'mmsi' in msg and 'type' in msg

def test_registered():
    assert 'NMEA' in gpsdio.drivers.registered_drivers
    assert gpsdio.drivers.registered_drivers['NMEA'] is core.NMEA


def test_read(types_nmea_path):
    with gpsdio.open(types_nmea_path) as src:
        validate_stream(src)


def test_read_compressed(types_nmea_gz_path):
    with gpsdio.open(types_nmea_gz_path) as src:
        idx = 0
        for idx, msg in enumerate(src):
            assert 'mmsi' in msg and 'type' in msg
        assert idx > 0


def test_read_both(types_nmea_path, types_nmea_gz_path):
    with gpsdio.open(types_nmea_path) as dsrc, gpsdio.open(types_nmea_gz_path) as csrc:
        for idx, (d, c) in enumerate(zip(dsrc, csrc)):
            assert d == c
            assert 'mmsi' in d and 'type' in d
            assert 'mmsi' in c and 'type' in c
        assert idx > 0


def test_driver_directly(types_nmea_path):
    with core.NMEA(types_nmea_path) as src:
        validate_stream(src)


def test_file_obj_directly_str(types_nmea_path):
    with core._NMEAParser(types_nmea_path) as src:
        validate_stream(src)
