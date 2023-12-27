import datetime
import json

#Input: takes building string from Alexa slot values defined in en_US.json
#output: returns an integer value to lambda_function to indicate whether input
        # was found in buildings dictionary

def OpenOrClosed(building, curr_time):

    """
    current__dt format looks like: 2021-06-25 07:58:56.550604
    Type: Object
    building: building name as a string
    """
    all_buildings = {}
    with open('build_info.json') as json_file:
        data = json.load(json_file)
    '''
    for x in data:
        building = Building(x['name'], x['type'])
        building.set_open(x['open_dic']['openHour'], x['open_dic']['openMin'], x['open_dic']['openSec'])
        building.set_close(x['close_dic']['closeHour'], x['close_dic']['closeMin'], x['close_dic']['closeSec'])
        all_buildings[x['name']] = building
        
    '''

    data = {k.lower(): v for k, v in data.items()}
    """
    for i in data.keys():
        data.keys()[i] = data.keys()[i].lower()
        print(data.keys()[i])
        """
    #returns time instance in 07:58:56.550604 format
    #print(data.keys())
    #curr_time = datetime.datetime.now().time()


    if building in data.keys():
        start = datetime.time(data[building]['open_dic']['openHour'], data[building]['open_dic']['openMin'], data[building]['open_dic']['openSec'])
        end = datetime.time(data[building]['close_dic']['closeHour'], data[building]['close_dic']['closeMin'], data[building]['close_dic']['closeSec'])
        
        if curr_time > start and curr_time < end:
            return 1
        else:
            return 0 
    else:
        print("No such building found")
        return -1

def checkBuildHours(building):
    with open('build_info.json') as json_file:
        data = json.load(json_file)
    data = {k.lower(): v for k, v in data.items()}
    if building in data.keys():
        type = data[building]['type']
        if type == 'appointment':
            return building + " only works by appointment today "
        else:
            start_hour = data[building]['open_dic']['openHour']
            start_minute = data[building]['open_dic']['openMin']
            if start_hour > 12:
                start_hour_format = start_hour - 12
            else:
                start_hour_format = start_hour
            if start_minute == 0:
                start = str(start_hour_format) + " o'clock"
            else:
                start = str(start_hour_format) + ' ' + str(start_minute)
            if start_hour < 12:
                start = start + " A M"
            elif start_hour >= 12:
                start = start + " P M"    
            end_hour = data[building]['close_dic']['closeHour']
            end_minute = data[building]['close_dic']['closeMin']
            if end_hour > 12:
                end_hour_format = end_hour - 12
            else:
                start_hour_format = start_hour
            if end_minute == 0:
                end = str(end_hour_format) + " o'clock"
            else:
                end = str(end_hour_format) + ' ' + str(end_minute)
            if end_hour < 12:
                end = end + " A M"
            elif end_hour >= 12:
                end = end + " P M"
            output = building + " opens at " + start + " and closes at " + end
            if type == "interruptions":
                return output + " with possible interruptions, like lunch break"
            else:
                return output
    else:
        print("No such building found")
        return "-1"