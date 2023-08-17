from flask import render_template
from flask import Flask,request
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS
from collections import defaultdict
import json
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
 'Accept-Language': 'en-US,en;q=0.9',
 'Accept-Encoding': 'gzip, deflate, br'}

app = Flask(__name__)
CORS(app)
response = requests.get("https://www.espn.com/nfl/teams",headers=headers).text
soup = BeautifulSoup(response,'lxml')
if(soup):
    print("made it")
#print(soup)
teams = soup.find('div', class_='layout is-split')

statistics_url = []

for link in teams.findAll('a', class_= 'AnchorLink'):
    try:
        stats_url = link['href'].split('/')
        #print(stats_url)
        if('stats' in stats_url):
            statistics_url.append(link['href'])

    except KeyError:
        pass
#print(statistics_url)
##this is where the stats page magic happens
count = 0
passing_table = defaultdict(list)
rushing_table = defaultdict(list)
rec_table = defaultdict(list)
defense_table = defaultdict(list)
for team in statistics_url:
    url = "https://espn.com" + team 
    team_url = requests.get(url,headers=headers).text
    #print(team_url)
    #print(team_url)
    stats = BeautifulSoup(team_url, 'lxml')
    yards = stats.find('div', class_='Wrapper Card__Content')
    #print(yards)
    #team_city = stats.find('div', class_='StickyContainer').find('span', class_='db pr3 nowrap').text
    #team_mascot = stats.find('div', class_='StickyContainer').find('span', class_='db fw-bold').text
    #team_name = team_city + " " + team_mascot
    ## for each playyer in each table:
    ############################################################################
    passing_stats   = yards.find('div',class_='ResponsiveTable ResponsiveTable--fixed-left mt5 remove_capitalize')
    passing_stats = passing_stats.find('div', class_='flex')
    qb_name = passing_stats.find('tr', class_='Table__TR Table__TR--sm Table__even').text.split('QB ')
    passing_stats_table = yards.find('div', class_='Table__ScrollerWrapper relative overflow-hidden').find('tr',class_='Table__TR Table__TR--sm Table__even')
    #print(passing_stats_table)

    ############################################################################
    rushing_stats_table = yards.find_all('div', class_='ResponsiveTable ResponsiveTable--fixed-left mt5 remove_capitalize')[1]
    rushing_numbers = rushing_stats_table.find('div', class_='Table__Scroller')
    rushing_numbers = rushing_numbers.find('tbody', class_='Table__TBODY')
    rushing_numbers = rushing_numbers.find('tr',class_="Table__TR Table__TR--sm Table__even")
    #

    ############################################################################
    receiving_stats_table = yards.find_all('div', class_='ResponsiveTable ResponsiveTable--fixed-left mt5 remove_capitalize')[2]
    receiving_numbers = receiving_stats_table.find('div', class_='Table__Scroller')
    receiving_numbers = receiving_numbers.find('tbody', class_='Table__TBODY')
    receiving_numbers = receiving_numbers.find('tr',class_="Table__TR Table__TR--sm Table__even")
    #

    ############################################################################
    defense_stats_table = yards.find_all('div', class_='ResponsiveTable ResponsiveTable--fixed-left mt5 remove_capitalize')[3]
    defense_numbers = defense_stats_table.find('div', class_='Table__Scroller')
    defense_numbers = defense_numbers.find('tbody', class_='Table__TBODY')
    defense_numbers = defense_numbers.find('tr',class_="Table__TR Table__TR--sm Table__even")
    
    
    passing_stats = {
                        'name'          : qb_name,
                        'games_played'  : passing_stats_table.findAll('td', class_='Table__TD')[0].text,
                        'completions'   : passing_stats_table.findAll('td', class_='Table__TD')[1].text,
                        'attempts'      : passing_stats_table.findAll('td', class_='Table__TD')[2].text,
                        'completion_per'  : passing_stats_table.findAll('td', class_='Table__TD')[3].text + "%",
                        'season_yards'  : passing_stats_table.findAll('td', class_='Table__TD')[4].text,
                        'avg'           : passing_stats_table.findAll('td', class_='Table__TD')[5].text,
                        'yards_per_game': passing_stats_table.findAll('td', class_='Table__TD')[6].text,
                        'longest_pass'  : passing_stats_table.findAll('td', class_='Table__TD')[7].text,
                        'touchdowns'    : passing_stats_table.findAll('td', class_='Table__TD')[8].text,
                        'interceptions' : passing_stats_table.findAll('td', class_='Table__TD')[9].text,
                        'sacks'         : passing_stats_table.findAll('td', class_='Table__TD')[10].text,
                        'qb_rating'     : passing_stats_table.findAll('td', class_='Table__TD')[12].text

                    }
    #print(passing_stats)
    passing_table[count].append(passing_stats)
    
    rushing_stats   = {
                        'name'         : rushing_stats_table.find_all('a', class_='AnchorLink')[0].text,
                        'games_played' : rushing_numbers.find_all('td', class_='Table__TD')[0].text,
                        'carries'      : rushing_numbers.find_all('td', class_='Table__TD')[1].text,
                        'yards'        : rushing_numbers.find_all('td', class_='Table__TD')[2].text,
                        'avg_att'      : rushing_numbers.find_all('td', class_='Table__TD')[3].text,
                        'longest_run'  : rushing_numbers.find_all('td', class_='Table__TD')[4].text,
                        'twenty_yard_runs' : rushing_numbers.find_all('td', class_='Table__TD')[5].text,
                        'touchdowns'   : rushing_numbers.find_all('td', class_='Table__TD')[6].text,
                        'yards_game'   : rushing_numbers.find_all('td', class_='Table__TD')[7].text,
                        'fumbles'      : rushing_numbers.find_all('td', class_='Table__TD')[8].text,
                        'fumbles_lost' : rushing_numbers.find_all('td', class_='Table__TD')[9].text,
                        'first_downs'  :rushing_numbers.find_all('td', class_='Table__TD')[10].text,


                        }
    rushing_table[count].append(rushing_stats)
    

    rec_stats       = {
                        'name'             : receiving_stats_table.find_all('a', class_='AnchorLink')[0].text,
                        'games_played'     : receiving_numbers.find_all('td', class_='Table__TD')[0].text,
                        'receptions'       : receiving_numbers.find_all('td', class_='Table__TD')[1].text,
                        'targets'          : receiving_numbers.find_all('td', class_='Table__TD')[2].text,
                        'yards'            : receiving_numbers.find_all('td', class_='Table__TD')[3].text,
                        'average'          : receiving_numbers.find_all('td', class_='Table__TD')[4].text,
                        'touchdowns'       : receiving_numbers.find_all('td', class_='Table__TD')[5].text,
                        'longest_catch'    : receiving_numbers.find_all('td', class_='Table__TD')[6].text,
                        '20+yard_catches'  : receiving_numbers.find_all('td', class_='Table__TD')[7].text,
                        'yards/game'       : receiving_numbers.find_all('td', class_='Table__TD')[8].text,
                        'fumbles'          : receiving_numbers.find_all('td', class_='Table__TD')[9].text,
                        'fumbles_lost'     : receiving_numbers.find_all('td', class_='Table__TD')[10].text,
                        'yards_after_catch': receiving_numbers.find_all('td', class_='Table__TD')[11].text,
                        'first_downs'      : receiving_numbers.find_all('td', class_='Table__TD')[12].text
                        }
    rec_table[count].append(rec_stats)
    
    '''for key, value in passing_stats.items():             use this for future reference on how to 
                                                            use specific stats if need be
        if key == 'name':
            print(value)
    for key, value in rushing_stats.items():
        if key == 'name':
            print(value)
    for key, value in rec_stats.items():
        if key == 'name':
            print(value)'''
    
    defense_stats   = {
                        'name'             : defense_stats_table.find_all('a', class_='AnchorLink')[0].text,
                        'games_played'     : defense_numbers.find_all('td', class_='Table__TD')[0].text,
                        'tackles_solo'     : defense_numbers.find_all('td', class_='Table__TD')[1].text,
                        'tackles_assisted' : defense_numbers.find_all('td', class_='Table__TD')[2].text,
                        'tackles_total'    : defense_numbers.find_all('td', class_='Table__TD')[3].text,
                        'sacks'            : defense_numbers.find_all('td', class_='Table__TD')[4].text,
                        'tackles_for_loss' : defense_numbers.find_all('td', class_='Table__TD')[6].text,
                        'passes_defended'  : defense_numbers.find_all('td', class_='Table__TD')[7].text,
                        'interceptions'    : defense_numbers.find_all('td', class_='Table__TD')[8].text,
                        'pick_six'         : defense_numbers.find_all('td', class_='Table__TD')[11].text,
                        'forced_fumbles'   : defense_numbers.find_all('td', class_='Table__TD')[12].text,
                        'fumble_recoveries': defense_numbers.find_all('td', class_='Table__TD')[13].text,
                        'fumble_touchdowns': defense_numbers.find_all('td', class_='Table__TD')[14].text


    }
    defense_table[count].append(defense_stats)
    #print(count)
    count = count + 1
'''
scoring_stats   = {}
returning_stats = {}
kicking_stats   = {}
punting_stats   = {}'''
#print(passing_table)
pretty_passing = json.dumps(passing_table, indent=4)
pretty_defense = json.dumps(defense_table, indent=4)
pretty_rushing = json.dumps(rushing_table, indent=4)
pretty_receiving = json.dumps(rec_table, indent=4)
#print(type(passing_table))
@app.route('/')
def home():
    return pretty_passing
    #return '{} {} {} {}'.format(pretty_passing,pretty_defense,pretty_rushing,pretty_receiving)
@app.route('/runners')
def runners():
    return pretty_rushing
if __name__ == "__main__": 
    app.run(port=5000,debug=True)
#print(team_name)
'''print()
print(pretty_passing)
print()
print(pretty_rushing)
print()
print(pretty_receiving)
print()
print(pretty_defense)'''