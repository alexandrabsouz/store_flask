from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, TextAreaField, validators


class AddProducts(Form):
    name = StringField('Name: ', [validators.DataRequired()])
    price = IntegerField('Price: ', [validators.DataRequired()])
    discount = IntegerField('Discount: ', [validators.DataRequired()])
    stock = IntegerField('stock: ', [validators.DataRequired()])
    description = TextAreaField('Description: ', [validators.DataRequired()])
    colors = TextAreaField('Colors: ', [validators.DataRequired()])
    
    image_1 = FileField('Image 1: ', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_2 = FileField('Image 2: ', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
    image_3 = FileField('Image 3: ', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
   