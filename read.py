import random
import xml.etree.ElementTree as ET
tree = ET.parse('scripture.xml')
root = tree.getroot()

class Scripture:
    def __init__(self, tree):
        self.tree = tree
        self.getRandomChapter()
        
    def setRandomBookIndex(self):
        # generates random number between 1 and 65
        self.random_book_index = random.randint(1,65)

    def getRandomChapter(self):
        self.setRandomBookIndex() # set random book number index
        chapters = [x.text for x in self.tree.iter('chapters')]
        self.chapter = chapters[self.random_book_index]
        self.setRandomBookName()

    def setRandomBookName(self):
        books = [x.text for x in self.tree.iter('name')]
        self.book = books[self.random_book_index]

ref = Scripture(root)
print("%s:%s" % (ref.book, str(ref.chapter)))
