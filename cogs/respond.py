import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class respond(commands.Cog):
    mod_role = None
    def __init__(self, client):
        self.client = client

    @commands.command()
    @has_permissions(manage_messages=True)
    async def respond(self, ctx, member: discord.Member=None, *, context):
      embed = discord.Embed(title="Message Received", description=context, color=discord.Color.red())
      embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar_url)
      embed.set_footer(text=f"{ctx.author} | {ctx.author.id}")
      await member.send(embed=embed)
      embed=discord.Embed(title="Message Sent", description=context, color=discord.Color.green())
      embed.set_author(name=f"Sent to {member}", icon_url=member.avatar_url)
      embed.set_footer(text=f"Sent by {ctx.author} | {ctx.author.id}")
      await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(respond(bot))
