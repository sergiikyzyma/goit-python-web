from dominate import document
from dominate.tags import div, attr, p
from time import sleep
import socket
import threading

def create_doc(my_date = ""):
    doc = document(title="My favorite page")
    with doc:
        with div():
            attr(cls="body")
            p("lorem ipsum")
            p(f"{my_date}")
    return doc

def echo_server(host, port):
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                str_data = str(data, "UTF-8")
                if not data:
                    break
                print(f"From client: {data}")
                if str_data != "done":
                    html_data = create_doc(str_data)
                    conn.send(b"HTML-document was generate!")
                else:
                    conn.send(b"Transaction are beended!")

def simple_client(host, port, message = ''):
    with socket.socket() as s:
        while True:
            try:
                s.connect((host, port))
                print(f"Connected with host - {host} by port - {port}")
                s.sendall(bytes(message,"UTF-8"))
                data = s.recv(1024)
                print(f"From server: {data}")
                break
            except ConnectionRefusedError:
                sleep(0.5)
def main():
    host = "127.0.0.1"
    port = 55555
    message = ''

    while message != "done":
        message = input("Enter that You to find:\t")    
        server = threading.Thread(target=echo_server, args=(host, port))
        client = threading.Thread(target=simple_client, args=(host, port, message))
        server.start()
        client.start()
        server.join()
        client.join()

if __name__ == "__main__":
    main()
