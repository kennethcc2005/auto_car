import io 
import socket
import struct
import time
import picamera

# create socket and bind host
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print '1'
client_socket.connect(('192.168.1.104', 8000))
print '2'
connection = client_socket.makefile('wb')
print '3'

try:
    print 'step1 ok'
    with picamera.PiCamera() as camera:
        print 'step2'
        camera.resolution = (320, 240)      # pi camera resolution
        camera.framerate = 10               # 10 frames/sec
        time.sleep(2)                       # give 2 secs for camera to initilize
        start = time.time()
        stream = io.BytesIO()
        
        # send jpeg format video stream
        for foo in camera.capture_continuous(stream, 'jpeg', use_video_port = True):
            print 'step3 loop'
            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()
            stream.seek(0)
            connection.write(stream.read())
            if time.time() - start > 600:
                break
            stream.seek(0)
            stream.truncate()
    connection.write(struct.pack('<L', 0))
finally:
    print '4'
    connection.close()
    client_socket.close()