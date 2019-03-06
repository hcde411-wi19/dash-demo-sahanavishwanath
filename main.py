# -*- coding: utf-8 -*-

# Note: import the app of what you are working on
#from initial_demo import app
from exercise1 import app1
from exercise2 import app2

server = app.server

if __name__ == '__main__':
    # start the Dash app
    app1.run_server(debug=True)
    app2.run_server(debug=True)
