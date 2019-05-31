<<<<<<< HEAD
from splinter import Browser
import time,sys

def overFillById(browser,id,fillString):
    if browser.is_element_present_by_id(id,wait_time=2):
        browser.find_by_id(id).fill(fillString)
    return;

def overClickById(browser,id):
    if browser.is_element_present_by_id(id,wait_time=2):
        browser.find_by_id(id).click() 
    return;

def overClickByText(browser,text):
    if browser.is_element_present_by_text(text,wait_time=2):
        browser.find_by_text(text).click() 
    return;

def insertNavRecord(browser,date,codiceCommessa,faseCommessa,hour ):
    time.sleep(1)
    overClickById(browser,'listaRigheOdT_btnNew')
    time.sleep(1)
    overClickById(browser,'btnRicercaCommessa')
    time.sleep(2)
    overFillById(browser,'searchCodCommessa',codiceCommessa)
    overFillById(browser,'searchFase',faseCommessa)
    browser.find_by_id('listaCommesse_btnFiltra').click()
    time.sleep(1)
    overClickByText(browser,codiceCommessa)
    time.sleep(2)
    overFillById(browser,'Data',date)
    overClickById(browser,'Note')
    overFillById(browser,'hord',hour)
    time.sleep(1)
    overClickById(browser,'btnSalva')
    time.sleep(2)
    return;

def navisionLogin(browser):
    browser.visit('https://navisionweb.lutech.it')
    browser.find_by_id('UserName').fill(user)
    browser.find_by_id('Password').fill(password)
    browser.find_by_id('btnLogin').click()
    return;

def newReport(browser):
    browser.find_by_id('menu1').click()
    time.sleep(1)
    if browser.is_element_present_by_id('listaOdT_btnNew',wait_time=2):
        browser.find_by_id('listaOdT_btnNew').click()
    time.sleep(1)
    return;  

def openBozzaReport(browser):
    browser.find_by_id('menu1').click()
    browser.find_by_text('BOZZA').click()
    time.sleep(1)
    if browser.is_element_present_by_id('listaOdT_btnEdit',wait_time=2):
        browser.find_by_id('listaOdT_btnEdit').click()
    time.sleep(1)
    return;  


scriptName, user, password, csv = sys.argv

browser = Browser('chrome')
navisionLogin(browser)
newReport(browser)
#openBozzaReport(browser)

f=open(csv, "r")
fl =f.readlines()
records = list()
listaDate = list()
for x in fl:
    #print (x)
    y = x.split(";")
    if y[0]!='IGNORE':
        if y[0]=='DATE':
            for k in y:
                if k != '' and k != '\n' and k!= 'DATE' and k!='END':
                    listaDate.append(k)
        if y[0]=='COMMESSA':
            for j in range(4,y.index('END\n')):
                record = list()
                record.append(listaDate[j-4])
                record.append(y[2])
                record.append(y[3])
                record.append(y[j])
                records.append(record)

for p in records:
    if p[0]!='' and p[1]!='' and p[2]!='' and p[3]!='':
        insertNavRecord(browser,p[0],p[1],p[2],p[3])

        

