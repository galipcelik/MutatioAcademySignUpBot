import discord
from discord.ext import commands
from environments import *
from buttons import *


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix="!!", intents=discord.Intents.all(), application_id=1012242115604004874)

    async def setup_hook(self):
        await self.load_extension(f"test")
        await self.load_extension(f"command")
        await bot.tree.sync(guild=discord.Object(id=1009896590128984064))

    async def on_ready(self):
        await print_info(bot_user_name=self.user.name, bot_user_id=bot.user.id, bot_get_all_members=self.get_all_members())

    async def on_command_error(self, ctx, error):
        await ctx.channel.purge(limit=1)
        await ctx.send("An error occurred.", delete_after=7)
        await ctx.send("The Error Message is:", delete_after=7)
        await ctx.send(error, delete_after=10)

    async def on_member_join(self, member):

        try:

            with open("members.json", "r") as doc:
                members = json.load(doc)

            if str(member.id) in members:
                return

            else:

                try:
                    text_tr = f"{texter('tr', '1')}\n{texter('tr', '2')}\n{texter('tr', '3')}"
                    text_gb = f"{texter('gb', '1')}\n{texter('gb', '2')}\n{texter('gb', '3')}"
                    text_cp = f"{texter('cp', '1')}\n{texter('cp', '2')}\n{texter('cp', '3')}"
                    text_es = f"{texter('es', '1')}\n{texter('es', '2')}\n{texter('es', '3')}"
                    text_de = f"{texter('de', '1')}\n{texter('de', '2')}\n{texter('de', '3')}"
                    await member.send(text_tr)
                    await member.send(text_gb)
                    await member.send(text_cp)
                    await member.send(text_de)
                    await member.send(text_es)
                    text = """\n\n\n**--------------------------------------------------------------------------------------**
                                PLEASE SELECT YOUR LANGUAGE"""
                    await member.send(f"{text}", view=await language_buttons())

                except Exception as e:
                    print(e)
                    channel = bot.get_channel(channel1)
                    await channel.send(f"{member.mention}, \n{texter('gb', '99')}")

        except Exception as e:
            print(e)
            channel = bot.get_channel(channel1)
            await channel.send(f"{member.mention}, Please allow dms.")
            await channel.send("Then use `.! dm` command.")

    async def on_raw_reaction_add(self, payload):
        channel = bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = bot.get_user(payload.user_id)
        member = message.guild.get_member(user.id)

        try:

            if user.bot:
                return

            else:

                if channel.id == 1010559556339900538:

                    if payload.emoji.name == react:

                        with open("members.json", "r") as doc:
                            members = json.load(doc)

                        if str(user.id) in members and "name" in members[str(user.id)] and "surname" in members[str(user.id)]:

                            role = discord.utils.get(message.guild.roles, name="Rookie")
                            role_2 = discord.utils.get(message.guild.roles, name="Indifferent")
                            await member.remove_roles(role_2)
                            await member.add_roles(role)

                        else:
                            return
                    else:
                        return
                else:
                    return

        except Exception as e:
            print(e)
            

TOKEN = os.getenv("TOKEN")

bot = Bot()
bot.run(str(TOKEN))
