from luno_python.client import Client;
import sockets

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('auction.localtunnel.me', 4000))

class Bidder:
	""" represents a bidder """
	def __init__(self, account_id, networkID, money, bid):
		self.account_id = account_id
		self.money = money
		self.bid = bid


# THIS IS THE BLOCK CHAIN STUFF
CLIENT_ID = ""
SECRET_ID = ""
server_acc = ""


# THIS IS THE BIDDING NETWORKING STUFF
cl = Client(CLIENT_ID, SECRET_ID)

# obtain the amount of bitcoin the client has
def getXBTBalance():
	balances = cl.get_balances()['balance']
	for i in len(balances):
		if balances[i]['asset'] == 'XBT':
			return balances[i]['balance']
	return 0

def getAccountID():
	balances = cl.get_balances()['balance']
	for i in len(balances):
		if balances[i]['asset'] == 'XBT':
			return balances[i]['account_id']
	return 0


def joinAuction():
	try:
		connecting to server
		
		if there is an auction going to start:
			if you want to participate:
			
				client_acc_id = getAccountID()
				## BOOK YOUR TICKET
				cl.send(server_acc, getXBTBalance(), currency='bitcoin', description=None, message=client_acc_id)
				
				while auction has started and has not ended:
					bid = double(input())
					str_pack = " " + account_id + " " + bid 
					clientsocket.send(str_pack)
