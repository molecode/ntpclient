import socket

ntp_server = 'pool.ntp.org'
ntp_port = 123
message = b'\x1b' + 47 * b'\00'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(message, (ntp_server, ntp_port))
data = sock.recv(1024)

print(data)
