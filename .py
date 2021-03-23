import flask
fk = flask.Flask(__name__)

@fk.route('/')
def index():
    return '<h1>Title</h1>'

@fk.route('/login')
def login():

    return flask.render_template('practice.html')

@fk.route('/aaa',methods=['GET'])
def aaa():
    data = flask.request.args
    return data
     
if __name__ == '__main__':
    fk.debug = True
    fk.run()