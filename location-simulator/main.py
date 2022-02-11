
import json
from uuid import uuid4

from datetime import datetime, timedelta, timezone
from time import sleep

from nmeasim.simulator import Simulator
from nmeasim.models import TZ_LOCAL


def generate_sentences(n):

    sim = Simulator()

    with sim.lock:
        sim.gps.output = ('RMC',)
        # araraquara lat lon
        sim.gps.lat = -21.79
        sim.gps.lon = -48.17
        sim.gps.kph = 70
        sim.gps.heading = 190.0
        sim.gps.mag_heading = 190.1
        sim.gps.date_time = datetime.now(TZ_LOCAL)

    return list(sim.get_output(n))        

def persist_data(data):
    with open('locations.json', 'w') as file:
        json.dump(data, file)


def simulate():

    data = {
        "DeviceId": str(uuid4()),
        "NMEASentences": generate_sentences(100) 
    }

    persist_data(data)

if __name__ == '__main__':
    simulate()

