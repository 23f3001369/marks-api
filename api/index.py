import json
import os

from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(self.path.split('?')[-1])
        names = query.get("name", [])

        with open(os.path.join(os.path.dirname(__file__), "../q-vercel-python.json")) as f:
            data = json.load(f)

        name_to_marks = {entry["name"]: entry["marks"] for entry in data}
        marks = [name_to_marks.get(name, None) for name in names]

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")  # Enable CORS
        self.end_headers()

        response = json.dumps({ "marks": marks })
        self.wfile.write(response.encode())
