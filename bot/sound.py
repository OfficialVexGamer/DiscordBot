from queue import Queue

import discord
import youtube_dl

voice = None
player = None
old_vol = 1.0
queue = Queue()


def add_queue(url: str):
    queue.put(url)


def change_vol(vol_add: int):
    global old_vol

    old_vol = vol_add

    if player:
        player.volume = old_vol


def clear_queue():
    while not queue.empty():
        queue.get()  # run out of queue items, there is probably a better way


def get_snd_mins(in_secs: int):
    m, s = divmod(in_secs, 60)
    h, m = divmod(m, 60)

    return "%s:%s:%s" % (h, m, s)


async def play(client: discord.Client, message: discord.Message, music_chan: str):
    global player

    try:
        player = await voice.create_ytdl_player(queue.get())
        for chan in message.server.channels:
            if chan.name == music_chan:
                await client.send_message(chan, """```""" + player.title + """
by """ + player.uploader + """ (""" + get_snd_mins(player.duration) + """)
""" + str(queue.qsize()) + """ songs left.```""")
                break

        player.volume = old_vol
        player.start()

        await client.change_status(game=discord.Game(name=player.title))
    except youtube_dl.utils.DownloadError as e:
        for chan in message.server.channels:
            if chan.name == music_chan:
                await client.send_message(chan, """```""" + str(e)[len("[0;31mERROR:[0m aaaaaaaaaaa: YouTube said:  "):] + """"```""")
                break