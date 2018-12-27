import socket
import time

ntp_server = 'pool.ntp.org'
ntp_port = 123

# unix epoch starts at 1970-01-01, ntp epoch at 1900-01-01, so we need the difference
ntp_epoch_offset = 2208988800
message = b'\x1b' + bytes(47)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.sendto(message, (ntp_server, ntp_port))
    data = sock.recv(1024)

# use int.from_bytes() method
sec = int.from_bytes(data[40:44], 'big') - ntp_epoch_offset # network response is big endian

# using struct is another possibilty to get the secs from the response
#import struct
#sec = struct.unpack('>12I', data)[10]
#sec -= ntp_epoch_offset

print(time.ctime(sec))
