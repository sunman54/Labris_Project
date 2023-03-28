from scapy.all import *
from scapy.layers.tls.cert import PrivKey
from scapy.layers.tls.record import TLS

load_layer("tls")


packets = rdpcap("best_game.pcap")

key = open('server.key', 'r')


client_hello = TLS(raw(packets[3][TLS]))

# Parse the Server Hello message, using the mirrored client_hello tlsSession object
server_hello = TLS(raw(packets[5][TLS]), tls_session=client_hello.tls_session.mirror())

server_hello.tls_session.server_rsa_key = PrivKey(key.read())

client_finished = TLS(raw(packets[7][TLS]), tls_session=server_hello.tls_session.mirror())
server_finished = TLS(raw(packets[9][TLS]), tls_session=client_finished.tls_session.mirror())

http_query = TLS(raw(packets[11][TLS]), tls_session=server_finished.tls_session.mirror())
http_query.show()

http_response = TLS(raw(packets[13][TLS]), tls_session=http_query.tls_session.mirror())
http_response.show()