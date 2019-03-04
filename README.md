# Tserver
Tserver is a threaded echo test server written in python3. It passes command like arguments to a TCP socket hosted on loopback.
Tserver requies the standard python3 library and is being releases for people who are new to python and networking.


Example command for running Server on loopback:

  python3 Tserver.py -a host -p 7500  (-a command for IP address, -p is the port opened to recieve connections(use anything above 1024))
 
 Example command for running Client(Tserver is threaded so you may run up to 5 client connections at once):
 
 python3 Tserver.py -a 127.0.0.1 -p 7500 (-a command for servers IP address, and -p for the port running Tserver.py)
 
 
 
 After establishing a connections, you may run the following commands:
 Time (will return the current server time from the datetime module)
 History (will return the IP address and Port number of past connections)
 Entering a string such as "hello" will echo back to the client
 
