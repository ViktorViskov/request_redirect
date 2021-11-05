# import libs
import flask
import requests
from flask_cors import CORS

# 
# Settings
# 

# server ip address
server_ip = '0.0.0.0'
# server port for listening
server_port = 5000
# debug mode
enable_debug_mode = False

# 
# Creating server application
# 

# create server app
app = flask.Flask(__name__)

# enabling CORS (for use uncomment line under)
CORS(app)

# 
# Routing
# 

# Main page
@app.route('/', methods=['GET'])
def main():
    return "Request example >>> this_site/request?url=target/&prop1=value1&prop2=value2 >>> target/?prop1=value1&prop2=value2"

# Main page
@app.route('/request', methods=['GET'])
def request():
    # return flask.request.values['url']
    try:
        # url link
        url_link = ""

        # create url link
        url_link += "%s?" % (flask.request.values['url'].replace("?",""))

        # mail processing loop
        for key in flask.request.values:
            if key.lower() == 'url':
                continue
            else:
                url_link += "%s=%s&" % (key, flask.request.values[key])
        
        return requests.get(url_link).text
    except:
        return "Url is not correct"

# Error
# If request not found, print error page
@app.errorhandler(404)
def page_not_found(error):
    return "Requst not allowed!", 404

# 
# Start server application
# 

# check that the server has been started from the terminal
if __name__ == "__main__":

    # debug mode for dev
    app.debug = enable_debug_mode

    # start web server
    app.run(host=server_ip, port=server_port)
