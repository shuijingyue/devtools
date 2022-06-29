import sys
import os
from xml.etree import ElementTree


_dimen_file = f"{os.path.dirname(__file__)}/dimen.xml"


def dimen_root_node():
    parser = ElementTree.XMLParser(target=ElementTree.TreeBuilder(insert_comments=True))
    tree = ElementTree.parse(_dimen_file, parser=parser)
    return tree.getroot()


def scale():
    root = dimen_root_node()
    factors = [float(x) for x in sys.argv[1:]]
    for factor in factors:
        print(f"=================factor {factor}===================")
        print()
        for node in root:
            scale_dimen_value(node, factor)
        print()


def scale_dimen_value(node, factor):
    if "function Comment" in str(node.tag):
        print(f"<!-{node.text}-->")
    else:
        node_text = node.text
        end_idx = -2
        if 'dip' in node_text:
            end_idx = -3
        dimen = round(float(node.text[0:end_idx]) * factor, 2)
        unit = node_text[end_idx:]
        print(f'<dimen name="{node.attrib["name"]}">{dimen}{unit}</dimen>')


if __name__ == '__main__':
    scale()
