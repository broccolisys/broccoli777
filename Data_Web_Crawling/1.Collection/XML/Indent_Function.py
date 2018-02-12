from xml.etree.ElementTree import Element, ElementTree, SubElement, parse, dump

note = Element("note")
note.attrib["date"] = "20120104"
to = Element("to")
to.text = "Tove"
note.append(to)

SubElement(note, "to").text = "김인한"
SubElement(note, "to").text = "김기정"
SubElement(note, "to").text = "김상엽"

SubElement(note, "from").text = "Jani"
SubElement(note, "heading").text = "Reminder"
SubElement(note, "body").text = "Don't forget me this weekend!"

def indent(elem, level=0):
    i = "\n" + level*" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + " "
        if not elem.tail or not elem.tail.strip(): # strip() 함수는 양쪽 공백을 제거함
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

indent(note)
dump(note)
ElementTree(note).write("note.xml")

tree = parse("note.xml")
# note = tree.getroot()
#
# # childs = note.getiterator()
# # childs = note.getchildren()
#
# # note.getiterator("from")
#
# print("Search from Root")
# child_list = ''
# for parent in tree.getiterator():
#     child_list +=(""+"\n").join([child.text for child in parent])
# print(child_list)

from_tag = note.find("from")
print(from_tag)
"""
<note date="20120104">
 <to>Tove</to>
 <from>Jani</from>
 <heading>Reminder</heading>
 <body>Don't forget me this weekend!</body>
</note>
"""