# What is modmail?

Modmail is a basic modmail bot written in python for the (discord.gg)[NFREALMUSIC] discord server, but the code can be changed to work in any server.

# How do I make it work in my server?

1. [Install python](https://python.org/).
2. Install discord.py by opening your terminal and typing `pip3 install discord` on linux and mac or `pip install discord` on windows.
3. [https://discord.com/developers/docs/game-sdk/applications](Create a bot application)
*If you need further help creating a bot application check out https://discordpy.readthedocs.io/en/stable/discord.html.*
4. Invite the bot to the server you want the modmail.
4. After you made the bot application copy the bot's token and paste it in the `mainy.py` file where it says `TOKEN_HERE`.
5. Then go the bot `modmail.py` file and replace `GUILD_ID_HERE` with the guild id of the server and the channel id where it says `CHANNEL_ID_HERE`.

After this you should have a working modmail bot, if you run into issues dm me on discord bread#2716.
