import io
import SocketServer
import struct
import time
import picamera

class MyTCPHandler(SocketServer.StreamRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
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
                #self.wfile.write(struct.pack('<L', stream.tell()))
                #self.flush()
                #stream.seek(0)
                #self.write(stream.read())
                self.data = stream.read()
                if time.time() - start > 600:
                    break
                stream.seek(0)
                stream.truncate()
        self.wfile.write(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "192.168.0.104", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

