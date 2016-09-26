#!/usr/bin/env python
# coding: Latin-1

# Load library functions we want
import socket
import time
import pygame
from pygame.locals import *
import numpy as np
import cv2

# # Settings for the RemoteKeyBorg client
# broadcastIP = '192.168.0.104'           # IP address to send to, 255 in one or more positions is a broadcast / wild-card
# broadcastPort = 9038                    # What message number to send with (LEDB on an LCD)
# leftDrive = 1                           # Drive number for left motor
# rightDrive = 3                          # Drive number for right motor
# interval = 0.1                          # Time between keyboard updates in seconds, smaller responds faster but uses more processor time
# regularUpdate = True                    # If True we send a command at a regular interval, if False we only send commands when keys are pressed or released

# # Setup the connection for sending on
# sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)       # Create the socket
# sender.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)                        # Enable broadcasting (sending to many IPs based on wild-cards)
# sender.bind(('0.0.0.0', 0))                                                         # Set the IP and port number to use locally, IP 0.0.0.0 means all connections and port 0 means assign a number for us (do not care)


'''
Receive images
'''
print 'ok'
server_socket = socket.socket()
try:
    server_socket.bind(('0.0.0.0', 8000))
    server_socket.listen(0)
    connection = server_socket.accept()[0].makefile('rb')
    print('Image is verified')
except:
    print "error"

    
finally:
    connection.close()
    server_socket.close()

# # connect to a seral port
# send_inst = True

# # create labels
# k = np.zeros((4, 4), 'float')
# for i in range(4):
#     k[i, i] = 1
# temp_label = np.zeros((1, 4), 'float')


# # Setup pygame and key states
# global hadEvent
# global moveUp
# global moveDown
# global moveLeft
# global moveRighte
# global moveQuit
# global command
# hadEvent = True
# moveUp = False
# moveDown = False
# moveLeft = False
# moveRight = False
# moveQuit = False
# command = 'w'
# pygame.init()
# screen = pygame.display.set_mode([300,300])
# pygame.display.set_caption("RemoteKeyBorg - Press [ESC] to quit")

# # Function to handle pygame events
# def PygameHandler(events):
#     # Variables accessible outside this function
#     global hadEvent
#     global moveUp
#     global moveDown
#     global moveLeft
#     global moveRight
#     global moveQuit
#     global command
#     # Handle each event individually
#     stream_bytes += connection.read(1024)
#     first = stream_bytes.find('\xff\xd8')
#     last = stream_bytes.find('\xff\xd9')
#     if first != -1 and last != -1:
#         jpg = stream_bytes[first:last + 2]
#         stream_bytes = stream_bytes[last + 2:]
#         image = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.CV_LOAD_IMAGE_GRAYSCALE)
        
#         # select lower half of the image
#         roi = image[120:240, :]
        
#         # save streamed images
#         cv2.imwrite('training_images/frame{:>05}.jpg'.format(frame), image)
        
#         #cv2.imshow('roi_image', roi)
#         cv2.imshow('image', image)
        
#         # reshape the roi image into one row array
#         temp_array = roi.reshape(1, 38400).astype(np.float32)
        
#         frame += 1
#         total_frame += 1
#     # get input from human drive
#     for event in events:
#         if event.type == pygame.QUIT:
#             # User exit
#             hadEvent = True
#             moveQuit = True
#         elif event.type == KEYDOWN:
#             key_input = pygame.key.get_pressed()
#             hadEvent = True
#             # print key_input
#             # complex orders
#             if (key_input[pygame.K_UP] and key_input[pygame.K_RIGHT]) or (key_input[pygame.K_w] and key_input[pygame.K_d]):
#                 print("Forward Right")
#                 image_array = np.vstack((image_array, temp_array))
#                 label_array = np.vstack((label_array, k[1]))
#                 saved_frame += 1
#                 command = 'wd'
#                 sender.sendto(command, (broadcastIP, broadcastPort))

#             elif (key_input[pygame.K_UP] and key_input[pygame.K_LEFT]) or (key_input[pygame.K_w] and key_input[pygame.K_a]):
#                 print("Forward Left")
#                 image_array = np.vstack((image_array, temp_array))
#                 label_array = np.vstack((label_array, k[0]))
#                 saved_frame += 1
#                 command = 'wa'
#                 sender.sendto(command, (broadcastIP, broadcastPort))

#             elif (key_input[pygame.K_DOWN] and key_input[pygame.K_RIGHT]) or (key_input[pygame.K_s] and key_input[pygame.K_d]):
#                 print("Reverse Right")
#                 command = 'sd'
#                 sender.sendto(command, (broadcastIP, broadcastPort))

#             elif (key_input[pygame.K_DOWN] and key_input[pygame.K_LEFT]) or (key_input[pygame.K_s] and key_input[pygame.K_a]):
#                 print("Reverse Left")
#                 command = 'sa'
#                 sender.sendto(command, (broadcastIP, broadcastPort))

#             # simple orders
#             elif (event.key == pygame.K_UP) or  (event.key == pygame.K_w):
#                 print("Forward")
#                 saved_frame += 1
#                 image_array = np.vstack((image_array, temp_array))
#                 label_array = np.vstack((label_array, k[2]))
#                 command = 'w'
#                 sender.sendto(command, (broadcastIP, broadcastPort))

#             elif (event.key == pygame.K_DOWN) or  (event.key == pygame.K_s):
#                 print("Reverse")
#                 saved_frame += 1
#                 image_array = np.vstack((image_array, temp_array))
#                 label_array = np.vstack((label_array, k[3]))
#                 command = 's'
#                 sender.sendto(command, (broadcastIP, broadcastPort))

#             elif (event.key == pygame.K_RIGHT) or  (event.key == pygame.K_d):
#                 print("Right")
#                 image_array = np.vstack((image_array, temp_array))
#                 label_array = np.vstack((label_array, k[1]))
#                 saved_frame += 1
#                 command = 'd'
#                 sender.sendto(command, (broadcastIP, broadcastPort))

#             elif (event.key == pygame.K_LEFT) or  (event.key == pygame.K_a):
#                 print("Left")
#                 image_array = np.vstack((image_array, temp_array))
#                 label_array = np.vstack((label_array, k[0]))
#                 saved_frame += 1
#                 command = 'a'
#                 sender.sendto(command, (broadcastIP, broadcastPort))

#             elif event.key == pygame.K_x or event.key == pygame.K_q:
#                 print 'Exit'
#                 hadEvent = True
#                 moveQuit = True
#                 command = 'x'
#                 sender.sendto(command, (broadcastIP, broadcastPort))
#                 exit()
#                 break



#         elif event.type == pygame.KEYUP:
#             hadEvent = True
#             key_input = pygame.key.get_pressed()
#             if (key_input[pygame.K_UP]) or  (key_input[pygame.K_w]):
#                 print("FR or FL to Forward")
#                 saved_frame += 1
#                 image_array = np.vstack((image_array, temp_array))
#                 label_array = np.vstack((label_array, k[2]))
#                 command = 'w0'
#                 sender.sendto(command, (broadcastIP, broadcastPort))
#             elif (key_input[pygame.K_DOWN]) or  (key_input[pygame.K_s]):
#                 print("RR or RL to Reverse")
#                 saved_frame += 1
#                 image_array = np.vstack((image_array, temp_array))
#                 label_array = np.vstack((label_array, k[3]))
#                 command = 's0'
#                 sender.sendto(command, (broadcastIP, broadcastPort))
#             if (not key_input[pygame.K_DOWN] and not key_input[pygame.K_UP]) and \
#                 (not key_input[pygame.K_w] and not key_input[pygame.K_s]):
#                 print 'no foward/backward key pressed'
#                 command = '0'
#                 sender.sendto(command, (broadcastIP, broadcastPort))

# try:
#     print 'Press [ESC] to quit'
#     # Loop indefinitely
#     # command = ''
#     saved_frame = 0
#     total_frame = 0

#     # collect images for training
#     print 'Start collecting images...'
#     e1 = cv2.getTickCount()
#     image_array = np.zeros((1, 38400))
#     label_array = np.zeros((1, 4), 'float')

#     # stream video frames one by one
#     stream_bytes = ' '
#     frame = 1
#     while True:
#         # Get the currently pressed keys on the keyboard
#         PygameHandler(pygame.event.get())
#         if command == 'x':
#             break
#         # Wait for the interval period
#         time.sleep(interval)
#     # Inform the server to stop
#     sender.sendto('ALLOFF', (broadcastIP, broadcastPort))
#     # save training images and labels
#     train = image_array[1:, :]
#     train_labels = label_array[1:, :]

#     # save training data as a numpy file
#     np.savez('training_data_temp/test08.npz', train=train, train_labels=train_labels)

#     e2 = cv2.getTickCount()
#     # calculate streaming duration
#     time0 = (e2 - e1) / cv2.getTickFrequency()
#     print 'Streaming duration:', time0

#     print(train.shape)
#     print(train_labels.shape)
#     print 'Total frame:', total_frame
#     print 'Saved frame:', saved_frame
#     print 'Dropped frame', total_frame - saved_frame

# except KeyboardInterrupt:
#     # CTRL+C exit, inform the server to stop
#     sender.sendto('ALLOFF', (broadcastIP, broadcastPort))
# finally:
#     connection.close()
#     server_socket.close()