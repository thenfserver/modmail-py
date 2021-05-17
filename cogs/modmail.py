import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class modmail(commands.Cog):
    mod_role = None
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
      if message.author.id == self.client.user.id:
        return
        
      if message.author != message.author.bot:
        if not message.guild:
          embed = discord.Embed(title="Message Received", description=message.content,color=discord.Color.red(),timestamp=message.created_at)
          embed.set_author(name=f"{message.author}", icon_url=message.author.avatar_url)
          embed.set_footer(text=f"{message.author} | {message.author.id}")
          await self.client.get_guild(475869084169273344).get_channel(764315204422991882).send(embed=embed)
          
          embed=discord.Embed(title="Message Sent", description=message.content, color=discord.Color.green(), timestamp=message.created_at)
          await message.author.send(embed=embed)

def setup(bot):
    bot.add_cog(modmail(bot))
