# DiscordBot
A (badly written) Discord bot. It does admin stuff and music

##Installation (Requires Python 3)
1. Clone repo
2. `pip3 install -r requirements.txt`
3. Copy `config_template.yml` as `config.yml` and edit it to your liking
4. *(optional)* populate images/ and symlink them to a web hosting folder (images will not be uploaded, but instead will get posted as a link)
5. Install the following in your Linux distro's package manager (I only support Linux, but it will work on Windows (my dev env) too!)
 - ffmpeg
 - libopus
6. Configure your Discord group
7. `python3 bot_start.py`
