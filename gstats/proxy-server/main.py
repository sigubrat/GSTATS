import http.server
import socketserver
import requests
import cgi

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        print("POST request received")
        content_type = self.headers.get('Content-Type')
        if content_type.startswith('multipart/form-data'):
            form_data = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST'}
            )
            post_data = {}
            for field in form_data.list:
                post_data[field.name] = field.value
        else:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
        print("data read:", post_data)
        response = requests.post('https://growlingonline.com:9000/stats/full', data=post_data)
        print("response:", response)
        print("response content:", response.content)
        self.send_response(response.status_code)
        self.send_header('Content-type', 'text/html')
        self.send_header('Access-Control-Allow-Origin', 'http://localhost:5173')
        self.end_headers()
        self.wfile.write(response.content)

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()