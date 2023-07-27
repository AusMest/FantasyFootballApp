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
#print(statistics_url[0])
#for team in statistics_url:
url = "https://espn.com" + statistics_url[0]
    #print(url)
team_url = requests.get(url).text
stats = BeautifulSoup(team_url, 'lxml')
#print(stats.prettify())
yards = stats.find('div', class_='Wrapper Card__Content')
#print(yards.prettify())

passing_stats   = yards.find('div',class_='ResponsiveTable ResponsiveTable--fixed-left mt5 remove_capitalize')
passing_stats = passing_stats.find('div', class_='flex')
#print(passing_stats.prettify())
qb_name = passing_stats.find('tr', class_='Table__TR Table__TR--sm Table__even').text.split('QB ')
passing_stats_table = yards.find('div', class_='Table__ScrollerWrapper relative overflow-hidden').find('tr',class_='Table__TR Table__TR--sm Table__even')

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
pretty_dict = json.dumps(passing_stats, indent=4)
print(pretty_dict)
rushing_stats   = {}
rec_stats       = {}
defense_stats   = {}
scoring_stats   = {}
returning_stats = {}
kicking_stats   = {}
punting_stats   = {}


