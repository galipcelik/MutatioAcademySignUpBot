# -*- coding: utf-8 -*-

import os
import discord
from colorama import Fore, Back
from text_tr import *
from text_gb import *
from text_cp import *
from text_de import *
from text_es import *


react = "✅"
command_prefix = "!!"
description = """
Bot Name: MutatioAcademy SignUp Bot
Coder: jcmaxwell
Version: 1.0.0

Purpose of Usage: We're trying to helping you while you're signing up to our server.

"""
intents = discord.Intents.all()
command_channel_id = 1012250908840693801
channel1 = 1010567975163658290


async def print_info(bot_user_name, bot_user_id, bot_get_all_members):
    os.system("cls")
    print(Back.LIGHTWHITE_EX + Fore.LIGHTRED_EX)
    print(f"----------")
    print(f"Connected Bot Name: {bot_user_name}\n")
    print(f"----------")
    print(f"Coneected Bot ID: {bot_user_id}\n")
    print(Fore.LIGHTGREEN_EX)
    print(f"Accessing {len(set(bot_get_all_members))} users...\n")
    print(Fore.LIGHTBLUE_EX)


def texter(language: str, index: str):
    if language == "tr" and index == "1":
        return text_1_tr

    elif language == "tr" and index == "2":
        return text_2_tr

    elif language == "tr" and index == "3":
        return text_3_tr

    elif language == "tr" and index == "4":
        return text_4_tr

    elif language == "tr" and index == "5":
        return text_5_tr

    elif language == "tr" and index == "6":
        return text_6_tr

    elif language == "tr" and index == "6_1":
        return text_6_1_tr

    elif language == "tr" and index == "7":
        return text_7_tr

    elif language == "tr" and index == "7_1":
        return text_7_1_tr

    elif language == "tr" and index == "8":
        return text_8_tr

    elif language == "tr" and index == "8_1":
        return text_8_1_tr

    elif language == "tr" and index == "9":
        return text_9_tr

    elif language == "tr" and index == "10":
        return text_10_tr

    elif language == "tr" and index == "10_1":
        return text_10_1_tr

    elif language == "tr" and index == "11":
        return text_11_tr

    elif language == "tr" and index == "99":
        return text_99_tr

    elif language == "gb" and index == "1":
        return text_1_gb

    elif language == "gb" and index == "2":
        return text_2_gb

    elif language == "gb" and index == "3":
        return text_3_gb

    elif language == "gb" and index == "4":
        return text_4_gb

    elif language == "gb" and index == "5":
        return text_5_gb

    elif language == "gb" and index == "6":
        return text_6_gb

    elif language == "gb" and index == "6_1":
        return text_6_1_gb

    elif language == "gb" and index == "7":
        return text_7_gb

    elif language == "gb" and index == "7_1":
        return text_7_1_gb

    elif language == "gb" and index == "8":
        return text_8_gb

    elif language == "gb" and index == "8_1":
        return text_8_1_gb

    elif language == "gb" and index == "9":
        return text_9_gb

    elif language == "gb" and index == "10":
        return text_10_gb

    elif language == "gb" and index == "10_1":
        return text_10_1_gb

    elif language == "gb" and index == "11":
        return text_11_gb

    elif language == "gb" and index == "99":
        return text_99_gb

    elif language == "cp" and index == "1":
        return text_1_cp

    elif language == "cp" and index == "2":
        return text_2_cp

    elif language == "cp" and index == "3":
        return text_3_cp

    elif language == "cp" and index == "4":
        return text_4_cp

    elif language == "cp" and index == "5":
        return text_5_cp

    elif language == "cp" and index == "6":
        return text_6_cp

    elif language == "cp" and index == "6_1":
        return text_6_1_cp

    elif language == "cp" and index == "7":
        return text_7_cp

    elif language == "cp" and index == "7_1":
        return text_7_1_cp

    elif language == "cp" and index == "8":
        return text_8_cp

    elif language == "cp" and index == "8_1":
        return text_8_1_cp

    elif language == "cp" and index == "9":
        return text_9_cp

    elif language == "cp" and index == "10":
        return text_10_cp

    elif language == "cp" and index == "10_1":
        return text_10_1_cp

    elif language == "cp" and index == "11":
        return text_11_cp

    elif language == "cp" and index == "99":
        return text_99_cp

    elif language == "es" and index == "1":
        return text_1_es

    elif language == "es" and index == "2":
        return text_2_es

    elif language == "es" and index == "3":
        return text_3_es

    elif language == "es" and index == "4":
        return text_4_es

    elif language == "es" and index == "5":
        return text_5_es

    elif language == "es" and index == "6":
        return text_6_es

    elif language == "es" and index == "6_1":
        return text_6_1_es

    elif language == "es" and index == "7":
        return text_7_es

    elif language == "es" and index == "7_1":
        return text_7_1_es

    elif language == "es" and index == "8":
        return text_8_es

    elif language == "es" and index == "8_1":
        return text_8_1_es

    elif language == "es" and index == "9":
        return text_9_es

    elif language == "es" and index == "10":
        return text_10_es

    elif language == "es" and index == "10_1":
        return text_10_1_es

    elif language == "es" and index == "11":
        return text_11_es

    elif language == "es" and index == "99":
        return text_99_es

    elif language == "de" and index == "1":
        return text_1_de

    elif language == "de" and index == "2":
        return text_2_de

    elif language == "de" and index == "3":
        return text_3_de

    elif language == "de" and index == "4":
        return text_4_de

    elif language == "de" and index == "5":
        return text_5_de

    elif language == "de" and index == "6":
        return text_6_de

    elif language == "de" and index == "6_1":
        return text_6_1_de

    elif language == "de" and index == "7":
        return text_7_de

    elif language == "de" and index == "7_1":
        return text_7_1_de

    elif language == "de" and index == "8":
        return text_8_de

    elif language == "de" and index == "8_1":
        return text_8_1_de

    elif language == "de" and index == "9":
        return text_9_de

    elif language == "de" and index == "10":
        return text_10_de

    elif language == "de" and index == "10_1":
        return text_10_1_de

    elif language == "de" and index == "11":
        return text_11_de

    elif language == "de" and index == "99":
        return text_99_de

    else:
        return print("Unknown language or index.")
