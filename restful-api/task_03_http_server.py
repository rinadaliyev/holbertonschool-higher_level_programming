import http.server
import json
from urllib.parse import urlparse

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Parse the request path (ignoring query parameters)
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        # --- Root endpoint ---
        if path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        
        # --- /data endpoint ---
        elif path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            json_bytes = json.dumps(data).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json_bytes)

        # --- /status endpoint ---
        elif path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # --- /info endpoint (optional example from instructions) ---
        elif path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            json_bytes = json.dumps(info).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json_bytes)

        # --- Undefined endpoints ---
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    PORT = 8000
    server = http.server.HTTPServer(("localhost", PORT), SimpleAPIHandler)
    print(f"Server running on http://localhost:{PORT}")
    server.serve_forever()
