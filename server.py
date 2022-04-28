"""Server for multithreaded (asynchronous) de Banque de Soukra-  application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from threading import Timer
from datetime import datetime
import select,time,threading
import os
import csv
  
#proccessus menu
class menu(object):
    
    
    
 
    def __init__(self, interval=1):
        self.interval = interval
 
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()
 
    def run(self):
        while True:
            # More statements comes here
            
                print(" ***** Soukra Bank ***** ")
                print("1- Account details ")
                print("2- Account bill ")
                print("3- History of transactions ")
                print("4- Exit")
                reponse = input()
                if (reponse =="1"):
                    ach =""
                    ach = input("Client reference : ")
                    with open('comptes.txt', mode='r') as csv_file:
                        csv_reader = csv.DictReader(csv_file)
                        line_count = 0
                        for row in csv_reader:
                            if row["Reference"] == ach :
                             print(f' {(row)}')        
                
                    """ach =""
                    ach = input("Client reference : ")
                    compt = open("comptes.txt","r")
                    l = compt.readlines()
                    print("Reference   	Valeur  	Etat	       Plafond Debit")
                    for i in l :
                        if i.split(" ")[0] == ach :
                            print(i)
                    compt.close()"""
                elif (reponse=="2"):
                    ach =""
                    ach = input("Client reference : ")
                    with open('factures.txt', mode='r') as csv_file:
                        csv_reader = csv.DictReader(csv_file)
                        line_count = 0
                        for row in csv_reader:
                            if row["Reference"] == ach : 
                             print(f' {(row)}')        
                        
                   
                elif (reponse=="3"):
                     with open('histo.txt', mode='r') as csv_file:
                        csv_reader = csv.DictReader(csv_file)
                        for row in csv_reader:
                             print(f' {(row)}')  
                 
                elif (reponse=="4"):
                     os._exit(0) #
                   
            
                else:
                    print("Wrong value")
 
 
 
        time.sleep(self.interval)
 
 
def accepter_connexions():
    while True:
        try:
            client, client_address = SERVER.accept()
            client.send(bytes("Connecting...","utf8"))
            Thread(target=gerer_client, args=(client,)).start()
        except:
            print("Not connected")
            break
 
 
 
 
def gerer_client(client):  
    global ref
    global amount
    choix = client.recv(BUFSIZ).decode("utf8")
    #debiter
    if int(choix)==1 :
        print("1.....")
        client.send(bytes('donner votre reference',"utf8"))
        ref= client.recv(BUFSIZ).decode("utf8")
        print("2.....")
        client.send(bytes('donner le montant a debiter',"utf8"))
        amount= client.recv(BUFSIZ).decode("utf8")
        print("3.....")
        with open('comptes.txt', mode='r') as csv_file:
                        csv_reader = csv.DictReader(csv_file)
                        exist=False
                        for row in csv_reader:
                            if row["Reference"] == ref :
                                exist=True
                                if row["Etat"]=="Positif":
                                    if int(row["valeur"])+int(row["Plafond_Debit"])>int(amount):                                        
                                        with open('histo.csv', mode='w') as histo_file:
                                         histo_writer = csv.writer(histo_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                                         histo_writer.writerow([ref,'Retrait',amount, 'succes','Positif'])
                                        with open('comptes.csv', mode='w') as compte_file:
                                         compte_file=csv.writer(compte_file,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)           
                                         compte_file.writerow([ref,int(row["valeur"])-int(amount)],'Positif',row["Plafond_Debit"])
                                         print("jawha behi")
                                    else :
                                         client.send(bytes('No so broke',"utf8"))
                                else:
                                    if int(row["Plafond_Debit"])-int(row["valeur"])>int(amount):            
                                        with open('histo.csv', mode='w') as histo_file:
                                         histo_writer = csv.writer(histo_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                                         histo_writer.writerow([ref,'Retrait',amount, 'succes','Negatif'])
                                        with open('comptes.csv', mode='w') as compte_file:
                                         compte_file=csv.writer(compte_file,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)           
                                         compte_file.writerow([ref,int(row["valeur"])-int(amount)],'Negatif',row["Plafond_Debit"])
                        if (exist==False): client.send(bytes('Compte non existant',"utf8"))

                          
 
 
 
 
 

 

HOST = '192.168.1.1'
PORT = 50000
BUFSIZ = 1024 #Nombre de bits par message 
ADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM) #le type du socket : SOCK_STREAM pour le protocole TCP
SERVER.bind(ADDR)
 
#SERVER.setblocking(0)
if __name__ == "__main__":
    while True :
 
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
 
        m=menu()   
 
        SERVER.listen(5)
        ACCEPT_THREAD = Thread(target=accepter_connexions)
        ACCEPT_THREAD.start()
        ACCEPT_THREAD.join()
        SERVER.close()