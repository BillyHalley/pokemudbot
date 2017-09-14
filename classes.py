class Room:
    def __init__(self, shortdescription, description, n, s, e, w, u, d):
        self.shortdescription = shortdescription
        self.description = description
        self.n = n
        self.s = s
        self.e = e
        self.w = w
        self.u = u
        self.d = d
        self.players_list = {}
