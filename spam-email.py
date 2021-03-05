# -*- coding: utf-8 -*-
#!/usr/bin/python3
import smtplib
import time
import os
import getpass
import sys

class bcolors:
	GREEN = "\033[92m"
	WARNING = "\033[93m"
	FAIL = "\033[91m"
	ENDC = "\033[0m"


def spam():
	os.system("clear")
	print( bcolors.GREEN + """
╔══════════════════════════════════════════════════════════════════════════════════╗
║ ███████╗██████╗  █████╗ ███╗   ███╗      ███████╗███╗   ███╗ █████╗ ██╗██╗       ║ 
║ ██╔════╝██╔══██╗██╔══██╗████╗ ████║      ██╔════╝████╗ ████║██╔══██╗██║██║       ║
║ ███████╗██████╔╝███████║██╔████╔██║█████╗█████╗  ██╔████╔██║███████║██║██║       ║
║ ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║╚════╝██╔══╝  ██║╚██╔╝██║██╔══██║██║██║       ║
║ ███████║██║     ██║  ██║██║ ╚═╝ ██║      ███████╗██║ ╚═╝ ██║██║  ██║██║███████╗  ║
║ ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝      ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝  ║
╚══════════════════════════════════════════════════════════════════════════════════╝""" + bcolors.ENDC)


os.system("clear")
try:
	file1 = open("logo.txt", "r")
	print(" ")
	print(bcolors.GREEN + file1.read() + bcolors.ENDC)
	file1.close()
except IOError:
	print("Banner File not found")

#Input
print(bcolors.WARNING + """
Email Services Menu:
1) Gmail
2) Yahoo
3) Hotmail / Outlook
""" + bcolors.ENDC + "")
try:
	server = input(bcolors.GREEN + "Mail Server: " + bcolors.ENDC)
	user = input(bcolors.GREEN + "Your Email: " + bcolors.ENDC)
	pwd = getpass.getpass(bcolors.GREEN + "Password: " + bcolors.ENDC)
	to = input(bcolors.GREEN + "To: " + bcolors.ENDC)
	subject = input(bcolors.GREEN + "Subject (Optional): " + bcolors.ENDC)
	body = input(bcolors.GREEN + "Message: " + bcolors.ENDC)
	nomes = input(bcolors.GREEN + "Number of Emails to send: " + bcolors.ENDC)
	no = 0
	message = "From: " + user + "\nSubject: " + subject + "\n" + body
except KeyboardInterrupt:
	print(bcolors.FAIL + "\nCanceled" + bcolors.ENDC)
	sys.exit()

