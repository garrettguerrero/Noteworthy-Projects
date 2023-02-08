# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Ethan Weber
# Garrett Guerrero
# Emily Wax
# Calvin Turrell
#
# Section: 208
# Assignment: Team 208-4 Final Project
# Date: 29 November, 2020

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

def race_select(race):
    '''Takes the user selected race and reads the ability score bonuses and speed from the corresponding file'''

    try:
        filename = race + '.txt'
        with open(filename, 'r') as race_file:
          race_info = race_file.read()
    except FileNotFoundError:
        home.destroy()
        messagebox.showerror('File Error', 'Please verify that you have downloaded all of the .txt files that go along with this program and are running the program from the same folder as these files. Then restart the program.')

    race_info = race_info.split('\n')
    for i in range(len(race_info)):
        race_info[i] = race_info[i].split()

    strn = int(race_info[0][1])
    dex = int(race_info[1][1])
    con = int(race_info[2][1])
    intl = int(race_info[3][1])
    wis = int(race_info[4][1])
    cha = int(race_info[5][1])

    speed = int(race_info[6][1])

    return(strn, dex, con, intl, wis, cha, speed)

def half_elf_atribute_add(stat, strn, dex, con, intl, wis, cha):
    '''Add +1 to the chosen attribute for Half-Elf'''
    if stat == 'Strength':
        strn += 1
    if stat == 'Dexterity':
        dex += 1
    if stat == 'Constitution':
        con += 1
    if stat == 'Intelligence':
        intl += 1
    if stat == 'Wisdom':
        wis += 1
    return(strn, dex, con, intl, wis, cha)

def class_select(char_class):
    '''Takes the user selected race and reads the ability score bonuses and speed from the corresponding file'''
      
    try:
        filename = str(char_class) + '.txt'
        with open(filename, 'r') as class_file:
            class_info = class_file.read()
    except FileNotFoundError:
        home.destroy()
        messagebox.showerror('File Error', 'Please verify that you have downloaded all of the .txt files that go along with this program and are running the program from the same folder as these files. Then restart the program.')

    class_info = class_info.split('\n')
    for i in range(len(class_info)):
        class_info[i] = class_info[i].split('-')

    hit_dice = class_info[0][1]
    HP_max = class_info[1][1]

    strn_prof = class_info[2][1]
    dex_prof = class_info[2][2]
    con_prof = class_info[2][3]
    intl_prof = class_info[2][4]
    wis_prof = class_info[2][5]
    cha_prof = class_info[2][6]

    skill_num = int(class_info[3][0])
    skill_profs = class_info[4]

    return(hit_dice, HP_max, strn_prof, dex_prof, con_prof, intl_prof, wis_prof, cha_prof, skill_profs, skill_num)

def skill_prof_marker(skill_prof_choices):
    ''' goes through possible skills proficiencies and marks which are chosen '''

    skill_profs = {'Acrobatics':'', 'Animal Handling':'', 'Arcana':'', 'Athletics':'', 'Deception':'', 'History':'', 'Insight':'', 'Intimidation':'', 'Investigation':'', 'Medicine':'', 'Nature':'', 'Perception':'', 'Performance':'', 'Persuasion':'', 'Religion':'', 'Sleight of Hand':'', 'Stealth':'', 'Survival':''}
    for skill in skill_profs.keys():
        for choice in skill_prof_choices:
            if skill == choice:
                skill_profs[skill] = 'X'

    return(skill_profs['Acrobatics'], skill_profs['Animal Handling'], skill_profs['Arcana'], skill_profs['Athletics'],skill_profs['Deception'], skill_profs['History'], skill_profs['Insight'], skill_profs['Intimidation'], skill_profs['Investigation'], skill_profs['Medicine'], skill_profs['Nature'], skill_profs['Perception'], skill_profs['Performance'], skill_profs['Persuasion'], skill_profs['Religion'], skill_profs['Sleight of Hand'], skill_profs['Stealth'], skill_profs['Survival'], [skill_profs['Acrobatics'], skill_profs['Animal Handling'], skill_profs['Arcana'], skill_profs['Deception'], skill_profs['History'], skill_profs['Insight'], skill_profs['Intimidation'], skill_profs['Investigation'], skill_profs['Medicine'], skill_profs['Nature'], skill_profs['Perception'], skill_profs['Performance'], skill_profs['Persuasion'], skill_profs['Religion'], skill_profs['Sleight of Hand'], skill_profs['Stealth'], skill_profs['Survival']])

def stat_roller():
    '''Returns 6 randomly generated numbers. 4 dice roll per # drop the lowest.'''

    num1 = []
    num2 = []
    num3 = []
    num4 = []
    num5 = []
    num6 = []

    n = 0
    while n < 4:
        stat1 = random.randint(1,6)
        stat2 = random.randint(1,6)
        stat3 = random.randint(1,6)
        stat4 = random.randint(1,6)
        stat5 = random.randint(1,6)
        stat6 = random.randint(1,6)

        num1.append(stat1)
        num2.append(stat2)
        num3.append(stat3)
        num4.append(stat4)
        num5.append(stat5)
        num6.append(stat6)
        n += 1


    num1.remove(min(num1))
    num2.remove(min(num2))
    num3.remove(min(num3))
    num4.remove(min(num4))
    num5.remove(min(num5))
    num6.remove(min(num6))

    stats = [sum(num1), sum(num2), sum(num3), sum(num4), sum(num5), sum(num6)]

    return(stats)

def ability_score_mod(strn, dex, con, intl, wis, cha):
    ''' uses score choices from previous function to correctly assign ability modifiers '''

    scores = [strn, dex, con, intl, wis, cha]
    modifiers = []
    for score in scores:
        if score == 3:
            modifiers.append(-4)
        elif score == 4 or score == 5:
            modifiers.append(-3)
        elif score == 6 or score == 7:
            modifiers.append(-2)
        elif score == 8 or score == 9:
            modifiers.append(-1)
        elif score == 10 or score == 11:
            modifiers.append(0)
        elif score == 12 or score == 13:
            modifiers.append(1)
        elif score == 14 or score == 15:
            modifiers.append(2)
        elif score == 16 or score == 17:
            modifiers.append(3)
        elif score == 18 or score == 19:
            modifiers.append(4)
        elif score == 20 or score == 21:
            modifiers.append(5)

    return(modifiers[0], modifiers[1], modifiers[2], modifiers[3], modifiers[4], modifiers[5])

def saving_throw_bonus(strn_prof, dex_prof, con_prof, intl_prof, wis_prof, cha_prof, strn_mod, dex_mod, con_mod, intl_mod, wis_mod, cha_mod):
    ''' adds bonuses (mods) to saving throws using stat mods and proficiencies '''
    stat_mods = [strn_mod, dex_mod, con_mod, intl_mod, wis_mod, cha_mod]
    save_profs = [strn_prof, dex_prof, con_prof, intl_prof, wis_prof, cha_prof]
    save_mods = []
    for i in range(len(save_profs)):
        if save_profs[i] == 'X':
            save_mods.append((2 + stat_mods[i]))
        else:
            save_mods.append(stat_mods[i])

    return(save_mods[0], save_mods[1], save_mods[2], save_mods[3], save_mods[4], save_mods[5])

def skill_mod(strn_mod,dex_mod,con_mod,intl_mod,wis_mod,cha_mod):
    ''' modifies skills based on the corresponding ability modifier '''

    acro_mod = dex_mod
    anim_mod = wis_mod
    arca_mod = intl_mod
    athl_mod = strn_mod
    dece_mod = cha_mod
    hist_mod = intl_mod
    insi_mod = wis_mod
    inti_mod = cha_mod
    inve_mod = intl_mod
    medi_mod = wis_mod
    natu_mod = intl_mod
    perc_mod = wis_mod
    perf_mod = cha_mod
    pers_mod = cha_mod
    reli_mod = intl_mod
    slei_mod = dex_mod
    stea_mod = dex_mod
    surv_mod = wis_mod

    return(acro_mod, anim_mod, arca_mod, athl_mod, dece_mod, hist_mod, insi_mod, inti_mod, inve_mod, medi_mod, natu_mod, perc_mod, perf_mod, pers_mod, reli_mod, slei_mod, stea_mod, surv_mod)

def skill_prof_bonus(acro_mod, anim_mod, arca_mod, athl_mod, dece_mod, hist_mod, insi_mod, inti_mod, inve_mod, medi_mod, natu_mod, perc_mod, perf_mod, pers_mod, reli_mod, slei_mod, stea_mod, surv_mod, skill_prof):
    '''Adds 2 to skills that are marked as proficient in the formatted list skill_profs'''

    skills = [acro_mod, anim_mod, arca_mod, athl_mod, dece_mod, hist_mod, insi_mod, inti_mod, inve_mod, medi_mod, natu_mod, perc_mod, perf_mod, pers_mod, reli_mod, slei_mod, stea_mod, surv_mod]

    for i in range(len(skill_prof)):

        if skill_prof[i] == 'X':
            skills[i] += 2

    return(acro_mod, anim_mod, arca_mod, athl_mod, dece_mod, hist_mod, insi_mod, inti_mod, inve_mod, medi_mod, natu_mod, perc_mod, perf_mod, pers_mod, reli_mod, slei_mod, stea_mod, surv_mod)

def misc_stats(dex_mod, con_mod, HP_max, perc_mod):
    ''' modifies additional stats based on corresponding modifiers '''
  
    pass_wis = 10 + perc_mod
    HP_max = int(HP_max)
    HP_max += con_mod
    initiative = dex_mod

    return(pass_wis, HP_max, initiative)

def char_sheet_format(char_name, char_class, background, play_name, race, alignment, strn, strn_mod, dex, dex_mod, con, con_mod, intl, intl_mod, wis, wis_mod, cha, cha_mod, initiative, speed, HP_max, hit_dice, strn_prof, strn_st_mod, dex_prof, dex_st_mod, con_prof, con_st_mod, intl_prof, intl_st_mod, wis_prof, wis_st_mod, cha_prof, cha_st_mod, acro_prof, acro_mod, anim_prof, anim_mod, arca_prof, arca_mod, athl_prof, athl_mod, dece_prof, dece_mod, hist_prof, hist_mod, insi_prof, insi_mod, inti_prof, inti_mod, inve_prof, inve_mod, medi_prof, medi_mod, natu_prof, natu_mod, perc_prof, perc_mod, perf_prof, perf_mod, pers_prof, pers_mod, reli_prof, reli_mod, slei_prof, slei_mod, stea_prof, stea_mod, surv_prof, surv_mod, pass_wis, filename):
    '''Takes all of the variables created in the program and formats them to match the character sheet and then writes the file as a .csv'''
    sheet_list_format = [['Identifying info: ', '', '', '', '', '', '', '', ''], ['Character Name:', char_name, '', 'Class:', char_class, 'Background: ', background, 'Player Name: ', play_name], ['', '', '', 'Race:', race, 'Alignment:', alignment, 'Experience Points:', '0'], ['', '', '', '', '', '', '', '', ''], ['Ability Scores: ', '', '', '', 'Armor Class:', 'Initiative:', 'Speed: ', '', ''], ['Attribute:', 'Value:', 'Modifier: ', '', '', initiative, speed, '', ''], ['Strength', strn, strn_mod, '', '', '', '', '', ''], ['Dexterity', dex, dex_mod, '', 'Hit Point Max:', HP_max, '', '', ''], ['Constitution', con, con_mod, '', '', '', '', '', ''], ['Intelligence', intl, intl_mod, '', 'Hit Dice:', hit_dice, '', '', ''], ['Wisdom', wis, wis_mod, '', '', '', '', '', ''], ['Charisma', cha, cha_mod, '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['Proficiency Bonus: ', '2', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['Saving Throws:', '', '', '', '', '', '', '', ''], ['Attribute:', 'Proficiency?:', 'Modifier:', '', '', '', '', '', ''], ['Strength', strn_prof, strn_st_mod, '', '', '', '', '', ''], ['Dexterity', dex_prof, dex_st_mod, '', '', '', '', '', ''], ['Constitution', con_prof, con_st_mod, '', '', '', '', '', ''], ['Intelligence', intl_prof, intl_st_mod, '', '', '', '', '', ''], ['Wisdom', wis_prof, wis_st_mod, '', '', '', '', '', ''], ['Charisma', cha_prof, cha_st_mod, '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['Skills:', '', '', '', '', '', '', '', ''], ['Skill:', 'Proficiency?:', 'Modifier:', '', '', '', '', '', ''], ['Acrobatics', acro_prof, acro_mod, '', '', '', '', '', ''], ['Animal Handling', anim_prof, anim_mod, '', '', '', '', '', ''], ['Arcana', arca_prof, arca_mod, '', '', '', '', '', ''], ['Athletics', athl_prof, athl_mod, '', '', '', '', '', ''], ['Deception', dece_prof, dece_mod, '', '', '', '', '', ''], ['History', hist_prof, hist_mod, '', '', '', '', '', ''], ['Insight', insi_prof, insi_mod, '', '', '', '', '', ''], ['Intimidation', inti_prof, inti_mod, '', '', '', '', '', ''], ['Investigation', inve_prof, inve_mod, '', '', '', '', '', ''], ['Medicine', medi_prof, medi_mod, '', '', '', '', '', ''], ['Nature', natu_prof, natu_mod, '', '', '', '', '', ''], ['Perception', perc_prof, perc_mod, '', '', '', '', '', ''], ['Performance', perf_prof, perf_mod, '', '', '', '', '', ''], ['Persuasion', pers_prof, pers_mod, '', '', '', '', '', ''], ['Religion', reli_prof, reli_mod, '', '', '', '', '', ''], ['Sleight of Hand', slei_prof, slei_mod, '', '', '', '', '', ''], ['Stealth', stea_prof, stea_mod, '', '', '', '', '', ''], ['Survival', surv_prof, surv_mod, '', '', '', '', '', ''], ['', '', '', '', '', '', '', '', ''], ['Passive Wisdom:', pass_wis, '', '', '', '', '', '', ''], ['']]
    sheet_string_format = ''
    for line in sheet_list_format:
        for value in line:
            sheet_string_format += (str(value) + ',')
        sheet_string_format += '\n'
    filename += '.csv'
    with open(filename, 'w') as file:
        file.write(sheet_string_format)

### Main Program ###
## forward and backward buttons ##

def go_to_page_1():
    ''' creates path to page 1 '''

    welcome.grid_forget()
    page_2.grid_forget()
    page_1.grid(row = 0, column = 0)

def go_to_page_2():
    ''' creates path to page 2 '''

    page_1.grid_forget()
    page_3.grid_forget()
    page_2.grid(row = 0, column = 0)

def go_to_page_3():
    ''' creates path to page 3 '''

    page_2.grid_forget()
    page_4.grid_forget()
    page_3.grid(row = 0, column = 0)
    
def go_to_page_4():
    ''' creates path to page 4 '''
    page_3.grid_forget()
    page_5.grid_forget()
    page_4.grid(row = 0, column = 0)

def go_to_page_5():
    ''' creates path to page 5 '''
    page_4.grid_forget()
    page_6.grid_forget()
    page_5.grid(row = 0, column = 0)
  
def go_to_page_6():
    ''' creates path to page 6 '''
    
    page_5.grid_forget()
    page_6.grid(row = 0, column = 0)

def go_to_welcome_page():
    ''' creates path to welcome page '''

    page_1.grid_forget()
    welcome.grid(row = 0, column = 0)
    
### Page 2 functions ###

def choose_race(event):
    ''' Adds extra dropdowns if Half-Elf is chosen, allowing user to select attributes '''

    global half_elf
    global half_elf_attributes
    
    if race_drop.get() == "Half-Elf":
        property_1_label.grid(row = 3, column = 0)
        property_2_label.grid(row = 4, column = 0)
        property_1.grid(row = 3, column = 1, sticky = 'w')
        property_2.grid(row = 4, column = 1, sticky = 'w')
        half_elf = True

    elif race_drop.get() != "Half-Elf" and half_elf == True:
        property_1.grid_forget()
        property_2.grid_forget()
        property_1_label.grid_forget()
        property_2_label.grid_forget()
        
        half_elf_attributes = reset_half_elf()

def reset_half_elf():
        ''' If user rechooses a non Half-Elf value, Half-Elf values are reset '''
        
        property_1.set('')
        property_2.set('')
        property_1['state'] = 'enabled'
        property_2['state'] = 'enabled' 
        property_1['values'] = half_elf_attributes_copy
        property_2['values'] = half_elf_attributes_copy
        return ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom']
        
def half_elf_values(event):
    ''' The first selected attribute will not appear in second dropdown and will be grayed out upon selection '''
    
    if property_1.get() != '' and property_1['state'] == 'enabled':
        half_elf_attributes.remove(property_1.get())
        property_2['values'] = half_elf_attributes
        property_1['state'] = 'disabled'

    if property_2.get() != '':
        half_elf_attributes.remove(property_2.get())
        property_1['values'] = half_elf_attributes
        property_2['state'] = 'disabled'

### Page 3 functions ###

def choose_class(event):
    ''' Gets chosen class and abilities from previous function. Adds extra proficiency choice for Bard if needed.'''

    char_class = str(class_drop.get())
    (hit_dice, HP_max, strn_prof, dex_prof, con_prof, intl_prof, wis_prof, cha_prof, skill_profs, skill_num) = class_select(char_class)
    prof_1['values'] = skill_profs
    prof_2['values'] = skill_profs
    prof_3['values'] = skill_profs
    prof_1.set('')
    prof_2.set('')
    prof_3.set('')
    print(skill_profs)
    global init_profs
    init_profs = skill_profs
    if class_drop.get() != 'Bard' and class_drop.get() != '':
        prof_1['state'] = 'enabled'
        prof_2['state'] = 'enabled'
        prof_3['state'] = 'disabled'
    elif class_drop.get() == 'Bard':
        prof_1['state'] = 'enabled'
        prof_2['state'] = 'enabled'
        prof_3['state'] = 'enabled'

### Page 4 functions ###

def select_prof(event):
    ''' Adds selected proficiencies to list, removes previous selections from list. '''

    if prof_1.get() != '':
        proficiencies = list(prof_1['values'])
        proficiencies.remove(prof_1.get())
        prof_1['state'] = 'disabled'
        
        if prof_2.get() == '':
            prof_2['values'] = proficiencies
        if prof_3.get() == '':
            prof_3['values'] = proficiencies
            
    if prof_2.get() != '':
        proficiencies = list(prof_2['values'])
        proficiencies.remove(prof_2.get())
        prof_2['state'] = 'disabled'
        
        if prof_1.get() == '':
            prof_1['values'] = proficiencies
        if prof_3.get() == '':
            prof_3['values'] = proficiencies
            
    if prof_3.get() != '':
        proficiencies = list(prof_3['values'])
        proficiencies.remove(prof_3.get())
        prof_3['state'] = 'disabled'
        
        if prof_1.get() == '':
            prof_1['values'] = proficiencies
        if prof_2.get() == '':
            prof_2['values'] = proficiencies

### page 5 functions ###

def roll_dice():
    ''' rolls dice using stat roller function and limits user to one roll '''

    print(stat_roller())
    dice_nums = stat_roller()
    roll_button['state'] = 'disabled'
    tk.Label(page_5, text = dice_nums).grid(row = 0, column = 1)

    strn_input['values'] = dice_nums
    dex_input['values'] = dice_nums
    con_input['values'] = dice_nums
    intl_input['values'] = dice_nums
    wis_input['values'] = dice_nums
    cha_input['values'] = dice_nums

    strn_input['state'] = 'enabled'
    dex_input['state'] = 'enabled'
    con_input['state'] = 'enabled'
    intl_input['state'] = 'enabled'
    wis_input['state'] = 'enabled'
    cha_input['state'] = 'enabled'

def ability_score_values(event):
    if strn_input.get() != '':
        rem_dice = list(strn_input['values'])
        rem_dice.remove(strn_input.get())
        strn_input['state'] = 'disabled'
        
        if dex_input.get() == '':
            dex_input['values'] = rem_dice
        if con_input.get() == '':
            con_input['values'] = rem_dice        
        if intl_input.get() == '':
            intl_input['values'] = rem_dice
        if wis_input.get() == '':
            wis_input['values'] = rem_dice
        if cha_input.get() == '':
            cha_input['values'] = rem_dice

    if dex_input.get() != '':
        rem_dice = list(dex_input['values'])
        rem_dice.remove(dex_input.get())
        dex_input['state'] = 'disabled'
        
        if strn_input.get() == '':
            strn_input['values'] = rem_dice
        if con_input.get() == '':
            con_input['values'] = rem_dice        
        if intl_input.get() == '':
            intl_input['values'] = rem_dice
        if wis_input.get() == '':
            wis_input['values'] = rem_dice
        if cha_input.get() == '':
            cha_input['values'] = rem_dice

    if con_input.get() != '':
        rem_dice = list(con_input['values'])
        rem_dice.remove(con_input.get())
        con_input['state'] = 'disabled'
        
        if strn_input.get() == '':
            strn_input['values'] = rem_dice
        if dex_input.get() == '':
            dex_input['values'] = rem_dice        
        if intl_input.get() == '':
            intl_input['values'] = rem_dice
        if wis_input.get() == '':
            wis_input['values'] = rem_dice
        if cha_input.get() == '':
            cha_input['values'] = rem_dice
    
    if intl_input.get() != '':
        rem_dice = list(intl_input['values'])
        rem_dice.remove(intl_input.get())
        intl_input['state'] = 'disabled'
        
        if strn_input.get() == '':
            strn_input['values'] = rem_dice
        if dex_input.get() == '':
            dex_input['values'] = rem_dice        
        if con_input.get() == '':
            con_input['values'] = rem_dice
        if wis_input.get() == '':
            wis_input['values'] = rem_dice
        if cha_input.get() == '':
            cha_input['values'] = rem_dice

    if wis_input.get() != '':
        rem_dice = list(wis_input['values'])
        rem_dice.remove(wis_input.get())
        wis_input['state'] = 'disabled'
        
        if strn_input.get() == '':
            strn_input['values'] = rem_dice
        if dex_input.get() == '':
            dex_input['values'] = rem_dice        
        if con_input.get() == '':
            con_input['values'] = rem_dice
        if intl_input.get() == '':
            intl_input['values'] = rem_dice
        if cha_input.get() == '':
            cha_input['values'] = rem_dice

    if cha_input.get() != '':
        rem_dice = list(cha_input['values'])
        rem_dice.remove(cha_input.get())
        cha_input['state'] = 'disabled'
        
        if strn_input.get() == '':
            strn_input['values'] = rem_dice
        if dex_input.get() == '':
            dex_input['values'] = rem_dice        
        if con_input.get() == '':
            con_input['values'] = rem_dice
        if intl_input.get() == '':
            intl_input['values'] = rem_dice
        if wis_input.get() == '':
            wis_input['values'] = rem_dice
            
### Page 6 functions ###

def finale():
    ''' getting and formatting all previous variables '''
    #Identity
    char_name = char_input.get()
    background = background_input.get()
    play_name = username_input.get()
    alignment = alignment_input.get()

    #Race
    race = race_drop.get()
    (strn, dex, con, intl, wis, cha, speed) = race_select(race)

    if race == 'Half-Elf':
        stat = property_1.get()
        (strn, dec, con, intl, wis, cha) = half_elf_atribute_add(stat, strn, dex, con, intl, wis, cha)
        stat = property_2.get()
        (strn, dec, con, intl, wis, cha) = half_elf_atribute_add(stat, strn, dex, con, intl, wis, cha)

    #Class
    char_class = str(class_drop.get())
    (hit_dice, HP_max, strn_prof, dex_prof, con_prof, intl_prof, wis_prof, cha_prof, skill_profs, skill_num) = class_select(char_class)
    
    #Ability Scores
    
    strn += int(strn_input.get())
    dex += int(dex_input.get())
    con += int(con_input.get())
    intl += int(intl_input.get())
    wis += int(wis_input.get())
    cha += int(cha_input.get())
    
    (strn_mod, dex_mod, con_mod, intl_mod, wis_mod, cha_mod) = ability_score_mod(
    strn, dex, con, intl, wis, cha)

    #Saving Throws
    (strn_st_mod, dex_st_mod, con_st_mod, intl_st_mod, wis_st_mod, cha_st_mod) = saving_throw_bonus(strn_prof, dex_prof, con_prof, intl_prof, wis_prof, cha_prof, strn_mod, dex_mod, con_mod, intl_mod, wis_mod, cha_mod)

    #Skills
    (acro_mod, anim_mod, arca_mod, athl_mod, dece_mod, hist_mod, insi_mod, inti_mod, inve_mod, medi_mod, natu_mod, perc_mod, perf_mod, pers_mod, reli_mod, slei_mod, stea_mod, surv_mod) = skill_mod(strn_mod, dex_mod, con_mod, intl_mod, wis_mod, cha_mod)

    skill_prof_choices = [prof_1.get(), prof_2.get(), prof_3.get()]
    (acro_prof, anim_prof, arca_prof, athl_prof, dece_prof, hist_prof, insi_prof, inti_prof, inve_prof, medi_prof, natu_prof, perc_prof, perf_prof, pers_prof, reli_prof, slei_prof, stea_prof, surv_prof, skill_prof) = skill_prof_marker(skill_prof_choices)
    
    (acro_mod, anim_mod, arca_mod, athl_mod, dece_mod, hist_mod, insi_mod, inti_mod, inve_mod, medi_mod, natu_mod, perc_mod, perf_mod, pers_mod, reli_mod, slei_mod, stea_mod, surv_mod) = skill_prof_bonus(acro_mod, anim_mod, arca_mod, athl_mod, dece_mod, hist_mod, insi_mod, inti_mod, inve_mod, medi_mod, natu_mod, perc_mod, perf_mod, pers_mod, reli_mod, slei_mod, stea_mod, surv_mod, skill_prof)

    #misc
    (pass_wis, HP_max, initiative) = misc_stats(dex_mod, con_mod, HP_max, perc_mod)

    #formatting
    filename = str(file_name_input.get())
    char_sheet_format(char_name, char_class, background, play_name, race, alignment, strn, strn_mod, dex, dex_mod, con, con_mod, intl, intl_mod, wis, wis_mod, cha, cha_mod, initiative, speed, HP_max, hit_dice, strn_prof, strn_st_mod, dex_prof, dex_st_mod, con_prof, con_st_mod, intl_prof, intl_st_mod, wis_prof, wis_st_mod, cha_prof, cha_st_mod, acro_prof, acro_mod, anim_prof, anim_mod, arca_prof, arca_mod, athl_prof, athl_mod, dece_prof, dece_mod, hist_prof, hist_mod, insi_prof, insi_mod, inti_prof, inti_mod, inve_prof, inve_mod, medi_prof, medi_mod, natu_prof, natu_mod, perc_prof, perc_mod, perf_prof, perf_mod, pers_prof, pers_mod, reli_prof, reli_mod, slei_prof, slei_mod, stea_prof, stea_mod, surv_prof, surv_mod, pass_wis, filename)
    home.destroy()

# set up tkinter environment
home = tk.Tk()
home.title("Birth a New Soul Into This Realm.")
home.geometry("400x400")

########## Welcome Page ##########
welcome = tk.LabelFrame(home, text = "Instructions", padx=10, pady = 10)
welcome.grid(row = 0, column = 0, sticky = 's')

# add some text
tk.Message(welcome, text = 'Welcome to the D&D 5E 1st level character creator. This program is designed to assist in the creation of first level characters for the fifth edition of D&D. You will begin by inputting the identifying characteristics of your character such as their name, background, and alignment. Next you will choose a race for your character. After that, you will choose a class for your character as well as the skills they are proficient in. Next, you wil roll 6 numbers and assign each of those to your ability scores. Finally, you will choose a name for your character sheet to be saved to. This character sheet will be saved as a .csv file with a layout similar to the D&D 5E character sheet. Have fun!', justify = 'center').grid(row = 0, column = 0)

# add a 'next page' button
page_1_button = tk.Button(welcome, text = "Page 1", command = go_to_page_1)
page_1_button.grid(row = 1, column = 0, sticky = 's')

########## PAGE 1: Identity ##########
page_1 = tk.LabelFrame(home, text = "Page 1", padx = 10, pady = 10)

# create text boxes and labels for character and player name
char_name_label = tk.Label(page_1, text = "Character name: ", width = 20)
char_name_label.grid(row = 0, column = 0)

char_input = tk.Entry(page_1, width = 15)
char_input.grid(row = 0, column = 1)

user_name_label = tk.Label(page_1, text = "Player name: ", width = 20)
user_name_label.grid(row = 1, column = 0)

username_input = tk.Entry(page_1, width = 15)
username_input.grid(row = 1, column = 1)

# create dropdowns and labels for character background and alignment
choose_background_label = tk.Label(page_1, text = "Background: ")
choose_background_label.grid(row = 2, column = 0)

background_input = ttk.Combobox(page_1, width = 12)
background_input['values'] = ["Acolyte", "Charlatan", "Criminal", "Entertainer", "Folk Hero", "Guild Artisan", "Hermit", "Ranger", "Noble", "Outlander", "Sage", "Sailor", "Soldier", "Urchin"]
background_input.grid(row = 2, column = 1, sticky = 'e')

choose_alignment_label = tk.Label(page_1, text = "Alignment: ")
choose_alignment_label.grid(row = 3, column = 0)

alignment_input = ttk.Combobox(page_1, width = 12)
alignment_input['values'] = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "True Neutral", "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil"]
alignment_input.grid(row = 3, column = 1, sticky = 'e')

# create "last page" and "next page" buttons
tk.Label(page_1, text = '   ').grid(row = 4, columnspan = 2)

back_button = tk.Button(page_1, text = 'Back', command = go_to_welcome_page)
back_button.grid(row = 5, column = 0, sticky = 'sw')

page_2_button = tk.Button(page_1, text = 'Page 2', command = go_to_page_2)
page_2_button.grid(row = 5, column = 1, sticky = 'se')

#variable assignment
char_name = char_input.get()
background = background_input.get()
play_name = username_input.get()
alignment = alignment_input.get()

########## PAGE 2: Race ##########
page_2 = tk.LabelFrame(home, text = "Page 2", padx = 10, pady = 10)

# half_elf boolean is used to determine if dropdown has been selected as half elf before
half_elf = False
# values for half elf attributes
half_elf_attributes = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom']
half_elf_attributes_copy = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom']

# add some text in an orderly fashion
races = ("Dragonborn:\n" + 
                  "Dwarf:\n" + 
                  "Elf:\n" + 
                  "Gnome:\n" + 
                  "Half-Elf:\n" + 
                  "Halfling:\n" +
                  "Half-Orc:\n" +
                  "Human:\n" +
                  "Tiefling: ") 
ability_scores = ("+2 Strength, +1 Charisma\n" +
                  "+2 Constitution\n" +
                  "+2 Dexterity\n" +
                  "+2 Intelligence\n" +
                  "+2 Charisma, +1 to two others\n" +
                  "+2 Dexterity\n" +
                  "+2 Strength, +1 Constitution\n" +
                  "+1 to all ability scores\n" +
                  "+2 Charisma, +1 intelligence\n")
tk.Message(page_2, text = races, justify = 'left').grid(row = 0, column = 0, sticky = 'nw')
tk.Message(page_2, text = ability_scores, justify = 'left').grid(row = 0, column = 1, sticky = 'ne')

# dropdown to choose race
race_drop_label = tk.Label(page_2, text = "Race:", width = 12)
race_drop_label.grid(row = 2, column = 0)

race_drop = ttk.Combobox(page_2, width = 12)
race_drop['values'] = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling", "Half-Orc", "Human", "Tiefling"]
race_drop.grid(row = 2, column = 1, sticky = 'w')
race_drop.bind("<<ComboboxSelected>>", choose_race)

# create dropdowns for when half elf is chosen
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

# "last page" and "next page" buttons
tk.Label(page_2, text = '     ').grid(row = 5, columnspan = 2)
page_1_button_2 = tk.Button(page_2, text = "Page 1", command = go_to_page_1)
page_1_button_2.grid(row = 6, column = 0, sticky = 'w')

page_3_button = tk.Button(page_2, text = "Page 3", command = go_to_page_3)
page_3_button.grid(row = 6, column = 1, sticky = 'e')

########## PAGE 3: Class ##########
page_3 = tk.LabelFrame(home, text = "Page 3", padx = 10, pady = 10)

# create a dropdown for class
class_drop_label = tk.Label(page_3, width = 12, text = "Class:")
class_drop_label.grid(row = 1, column = 0)

class_drop = ttk.Combobox(page_3, width = 12)
class_drop['values'] = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
class_drop.grid(row = 1, column = 1, sticky = 'e')
class_drop.bind("<<ComboboxSelected>>", choose_class)

#display some text for the user in an orderly fashion
classes = ("Barbarian:\nBard:\nCleric:\nDruid:\nFighter:\nMonk:\nPaladin:\nRanger:\nRogue:\nSorcerer:\nWarlock:\nWizard:\n")
primary_abilities = ("Strength\nCharisma\nWisdom\nWisdom\nStrength or Dexterity\nDexterity & Wisdom\nStrength & Charisma\nDexterity & Wisdom\nDexterity\nCharisma\nCharisma\nIntelligence")

tk.Message(page_3, text = classes, justify = 'left').grid(row = 0, column = 0, sticky = 'nw')
tk.Message(page_3, text = primary_abilities, justify = 'left').grid(row = 0, column = 1, sticky = 'ne')

# "last page" and "next page" buttons
tk.Label(page_3, text = '     ').grid(row = 4, columnspan = 2)
page_2_button_2 = tk.Button(page_3, text = "Page 2", command = go_to_page_2)
page_2_button_2.grid(row = 5, column = 0, sticky = 'w')

page_4_button = tk.Button(page_3, text = "Page 4", command = go_to_page_4)
page_4_button.grid(row = 5, column = 1, sticky = 'e')

########## PAGE 4: Proficiency ##########
page_4 = tk.LabelFrame(home, text = "Page 4", padx = 10, pady = 10)

# create dropdowns for 3 proficiencies
prof_1_label = tk.Label(page_4, text = "Prof. 1", width = 12)
prof_1_label.grid(row = 0, column = 0)

prof_1 = ttk.Combobox(page_4, width = 12)
prof_1.grid(row = 0, column = 1)
prof_1['state'] = 'disabled'
prof_1.bind("<<ComboboxSelected>>", select_prof)

prof_2_label = tk.Label(page_4, text = "Prof. 2", width = 12)
prof_2_label.grid(row = 1, column = 0)

prof_2 = ttk.Combobox(page_4, width = 12)
prof_2.grid(row = 1, column = 1)
prof_2['state'] = 'disabled'
prof_2.bind("<<ComboboxSelected>>", select_prof)


prof_3_label = tk.Label(page_4, text = "Prof. 3", width = 12)
prof_3_label.grid(row = 2, column = 0)

prof_3 = ttk.Combobox(page_4, width = 12)
prof_3.grid(row = 2, column = 1)
prof_3['state'] = 'disabled'
prof_3.bind("<<ComboboxSelected>>", select_prof)

# "next page" and "last page" buttons
tk.Label(page_4, text = '     ').grid(row = 5, columnspan = 2)
page_3_button_2 = tk.Button(page_4, text = "Page 3", command = go_to_page_3)
page_3_button_2.grid(row = 6, column = 0, sticky = 'w')

page_5_button = tk.Button(page_4, text = "Page 5", command = go_to_page_5)
page_5_button.grid(row = 6, column = 1, sticky = 'e')

########## PAGE 5: Ability Scores ##########
page_5 = tk.LabelFrame(home, text = 'Page 5', padx = 10, pady = 20)

# create dropdowns for each ability score modifier
strn_label = tk.Label(page_5, text = 'Strength:', width = 12)
strn_label.grid(row = 1, column = 0, sticky = 'w')

strn_input = ttk.Combobox(page_5, width = 12)
strn_input.grid(row = 1, column = 1, sticky = 'e')
strn_input.bind("<<ComboboxSelected>>", ability_score_values)

dex_label = tk.Label(page_5, text = 'Dexterity:', width = 12)
dex_label.grid(row = 2, column = 0, sticky = 'w')

dex_input = ttk.Combobox(page_5, width = 12)
dex_input.grid(row = 2, column = 1, sticky = 'e')
dex_input.bind("<<ComboboxSelected>>", ability_score_values)

con_label = tk.Label(page_5, text = 'Constituion:', width = 12)
con_label.grid(row = 3, column = 0, sticky = 'w')

con_input = ttk.Combobox(page_5, width = 12)
con_input.grid(row = 3, column = 1, sticky = 'e')
con_input.bind("<<ComboboxSelected>>", ability_score_values)

intl_label = tk.Label(page_5, text = 'Intelligence:', width = 12)
intl_label.grid(row = 4, column = 0, sticky = 'w')

intl_input = ttk.Combobox(page_5, width = 12)
intl_input.grid(row = 4, column = 1, sticky = 'e')
intl_input.bind("<<ComboboxSelected>>", ability_score_values)

wis_label = tk.Label(page_5, text = 'Wisdom:', width = 12)
wis_label.grid(row = 5, column = 0, sticky = 'w')

wis_input = ttk.Combobox(page_5, width = 12)
wis_input.grid(row = 5, column = 1, sticky = 'e')
wis_input.bind("<<ComboboxSelected>>", ability_score_values)

cha_label = tk.Label(page_5, text = 'Charisma:', width = 12)
cha_label.grid(row = 6, column = 0, sticky = 'w')

cha_input = ttk.Combobox(page_5, width = 12)
cha_input.grid(row = 6, column = 1, sticky = 'e')
cha_input.bind("<<ComboboxSelected>>", ability_score_values)

# create a button that "rolls the die"
roll_button = tk.Button(page_5, text = "Roll", command = roll_dice)
roll_button.grid(row = 0, column = 0)

# "last page" and "next page" buttons
tk.Label(page_5, text = "    ").grid(row = 9, columnspan = 2)
page_4_button_2 = tk.Button(page_5, text = "Page 4", command = go_to_page_4)
page_4_button_2.grid(row = 10, column = 0, sticky = 'w')

page_6_button = tk.Button(page_5, text = "Page 6", command = go_to_page_6)
page_6_button.grid(row = 10, column = 1, sticky = 'e')

########## Page 6: File Name and Exit ##########
page_6 = tk. LabelFrame(home, text = "Choose a file name for the Character Sheet", padx = 10, pady = 10)

# create text box for output file name
file_name_label = tk.Label(page_6, text = "File Name: ", width = 20)
file_name_label.grid(row = 0, column = 0)

file_name_input = tk.Entry(page_6, width = 15)
file_name_input.grid(row = 0, column = 1)

# "last page" and "save and exit" buttons
tk.Label(page_6, text = '     ').grid(row = 1, columnspan = 2)
page_5_button_2 = tk.Button(page_6, text = "Page 5", command = go_to_page_5)
page_5_button_2.grid(row = 2, column = 0, sticky = 'w')

page_6_exit_button = tk.Button(page_6, text = "Save & Exit", command = finale)
page_6_exit_button.grid(row = 2, column = 1, sticky = 'e')

tk.mainloop()                                                                                                                                                                                                                                                                                                                                                                                                                                           