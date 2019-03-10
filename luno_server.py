import time
import operator
from luno_python.client import Client
import socket

server = Client("api key","api secret key")

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('0.0.0.0', 4000))
serversocket.listen(10) # become a server socket, maximum 10 connections

def receiveString():
    connection, address = serversocket.accept()
    buf = connection.recv(1)
    if len(buf) > 0:
    	if len(buf.split(' ')) == 2:
    		return buf
    return None 

class Bidder:
	""" represents a participant """
	def __init__(self, account_id, networkID, money, bid):
		self.account_id = account_id # for bitcoin
		self.money = money
		self.bid = bid

class Auction:
	"""
	ownerID : account ID of seller of intel
	auctionStartTime : (YY, MM, DD, HOUR, SECONDS)
	duration : how long the auction is supposed to last (in seconds)
	min bid : min bidself.networkID = networkID # for bidding and normal communication
		
	"""
	def __init__(self, ownerID, auctionStartTime, duration):
			self.ownerID = ownerID
			self.ast = auctionStartTime
			self.duration = duration
			self.participants = {}
			self.bids = {}
			self.starttime = 0
			self.auctionOpened = False
			self.refunded = False

	def hasStarted():
		if time.strftime("%Y") > ast[0]:
			if (time.strftime("%m") > ast[1]):
				if (time.strftime("%d") > ast[2]):
					if (time.strftime("%H") > ast[3]):
						if (time.strftime("%S") >= ast[4]):
							if (not self.auctionOpened):
								self.bids = self.participants.copy()
								self.starttime = time.time()
							self.auctionOpened = True
							return True
		return False


	def hasEnded():
		if time.time() > (self.starttime+self.duration) :
			return True
		return False 

	## ONLY CALL THIS FUNCTION WHEN THERE'S AN AUCTION GOING ON
	def receiveBids():
		str_data = receiveString()
		account_id, bid = str_data.split(" ")
		if (account_id in participants):
			if (bid > bids[account_id] and bid <= participants[account_id]):
				bids[account_id] = bid

	def registerBidder():
		GO THROUGH TRANSACTION HISTORY.
		ACCESS MESSAGES:
			CHECK IF THEY HAVE A POSITIVE BALANCE
			Participant[account_id] = money_deposited (=balance)
			bids[account_id] = 0
			
	def payMoney(accId, amount, msg):
		server.send(accId, amount, currency='bitcoin', description=None, message=msg)
	
	def run():

		if self.auctionOpened:

			if not self.hasEnded():
				self.receiveBids()
				emitAll(max(self.bids.values()))

			else: 

				if not self.refunded:
					
					# get the maximum winner
					winner = max(self.bids.items(), key=operator.itemgetter(1))[0]:
					
					# refund all losers their money
					for i in self.participants:
						if (i != winner):
							payMoney(i, self.participants[i], "funds refunded")

					# refund the winner any extra remaning money
					payMoney(winner, self.participants[winner]-bids[winner], "Funds refunded")
					payMoney(self.ownerID, self.bids[winner], "Item sold!")
					self.refunded = True
					self.auctionOpened=False

									