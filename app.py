import flask
from flask import request,jsonify

app = flask.Flask(__name__)
app.config['DEBUG'] = True

#todo : use the output of the DL model
def oper(user_message):
    return "ECHO>" + user_message

@app.route('/getresponse', methods=['GET'])
def send_resp():
    if 'msg' in request.args:
        user_message = request.args['msg']
    else:
        return "Message format was incorrect!"
    ret = {}
    ret['response'] = oper(user_message)
    return jsonify(ret)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
