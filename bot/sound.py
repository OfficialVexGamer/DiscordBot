from queue import Queue

voice = None
player = None
old_vol = 1.0
queue = Queue()


def add_queue(url):
    queue.put(url)


def change_vol(vol_add):
    global old_vol

    old_vol = vol_add

    if player:
        player.volume = old_vol


def clear_queue():
    while not queue.empty():
        queue.get()  # run out of queue items, there is probably a better way


def get_snd_mins(in_secs):
    m, s = divmod(in_secs, 60)
    h, m = divmod(m, 60)

    return "%s:%s:%s" % (h, m, s)


async def play(client, message):
    global player

    player = await voice.create_ytdl_player(queue.get())
    await client.send_message(message.channel, """```""" + player.title + """
by """ + player.uploader + """ (""" + get_snd_mins(player.duration) + """)```""")

    player.volume = old_vol
    player.start()
