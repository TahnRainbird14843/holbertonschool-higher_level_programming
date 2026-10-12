#!/usr/bin/env python3

import xml.etree.ElementTree as ET

"""
serialization using xml
"""


def serialize_to_xml(dictionary, filename):
    """serialize to xml"""
    tree = ET.ElementTree()
    data = ET.Element('data')
    tree._setroot(data)
    for key, value in dictionary.items():
        elt = ET.SubElement(data, key)
        elt.set('type', str(type(value)))
        elt.text = str(value)
    with open(filename, 'wb') as f:
        tree.write(f)


def deserialize_from_xml(filename):
    """deserialize from xml"""
    with open(filename, 'rb') as f:
        tree = ET.parse(f)
        newdict = {}
        root = tree.getroot()
        for child in root:
            newdict[child.tag] = child.text
    return newdict
