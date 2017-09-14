import shelve
from pprint import pprint
from kanto import kanto

players_locations = shelve.open('locations')
players_locations['kanto'] = {}
kanto_dic = players_locations['kanto']
for kanto_room in kanto.keys():
    print(kanto_room)
    kanto_dic[kanto_room] = {}
players_locations['kanto'] = kanto_dic
pprint(players_locations['kanto'])
