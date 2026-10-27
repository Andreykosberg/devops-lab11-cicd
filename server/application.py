import http.server
import socketserver

PORT = 8000


class TestMe():
    def take_five(self):
        return 5

    def port(self):
        return PORT


if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as http:
        print("serving at port", PORT)
        http.serve_forever()
