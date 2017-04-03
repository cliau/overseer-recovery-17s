import json
import urllib2
import datetime
import matplotlib.pyplot as plt


def get_winds(url): # returns date as json object and avg wind speed
    data = json.load(urllib2.urlopen(url))
    parsed_json = json.loads(json.dumps(data))

    obs = parsed_json['history']['observations']

    dates = []
    wind_speeds = []
    wind_dirs = []

    for datum in obs:
        date = datum["date"] # convert date into datetime object usable by python
        dates.append(datetime.datetime(int(date['year']), int(date['mon']), int(date['mday']), int(date['hour']), int(date['min'])));
        wind_speeds.append(datum['wspdm']) # there's also a wspdi field, but wspdm is the one available on the public site
        wind_dirs.append(datum['wdird'])

    return (dates, wind_speeds, wind_dirs)

def plotwinds(dates, speeds):
    plt.plot(dates, speeds)
    plt.ylabel('wind speeds (mph)')
    plt.xticks(rotation=70)
    plt.show()


cities = ['Santa Clarita', 'Castaic', 'Ravenna', 'Cantil', 'Mojave', 'California City']

url = "http://api.wunderground.com/api/[KEY]/history_20170402/q/CA/Mojave.json"

def main():
    val = get_winds(url)
    plotwinds(val[0], val[1])
    # to do:
        # specify range of dates
        # iterate through list of cities
        # output as csv

if __name__== "__main__": # if this script is being run as the main program
    main()