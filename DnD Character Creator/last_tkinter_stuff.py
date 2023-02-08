# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 18:17:49 2020

@author: garre
"""

# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Ethan Weber
#
#        Emily Wax
# Calvin Turrell
# Section: 208
# Assignment: Team 208-4 Final Project
# Date: 29 November, 2020

import tkinter as tk
from tkinter import ttk
# from tkinter import ttk
# from tkinter import messagebox
# import random

# def race_select():
#     print('Races:     | Stat Bonuses:')
#     print('-----------|------------------------')
#     print('Dragonborn | +2 Str, +1 Cha')
#     print('Dwarf      | +2 Con')
#     print('Elf        | +2 Dex')
#     print('Gnome      | +2 Int')
#     print('Half-Elf   | +2 Cha, +1 to 2 others')
#     print('Halfling   | +2 Dex')
#     print('Half-Orc   | +2 Str, +1 Con')
#     print('Human      | +1 to all')
#     print('Tiefling   | +2 Cha, +1 Int')
#     print()
#     print('For more information on races, follow this link: https://www.dndbeyond.com/races')
#     print()
#     print('Choices: [Dragonborn, Dwarf, Elf, Gnome, Half-Elf, Halfling, Half-Orc, Human, Tiefling]')
#     race = input('Please choose a race: ')

#     race_list = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Halfling', 'Half-Orc', 'Human', 'Tiefling']

#     invalid_race = True
#     while invalid_race == True:
#         for race_name in race_list:
#             if race_name == race:
#                 invalid_race = False
#                 break
#         if invalid_race == True:
#             race = input('Please choose a valid race: ')

#     filename = race + '.txt'
#     with open(filename, 'r') as race_file:
#         race_info = race_file.read()

#     race_info = race_info.split('\n')
#     for i in range(len(race_info)):
#         race_info[i] = race_info[i].split()

#     strn = int(race_info[0][1])
#     dex = int(race_info[1][1])
#     con = int(race_info[2][1])
#     intl = int(race_info[3][1])
#     wis = int(race_info[4][1])
#     cha = int(race_info[5][1])

#     speed = int(race_info[6][1])

#     #special case where 2 attributes can be chosen for half-elf
#     if race == 'Half-Elf':
#         stat_1 = input('Enter the first attribute to increase: ')
#         stat_2 = input('Enter the second attribute to increase: ')

#         while True:
#             if stat_1 == stat_2:
#                 print('Please choose two different attributes')
#                 stat_1 = input('Enter the first attribute to increase: ')
#                 stat_2 = input('Enter the second attribute to increase: ')
#             elif stat_1 == 'Charisma' or stat_2 == "Charisma":
#                 print('Please choose attributes other than Charisma')
#                 stat_1 = input('Enter the first attribute to increase: ')
#                 stat_2 = input('Enter the second attribute to increase: ')
#             else:
#                 break

#         stat_list = [stat_1, stat_2]
#         for i in range(2):
#             if stat_list[i] == 'Strength':
#                 strn += 1
#             if stat_list[i] == 'Dexterity':
#                 dex += 1
#             if stat_list[i] == 'Constitution':
#                 con += 1
#             if stat_list[i] == 'Intelligence':
#                 intl += 1
#             if stat_list[i] == 'Wisdom':
#                 wis += 1

#     return(race, strn, dex, con, intl, wis, cha, speed)

# def class_select():
#     print('Class:     | Primary Ability:')
#     print('-----------|-----------------------')
#     print('Barbarian  | Strength')
#     print('Bard       | Charisma')
#     print('Cleric     | Wisdom')
#     print('Druid      | Wisdom')
#     print('Fighter    | Strength or Dexterity')
#     print('Monk       | Dexterity & Wisdom')
#     print('Paladin    | Strength & Charisma')
#     print('Ranger     | Dexterity & Wisdom')
#     print('Rogue      | Dexterity')
#     print('Sorcerer   | Charisma')
#     print('Warlock    | Charisma')
#     print('Wizard     | Intelligence')
#     print()
#     print('For more information on classes, follow this link: https://www.dndbeyond.com/classes')
#     print()
#     print('Choices: [Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard]')
#     char_class = input('Please choose a class: ')

#     class_list = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']

#     invalid_class = True
#     while invalid_class == True:
#         for class_name in class_list:
#             if class_name == char_class:
#                 invalid_class = False
#                 break
#         if invalid_class == True:
#             char_class = input('Please choose a valid class (exactly as written: ')

#     try:
#         filename = char_class + '.txt'
#         with open(filename, 'r') as class_file:
#             class_info = class_file.read()
#     except FileNotFoundError:
#         messagebox.showerror('File Error', 'Please verify that you have downloaded all of the .txt files that go along with this program and are running the program from the same folder as these files. Then Restart')

#     filename = char_class + '.txt'
#     with open(filename, 'r') as class_file:
#         class_info = class_file.read()

#     class_info = class_info.split('\n')
#     for i in range(len(class_info)):
#         class_info[i] = class_info[i].split('-')

#     hit_dice = class_info[0][1]
#     HP_max = class_info[1][1]

#     strn_prof = class_info[2][1]
#     dex_prof = class_info[2][2]
#     con_prof = class_info[2][3]
#     intl_prof = class_info[2][4]
#     wis_prof = class_info[2][5]
#     cha_prof = class_info[2][6]

#     skill_num = class_info[3][0]
#     skill_profs = class_info[4]

#     print('Skill Proficiency Choices:')
#     print(skill_profs)

#     skill_prof_choices = []
#     choices = int(skill_num)
#     while choices > 0:
#         choice = input('Choose a skill from the list above: ')
#         match = False
#         for skill in skill_profs:
#             if skill == choice:
#                 match = True
#         if match == True:
#             skill_prof_choices.append(choice)
#             choices -= 1
#         else:
#             print('Invalid choice!')

#     return(char_class, hit_dice, HP_max, strn_prof, dex_prof, con_prof, intl_prof, wis_prof, cha_prof, skill_prof_choices)

# def skill_prof_marker(skill_prof_choices):
#     skill_profs = {'Acrobatics':'', 'Animal Handling':'', 'Arcana':'', 'Athletics':'', 'Deception':'', 'History':'', 'Insight':'', 'Intimidation':'', 'Investigation':'', 'Medicine':'', 'Nature':'', 'Perception':'', 'Performance':'', 'Persuasion':'', 'Religion':'', 'Sleight of Hand':'', 'Stealth':'', 'Survival':''}
#     for skill in skill_profs.keys():
#         for choice in skill_prof_choices:
#             if skill == choice:
#                 skill_profs[skill] = 'X'

#     return(skill_profs['Acrobatics'], skill_profs['Animal Handling'], skill_profs['Arcana'], skill_profs['Athletics'],skill_profs['Deception'], skill_profs['History'], skill_profs['Insight'], skill_profs['Intimidation'], skill_profs['Investigation'], skill_profs['Medicine'], skill_profs['Nature'], skill_profs['Perception'], skill_profs['Performance'], skill_profs['Persuasion'], skill_profs['Religion'], skill_profs['Sleight of Hand'], skill_profs['Stealth'], skill_profs['Survival'], [skill_profs['Acrobatics'], skill_profs['Animal Handling'], skill_profs['Arcana'], skill_profs['Deception'], skill_profs['History'], skill_profs['Insight'], skill_profs['Intimidation'], skill_profs['Investigation'], skill_profs['Medicine'], skill_profs['Nature'], skill_profs['Perception'], skill_profs['Performance'], skill_profs['Persuasion'], skill_profs['Religion'], skill_profs['Sleight of Hand'], skill_profs['Stealth'], skill_profs['Survival']])

# def stat_roller():
#     '''Returns 6 randomly generated numbers. 4 dice roll per # drop the lowest.'''

#     num1 = []
#     num2 = []
#     num3 = []
#     num4 = []
#     num5 = []
#     num6 = []

#     n = 0
#     while n < 4:
#         stat1 = random.randint(1,6)
#         stat2 = random.randint(1,6)
#         stat3 = random.randint(1,6)
#         stat4 = random.randint(1,6)
#         stat5 = random.randint(1,6)
#         stat6 = random.randint(1,6)

#         num1.append(stat1)
#         num2.append(stat2)
#         num3.append(stat3)
#         num4.append(stat4)
#         num5.append(stat5)
#         num6.append(stat6)
#         n += 1


#     num1.remove(min(num1))
#     num2.remove(min(num2))
#     num3.remove(min(num3))
#     num4.remove(min(num4))
#     num5.remove(min(num5))
#     num6.remove(min(num6))

#     stats = [sum(num1), sum(num2), sum(num3), sum(num4), sum(num5), sum(num6)]

#     return(stats)

# def ability_score_assign(stats, strn, dex, con, intl, wis, cha):

#     stat_match = False
#     print('Score Choices:', stats)
#     choice = int(input('Please choose a score for Strength: '))
#     while stat_match == False:
#         for stat in stats:
#             if stat == choice:
#                 strn += choice
#                 stats.remove(choice)
#                 stat_match = True
#                 break
#         if stat_match == False:
#             choice = input('Please choose a valid value from the list above: ')

#     stat_match = False
#     print('Remaining Score Choices:', stats)
#     choice = int(input('Please choose a score for Dexterity: '))
#     while stat_match == False:
#         for stat in stats:
#             if stat == choice:
#                 dex += choice
#                 stats.remove(choice)
#                 stat_match = True
#                 break
#         if stat_match == False:
#             choice = input('Please choose a valid value from the list above: ')

#     stat_match = False
#     print('Remaining Score Choices:', stats)
#     choice = int(input('Please choose a score for Constitution: '))
#     while stat_match == False:
#         for stat in stats:
#             if stat == choice:
#                 con += choice
#                 stats.remove(choice)
#                 stat_match = True
#                 break
#         if stat_match == False:
#             choice = input('Please choose a valid value from the list above: ')

#     stat_match = False
#     print('Remaining Score Choices:', stats)
#     choice = int(input('Please choose a score for Intelligence: '))
#     while stat_match == False:
#         for stat in stats:
#             if stat == choice:
#                 intl += choice
#                 stats.remove(choice)
#                 stat_match = True
#                 break
#         if stat_match == False:
#             choice = input('Please choose a valid value from the list above: ')

#     stat_match = False
#     print('Remaining Score Choices:', stats)
#     choice = int(input('Please choose a score for Wisdom: '))
#     while stat_match == False:
#         for stat in stats:
#             if stat == choice:
#                 wis += choice
#                 stats.remove(choice)
#                 stat_match = True
#                 break
#         if stat_match == False:
#             choice = input('Please choose a valid value from the list above: ')

#     stat_match = False
#     print('Remaining Score Choices:', stats)
#     choice = int(input('Please choose a score for Charisma: '))
#     while stat_match == False:
#         for stat in stats:
#             if stat == choice:
#                 cha += choice
#                 stats.remove(choice)
#                 stat_match = True
#                 break
#         if stat_match == False:
#             choice = input('Please choose a valid value from the list above: ')

#     return(strn, dex, con, intl, wis, cha)

# def ability_score_mod(strn, dex, con, intl, wis, cha):
#     scores = [strn, dex, con, intl, wis, cha]
#     modifiers = []
#     for score in scores:
#         if score == 3:
#             modifiers.append(-4)
#         elif score == 4 or score == 5:
#             modifiers.sappend(-3)
#         elif score == 6 or score == 7:
#             modifiers.append(-2)
#         elif score == 8 or score == 9:
#             modifiers.append(-1)
#         elif score == 10 or score == 11:
#             modifiers.append(0)
#         elif score == 12 or score == 13:
#             modifiers.append(1)
#         elif score == 14 or score == 15:
#             modifiers.append(2)
#         elif score == 16 or score == 17:
#             modifiers.append(3)
#         elif score == 18 or score == 19:
#             modifiers.append(4)
#         elif score == 20 or score == 21:
#             modifiers.append(5)

#     return(modifiers[0], modifiers[1], modifiers[2], modifiers[3], modifiers[4], modifiers[5])

# def saving_throw_bonus(strn_prof, dex_prof, con_prof, intl_prof, wis_prof, cha_prof, strn_mod, dex_mod, con_mod, intl_mod, wis_mod, cha_mod):
#     stat_mods = [strn_mod, dex_mod, con_mod, intl_mod, wis_mod, cha_mod]
#     save_profs = [strn_prof, dex_prof, con_prof, intl_prof, wis_prof, cha_prof]
#     save_mods = []
#     for i in range(len(save_profs)):
#         if save_profs[i] == 'X':
#             save_mods.append((2 + stat_mods[i]))
#         else:
#             save_mods.append(stat_mods[i])

#     return(save_mods[0], save_mods[1], save_mods[2], save_mods[3], save_mods[4], save_mods[5])

# def skill_mod(strn_mod,dex_mod,con_mod,intl_mod,wis_mod,cha_mod):

#     acro_mod = dex_mod
#     anim_mod = wis_mod
#     arca_mod = intl_mod
#     athl_mod = strn_mod
#     dece_mod = cha_mod
#     hist_mod = intl_mod
#     insi_mod = wis_mod
#     inti_mod = cha_mod
#     inve_mod = intl_mod
#     medi_mod = wis_mod
#     natu_mod = intl_mod
#     perc_mod = wis_mod
#     perf_mod = cha_mod
#     pers_mod = cha_mod
#     reli_mod = intl_mod
#     slei_mod = dex_mod
#     stea_mod = dex_mod
#     surv_mod = wis_mod

#     return(acro_mod, anim_mod, arca_mod, athl_mod, dece_mod, hist_mod, insi_mod, inti_mod, inve_mod, medi_mod, natu_mod, perc_mod, perf_mod, pers_mod, reli_mod, slei_mod, stea_mod, surv_mod)

# def skill_prof_bonus(acro_mod, anim_mod, arca_mod, athl_mod, dece_mod, hist_mod, insi_mod, inti_mod, inve_mod, medi_mod, natu_mod, perc_mod, perf_mod, pers_mod, reli_mod, slei_mod, stea_mod, surv_mod, skill_prof):
#     '''Adds 2 to skills that are marked as proficient in the formatted list skill_profs'''

#     skills = [acro_mod, anim_mod, arca_mod, athl_mod, dece_mod, hist_mod, insi_mod, inti_mod, inve_mod, medi_mod, natu_mod, perc_mod, perf_mod, pers_mod, reli_mod, slei_mod, stea_mod, surv_mod]

#     for i in range(len(skill_prof)):

#         if skill_prof[i] == 'X':
#             skills[i] += 2

#     return(acro_mod, anim_mod, arca_mod, athl_mod, dece_mod, hist_mod, insi_mod, inti_mod, inve_mod, medi_mod, natu_mod, perc_mod, perf_mod, pers_mod, reli_mod, slei_mod, stea_mod, surv_mod)

# def misc_stats(dex_mod, con_mod, HP_max, perc_mod):
#     pass_wis = 10 + perc_mod
#     HP_max = int(HP_max)
#     HP_max += con_mod
#     initiative = dex_mod

#     return(pass_wis, HP_max, initiative)

# def char_sheet_format(char_name, char_class, background, play_name, race, alignment, strn, strn_mod, dex, dex_mod, con, con_mod, intl, intl_mod, wis, wis_mod, cha, cha_mod, initiative, speed, HP_max, hit_dice, strn_prof, strn_st_mod, dex_prof, dex_st_mod, con_prof, con_st_mod, intl_prof, intl_st_mod, wis_prof, wis_st_mod, cha_prof, cha_st_mod, acro_prof, acro_mod, anim_prof, anim_mod, arca_prof, arca_mod, athl_prof, athl_mod, dece_prof, dece_mod, hist_prof, hist_mod, insi_prof, insi_mod, inti_prof, inti_mod, inve_prof, inve_mod, medi_prof, medi_mod, natu_prof, natu_mod, perc_prof, perc_mod, perf_prof, perf_mod, pers_prof, pers_mod, reli_prof, reli_mod, slei_prof, slei_mod, stea_prof, stea_mod, surv_prof, surv_mod, pass_wis):
#     sheet_list_format = [['Identifying info: ', '', '', '', '', '', '', '', ''], ['Character Name:', char_name, '', 'Class:', char_class, 'Background: ', background, 'Player Name: ', play_name], ['', '', '', 'Race:', race, 'Alignment:', alignment, 'Experience Points:', '0'], ['', '', '', '', '', '', '', '', ''], ['Ability Scores: ', '', '', '', 'Armor Class:', 'Initiative:', 'Speed: ', '', ''], ['Attribute:', 'Value:', 'Modifier: ', '', '', initiative, speed, '', ''], ['Strength', strn, strn_mod, '', '', '', '', '', ''], ['Dexterity', dex, dex_mod, '', 'Hit Point Max:', HP_max, '', '', ''], ['Constitution', con, con_mod, '', '', '', '', '', ''], ['Intelligence', intl, intl_mod, '', 'Hit Dice:', hit_dice, '', '', ''], ['Wisdom', wis, wis_mod, '', '', '', '', '', ''], ['Charisma', cha, cha_mod, '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['Proficiency Bonus: ', '2', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['Saving Throws:', '', '', '', '', '', '', '', ''], ['Attribute:', 'Proficiency?:', 'Modifier:', '', '', '', '', '', ''], ['Strength', strn_prof, strn_st_mod, '', '', '', '', '', ''], ['Dexterity', dex_prof, dex_st_mod, '', '', '', '', '', ''], ['Constitution', con_prof, con_st_mod, '', '', '', '', '', ''], ['Intelligence', intl_prof, intl_st_mod, '', '', '', '', '', ''], ['Wisdom', wis_prof, wis_st_mod, '', '', '', '', '', ''], ['Charisma', cha_prof, cha_st_mod, '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['Skills:', '', '', '', '', '', '', '', ''], ['Skill:', 'Proficiency?:', 'Modifier:', '', '', '', '', '', ''], ['Acrobatics', acro_prof, acro_mod, '', '', '', '', '', ''], ['Animal Handling', anim_prof, anim_mod, '', '', '', '', '', ''], ['Arcana', arca_prof, arca_mod, '', '', '', '', '', ''], ['Athletics', athl_prof, athl_mod, '', '', '', '', '', ''], ['Deception', dece_prof, dece_mod, '', '', '', '', '', ''], ['History', hist_prof, hist_mod, '', '', '', '', '', ''], ['Insight', insi_prof, insi_mod, '', '', '', '', '', ''], ['Intimidation', inti_prof, inti_mod, '', '', '', '', '', ''], ['Investigation', inve_prof, inve_mod, '', '', '', '', '', ''], ['Medicine', medi_prof, medi_mod, '', '', '', '', '', ''], ['Nature', natu_prof, natu_mod, '', '', '', '', '', ''], ['Perception', perc_prof, perc_mod, '', '', '', '', '', ''], ['Performance', perf_prof, perf_mod, '', '', '', '', '', ''], ['Persuasion', pers_prof, pers_mod, '', '', '', '', '', ''], ['Religion', reli_prof, reli_mod, '', '', '', '', '', ''], ['Sleight of Hand', slei_prof, slei_mod, '', '', '', '', '', ''], ['Stealth', stea_prof, stea_mod, '', '', '', '', '', ''], ['Survival', surv_prof, surv_mod, '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['Passive Wisdom:', pass_wis, '', '', '', '', '', '', ''], ['']]
#     sheet_string_format = ''
#     for line in sheet_list_format:
#         for value in line:
#             sheet_string_format += (str(value) + ',')
#         sheet_string_format += '\n'
#     filename = input('Choose a name for your file: ')
#     filename += '.csv'
#     with open(filename, 'w') as file:
#         file.write(sheet_string_format)

##### Program #####

# (char_name, background, play_name, alignment) = identity()

# (race, strn, dex, con, intl, wis, cha, speed) = race_select()

# (char_class, hit_dice, HP_max, strn_prof, dex_prof, con_prof, intl_prof,
#  wis_prof, cha_prof, skill_prof_choices) = class_select()

# (acro_prof, anim_prof, arca_prof, athl_prof, dece_prof, hist_prof, insi_prof,
#  inti_prof, inve_prof, medi_prof, natu_prof, perc_prof, perf_prof, pers_prof,
#  reli_prof, slei_prof, stea_prof, surv_prof,
#  skill_prof) = skill_prof_marker(skill_prof_choices)

# stats = stat_roller()

# (strn, dex, con, intl, wis, cha) = ability_score_assign(
#     stats, strn, dex, con, intl, wis, cha)

# (strn_mod, dex_mod, con_mod, intl_mod, wis_mod, cha_mod) = ability_score_mod(
#     strn, dex, con, intl, wis, cha)

# (strn_st_mod, dex_st_mod, con_st_mod,
#  intl_st_mod, wis_st_mod, cha_st_mod) = saving_throw_bonus(
#      strn_prof, dex_prof, con_prof, intl_prof, wis_prof, cha_prof, strn_mod,
#      dex_mod, con_mod, intl_mod, wis_mod, cha_mod)

# (acro_mod, anim_mod, arca_mod, athl_mod, dece_mod, hist_mod, insi_mod,
#  inti_mod, inve_mod, medi_mod, natu_mod, perc_mod, perf_mod,
#  pers_mod, reli_mod, slei_mod, stea_mod, surv_mod) = skill_mod(
#      strn_mod, dex_mod, con_mod, intl_mod, wis_mod, cha_mod)

# (acro_mod, anim_mod, arca_mod, athl_mod, dece_mod, hist_mod, insi_mod,
#  inti_mod, inve_mod, medi_mod, natu_mod, perc_mod, perf_mod, pers_mod,
#  reli_mod, slei_mod, stea_mod, surv_mod) = skill_prof_bonus(
#      acro_mod, anim_mod, arca_mod, athl_mod, dece_mod, hist_mod, insi_mod,
#      inti_mod, inve_mod, medi_mod, natu_mod, perc_mod, perf_mod, pers_mod,
#      reli_mod, slei_mod, stea_mod, surv_mod, skill_prof)

# (pass_wis, HP_max, initiative) = misc_stats(dex_mod, con_mod, HP_max, perc_mod)

# char_sheet_format(
#     char_name, char_class, background, play_name, race, alignment, strn,
#     strn_mod, dex, dex_mod, con, con_mod, intl, intl_mod, wis, wis_mod, cha,
#     cha_mod, initiative, speed, HP_max, hit_dice, strn_prof, strn_st_mod,
#     dex_prof, dex_st_mod, con_prof, con_st_mod, intl_prof, intl_st_mod,
#     wis_prof, wis_st_mod, cha_prof, cha_st_mod, acro_prof, acro_mod, anim_prof,
#     anim_mod, arca_prof, arca_mod, athl_prof, athl_mod, dece_prof, dece_mod,
#     hist_prof, hist_mod, insi_prof, insi_mod, inti_prof, inti_mod, inve_prof,
#     inve_mod, medi_prof, medi_mod, natu_prof, natu_mod, perc_prof, perc_mod,
#     perf_prof, perf_mod, pers_prof, pers_mod, reli_prof, reli_mod, slei_prof,
#     slei_mod, stea_prof, stea_mod, surv_prof, surv_mod, pass_wis)

home = tk.Tk()
home.title("Birth a New Soul Into This Realm")
home.geometry("400x400")

def go_to_page_2():
    page_1.grid_forget()
    page_2.grid(row = 0, column = 0)

########## PAGE 1: Identity ##########
page_1 = tk.LabelFrame(home, text = "Page 1", padx = 10, pady = 10)
page_1.grid(row = 0, column = 0)

char_name_label = tk.Label(page_1, text = "Character name: ", width = 20)
char_name_label.grid(row = 0, column = 0)

char_name = tk.Entry(page_1, width = 15)
char_name.grid(row = 0, column = 1)

user_name_label = tk.Label(page_1, text = "Player name: ", width = 20)
user_name_label.grid(row = 1, column = 0)

user_name = tk.Entry(page_1, width = 15)
user_name.grid(row = 1, column = 1)

choose_background_label = tk.Label(page_1, text = "Background: ")
choose_background_label.grid(row = 2, column = 0)

background_drop = ttk.Combobox(page_1, width = 12)
background_drop['values'] = ["Acolyte", "Charlatan", "Criminal", "Entertainer", "Folk Hero", "Guild Artisan", "Hermit", "Ranger", "Noble", "Outlander", "Sage", "Sailor", "Soldier", "Urchin"]
background_drop.grid(row = 2, column = 1, sticky = 'e')

choose_alignment_label = tk.Label(page_1, text = "Alignment: ")
choose_alignment_label.grid(row = 3, column = 0)

alignment_drop = ttk.Combobox(page_1, width = 12)
alignment_drop['values'] = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "True Neutral", "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil"]
alignment_drop.grid(row = 3, column = 1, sticky = 'e')

tk.Label(page_1, text = '   ').grid(row = 4, columnspan = 2)
page_2_button = tk.Button(page_1, text = 'Page 2', command = go_to_page_2)
page_2_button.grid(row = 5, columnspan = 2, sticky = 's')

########## PAGE 2: Race ##########
def choose_race(event):
    global half_elf
    global half_elf_attributes
    print(race_drop.get(), half_elf)
    if race_drop.get() == "Half-Elf":
        property_1_label.grid(row = 3, column = 0)
        property_2_label.grid(row = 4, column = 0)
        property_1.grid(row = 3, column = 1, sticky = 'e')
        property_2.grid(row = 4, column = 1, sticky = 'e')
        half_elf = True

    elif race_drop.get() != "Half-Elf" and half_elf == True:
        property_1.grid_forget()
        property_2.grid_forget()
        property_1_label.grid_forget()
        property_2_label.grid_forget()
        
        half_elf_attributes = reset_half_elf()

def reset_half_elf():
        property_1.set('')
        property_2.set('')
        property_1['state'] = 'enabled'
        property_2['state'] = 'enabled' 
        property_1['values'] = half_elf_attributes_copy
        property_2['values'] = half_elf_attributes_copy
        return ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom']
        
def half_elf_values(event):
    if property_1.get() != '' and property_1['state'] == 'enabled':
        half_elf_attributes.remove(property_1.get())
        property_2['values'] = half_elf_attributes
        property_1['state'] = 'disabled'
    if property_2.get() != '':
        half_elf_attributes.remove(property_2.get())
        property_1['values'] = half_elf_attributes
        property_2['state'] = 'disabled'

page_2 = tk.LabelFrame(home, text = "Page 2", padx = 10, pady = 10)

race_drop = ttk.Combobox(page_2, width = 12)
race_drop['values'] = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling", "Half-Orc", "Human", "Tiefling"]
race_drop.grid(row = 2, column = 1, sticky = 'e')
race_drop.bind("<<ComboboxSelected>>", choose_race)

property_1_label = tk.Label(page_2, text = 'Half-Elf Attr. 1')

property_1 = ttk.Combobox(page_2, width = 12)
property_1['values'] = half_elf_attributes
property_1.bind("<<ComboboxSelected>>", half_elf_values)
property_1['state'] = 'enabled'

property_2_label = tk.Label(page_2, text = 'Half-Elf Attr. 2')

property_2 = ttk.Combobox(page_2, width = 12)
property_2['values'] = half_elf_attributes
property_2.bind("<<ComboboxSelected>>", half_elf_values)
property_2['state'] = 'enabled'
########## PAGE 3: Class ##########

########## PAGE 4: Proficiency ##########

########## PAGE 5: Dice Rolls ##########

tk.mainloop()