from queue import Queue

import discord
import youtube_dl

voice = list()
player = list()
old_vol = list()
queue = list()


def mk_server_queue(id: str):
    queue[id] = Queue()


def add_queue(id: str, url: str):
    queue[id].put(url)


def change_vol(id: str, vol_add: float):
    global old_vol

    old_vol[id] = vol_add

    if player[id]:
        player[id].volume = old_vol[id]


def clear_queue(id: str):
    while not queue[id].empty():
        queue[id].get()  # run out of queue items, there is probably a better way


def get_snd_mins(in_secs: int):
    m, s = divmod(in_secs, 60)
    h, m = divmod(m, 60)

    return "%s:%s:%s" % (h, m, s)


async def play(id: str, client: discord.Client, message: discord.Message, music_chan: str):
    global player

    try:
        player[id] = await voice[id].create_ytdl_player(queue[id].get())
        for chan in message.server.channels:
            if chan.name == music_chan:
                await client.send_message(chan, """```""" + player[id].title + """
by """ + player.uploader + """ (""" + get_snd_mins(player[id].duration) + """)
""" + str(queue[id].qsize()) + """ songs left.```""")
                break

        player.volume = old_vol
        player.start()
    except youtube_dl.utils.DownloadError as e:
        for chan in message.server.channels:
            if chan.name == music_chan:
                await client.send_message(chan, """```""" + str(e)[len("[0;31mERROR:[0m aaaaaaaaaaa: YouTube said:  "):] + """"```""")
                break
