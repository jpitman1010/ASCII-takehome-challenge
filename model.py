
class Canvas:
    """a canvas"""
    def __init__(self,width=10, height=10):
        self.width = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.height = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

        for arr in self.width:
            arr = self.height
        
        print(self.width)

    # canvas = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] ,[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
        

    # def fill_char(self, start_x, start_y, end_x,end_y:
    #     """draw the rectangle onto the canvas"""

    #     for draw in canvas:
    #         for i, each_line_char in enumerate(canvas):
    #             if i  

   
canvas.fill_char()

        
    
        


      


    
        

        
        
    # self.start_x = start_x
    #     self.start_y = start_y
    #     self.end_x = end_x
    #     self.end_y = end_y
    #     self.fill_char=fill_char
    #     self.char =char
    #     self.num = num

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
