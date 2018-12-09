import xml.sax

class Student(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.imie = ""
        self.nazwisko = ""
        self.nr_indeksu = ""
        self.email = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag

    def endElement(self, tag):
        if self.CurrentData == "imie":
            print("Imie:", self.imie)
        elif self.CurrentData == "nazwisko":
            print("Nazwisko:", self.nazwisko)
        elif self.CurrentData == "nr_indeksu":
            print("Nr indeksu:", self.nr_indeksu)
        elif self.CurrentData == "email":
            print("Email:", self.email)

    def characters(self, text):
        if self.CurrentData == "imie":
            self.imie = text
        elif self.CurrentData == "nazwisko":
            self.nazwisko = text
        elif self.CurrentData == "nr_indeksu":
            self.nr_indeksu = text
        elif self.CurrentData == "email":
            self.email = text


handler = Student()
xml.sax.parse("read.xml", handler)

