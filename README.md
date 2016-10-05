# DiscordBot
A (badly written) Discord bot. It does admin stuff and music

##Add to your server
1. Go to https://admi.ml/a2RLx (or to https://admi.ml/ApURo for the test version that only gets online when i'm testing it)
2. Select your server
3. Configure bot
4. Profit!

##Installation (Requires Python 3)
1. Clone repo
2. `pip3 install -r requirements.txt`
3. Copy `config_template.yml` as `config.yml` and edit it to your liking
4. Install the following
 - ffmpeg
 - libopus
5. Configure your Discord group
6. `python3 bot_start.py`


##Commands
Do `!help` in your server while the bot is running.

##Configuration
You can configure the bot using the `!conf <key> <value>` command. The keys and defaults can be found [here](/conf/_template.yml). Lists are seperated using commas (without spaces) (ex. `!conf admin_roles Admin,Moderator,Developer`)
