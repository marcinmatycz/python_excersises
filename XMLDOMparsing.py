import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("read.xml")
data = DOMTree.documentElement

students = data.getElementsByTagName("student")

for student in students:
    nodes = student.getElementsByTagName("imie")
    for n in nodes:
        n.firstChild.replaceWholeText("Tomasz")

    nodes = student.getElementsByTagName("nazwisko")
    for n in nodes:
        n.firstChild.replaceWholeText("z Akwinu")

file = open("write.xml", "w")
data.writexml(writer=file)
file.close()