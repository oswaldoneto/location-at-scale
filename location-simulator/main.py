

from datetime import datetime, timedelta, timezone
from time import sleep

from nmeasim.simulator import Simulator
from nmeasim.models import TZ_LOCAL

def print_gps():


    sim = Simulator()

    with sim.lock:
        # sim.gps.output = ('GGA', 'GLL', 'GSA', 'GSV', 'RMC', 'VTG', 'ZDA')
        sim.gps.output = ('RMC',)
        sim.gps.num_sats = 14
        # araraquara lat lon
        sim.gps.lat = -21.79
        sim.gps.lon = -48.17
        sim.gps.kph = 70
        sim.gps.heading = 190.0
        sim.gps.mag_heading = 190.1
        sim.gps.date_time = datetime.now(TZ_LOCAL)



    file = open('locations.nmea', 'w')

    for sentence in list(sim.get_output(100)):
        file.write(sentence)
        file.write('\n')
        print(sentence)
        # sleep(1)


    file.close()







# gps = GpsReceiver(
    #     date_time=datetime(2022, 2, 12, 12, 34, 56, tzinfo=timezone.utc),
    #     output=('RMC',)
    # )
    #
    # for i in range(1000):
    #     gps.date_time += timedelta(seconds=1)
    #     print(gps.get_output())

if __name__ == '__main__':
    print_gps()

