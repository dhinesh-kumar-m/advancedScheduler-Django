from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from forecastUpdater import forecastApi

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(forecastApi.update_forecast, 'interval', minutes=1)
    # scheduler.add_job(id = None,func = forecastApi.update_forecast, trigger = 'cron',misfire_grace_time = 600, hour=11,minute = 00)
    scheduler.start()