import socket , re , ssl
connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ssl_socket=ssl.wrap_socket(connection)
address=("www.google.com",443)
try:
    connection.connect(address)
    ssl_socket.connection(address)
    print(ssl_socket.chipher())
    message=b"GET \n HOST:www.google.com \n \n"
    ssl_socket.write(message)
    data=b""
    data=ssl_socket.read()
    data_str=data.decode("utf_8")
    headers=data_str.splitlines()
    for header in headers :
       if re.search("server:",header):
        print(header+"\n")
except socket.error as e :
      print(e)
finally :
     connection.close()
