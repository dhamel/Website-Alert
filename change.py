# -*- coding: utf-8 -*-
import time
import requests
import smtplib
from timeit import default_timer as timer




start = timer()


def send_email(user ,password, recipient, subject, body):
    gmail_user = user
    gmail_pwd = password
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587) #start smtp server on port 587
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd) #login to gmail server
        server.sendmail(FROM, TO, message) #actually perform sending of mail
        server.close() #end server
        print 'successfully sent the mail' #alert user mail was sent
    except Exception, e: #else tell user it failed and why (exception e)
            print "failed to send mail, " +str(e)


def main():
    with requests.Session() as c:
        url = "http://store.nike.com/us/en_us/"
        wait_time = 120
        user = "releasealerter@gmail.com"
        password = "xusxhxodmarocenf"
        recipient = "dhamel9696@gmail.com"
        subject = "Site Updated"
        body = "Change at : " + str(url)
        page1 = c.get(url)
        #time.sleep(wait_time)
        page2 = c.get(url)
        if page1.content == page2.content:
            end = timer()
            if ((end-start)) >= 60:
                timeMinutes = (end-start) / 60
                print "[-]No Change Detected @ " +str(url)+ "\n[-]Elapsed Time: " +str(timeMinutes)+ " minutes"
            else:
                print '[-]No Change Detected @ ' +str(url)+ "\n[+]Elapsed Time: " +str((end-start))+ " seconds"


        else:
            end = timer()
            if int((end-start)) >= 60:
                timeMinutes = (end-start) / 60
                print '[+]Change Detected - \n[+]Elapsed Time: ' +str(timeMinutes)+ " minutes"
            else:
                print '[+]Change Detected - \n[+]Elapsed Time: ' +str((end-start))+ " seconds"


                send_email(user, password, recipient, subject, body) #send notification email

        page2 = None
        print "Loop ran"
        main()  # this is shit fix this later


if __name__ == "__main__":
    main()
