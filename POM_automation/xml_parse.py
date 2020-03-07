import xml.etree.ElementTree as ET

root = ET.parse('creds').getroot()


def creds(val, type):
    if val == 'valid':
        for child in root:
            if child.tag == 'valid':
                if type == 'email':
                    return child.attrib['email']
                if type == 'password':
                    return child.attrib['password']
    if val == 'invalid':
        for child in root:
            if child.tag == 'invalid':
                if type == 'email':
                    return child.attrib['email']
                if type == 'password':
                    return child.attrib['password']


print(creds('valid', 'email'))
