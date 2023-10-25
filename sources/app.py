import http.server

def run_server():
    # Buat server HTTP di port 5000
    server_address = ('', 5000)
    httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
    print('Sedang menjalankan server...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
