import discord
from discord.ui import Button, View
from text_tr import *
from text_gb import *
from text_de import *
from text_cp import *
from text_es import *
import json


async def language_buttons():
    button_tr = Button(label="TR", style=discord.ButtonStyle.blurple)
    button_gb = Button(label="GB", style=discord.ButtonStyle.blurple)
    button_de = Button(label="DE", style=discord.ButtonStyle.blurple)
    button_cp = Button(label="CP", style=discord.ButtonStyle.blurple)
    button_es = Button(label="ES", style=discord.ButtonStyle.blurple)

    async def button_tr_callback(interaction: discord.Interaction):
        with open("members.json", "r") as doc:
            users = json.load(doc)

        users[str(interaction.user.id)] = {"language": "tr"}

        with open("members.json", "w") as doc:
            json.dump(users, doc)

        content = text_4_tr
        role = interaction.client.guilds[0].get_role(1022229451733471292)
        member = interaction.client.guilds[0].get_member(interaction.user.id)
        await member.add_roles(role)
        await interaction.response.edit_message(content=content, view=await new_language_buttons(item="TR"))
        await interaction.followup.send(text_5_tr)
        await interaction.followup.send(text_6_tr)
        await interaction.followup.send(text_7_tr)
        await interaction.followup.send(text_9_tr)
        await interaction.followup.send(text_10_tr)

    async def button_gb_callback(interaction: discord.Interaction):

        with open("members.json", "r") as doc:
            users = json.load(doc)

        users[str(interaction.user.id)] = {"language": "gb"}

        with open("members.json", "w") as doc:
            json.dump(users, doc)

        content = text_4_gb
        role = interaction.client.guilds[0].get_role(1022229615273594991)
        member = interaction.client.guilds[0].get_member(interaction.user.id)
        await member.add_roles(role)
        await interaction.response.edit_message(content=content, view=await new_language_buttons(item="GB"))
        await interaction.followup.send(text_5_gb)
        await interaction.followup.send(text_6_gb)
        await interaction.followup.send(text_7_gb)
        await interaction.followup.send(text_9_gb)
        await interaction.followup.send(text_10_gb)

    async def button_de_callback(interaction: discord.Interaction):

        with open("members.json", "r") as doc:
            users = json.load(doc)

        users[str(interaction.user.id)] = {"language": "de"}

        with open("members.json", "w") as doc:
            json.dump(users, doc)

        content = text_4_de
        role = interaction.client.guilds[0].get_role(1022229714900893706)
        member = interaction.client.guilds[0].get_member(interaction.user.id)
        await member.add_roles(role)
        await interaction.response.edit_message(content=content, view=await new_language_buttons(item="DE"))
        await interaction.followup.send(text_5_de)
        await interaction.followup.send(text_6_de)
        await interaction.followup.send(text_7_de)
        await interaction.followup.send(text_9_de)
        await interaction.followup.send(text_10_de)

    async def button_cp_callback(interaction: discord.Interaction):

        with open("members.json", "r") as doc:
            users = json.load(doc)

        users[str(interaction.user.id)] = {"language": "cp"}

        with open("members.json", "w") as doc:
            json.dump(users, doc)

        content = text_4_cp
        role = interaction.client.guilds[0].get_role(1022229779149234227)
        member = interaction.client.guilds[0].get_member(interaction.user.id)
        await member.add_roles(role)
        await interaction.response.edit_message(content=content, view=await new_language_buttons(item="CP"))
        await interaction.followup.send(text_5_cp)
        await interaction.followup.send(text_6_cp)
        await interaction.followup.send(text_7_cp)
        await interaction.followup.send(text_9_cp)
        await interaction.followup.send(text_10_cp)

    async def button_es_callback(interaction: discord.Interaction):

        with open("members.json", "r") as doc:
            users = json.load(doc)

        users[str(interaction.user.id)] = {"language": "es"}

        with open("members.json", "w") as doc:
            json.dump(users, doc)
        content = text_4_es
        role = interaction.client.guilds[0].get_role(1022229911496314913)
        member = interaction.client.guilds[0].get_member(interaction.user.id)
        await member.add_roles(role)
        await interaction.response.edit_message(content=content, view=await new_language_buttons(item="ES"))
        await interaction.followup.send(text_5_es)
        await interaction.followup.send(text_6_es)
        await interaction.followup.send(text_7_es)
        await interaction.followup.send(text_9_es)
        await interaction.followup.send(text_10_es)

    button_tr.callback = button_tr_callback
    button_gb.callback = button_gb_callback
    button_de.callback = button_de_callback
    button_cp.callback = button_cp_callback
    button_es.callback = button_es_callback

    myview = View(timeout=None)
    myview.add_item(button_tr)
    myview.add_item(button_gb)
    myview.add_item(button_de)
    myview.add_item(button_cp)
    myview.add_item(button_es)

    return myview


async def new_language_buttons(item: str):
    mylist = ["TR", "GB", "DE", "CP", "ES"]
    mylist.remove(item)
    indexes = []

    new_view = View()

    my_button = Button(label=f"{item}", style=discord.ButtonStyle.green, disabled=True)
    new_view.add_item(my_button)

    for i in mylist:
        indexes.append(int(mylist.index(i)))

    for x in indexes:
        label = mylist[x]
        my_button = Button(label=label, style=discord.ButtonStyle.gray, disabled=True)
        new_view.add_item(my_button)

    return new_view
