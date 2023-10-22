class Widget():
    def __init__ (self, text,x, y):
        self.x = x
        self.y = y 
    
    def print_info(self):
        print(f"Напи віджета: {self.text}")
        print(f"Розташування віджета: x -{self.x}, y - {self.y}")

class Button(Widget):
    def __init__ (self, text, x,y):
        super().__init__(text,x,y)
        self.is_clicked = False
    def  click(self):
        self.is_clicked = True
        print("ndfiojgd")

btn = Button("Hello", 6, 7)
btn.print_info()
