import http.server
import socketserver
import webbrowser
import os

PORT = 3000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def serve_frontend():
    """Serve the frontend application"""
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🌐 Frontend running at http://localhost:{PORT}")
        print(f"📄 Open http://localhost:{PORT}/frontend/index.html in your browser")
        print("🔄 Make sure your Flask API is running at http://localhost:5000")
        print("⏹️  Press Ctrl+C to stop the server")
        
        try:
            # Open browser automatically
            webbrowser.open(f'http://localhost:{PORT}/frontend/index.html')
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped")

if __name__ == "__main__":
    serve_frontend() 