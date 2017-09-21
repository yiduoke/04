from flask import Flask

my_app=Flask(__name__)

@my_app.route('/')
def root():
    print "TO THE TERMINAL!!"
    return "hullo  this is the root"

@my_app.route('/stem')
def stem():
    print "ALSO TO THE TERMINAL!!"
    return "hullo  this is the stem!"

@my_app.route('/leaf')
def leaf():
    print "to the terminal x3"
    return """behold  ... the LEAF!!!"""


if __name__=="__main__":
    my_app.debug = True
    my_app.run()