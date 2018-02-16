#!/home/salhagen/opt/python-3.6.3/bin/python3
import sys
from apscheduler.schedulers.blocking import BlockingScheduler
from chanscraper import *
from colocation import *
from startwordanalysis import *

print('Content-type: text/html\n\n')

print('<html><body>ma domain running python ' + sys.version + '<body></html>')

def startcode():
    print('Creating snapshot csv')
    outputcsv = startSnapshot(False)                #bool represents whether images should be fetched
    print('Snapshot csv created')
    # print('Started word analysis...')
    # startWordAnalysis(outputcsv)
    print('Resetting variables')
    resetVariables()
    # print('Code finished!')
    print('Waiting a few mins before next update...')

def scheduleChanScraping(timespan):
    createNewSnapshot()
    scheduler = BlockingScheduler()
    scheduler.add_job(startcode, 'interval', minutes=timespan, start_date='2018-02-16 20:25:00') #add , start_date='2018-01-05 17:21:00' later
    scheduler.start()

quit()
scheduleChanScraping(5)