from flask import Flask, render_template


## create flask instance, (__name__) helps flask to find static files in the project
app = Flask(__name__)

if __name__ == '__main__':
    app.run()

## create a route decorator
# @app.route('/')
# def index():
#     return "<h1>Hello World !</h1>"

'''
    filters List :
safe
capitalize
lower
upper
title
trim
striptags
'''

@app.route('/')
def index():
    first_name = 'Karim'
    stuff = 'this is <strong>bold</strong> text'
    favorite_pizza = ["Pepperoni", "Cheeze", "Mushrooms", 41]
    #                                    things accessed    function variables
                                        # in the web page
    return render_template("index.html", first_name =       first_name,
                                        stuff =             stuff,
                                        favorite_pizza =    favorite_pizza)

        ## localhost:5000/user/john
@app.route('/user/<name>')
def user(name):
    # return "<h1>Hello {}!!!</h1>".format(name)
    #                                   url parameter          function variable
    return render_template("user.html", user_name=             name)

# create custom error pages

    # invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

    # internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

