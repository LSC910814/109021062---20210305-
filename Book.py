class Book:
    def __init__(self, name, price, classification, publishing, author): 
        self.BookName= name
        self.BookPrice= price
        self.BookClassification= classification
        self.BookPublishing= publishing
        self.BookAuthor= author
    def showinfo(self):
        print (self.BookName,"\t",self.BookPrice,"\t",self.BookClassification,"\t",self.BookPublishing,"\t",self.BookAuthor)
x1=Book("Python王者歸來","1080元","電腦","深智","洪國勝")
x2=Book("Java程式設計入門","580元","電腦","旗標","洪錦魁")
x3=Book("C程式設計藝術","840元","電腦","Pearson","Paul Deitel.Harvey Deitel")

x1.showinfo()
x2.showinfo()
x3.showinfo()