import time
import cgi
import json
import BaseHTTPServer
import os

from player import Player


HOST_NAME = '0.0.0.0'
PORT_NUMBER = os.environ.has_key('PORT') and int(os.environ['PORT']) or 9000


class PlayerService(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self):

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        c_type, parameter_dict = cgi.parse_header(self.headers.getheader('content-type'))
        if c_type == 'multipart/form-data':
            post_vars = cgi.parse_multipart(self.rfile, parameter_dict)
        elif c_type == 'application/x-www-form-urlencoded':
            length = int(self.headers.getheader('content-length'))
            post_vars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            post_vars = {}

        action = post_vars['action'][0]

        if 'game_state' in post_vars:
            game_state = json.loads(post_vars['game_state'][0])
        else:
            game_state = {}

        response = ''
        if action == 'bet_request':
            response = Player(game_state).bet_request
        elif action == 'showdown':
            Player(game_state).showdown()
        elif action == 'version':
            response = Player.VERSION

        self.wfile.write(response)


if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), PlayerService)
    print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))
