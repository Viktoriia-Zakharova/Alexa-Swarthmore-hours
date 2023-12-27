from buildingFuncs import checkBuildHours
import json
import datetime

#This file is used for testing purposes .
def main():
    print("hello world")
    #dict = {}
    #print(checkBuildHours("BCC"))
    '''
    with open('hours.json') as json_file:
        data = json.load(json_file)
    for x in data:
        building = Building(x['name'], x['type'])
        building.set_open(x['open']['hour'], x['open']['minute'], x['open']['second'])
        building.set_close(x['close']['hour'], x['close']['minute'], x['close']['second'])
        dict[x['name']] = building
    print(dict['Bookstore'].get_end())
    '''
    curr_time = datetime.datetime.now().time()
    print(checkBuildHours('bookstore'))
    print(checkBuildHours('friends historical library'))
    print(checkBuildHours('media center'))
    print(checkBuildHours('career services'))

'''
{
          "name": "HelloWorldIntent",
          "slots": [],
          "samples": [
            "hello",
            "how are you",
            "say hi world",
            "say hi",
            "hi",
            "say hello world",
            "say hello"
          ]
        },'''


main()
