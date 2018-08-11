#!usr\bin\python

import smtplib

content = ''

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

serviceProvider = "n/a"

while serviceProvider == "n/a":
	serviceProvider = input("Who is the service provider of the phone number to send to? -> ")
	if serviceProvider == "Telus" or serviceProvider == "telus":
		provide_ = "@msg.telus.com"
	elif serviceProvider == "Rogers" or serviceProvider == "rogers":
		provide_ = "@pcs.rogers.com"
	elif serviceProvider == "bell" or serviceProvider == "Bell":
		print("Sorry... no can do")
		serviceProvider = "n/a"
	else:
		print("either that is not a valid service provider or something went wrong... please try again if that is a valid request")
		serviceProvider = "n/a"

user = input("Enter your email here -> ")
passw = input("Enter your password here -> ")
msg = input("Enter your message here -> ")
recv_num = input("Enter the recipient\'s number")

print("[Y] or [N]")
login_conf = input("Confirm login? -> ")
if login_conf == "Y":
	server.login(user, passw)
if login_conf != "Y":
	print("Something has gone wrong... either that or you aborted.. good day!")
	quit()

send2 = recv_num + serviceProvider

print("Would you like to spam texts?")
spam_conf = input("[Y] or [N]")
if spam_conf == "Y":
	num = input("How many times? (* = infinite) -> ")
	if num != "*":
		for x in range(0, int(num)):
			server.login(user, send2, msg)
	if num == "*":
		while True:
			server.login(user, send2, msg)
if spam_conf == "N":
	server.login(user, send2, msg)
if spam_conf != "N" and spam_conf != "Y":
	for x in range(0, 10):
		print("You have fucked up royally...")
		for x in range(0, 999999):
			pass
	quit()