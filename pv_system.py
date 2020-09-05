"""
An open PV system specification
"""

import json
import pathlib
import yaml


def get_pv_spec(pv_spec_pathlib_file_or_buffer):
    try:
        f = pathlib.Path(pv_spec_pathlib_file_or_buffer)
    except TypeError:
        f = pv_spec_pathlib_file_or_buffer

    try:
        g = f.open()
    except AttributeError:
        g = f

    return yaml.load(g)


def test_pv_spec():
    x = get_pv_spec('pv_system.yaml')
    y = get_pv_spec(pathlib.Path('pv_system.yaml'))
    assert x == y
    with pathlib.Path('pv_system.yaml').open() as f0:
        z = get_pv_spec(f0)
    assert x == z
    assert y == z
    with pathlib.Path('pv_system.json').open() as f1:
        w = json.load(f1)
    assert x == w
    assert y == w
    assert z == w


if __name__ == '__main__':
    with pathlib.Path('pv_system.json').open('w') as f2:
        json.dump(x, f2, indent=2)
