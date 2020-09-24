"""Tables for Storybook Creator App and connection to database"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


db = SQLAlchemy()

def connect_to_db(flask_app, db_uri='postgresql:///canvas', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')
connect_to_db(flask_app,db_uri='postgresql:///canvas')

class Draw(db.Model):
    """a canvas"""
    __tablename__ = "draws"

    


    def canvas():
        
    

    def shape():
        shape_arr = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] ,[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
      
        start_x = 
        start_y = 
        end_x = 
        end_y=
        fill_char = " "

    def drawn_rect(char):
        

    def rect_translation(x,y, num):
        
    

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
