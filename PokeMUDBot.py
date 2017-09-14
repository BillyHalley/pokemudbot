import telepot
from telepot.loop import MessageLoop
import time
import shelve
from os.path import join
from os.path import exists
from datetime import datetime
from kanto import kanto

token_file = open('.token', 'r')
TOKEN = token_file.read()
bot = telepot.Bot(TOKEN)


def p_register(p_shelve, name):
    time = str(datetime.now())[:-7]
    player_info = {'name': name, 'time': time}
    p_shelve['info'] = player_info
    belt = {}
    for i in range(6):
        belt['slot' +
             str(i + 1)] = {}
    p_shelve['belt'] = belt
    player_pc = {}
    for i in range(30):
        index = str(i + 1)
        if len(index) == 1:
            index = "0" + index
        player_pc['box' + index] = {}
    p_shelve['pc'] = player_pc
    # TODO different professors for each region
    p_shelve['location'] = {'region': 'kanto', 'room': 'pallet_town'}
    pokedex = {}
    for i in range(802):
        index = str(i + 1)
        if len(index) == 1:
            index = "00" + index
        elif len(index) == 2:
            index = "0" + index
        pokedex[index] = {'seen': False, 'caught': False}
    # TODO different regions pokedex
    p_shelve['pokedex'] = pokedex
    # bag
    # badges
    # journal
    # friends


def list_users():
    users = {}


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    def print_room(room):
        bot.sendMessage(
            chat_id, room.shortdescription + "\n" + room.description)

    p_path = join("players", "p_" + str(chat_id))

    if content_type == 'text':
        txt = msg['text']
        if not exists(p_path):
            if '/start' in txt:
                bot.sendMessage(
                    chat_id, "Welcome to PokeMUD! Let's create your character!")
                bot.sendMessage(chat_id, "To register type /register Name")
            if '/register' in txt:
                with shelve.open(p_path) as p_shelve:
                    p_register(p_shelve, txt[10:])
        else:
            p_shelve = shelve.open(p_path)
            location = p_shelve['location']
            room = kanto[location['room']]
            if '/player' in txt:
                bot.sendMessage(
                    chat_id, "Name: " + p_shelve['info']['name'])
            elif '/location' in txt:
                print_room(room)
            elif txt == '/north':
                if room.n is not None:
                    location['room'] = room.n
                    print_room(kanto[location['room']])
                else:
                    bot.sendMessage(chat_id, "Sorry, you can't go that way")
            elif txt == '/south':
                if room.s is not None:
                    location['room'] = room.s
                    print_room(kanto[location['room']])
                else:
                    bot.sendMessage(chat_id, "Sorry, you can't go that way")
            elif txt == '/east':
                if room.e is not None:
                    location['room'] = room.e
                    print_room(kanto[location['room']])
                else:
                    bot.sendMessage(chat_id, "Sorry, you can't go that way")
            elif txt == '/west':
                if room.w is not None:
                    location['room'] = room.w
                    print_room(kanto[location['room']])
                else:
                    bot.sendMessage(chat_id, "Sorry, you can't go that way")
            elif txt == '/up':
                if room.u is not None:
                    location['room'] = room.u
                    print_room(kanto[location['room']])
                else:
                    bot.sendMessage(chat_id, "Sorry, you can't go that way")
            elif txt == '/down':
                if room.d is not None:
                    location['room'] = room.d
                    print_room(kanto[location['room']])
                else:
                    bot.sendMessage(chat_id, "Sorry, you can't go that way")

            p_shelve['location'] = location
            p_shelve.close()

    # if content_type == 'text':
    #     txt = msg['text']

    #     s = shelve.open("players/" + str(chat_id))

    #     if "/name" in txt:
    #         s['name'] = txt.split(" ")[1]
    #         bot.sendMessage(chat_id, "So, your name is " + s['name'])
    #         bot.sendMessage(
    #             chat_id, "Are you a boy or a girl?\nUse /male or /female")
    #     if "/male" in txt:
    #         bot.sendMessage(chat_id, "So, you're a boy!")
    #         s['gender'] = 'Male'
    #         bot.sendMessage(
    #             chat_id, "Select your starter\nUse /starter PokemonName")
    #     if "/female" in txt:
    #         bot.sendMessage(chat_id, "So, you're a girl!")
    #         s['gender'] = 'Female'
    #         bot.sendMessage(
    #             chat_id, "Select your starter\nUse /starter PokemonName")
    #     if "/starter" in txt:
    #         name = txt.split(" ")[1]
    #         bot.sendPhoto(chat_id, 'https://img.pokemondb.net/artwork/' +
    #                       name.lower() + '.jpg', "So, you chose " + name + "!")
    #         s['pokemon'] = name
    #         bot.sendMessage(
    #             chat_id, "Your character is complete, use /player to list your informations")

    #     if "/player" in txt:
    #         bot.sendMessage(chat_id, "Your name is: " +
    #                         s['name'] + "\nYou are a: " + s['gender'] + "\nYou chose: " + s['pokemon'])

    #     s.close()


MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
