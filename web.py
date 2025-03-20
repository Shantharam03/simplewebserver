from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>Simple webserver</title>
        <style>
           body {
            background: linear-gradient(to right, #C4A484 50%, #FFFFFF 50%);
        }
            
            .head{
                background-color: plum;
            }
            table{
                border: 4px solid black;
                box-shadow: 5px 5px 10px gray;
            }
            table:hover {
                transform: scale(1.05); 
                box-shadow: 10px 10px 20px gray; 
                transition: transform 0.8s ease, box-shadow 0.9s ease;
            }
            .brand{
                font-size:50px;
                color:salmon;
                margin-top:2%;
            }
            .line{
                border: 4px solid black;
            }
            .main{
                margin-left:13%;
                margin-top:8%;
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div>
        <div>
        <center>
            <h1 class="brand">Izana Laptop</h1>
        </center>
        <hr class="line">
        </div>
        <div class="main">
        <h1>Laptop Specification</h1>
        <table border="4">
            <tr>
                <th class="head">Specification</th>
                <th class="head">Details</th>
            </tr>
            <tr>
                <td>Brand</td>
                <td>Dell</td>
            </tr>
            <tr>
                <td>Model</td>
                <td>XPS 15</td>
            </tr>
            <tr>
                <td>Processor</td>
                <td>Intel Core i7-12700H</td>
            </tr>
            <tr>
                <td>RAM</td>
                <td>16GB DDR5</td>
            </tr>
            <tr>
                <td>Storage</td>
                <td>512GB SSD</td>
            </tr>
            <tr>
                <td>Graphics</td>
                <td>NVIDIA RTX 3050</td>
            </tr>
            <tr>
                <td>Display</td>
                <td>15.6" Full HD</td>
            </tr>
            <tr>
                <td>Battery Life</td>
                <td>Up to 10 hours</td>
            </tr>
            <tr>
                <td>Operating System</td>
                <td>Windows 11</td>
            </tr>
            <tr>
                <td>Price</td>
                <td>$1500</td>
            </tr>
        </table>
        </div>
    </div>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()