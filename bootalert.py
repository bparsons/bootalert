#!/usr/bin/python2
"""

bootalert

Sends email with hostname and IP address

Brian Parsons <brian@pmex.com>

"""

import ConfigParser
import datetime
import re
import smtplib
import socket
import sys
import urllib

# Get Hostname
hostname = socket.gethostname()

# Get current IP
try:
    ipsite = urllib.urlopen('http://checkip.dyndns.org')
except:
    print 'Connection error getting IP address.'
    sys.exit(1)

response = ipsite.read()
ips = re.findall("(?:\d{1,3}\.){3}\d{1,3}", response)
if type(ips) in [list,  tuple,  set]:
    for record in ips:
        newip = record

try:
    newip
except NameError:
    print 'Unable to find IP address in response from check site.'
    sys.exit(1)

# Verify it's a good ip
try:
    socket.inet_aton(newip)
except socket.error:
    print 'Received invalid IP address.'
    sys.exit(1)

print 'Current IP: %s' % newip

# Parse Config File
config = ConfigParser.ConfigParser()
config.read("/etc/conf.d/bootalert")
try:
    confmailto = config.get("bootalert", "mailto")
    confmailfrom = config.get("bootalert", "mailfrom")
except ConfigParser.NoSectionError:
        print("Config file /etc/conf.d/bootalert not found")

# Send Message
# Get mail to address from conf file or default to root
try:
    mailto = confmailto
except NameError:
    mailto = "root"

# Get mail from address from conf file or default to root
try:
    mailfrom = confmailfrom
except NameError:
    mailfrom = "root"

now = datetime.datetime.now()

print("Sending mail from " + mailfrom + " to " + mailto + ".")
# compose boot email
messageheader = "From: Boot Alert <" + mailfrom + ">\n"
messageheader += "To: " + mailto + "\n"
messageheader += "Subject: " + hostname + "\n\n"
message = messageheader + hostname + " booted " + now.strftime("%a %b %d %H:%M:%S %Z %Y") + " with IP: " + newip + ".\n\n"

# send boot email
try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(mailfrom, mailto, message)
except:
    print("Error: unable to send boot alert email. Mail server running?")
    sys.exit(1)


