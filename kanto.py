from classes import Room

kanto = {}
kanto['pallet_town'] = Room(
    "Pallet Town", "You just moved here, there is your house, along with other three.\nA route starts from the north.", 'route1', None, None, None, None, None)
kanto['route1'] = Room("Route 1", "Route from Pallet Town to Viridian City.",
                       None, 'pallet_town', None, None, None, None)
