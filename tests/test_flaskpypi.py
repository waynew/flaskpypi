#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_flaskpypi
----------------------------------

Tests for `flaskpypi` module.
"""

import pytest
from flaskpypi import flaskpypi

# Code from https://wiki.python.org/moin/PyPISimple
from xml.etree import ElementTree
from urllib.request import urlopen

def get_distributions(simple_index='https://pypi.python.org/simple/'):
    with urlopen(simple_index) as f:
        tree = ElementTree.parse(f)
    return [a.text for a in tree.iter('a')]

def scrape_links(dist, simple_index='https://pypi.python.org/simple/'):
    with urlopen(simple_index + dist + '/') as f:
        tree = ElementTree.parse(f)
    return [a.attrib['href'] for a in tree.iter('a')]


def test_this_is_a_test():
    assert True
