import config
import json, urllib.request
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from datetime import datetime



# rows = []
# for member in members.values():
#     row = [member['name'], member['local_score']]
#     if member['name'] is None:
#         row[0] = member['id']
#     rows.append(row)
# print(tabulate(rows, headers=['name', 'score']))

def get_star_time(member, date, part):
    try:   
        time = datetime.fromtimestamp(int(member['completion_day_level'][str(date)][str(part)]['get_star_ts'])).strftime('%m/%d    %H:%M:%S')
        return time
    except:
        return None

def nonesorter(a):
    if not a:
        return 'Incomplete'
    return a

def print_day_ranking(day, members):
    '''Print out the times for each person for a specific day'''
    rows = sorted([[member['name'] or '(#'+member['id']+')', 
                    get_star_time(member, day, 1), 
                    get_star_time(member, day, 2)]  
                   for member in members.values()], key=lambda row: nonesorter(row[2]))
    print(tabulate(rows, headers=['Day '+str(day), 'Part 1', 'Part 2'], tablefmt='simple'))
    print('\n\n')



leaderboard_url = config.leaderboard_url

webpage = requests.get(leaderboard_url, cookies={'session':config.session_cookie}).text
leaderboard_json = json.loads(webpage)

members = leaderboard_json['members']

for day in range(1, 6):
    print_day_ranking(day, members)



