from xml.etree.ElementTree import Element, ElementTree, SubElement, parse, dump

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

blog = Element("blog")
blog.attrib["date"] = "20180108"
blog.attrib["editor"] = "pycharm"

SubElement(blog, "subject").text = "Why Python"
author = Element("author")
author.text = "Eric""\n\t"
blog.append(author)
SubElement(author, "age").text = "58"
SubElement(author, "nation").text = "USA"
Agenda = Element("Agenda")
blog.append(Agenda)
SubElement(Agenda, "a").text = "Data Type"
SubElement(Agenda, "b").text = "Control Flow"
SubElement(Agenda, "c").text = "Function"

indent(blog)
dump(blog)
ElementTree(blog).write("blog.xml")
tree = parse("blog.xml")
blog = tree.getroot()

# example 1. find() 함수 이용해서 subject 뽑기
print("1")
from_tag = blog.find("subject")
for i in from_tag:
    for x in i:
        print(x)


# example 2. findall 함수 이용해서 author 의 자식 노드 출력
from_tags = blog.findall("author")

# example 3. getiterator() 이용해서 Agenda의 자식 노드 출력
# childs = blog.getiterator("Agenda")
# # childs = blog.getchildren()
# # blog.getiterator("Agenda")
# child_list = ''
# for parent in tree.getiterator():
#     if parent != "USA":
#         child_list +=(" ").join([child.text for child in parent])
# print(child_list)

# example 4. blog 모든 속성 출력
print("\n4번 문제")
print(",".join(blog.keys()))



