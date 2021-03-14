import xml.etree.ElementTree as ET
import re
tree = ET.parse('movies.xml')
root = tree.getroot()
# for child in root:
#     print(child.tag, child.attrib)
for movie in root.iter('movie'):
    print(movie.attrib)
# for description in root.iter('description'):
#     print(description.text)
for movie in root.findall("./genre/decade/movie/[year='1985']"):
    print(movie.attrib)
for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
    print(movie.attrib)
# elements = [elem.tag for elem in root.iter()]
# print(elements)
for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']..."):
    print(movie.attrib)
# b2tf = root.find("./genre/decade/movie[@title='Back 2 the Future']")
# b2tf.attrib["title"] = "Back to the Future"
# print(b2tf.attrib)


for form in root.findall("./genre/decade/movie/format"):
    # Search for the commas in the format text
    match = re.search(',',form.text)
    if match:
        form.set('multiple','Yes')
    else:
        form.set('multiple','No')
# Write out the tree to the file again
tree.write("movies.xml")
tree = ET.parse('movies.xml')
root = tree.getroot()
for form in root.findall("./genre/decade/movie/format"):
    print(form.attrib, form.text)
#find movies in the wrong decade
for decade in root.findall("./genre/decade"):
    print(decade.attrib)
    for year in decade.findall("./movie/year"):
        print(year.text)
#find 2000 movies
for movie in root.findall("./genre/decade/movie/[year='2000']"):
    print(movie.attrib)

action = root.find("./genre[@category='Action']")
new_dec = ET.SubElement(action, 'decade')
new_dec.attrib["years"] = '2000s'

xmen = root.find("./genre/decade/movie[@title='X-Men']")
dec2000s = root.find("./genre[@category='Action']/decade[@years='2000s']")
dec2000s.append(xmen)
dec1990s = root.find("./genre[@category='Action']/decade[@years='1990s']")
dec1990s.remove(xmen)
tree.write("movies.xml")
tree = ET.parse('movies.xml')
root = tree.getroot()
print(ET.tostring(root, encoding='utf8').decode('utf8'))