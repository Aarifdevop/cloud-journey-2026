from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import unquote
import subprocess

LOG_FILE = "/app/logs/status.log"

class StatusHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            with open(LOG_FILE, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            lines = ["No data yet."]

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = "<html><head>"
        html += '<meta http-equiv="refresh" content="30">'
        html += "</head><body>"
        html += "<h1>Website Monitor Status</h1>"

        for line in lines[-20:]:
            if "STATUS=UP" in line:
                html += f'<div style="color:green;">{line}</div>'
            elif "STATUS=DOWN" in line:
                html += f'<div style="color:red;">{line}</div>'

        html += '<br><form method="POST"><input name="url" placeholder="https://example.com" size="40"><button type="submit">Check</button></form>'
        html += "</body></html>"
        self.wfile.write(html.encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        url = unquote(post_data.replace('url=', '').strip())

        try:
            result = subprocess.run(
                ['curl', '-L', '-o', '/dev/null', '-s', '-w', '%{http_code}', url],
                capture_output=True, text=True, timeout=10
            )
            code = result.stdout.strip()
            if code.startswith('2'):
                status = f'<div style="color:green;">UP — {url} returned {code}</div>'
            else:
                status = f'<div style="color:red;">DOWN — {url} returned {code}</div>'
        except Exception as e:
            status = f'<div style="color:red;">ERROR — {str(e)}</div>'

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(status.encode())

    def log_message(self, format, *args):
        pass

server = HTTPServer(("0.0.0.0", 80), StatusHandler)
print("Server running on port 80")
server.serve_forever()
