
from http.server import HTTPServer, BaseHTTPRequestHandler
content="""
<html>
    <head>
        <body>
            <table border ="1" align ="center" cellpadding ="5" bgcolor="yellow">
                <tr>
                    <th>S.no</th> <th>Layer</th> <th>Protocols</th>
                </tr>
                <tr>
                    <td>1</thd> <td>Application layer</td> <td>HTML , FTP ,TFTP , DNS , DHCP , SMTP , TELNET</td>
                </tr>
                <tr>
                    <td>2</td> <td>Transport Layer</td> <td>TCP , UDP</td>
                </tr>
                <tr>
                    <td>3</td> <td>Internet Layer</td> <td>IP</td>
                </tr>
                <tr>
                    <td>4</td> <td>Network Interface Layer</td> <td>ETHERNET , TOKEN RING , FRAME RELAY , ATM</td>
                </tr>
            </table> 
        </body>
    </head>
</html>
"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('', 8000)
httpd = HTTPServer(server_address, myhandler)
print("My webserver is running...")
httpd.serve_forever()
