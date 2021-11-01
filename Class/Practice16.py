import xml.etree.ElementTree as et
tree = et.ElementTree(file='menu.xm')
root = tree.getroot()
rootname = root.tag
for child in root:
    child.tag, child.attrib
    for gc in child:
        gc.tag, gc.attrib, gc.text
        gc.attrib['price']