from flask import Flask
app = Flask(__name__)

from apscheduler.scheduler import Scheduler 

 
sched = Scheduler() # Scheduler object 
sched.start() 
 
def fetch_data_from_api(): 
    ''' 
     Do your job here 
    ''' 
 
#add your job here 
sched.add_interval_job(fetch_data_from_api,minutes=10) 
 
''' 
All of your app.routes here 
''' 
 
# finally 
app.run() 
from app import routes

