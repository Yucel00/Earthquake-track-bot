import random
import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

libraryy=[]

def send_phone(msg): #service of sending message twilio
    account_sid = 'your account sid given from twillio'
    auth_token = 'your token given from twilio'
    client = Client(account_sid, auth_token)

    client.messages.create(
    body=msg,
    from_='your demo number given from twillio',
    to='your number'
    
)
 

while True:
    response=requests.get("https://deprem.afad.gov.tr/last-earthquakes.html") #i throw request this website for attracting data
    soup=BeautifulSoup(response.content,"html.parser")

    table=soup.find("table")#i find table tag from html content
    rows=table.find_all("tr")#i find all tr tag from table and assign rows variable

    for row in rows[1:2]: #take firs row from rows
        cells = row.find_all("td")#i find all td tag from row and assign cells variable
        date=cells[0].text.strip()
        magnitude=cells[5].text.strip()
        location=cells[6].text.strip()
        id=date.split(" ")
        id=id[1]
        id=id.split(":")
        id=id[2]
        message=f"{date}-{magnitude}-{location}"
        if id in libraryy:
            continue
        else:
            magnitude=float(magnitude)
            if magnitude>=4.5:
                send_phone(message)
                libraryy.append(id)