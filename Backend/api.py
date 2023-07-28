import requests
from bs4 import BeautifulSoup
import json

response = requests.get("https://www.espn.com/nfl/teams").text
soup = BeautifulSoup(response,'lxml')
teams = soup.find('div', class_='layout is-split')
statistics_url = []

for link in teams.findAll('a', {'class': 'AnchorLink'}):
    try:
        stats_url = link['href'].split('/')
        #print(stats_url)
        if('stats' in stats_url):
            statistics_url.append(link['href'])

    except KeyError:
        pass

for team in statistics_url:
    url = "https://espn.com" + team 
    team_url = requests.get(url).text
    stats = BeautifulSoup(team_url, 'lxml')
    yards = stats.find('div', class_='Wrapper Card__Content')
    
    team_city = stats.find('div', class_='StickyContainer').find('span', class_='db pr3 nowrap').text
    team_mascot = stats.find('div', class_='StickyContainer').find('span', class_='db fw-bold').text
    team_name = team_city + " " + team_mascot

    ############################################################################
    passing_stats   = yards.find('div',class_='ResponsiveTable ResponsiveTable--fixed-left mt5 remove_capitalize')
    passing_stats = passing_stats.find('div', class_='flex')
    qb_name = passing_stats.find('tr', class_='Table__TR Table__TR--sm Table__even').text.split('QB ')
    passing_stats_table = yards.find('div', class_='Table__ScrollerWrapper relative overflow-hidden').find('tr',class_='Table__TR Table__TR--sm Table__even')
    pretty_passing = json.dumps(passing_stats, indent=4)

    ############################################################################
    rushing_stats_table = yards.find_all('div', class_='ResponsiveTable ResponsiveTable--fixed-left mt5 remove_capitalize')[1]
    
    rushing_numbers = rushing_stats_table.find('div', class_='Table__Scroller')
    rushing_numbers = rushing_numbers.find('tbody', class_='Table__TBODY')
    rushing_numbers = rushing_numbers.find('tr',class_="Table__TR Table__TR--sm Table__even")
    pretty_rushing = json.dumps(rushing_stats, indent=4)

    ############################################################################
    receiving_stats_table = yards.find_all('div', class_='ResponsiveTable ResponsiveTable--fixed-left mt5 remove_capitalize')[2]
    receiving_numbers = receiving_stats_table.find('div', class_='Table__Scroller')
    receiving_numbers = receiving_numbers.find('tbody', class_='Table__TBODY')
    receiving_numbers = receiving_numbers.find('tr',class_="Table__TR Table__TR--sm Table__even")
    pretty_receiving = json.dumps(rec_stats, indent=4)

    passing_stats = {
                        'name'          : qb_name,
                        'games_played'  : passing_stats_table.findAll('td', class_='Table__TD')[0].text,
                        'completions'   : passing_stats_table.findAll('td', class_='Table__TD')[1].text,
                        'attempts'      : passing_stats_table.findAll('td', class_='Table__TD')[2].text,
                        'completion_%'  : passing_stats_table.findAll('td', class_='Table__TD')[3].text + "%",
                        'season_yards'  : passing_stats_table.findAll('td', class_='Table__TD')[4].text,
                        'avg'           : passing_stats_table.findAll('td', class_='Table__TD')[5].text,
                        'yards/g'       : passing_stats_table.findAll('td', class_='Table__TD')[6].text,
                        'longest_pass'  : passing_stats_table.findAll('td', class_='Table__TD')[7].text,
                        'touchdowns'    : passing_stats_table.findAll('td', class_='Table__TD')[8].text,
                        'interceptions' : passing_stats_table.findAll('td', class_='Table__TD')[9].text,
                        'sacks'         : passing_stats_table.findAll('td', class_='Table__TD')[10].text,
                        'qb_rating'     : passing_stats_table.findAll('td', class_='Table__TD')[12].text

                    }
    
    rushing_stats   = {
                        'name'         : rushing_stats_table.find_all('a', class_='AnchorLink')[0].text,
                        'games_played' : rushing_numbers.find_all('td', class_='Table__TD')[0].text,
                        'carries'      : rushing_numbers.find_all('td', class_='Table__TD')[1].text,
                        'yards'        : rushing_numbers.find_all('td', class_='Table__TD')[2].text,
                        'avg/att'      : rushing_numbers.find_all('td', class_='Table__TD')[3].text,
                        'longest_run'  : rushing_numbers.find_all('td', class_='Table__TD')[4].text,
                        '20+yard_runs' : rushing_numbers.find_all('td', class_='Table__TD')[5].text,
                        'touchdowns'   : rushing_numbers.find_all('td', class_='Table__TD')[6].text,
                        'yards/game'   : rushing_numbers.find_all('td', class_='Table__TD')[7].text,
                        'fumbles'      : rushing_numbers.find_all('td', class_='Table__TD')[8].text,
                        'fumbles_lost' : rushing_numbers.find_all('td', class_='Table__TD')[9].text,
                        'first_downs'  :rushing_numbers.find_all('td', class_='Table__TD')[10].text,


                        }
    

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
    '''print(team_name)
    print()
    print(pretty_passing)
    print()
    print(pretty_rushing)
    print()
    print(pretty_receiving)'''
'''defense_stats   = {}
scoring_stats   = {}
returning_stats = {}
kicking_stats   = {}
punting_stats   = {}'''


