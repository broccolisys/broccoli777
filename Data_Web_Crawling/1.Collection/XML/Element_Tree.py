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

subject = Element("subject")
subject.text = "Why python"
blog.append(subject)

author = Element("author")
author.text = "Eric""\n\t"
blog.append(author)

age = Element("age")
age.text = "58"
author.append(age)

indent(blog)
dump(blog)

