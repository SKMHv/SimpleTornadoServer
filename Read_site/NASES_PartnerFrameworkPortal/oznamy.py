'''
Created on May 20, 2019

@author: root
'''

from NASES_PartnerFrameworkPortal  import porovnaj, loger, notifi_oznamy
import eMail_notification
import sys

# ==============================================================================================
# odosli mailom
# ==============================================================================================
sender_email = "michal.hvila@gmail.com"
receiver_email = "hvila.michal@gmail.com"   
subject_email = "Notifikacia zmien odstavok z NASES ...."
html_oznamy = repr(notifi_oznamy())

#===============================================================================
# last="oznamy.txt"
# with open(last, 'w') as file_a:
#     file_a.write(html_oznamy)
# 
# print(porovnaj(html_oznamy, last))
#===============================================================================

print("---------------------")
try:
    if html_oznamy:
        last="oznamy.html"
        print("Idem porovnat verzie - v pripadne nezhody odoslat email s oznammi.")
        if porovnaj(html_oznamy, last) != True:        
            mail_a = eMail_notification.Email(subject_email, sender_email, receiver_email, html_oznamy)
            mail_a.odosli()
            with open(last, 'w') as file_a:
                file_a.write(html_oznamy) 
                loger("Odoslal som email + do 'oznamy.txt' som zapisal novy obsah ....")
        else:
            print("Z dovody zhody verzii sa neodoslal email")

except Exception as e:
    print(e)
    sys.exit()
                      
