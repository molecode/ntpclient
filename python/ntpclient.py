import struct
import socket
from datetime import datetime

ntp_server = 'pool.ntp.org'
ntp_port = 123

# unix epoch starts at 1970-01-01, ntp epoch at 1900-01-01, so we need the difference
ntp_epoch_offset = 2208988800
message = b'\x1b' + 47 * b'\00'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(message, (ntp_server, ntp_port))
data = sock.recv(1024)

sec = struct.unpack('>12I', data)[10]
current_time = sec - ntp_epoch_offset

print(datetime.utcfromtimestamp(current_time))
