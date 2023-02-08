# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 18:35:33 2020

@author: garre
"""

import tkinter as tk
from tkinter import ttk
from ENGR102_Final_Project import stat_roller

half_elf = False
half_elf_attributes = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom']
half_elf_attributes_copy = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom']

dice_roll = stat_roller()


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

def choose_die(event):
    global dice_roll
    global strength
    global dexterity
    global constitution
    global intelligence
    global wisdom
    global charisma

    if strength.get() != '' and strength['state'] == 'enabled':
        dice_roll.remove(int(strength.get()))
        dexterity['values'] = dice_roll
        constitution['values'] = dice_roll
        intelligence['values'] = dice_roll
        wisdom['values'] = dice_roll
        charisma['values'] = dice_roll
        strength['state'] = 'disabled'
        
    elif dexterity.get() != '' and dexterity['state'] == 'enabled':
        dice_roll.remove(int(dexterity.get()))
        strength['values'] = dice_roll
        constitution['values'] = dice_roll
        intelligence['values'] = dice_roll
        wisdom['values'] = dice_roll
        charisma['values'] = dice_roll
        dexterity['state'] = 'disabled'
        
    elif constitution.get() != '' and constitution['state'] == 'enabled':
        dice_roll.remove(int(constitution.get()))
        strength['values'] = dice_roll
        dexterity['values'] = dice_roll
        intelligence['values'] = dice_roll
        wisdom['values'] = dice_roll
        charisma['values'] = dice_roll
        constitution['state'] = 'disabled'
        
    elif intelligence.get() != '' and intelligence['state'] == 'enabled':
        dice_roll.remove(int(intelligence.get()))
        strength['values'] = dice_roll
        constitution['values'] = dice_roll
        dexterity['values'] = dice_roll
        wisdom['values'] = dice_roll
        charisma['values'] = dice_roll
        intelligence['state'] = 'disabled'
        
    elif wisdom.get() != '' and wisdom['state'] == 'enabled':
        dice_roll.remove(int(wisdom.get()))
        strength['values'] = dice_roll
        constitution['values'] = dice_roll
        intelligence['values'] = dice_roll
        dexterity['values'] = dice_roll
        charisma['values'] = dice_roll
        wisdom['state'] = 'disabled'
        
    elif charisma.get() != '' and charisma['state'] == 'enabled':
        dice_roll.remove(int(charisma.get()))
        strength['values'] = dice_roll
        constitution['values'] = dice_roll
        intelligence['values'] = dice_roll
        wisdom['values'] = dice_roll
        dexterity['values'] = dice_roll
        charisma['state'] = 'disabled'
    
def reset_dice_roll():
    global dice_roll
    global strength
    global dexterity
    global constitution
    global intelligence
    global wisdom
    global charisma
    
    strength['state'] = 'enabled'
    dexterity['state'] = 'enabled'
    constitution['state'] = 'enabled'
    intelligence['state'] = 'enabled'
    wisdom['state'] = 'enabled'
    charisma['state'] = 'enabled'
    
    strength['values'] = dice_roll
    dexterity['values'] = dice_roll
    constitution['values'] = dice_roll
    intelligence['values'] = dice_roll
    wisdom['values'] = dice_roll
    charisma['values'] = dice_roll
    
    strength.set('')
    dexterity.set('')
    constitution.set('')
    intelligence.set('')
    wisdom.set('')
    charisma.set('')

# def choose_class(event):
    # global class_label
    # class_label['text'] = class_drop.get()

# def choose_background(event):
#     global background_label
#     background_label['text'] = background_drop.get()
    
def page_2():
    # outfile = open("character.txt", "w")
    # outfile.write(user_name + '\n')
    # outfile.write(char_name + '\n')
    # outfile.write(user_race + '\n')
    # outfile.write(user_class + '\n')
    # outfile.write(user_background + '\n')
    # outfile.close()
    frame.grid_forget()
    frame2.grid(row = 0, column = 0, sticky = 'n')
    
def page_1():
    # ability_score_mod(strength.get(), dexterity.get(), constitution.get(), intelligence.get(), wisdom.get(), charisma.get())
    frame2.grid_forget()
    frame.grid(row = 0, column = 0, sticky = 'n')

def save_and_exit():
    home.destroy()

home = tk.Tk()
home.title("Birth a new soul into this realm")  
home.configure(bg = '#738073')

########## PAGE 1 ##########

frame = tk.LabelFrame(home, padx = 10, pady = 10, fg = 'white', bg = '#8b998b')
frame.grid(row = 0, column = 0, sticky = 'n')

char_name = tk.Entry(frame, width = 43)
char_name.insert(0, "Enter your character's name")
char_name.grid(row = 0, column = 0, columnspan = 2)

user_name = tk.Entry(frame, width = 43)
user_name.insert(0, "Enter your name")
user_name.grid(row = 1, column = 0, columnspan = 2)

# first-column labels
## race
property_1_label = tk.Label(frame, text = 'Half-Elf Attr. 1', bg = '#8b998b', fg = 'white')
property_2_label = tk.Label(frame, text = 'Half-Elf Attr. 2', bg = '#8b998b', fg = 'white')

choose_race_label = tk.Label(frame, width = 10, text = 'Race: ', bg = '#8b998b', fg = 'white')
choose_race_label.grid(row = 2, column = 0)

## class
choose_class_label = tk.Label(frame, width = 10, text = "Class: ", bg = '#8b998b', fg = 'white')
choose_class_label.grid(row = 5, column = 0)

## background
choose_background_label = tk.Label(frame, text = "Background: ", bg = '#8b998b', fg = 'white')
choose_background_label.grid(row = 7, column = 0)

## alignment
choose_alignment_label = tk.Label(frame, text = "Alignment: ", bg = '#8b998b', fg = 'white')
choose_alignment_label.grid(row = 8, column = 0)


# dropdowns
## race
race_drop = ttk.Combobox(frame, width = 12)
race_drop['values'] = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", 
                       "Halfling", "Half-Orc", "Human", "Tiefling"]
race_drop.grid(row = 2, column = 1, sticky = 'e')
race_drop.bind("<<ComboboxSelected>>", choose_race)

property_1 = ttk.Combobox(frame, width = 12)
property_1['values'] = half_elf_attributes
property_1.bind("<<ComboboxSelected>>", half_elf_values)
property_1['state'] = 'enabled'

property_2 = ttk.Combobox(frame, width = 12)
property_2['values'] = half_elf_attributes
property_2.bind("<<ComboboxSelected>>", half_elf_values)
property_2['state'] = 'enabled'

## class and skill proficiency
class_drop = ttk.Combobox(frame, width = 12)
class_drop['values'] = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", 
                       "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", 
                       "Warlock", "Wizard"]
class_drop.grid(row = 5, column = 1, sticky = 'e')
# class_drop.bind("<<ComboboxSelected>>", choose_class)

## background
background_drop = ttk.Combobox(frame, width = 12)
background_drop['values'] = ["Acolyte", "Charlatan", "Criminal", "Entertainer", 
                        "Folk Hero", "Guild Artisan", "Hermit", "Ranger", 
                        "Noble", "Outlander", "Sage", "Sailor", "Soldier", 
                        "Urchin"]
background_drop.grid(row = 7, column = 1, sticky = 'e')
# background_drop.bind("<<ComboboxSelected>>", choose_background)

## alignment
alignment_drop = ttk.Combobox(frame, width = 12)
alignment_drop['values'] = ["Lawful Good", "Neutral Good", "Chaotic Good", 
                            "Lawful Neutral", "True Neutral", "Chaotic Neutral", 
                            "Lawful Evil", "Neutral Evil", "Chaotic Evil"]
alignment_drop.grid(row = 8, column = 1, sticky = 'e')

# # third-column labels
# ## race
# race_label = tk.Label(frame, width = 12,
#                       bg = "#8b998b", fg = 'white')
# race_label.grid(row = 2, column = 2)

# ## class
# class_label = tk.Label(frame, width = 12,
#                       bg = "#8b998b", fg = 'white')
# class_label.grid(row = 3, column = 2)

# ## background
# background_label = tk.Label(frame, width = 12,
#                       bg = "#8b998b", fg = 'white')
# background_label.grid(row = 4, column = 2)

########## PAGE 2 ##########

# setup frame
frame2 = tk.LabelFrame(home, padx = 10, pady = 10, fg = 'white', bg = '#8b998b')

# create label with dice numbers
die_results = tk.Label(frame2, text = dice_roll, bg = '#8b998b', fg = 'white').grid(row = 0, column = 1)

# create dropdowns and labels for each ability
strength_label = tk.Label(frame2, text = "Strength:", bg = '#8b998b', fg = 'white').grid(row = 1, column = 0, sticky = 'w')
strength = ttk.Combobox(frame2, width = 6)
strength['values'] = dice_roll
strength.grid(row = 1, column = 1, columnspan = 2, sticky = 'e')
strength.bind("<<ComboboxSelected>>", choose_die)

dexterity_label = tk.Label(frame2, text = "Dexterity:", bg = '#8b998b', fg = 'white').grid(row = 2, column = 0, sticky = 'w')
dexterity = ttk.Combobox(frame2, width = 6)
dexterity['values'] = dice_roll
dexterity.grid(row = 2, column = 1, columnspan = 2, sticky = 'e')
dexterity.bind("<<ComboboxSelected>>", choose_die)

constitution_label = tk.Label(frame2, text = "Constitution:", bg = '#8b998b', fg = 'white').grid(row = 3, column = 0, sticky = 'w')
constitution = ttk.Combobox(frame2, width = 6)
constitution['values'] = dice_roll
constitution.grid(row = 3, column = 1, columnspan = 2, sticky = 'e')
constitution.bind("<<ComboboxSelected>>", choose_die)

intelligence_label = tk.Label(frame2, text = "Intelligence:", bg = '#8b998b', fg = 'white').grid(row = 4, column = 0, sticky = 'w')
intelligence = ttk.Combobox(frame2, width = 6)
intelligence['values'] = dice_roll
intelligence.grid(row = 4, column = 1, columnspan = 2, sticky = 'e')
intelligence.bind("<<ComboboxSelected>>", choose_die)

wisdom_label = tk.Label(frame2, text = "Wisdom:", bg = '#8b998b', fg = 'white').grid(row = 5, column = 0, sticky = 'w')
wisdom = ttk.Combobox(frame2, width = 6)
wisdom['values'] = dice_roll
wisdom.grid(row = 5, column = 1, columnspan = 2, sticky = 'e')
wisdom.bind("<<ComboboxSelected>>", choose_die)

charisma_label = tk.Label(frame2, text = "Charisma:", bg = '#8b998b', fg = 'white').grid(row = 6, column = 0, sticky = 'w')
charisma = ttk.Combobox(frame2, width = 6)
charisma['values'] = dice_roll
charisma.grid(row = 6, column = 1, columnspan = 2, sticky = 'e')
charisma.bind("<<ComboboxSelected>>", choose_die)

strength['state'] = 'enabled'
dexterity['state'] = 'enabled'
constitution['state'] = 'enabled'
intelligence['state'] = 'enabled'
wisdom['state'] = 'enabled'
charisma['state'] = 'enabled'

# make a reset button
reset_button = tk.Button(frame2, width = 6, text = "Reset", command = reset_dice_roll)
reset_button.grid(row = 0, sticky = 'w', columnspan = 3)



# page buttons and labels

page_1_button = tk.Button(frame2, text = "Page 1", command = page_1)
page_1_button.grid(row = 7, column = 0, sticky = 'sw')

page_3_button = tk.Button(frame2, text = 'Page 3')
page_3_button.grid(row = 7, column = 1, sticky = 'se')

page_2_button = tk.Button(frame, text = 'Page 2', command = page_2)
page_2_button.grid(row = 9, column = 1, sticky = 'se')

page_1_label = tk.Label(frame, text = "Page 1", fg = 'white', bg = '#8b998b').grid(row = 9, column = 0, sticky = 's', columnspan = 2)

page_2_label = tk.Label(frame2, text = "Page 2", fg = 'white', bg = '#8b998b').grid(row = 7, column = 0, columnspan = 2, sticky = 's')


########## Status Frame ##########

# status_frame = tk.LabelFrame(home, text = "Current Score")
# status_frame.grid(row = 1, column = 0)

# ability_score = tk.Label(status_frame, width = 10, text = 0)
# ability_score.grid(row = 0, column = 04

########## Message Frame ##########

directory_frame = tk.LabelFrame(home, text = "Race Ability Scores", padx = 10, pady = 10, bg = "#f5f0ce")
directory_frame.grid(row = 2, column = 0, sticky = 's')

races = ("Bloodborn:\n" + 
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
                  "+2 Charisma, +1 to two other ability scores\n" +
                  "+2 Dexterity\n" +
                  "+2 Strength, +1 Constitution\n" +
                  "+1 to all ability scores\n" +
                  "+2 Charisma, +1 intelligence\n")
tk.Message(directory_frame, text = races, width = 2000, justify = 'left', bg = "#f5f0ce").grid(row = 0, column = 0, sticky = 'nw')
tk.Message(directory_frame, text = ability_scores, width = 2000, justify = 'left', bg = '#f5f0ce').grid(row = 0, column = 1, sticky = 'ne')

output_file_name = tk.Entry(home, width = 41, border = 4)
output_file_name.grid(row = 3, column = 0, sticky = 'ne')
output_file_name.insert(0, "Output.txt")
save_and_exit_button = tk.Button(home, text = "Save and Exit", height = 1, command = save_and_exit).grid(row = 3, column = 0, sticky = 'sw')


tk.mainloop()


