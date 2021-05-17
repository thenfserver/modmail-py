# What is modmail?
Modmail is a way that server members can report members to the staff team if they're breaking the rules or just asking general questions about the server.

# What is the modmail bot?
Modmail is a basic modmail bot written in python for the [NFREALMUSIC](discord.gg) discord server, but the code can be changed to work in any server.

# How do I make it work in my server?

1. [Install python](https://python.org/).
2. Install discord.py by opening your terminal and typing `pip3 install discord` on linux and mac or `pip install discord` on windows.
3. [Create a bot application](https://discord.com/developers/docs/game-sdk/applications)
4. *[Click here if you need further help making the bot application](https://discordpy.readthedocs.io/en/stable/discord.html).*
5. Invite the bot to the server you want the modmail.
6. After you made the bot application copy the bot's token and paste it in the `mainy.py` file where it says `TOKEN_HERE`.
7. Then go the bot `modmail.py` file and replace `GUILD_ID_HERE` with the guild id of the server and the channel id where it says `CHANNEL_ID_HERE`.

After this you should have a working modmail bot, if you run into issues dm me on discord bread#2716.
