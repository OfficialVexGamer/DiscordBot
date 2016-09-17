from queue import Queue

voice = None
player = None
old_vol = 1.0
queue = Queue()


def add_queue(url):
    queue.put(url)
    print(url + " to music queue")


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
