import requests
import urllib.parse
from pprint import pprint
import secrety

def getStats(platform, name):

    apexStats = requests.get(f'https://public-api.tracker.gg/v2/apex/standard/profile/{platform}/{name}', headers = {'TRN-API-key': secrety.my_api_key['TRN-Api-Key']})
    # Your personal API key goes in as the value of 'TRN-API-key'

    apexStats = apexStats.json()

    relevant_stats = {}

    try:
        apexStats['data']
    except:
        return ('User not Found')
        exit()

    relevant_stats['Featured Legend'] = apexStats['data']['metadata']['activeLegendName']
    relevant_stats['Level'] = apexStats['data']['segments'][0]['stats']['level']['value']
    relevant_stats['Kills'] = apexStats['data']['segments'][0]['stats']['kills']['value']

    try:
        relevant_stats['Winning Kills'] = apexStats['data']['segments'][0]['stats']['winningKills']['value']
    except:
        relevant_stats['Winning Kills'] = 'Winning Kills not shown by User'
        del relevant_stats['Winning Kills']

    try:
        relevant_stats['Damage Done'] = apexStats['data']['segments'][0]['stats']['damage']['value']
    except:
        relevant_stats['Damage Done'] = 'Damage Done not shown by User'
        del relevant_stats['Damage Done']

    try:
        relevant_stats['Headshots'] = apexStats['data']['segments'][0]['stats']['headshots']['value']
    except: 
        relevant_stats['Headshots'] = 'Headshots not shown by User'
        del relevant_stats['Headshots']

    try:
        relevant_stats['Finishers'] = apexStats['data']['segments'][0]['stats']['finishers']['value']
    except: 
        relevant_stats['Finishers'] = 'Finishers not shown by User'
        del relevant_stats['Finishers']

    try:
        relevant_stats['Revives'] = apexStats['data']['segments'][0]['stats']['revives']['value']
    except: 
        relevant_stats['Revives'] = 'Revives not shown by User'
        del relevant_stats['Revives']

    try:
        relevant_stats['Wins With Full Squad'] = apexStats['data']['segments'][0]['stats']['winsWithFullSquad']['value']
    except: 
        relevant_stats['Wins With Full Squad'] = 'Wins With Full Squad not shown by User'
        del relevant_stats['Wins With Full Squad']

    try:
        relevant_stats['Season Damage'] = apexStats['data']['segments'][0]['stats']['seasonDamage']['value']
    except: 
        relevant_stats['Season Damage'] = 'Season Damage not shown by User'
        del relevant_stats['Season Damage']

    try:
        relevant_stats['Matches Played'] = apexStats['data']['segments'][0]['stats']['matchesPlayed']['value']
    except: 
        relevant_stats['Matches Played'] = 'Matches Played not shown by User'
        del relevant_stats['Matches Played']

    try:
        relevant_stats['Shotgun Kills'] = apexStats['data']['segments'][0]['stats']['shotgunKills']['value']
    except: 
        relevant_stats['Shotgun Kills'] = 'Shotgun Kills not shown by User'
        del relevant_stats['Shotgun Kills']

    try:
        relevant_stats['SMG Kills'] = apexStats['data']['segments'][0]['stats']['smgKills']['value']
    except: 
        relevant_stats['SMG Kills'] = 'SMG Kills not shown by User'
        del relevant_stats['SMG Kills']

    try:
        relevant_stats['Sniper Kills'] = apexStats['data']['segments'][0]['stats']['sniperKills']['value']
    except: 
        relevant_stats['Sniper Kills'] = 'Sniper Kills not shown by User'
        del relevant_stats['Sniper Kills']

    return relevant_stats
    
