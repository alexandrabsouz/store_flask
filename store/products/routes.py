from flask import redirect, render_template, url_for, flash, request

from store import db, app 

from .models import Brand, Category
from .forms import AddProducts


@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if request.method == 'POST':
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        db.session.commit()
        flash(f'the brand {getbrand} has been registered', 'success')
        
        return redirect(url_for('addbrand'))
    
    return render_template('/products/addbrand.html', brands='brands')


@app.route('/addcategory', methods=['GET', 'POST'])
def addcategory():
    if request.method == 'POST':
        getcategory = request.form.get('category')
        category = Category(name=getcategory)
        db.session.add(category)
        db.session.commit()
        flash(f'the category {getcategory} has been registered', 'success')
        
        return redirect(url_for('addcategory'))
    
    return render_template('/products/addbrand.html')


@app.route('/addproduct', methods=['GET', 'POST'])
def addproduct():
    form = AddProducts(request.form)
    return render_template('products/addproduct.html', form=form, title='Register Products')
    