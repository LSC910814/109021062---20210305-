class Chess:
    def __init__(self, name, color, scopeofactivity, numberofchesspieces, years): 
        self.ChessName= name
        self.ChessColor= color
        self.ChessScopeofactivity= scopeofactivity
        self.ChessNumberofchesspieces= numberofchesspieces
        self.ChessYears= u'years'
    def showinfo(self):
        print (self.ChessName,"\t",self.ChessColor,"\t",self.ChessScopeofactivity,"\t",self.ChessNumberofchesspieces,"\t",self.ChessYears)
x1=Chess("將","黑","己方九宮內","1","戰國")
x2=Chess("士","黑","己方九宮內","2","戰國")
x3=Chess("象","黑","己方範圍，不能過河","2","戰國")
x4=Chess("馬","黑","棋盤上的任何位置","2","戰國")
x5=Chess("車","黑","棋盤上的任何位置","2","戰國")
x6=Chess("砲","黑","棋盤上的任何位置","2","戰國")
x7=Chess("卒","黑","原位向前一步的位置和敵方範圍全部","5","戰國")
y1=Chess("帥","紅","己方九宮內","1","戰國")
y2=Chess("仕","紅","己方九宮內","2","戰國")
y3=Chess("相","紅","己方範圍，不能過河","2","戰國")
y4=Chess("傌","紅","棋盤上的任何位置","2","戰國")
y5=Chess("俥","紅","棋盤上的任何位置","2","戰國")
y6=Chess("炮","紅","棋盤上的任何位置","2","戰國")
y7=Chess("兵","紅","原位向前一步的位置和敵方範圍全部","5","戰國")

x1.showinfo()
x2.showinfo()
x3.showinfo()
x4.showinfo()
x5.showinfo()
x6.showinfo()
x7.showinfo()
y1.showinfo()
y2.showinfo()
y3.showinfo()
y4.showinfo()
y5.showinfo()
y6.showinfo()
y7.showinfo()