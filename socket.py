import socket
import threading
import time

conn = None
flow = False

def flow_thread():
    global conn
    global flow
    while True:
        print("thread")
        if(flow):
            flowfile = open('/home/pi/MindLabs/flow.txt', 'r')
            flows = flowfile.read()
            print(flows)
            conn.send(flows.encode())
        time.sleep(1)
        
def server_program():
    host = '192.168.0.72'
    port = 3000

    global conn
    global flow

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)

    while True:
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        statefile = open('/home/pi/MindLabs/temp.txt', 'r')
        state = statefile.read()
        print(state)
        conn.send(state.encode())
        flow = True
        while True:
            try:
                # receive data stream. it won't accept data packet greater than 1024 bytes
                data = conn.recv(1024).decode()
                if not data:
                    # if data is not received break
                    break

                print("valve: " + str(data[2:len(data)]))
            except:
                print("oops")
                
            try:
                if(int(data[2:len(data)]) >= 0):
                    print("flow max"+ str(data[2:len(data)]))
                    file = open('/home/pi/MindLabs/maxTime.txt', 'w')
                    file.write(str(data[2:len(data)]))
                    file.close()
            except:
                print("state" + str(data[2:len(data)]))
                file = open('/home/pi/MindLabs/temp.txt', 'w')
                file.write(str(data[2:len(data)]))
                file.close()

            time.sleep(.2)

        flow = False
        print('closing connection')
        conn.close()
    
if __name__ == '__main__':
    threading.Thread(target=flow_thread).start()
    server_program()
