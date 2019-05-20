'''
Created on May 18, 2019

@author: root
'''
from NASES_PartnerFrameworkPortal  import notifi_odstavky, porovnaj, loger
import eMail_notification
import sys

# ==============================================================================================
# odosli mailom
# ==============================================================================================
sender_email = "michal.hvila@gmail.com"
receiver_email = "hvila.michal@gmail.com"   
subject_email = "Notifikacia zmien odstavok z NASES ...."


try:
    for i in notifi_odstavky():
        if i.find("technicke-odstavky-fix") != -1:
            print("Idem porovnat verzie - v pripadne nezhody odoslat email za odstavky UPVS FIX")
            last="odstavky_fix.html"
            
            if porovnaj(i, last) != True:        
                mail_a = eMail_notification.Email(subject_email, sender_email, receiver_email, i)
                mail_a.odosli()
                with open(last, 'w') as file_o:
                    file_o.write(i) 
                    loger("Odoslal som email + do 'odstavky_fix.html' som zapisal novy obsah ....")
            else:
                print("Z dovody zhody verzii sa neodoslal mail")
                    
        else:
            print("Idem porovnat verzie - v pripadne nezhody odoslat email za odstavky UPVS PROD")
            last="odstavky_prod.html"
            if porovnaj(i, last) != True:
                mail_a = eMail_notification.Email(subject_email, sender_email, receiver_email, i)
                mail_a.odosli()
                with open(last, 'w') as file_o:
                    file_o.write(i) 
                    loger("Odoslal som email + do 'odstavky_prod.html' som zapisal novy obsah ....")
            else:
                print("Z dovody zhody verzii sa neodoslal mail")
        print("------------------------------------------------")

except Exception as e:
    print(e)
    sys.exit()

loger("Notifikacny email s odstavkami bol odoslany ...")
     

