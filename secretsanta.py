import random
import smtplib 

people = {'name':'email',\
          'name':'email'}
          
Sender = "SecretSantaEmail"
Password = "PasswordToSecretSantaEmail"


def match(names):

	random.shuffle(names)
	send = names[:]
	recieve = send[:]
	recieve.append(recieve.pop(0))
	matchlist = []
	for x in range(len(names)):
		matchlist.append((send[x],recieve[x]))
	return matchlist
	
def sendmail(recipient, to_addr):
	header = 'From: forever2secretsanta@gmail.com\n'
	header += 'To: %s\n' % to_addr
	header += 'Subject: Secret Santa round 2 w0w\n\n' 
	message = header + 'you got ' + recipient + ' for secret santa'
	try:
		smtpObj = smtplib.SMTP('smtp.gmail.com',587)
		smtpObj.starttls()
		smtpObj.login(Sender, Password)
		smtpObj.sendmail(Sender, to_addr, message)  
		smtpObj.quit()
		print "Successfully sent email"
	except smtplib.SMTPException, e:
		print "Error unable to send email: " + e
		
		
def secretsanta(people):
	names = list(people.keys())
	matchlist = match(names)
	for x in matchlist:
		sender,reciever = x
		sendmail(reciever, people[sender])
	
secretsanta(people)
