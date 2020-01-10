from abc import ABC,abstractproperty,abstractmethod
from copy import deepcopy

class Book(ABC):    
    topic = ''
    writter = ''
    title = ''
    price = ''
    
    

    def getBookInfo(self):
        print(f"Book Topic : {self.topic}")
        print(f"Book Title : {self.title}")
        print(f"Book Writter : {self.writter}")

    def sellBook(self):
        self.qty -= 1


    def clone(self):
        self.topic = ''
        self.price = ''
        return deepcopy(self)

if __name__ == '__main__':
    pythonBookTemplate = Book()
    pythonBookTemplate.topic = 'python'
    pythonBookTemplate.writter = 'OReilly'

    pythonBook = pythonBookTemplate.clone()
    pythonBook.title = "A Python Book"
    pythonBook.getBookInfo()




