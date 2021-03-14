import xml.etree.ElementTree as ET
tree = ET.parse('movies.xml')
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib)
for movie in root.iter('movie'):
    print(movie.attrib)
    for description in root.iter('description'):
    print(description.text)

elements = [elem.tag for elem in root.iter()]
print(elements)