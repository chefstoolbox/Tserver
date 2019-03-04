import socket, sys, argparse, datetime
from threading import Thread

# Main Function
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--address', dest='ip',  type=str, help='Echo Server\'s IP Address')
    parser.add_argument('-p', '--port',  dest='port', type=int,  help='Port Number OPENED for Connection.')
    options = parser.parse_args()
    if options.ip == 'host':
        options.ip = '127.0.0.1'

#Pass arguments to server and start
    startServer(options)

# Create a TCP/IP socket
def startServer(options):
    server_address = (options.ip, options.port) 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind(server_address)
            sock.settimeout(60)
            print('Starting EchoServer up on {} port {}'.format(*server_address))
        except Exception:
            print('Server bind error:' + str(sys.exc_info()))
            sys.exit()  
              
        sock.listen(5)
        print('Waiting for a connection...')

#Communication Loop
        while True:
            history = []
            connection, client_address = sock.accept()
            history.append(client_address)
            print('Connected to : {} '.format(client_address))
            message = '[{}] Welcome to TServer'.format(datetime.datetime.now())
            connection.send(message.encode('utf8'))
            thread = Thread(target=clientThread, args=(connection, client_address, history))
            try:
                thread.daemon = True
                thread.start()
                print('Starting Thread for: ', client_address)
            except Exception:
                print('Client thread did not start.')
                traceback.print_exc()
				

#Threading for Clients in sock.listen()
def clientThread (connection, client_address, history):
    threading = True
    while threading:
	#Listening for data to be received 
        data = connection.recv(512).decode('utf8')
        dataParser(connection, client_address,history, data)
    connection.close()
	
#Data return function
def dataParser(connection, client_address, history, data):
    print('From Client: {}   Received: {}'.format(client_address, data))
    while data != 'Exit':
        if 'History' in data:
            message = str(history)
            connection.send(message.encode('utf8'))
            return True

        elif 'Time' in data:
            message = str(datetime.datetime.now().time())
            connection.send(message.encode('utf8'))
            return True
        else:
            connection.send(data.encode('utf8'))
            return True
    
        if data == 'Exit':
            message = str('Terminating Connection...')
            connection.send(message.encode('utf8'))
            print ('Connection to: %s  : Closed' % (client_address))
            return False

                    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('CTRL-C Pressed. Shutting Server Down.')
        sock.close()
   #     sys.exit()
