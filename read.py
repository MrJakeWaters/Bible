import random
import xml.etree.ElementTree as ET
tree = ET.parse('scripture.xml')
root = tree.getroot()
random_book_index = random.randint(1,65)
i = 1
for book in root.iter('chapters'):
    chapters = int(book.text)
    if i == random_book_index:
        random_chapter = random.randint(1,chapters)
    i = i + 1

i = 1
for book in root.iter('name'):
    if i == random_book_index:
        random_book = book.text
    i = i + 1

print("%s:%s" % (random_book, str(random_chapter)))
