#
# Created by Kastra on Asura.
# Feel free to /tell in game or send a PM on FFXIAH you have questions, comments, or suggestions.
#
# Version date: 2022 February 26
#
# This file contains a list of all gear to be considered.
# "Name" is the item name as seen in-game. "Name" is used to pull the correct item ID from the equipviewer icons to create the fancy plot in the end.
# "Name2" is the same as "Name", but it includes augment paths. "Name2" is only used to distinguish between augment paths. Not all items need a "Name2". This is the reason the main code uses so many try/except blocks...
# "Skill Type" for weapons is the weapon type (katana, club, sword, etc) that gains some amount of skill.
# "Type" is used exclusively for melee, ranged, and ammo slots. "Type" is used for the code to distinguish between a grip and an off-hand weapon such that a grip in the off-hand does not trigger an off-hand attack. The options are "weapon", "grip", "ranged", "ammo", "shuriken", "throwing".
# Augmented gear shows its augmented stats as additions to the base stats. For example: Heishi has "159+7" DMG and "0+30" Accuracy when fully augmented. This isn't necessary, but it makes the book-keeping much easier.
# "jobs" is the list of jobs that can use the item. Still in-progress, but with no immediate plans for it.

# The last dictionary key for each gear piece is the jobs that can wear it. This is used to quickly gather all pieces of gear that a job can wear to be tested. (if 'nin' in jobs). Future work.
all_jobs = ['war','mnk','whm','blm','rdm','thf','pld','drk','bst','brd','rng','smn','sam','nin','drg','blu','cor','pup','dnc','sch','geo','run']

Empty = {'Name': 'Empty'}

Grape_Daifuku = {'Name': 'Grape Daifuku', 'Type':'Food','STR':2, 'VIT':3, 'Attack':50, 'Ranged Attack':50, 'Accuracy':80, 'Ranged Accuracy':80, 'Magic Attack':3}
Sublime_Sushi = {'Name': 'Sublime Sushi', 'Type':'Food','STR':6, 'DEX':7, 'MND':-3, 'CHR':6, 'Accuracy':100, 'Ranged Accuracy':100}

# If adding new weapons, you must include a dictionary key for "Skill Type", "Type", "DMG", and "Delay". Use the entries already present as examples
Amanomurakumo = {'Name': 'Amanomurakumo', 'Name2': 'Amanomurakumo R15', 'Skill Type': 'Great Katana', 'Type':'Weapon', 'DMG': 308+18, 'Delay': 437, 'Accuracy': 60, 'Great Katana Skill': 269, 'Magic Accuracy Skill': 228, 'Store TP':10, 'Skillchain Bonus':5, 'Jobs':[]}
Anguta = {'Name': "Anguta", 'Name2': "Anguta R15", 'Skill Type': 'Scythe', 'Type':'Weapon', 'DMG':370+17, 'Delay':528, 'Magic Damage':186, 'Scythe Skill':269, 'Magic Accuracy Skill':242, 'Accuracy':0+30, 'Magic Accuracy':0+30, 'Store TP':10,}
Apocalypse = {'Name': "Apocalypse", 'Name2': "Apocalypse R15", 'Skill Type': 'Scythe', 'Type':'Weapon', 'DMG':362+21, 'Delay':513, 'Magic Damage':217, 'Scythe Skill':269, 'Magic Accuracy Skill':242, 'Accuracy':60+15, 'JA Haste':10,}
Crepuscular_Knife = {'Name': 'Twilight Knife', 'Name2': 'Crepuscular Knife', 'Skill Type': 'Dagger', 'Type':'Weapon', 'DMG':133, 'Delay':190, 'DEX':15, 'AGI':15, 'CHR':15, 'Accuracy':40, 'Magic Accuracy':40, 'Dagger Skill':248, 'Magic Accuracy Skill':248, 'QA':5, 'Jobs':[]}
Dojikiri = {'Name': 'Dojikiri Yasatsuna','Name2': 'Dojikiri Yasatsuna R15', 'Skill Type': 'Great Katana', 'Type':'Weapon', 'DMG': 315+15, 'Delay': 450, 'Store TP': 10, 'Accuracy': 0+30, 'Magic Accuracy':0+30, 'TP Bonus': 500, 'Great Katana Skill': 269, 'Magic Accuracy Skill': 228, 'Magic Damage': 155, 'Jobs':[]}
Gleti_Knife = {'Name': "Gleti's Knife", 'Name2': "Gleti's Knife R25", 'Skill Type': 'Dagger', 'Type':'Weapon', 'DMG':133+10, 'Delay':200, 'DEX':15, 'AGI':15, 'Accuracy':40+10, 'Attack':30+40, 'Magic Accuracy':40+10, 'Dagger Skill':255, 'Magic Accuracy Skill':242,'Crit Rate':5,"TA":6, 'Jobs':[]}
Gleti_Knife30 = {'Name': "Gleti's Knife", 'Name2': "Gleti's Knife R30", 'Skill Type': 'Dagger', 'Type':'Weapon', 'DMG':133+11, 'Delay':200, 'DEX':15, 'AGI':15, 'Accuracy':40+15, 'Attack':30+45, 'Magic Accuracy':40+15, 'Dagger Skill':255, 'Magic Accuracy Skill':242,'Crit Rate':5,"TA":6, 'Jobs':[]}
Gokotai = {'Name': 'Gokotai', 'Name2': 'Gokotai', 'Skill Type': 'Katana', 'Type':'Weapon', 'DMG': 157, 'Delay': 227, 'Katana Skill': 250, 'Magic Accuracy Skill': 250, 'Magic Damage': 217, 'DEX': 15, 'AGI':15, 'INT':15, 'Accuracy': 40, 'Attack': 30, 'Ranged Accuracy': 40, 'Magic Accuracy': 40, 'Magic Attack': 16, 'Jobs':[]}
Hachimonji = {'Name': 'Hachimonji', 'Name2': "Hachimonji", 'Skill Type': 'Great Katana', 'Type':'Weapon', 'DMG': 318, 'Delay':450, 'STR':20, 'DEX':20, 'VIT':20, 'Accuracy':40, 'Attack':30, 'Magic Accuracy':40, 'Great Katana Skill':250, 'Magic Accuracy Skill':250, 'Jobs':[]}
Heishi = {'Name': 'Heishi Shorinken', 'Name2': 'Heishi Shorinken R15', 'Skill Type': 'Katana', 'Type':'Weapon', 'DMG': 159+7, 'Delay': 227, 'Store TP': 10, 'Accuracy': 0+30, 'Magic Accuracy':0+30, 'TP Bonus': 500, 'Katana Skill': 269, 'Magic Accuracy Skill': 242, 'Magic Damage': 186, 'Jobs':[]}
Hitaki = {'Name': 'Hitaki', 'Name2': 'Hitaki', 'Skill Type': 'Katana', 'Type':'Weapon', 'DMG':  49, 'Delay': 216, 'TP Bonus': 1000, 'Katana Skill': 0, 'Jobs':[]}
Kannagi = {'Name': 'Kannagi', 'Name2': 'Kannagi R15', 'Skill Type': 'Katana', 'Type':'Weapon', 'DMG': 148+5, 'Delay': 210, 'Katana Skill': 269, 'Magic Accuracy Skill': 242, 'Magic Damage': 186, 'DEX': 0+20, 'AGI':50+20, 'Jobs':[]}
Kikoku = {'Name': 'Kikoku', 'Name2': 'Kikoku R15', 'Skill Type': 'Katana', 'Type':'Weapon', 'DMG': 148+8, 'Delay': 210, 'Attack': 60, 'Katana Skill': 269, 'Magic Accuracy Skill': 242, 'Magic Damage': 186, 'Jobs':[]}
Kogarasumaru = {'Name': 'Kogarasumaru', 'Name2': 'Kogarasumaru R15', 'Skill Type': 'Great Katana', 'Type':'Weapon', 'DMG': 281+29, 'Delay': 450, 'Accuracy': 0+30, 'Magic Accuracy':0+30, 'Great Katana Skill': 269, 'Magic Accuracy Skill': 228, 'Jobs':[]}
Kraken_Club = {'Name': 'Kraken Club', 'Name2': 'Kraken Club', 'Skill Type': 'Club', 'Type':'Weapon', 'DMG':11, 'Delay':264, 'OA2':15, 'OA3':25, 'OA4':25, 'OA5':15, 'OA6':10, 'OA7':3, 'OA8':2, 'Jobs':[]}
Kujaku = {'Name': 'Kujaku', 'Name2': 'Kujaku', 'Skill Type': 'Katana', 'Type':'Weapon', 'DMG':118, 'Delay':227, 'Accuracy':15,'Katana Skill':242,'Magic Accuracy Skill':242, 'Jobs':[]}
Kunimitsu = {'Name': 'Kunimitsu', 'Name2': 'Kunimitsu R25', 'Skill Type': 'Katana', 'Type':'Weapon', 'DMG':151+11, 'Delay':227, 'DEX':15, 'AGI':15, 'Accuracy':40+10, 'Attack':30+40, 'Ranged Accuracy':40, 'Magic Accuracy':40+10,'Magic Attack':20, 'Magic Damage':217, 'Magic Burst Damage':10,'Store TP':5, 'Magic Accuracy Skill':248, 'Katana Skill': 248, 'Weaponskill Damage':5, 'Jobs':[]}
Kunimitsu30 = {'Name': 'Kunimitsu', 'Name2': 'Kunimitsu R30', 'Skill Type': 'Katana', 'Type':'Weapon', 'DMG':151+12, 'Delay':227, 'DEX':15, 'AGI':15, 'Accuracy':40+15, 'Attack':30+45, 'Ranged Accuracy':40, 'Magic Accuracy':40+15,'Magic Attack':20, 'Magic Damage':217, 'Magic Burst Damage':10, 'Store TP':5, 'Magic Accuracy Skill':248, 'Katana Skill': 248, 'Weaponskill Damage':5, 'Jobs':[]}
Liberator = {'Name': "Liberator", 'Name2': "Liberator R15", 'Skill Type': 'Scythe', 'Type':'Weapon', 'DMG':330+34, 'Delay':528, 'Magic Accuracy':50+30, 'Magic Damage':217, 'Scythe Skill':269, 'Magic Accuracy Skill':242, 'Accuracy':0+30}
Masamune = {'Name': 'Masamune', 'Name2': 'Masamune R15', 'Skill Type': 'Great Katana', 'Type':'Weapon', 'DMG': 308+11, 'Delay': 437, 'Great Katana Skill': 269, 'Magic Accuracy Skill': 228, 'AGI': 0+20, 'STR':50+20, 'Jobs':[]}
Naegling = {'Name': 'Naegling', 'Name2': 'Naegling', 'Skill Type': 'Sword', 'Type':'Weapon', 'DMG': 166, 'Delay': 240, 'Sword Skill': 250, 'Magic Accuracy Skill': 250, 'Magic Damage': 217, 'DEX': 15, 'MND':15, 'INT':15, 'Accuracy': 40, 'Attack': 30, 'Magic Accuracy': 40, 'Magic Attack': 16, 'Jobs':[]}
Nagi = {'Name': 'Nagi', 'Name2': 'Nagi R15', 'Skill Type': 'Katana', 'Type':'Weapon', 'DMG': 142+14, 'Delay': 227, 'Accuracy': 0+30, 'Magic Accuracy':40+30, 'Katana Skill': 269, 'Magic Accuracy Skill': 242, 'Magic Damage': 186, 'Jobs':[]}
Shining_One = {'Name': 'Shining One', 'Name2': "Shining One", 'Skill Type': 'Polearm', 'Type': 'Weapon', 'DMG':333, 'Delay':480, 'STR':20, 'INT':20, 'MND':20, 'Accuracy':40, 'Attack':30, 'Magic Accuracy':40, 'Magic Attack':21, 'Magic damage':226, 'Polearm Skil':250, 'Magic Accuracy Skill':250 , 'Jobs':[]}
Tauret = {'Name': 'Tauret', 'Name2': 'Tauret', 'Skill Type': 'Dagger', 'Type':'Weapon', 'DMG': 125, 'Delay': 180, 'Dagger Skill': 250, 'Magic Accuracy Skill': 250, 'Magic Damage': 217, 'DEX': 15, 'MND':15, 'INT':15, 'Accuracy': 40, 'Attack': 30, 'Magic Accuracy': 40, 'Magic Attack': 16, 'Jobs':[]}
Ternion = {'Name': 'Ternion Dagger +1','Name2': 'Ternion Dagger +1 R15', 'Skill Type': 'Dagger', 'Type':'Weapon', 'DMG': 100+17, 'Delay': 175, 'Accuracy':27+40, 'Magic Accuracy':0+40, 'Dagger Skill':228, 'Magic Accuracy Skill':188, "TA":4, 'AGI':14, 'Weaponskill Damage':5, 'Jobs':[]}
Tsuru = {'Name': 'Tsuru', 'Name2': 'Tsuru R25', 'Skill Type': 'Katana', 'Type':'Weapon', 'DMG':131, 'Delay':190,'VIT':15,'AGI':15,'Accuracy':40,'Ranged Accuracy':40, 'Katana Skill':242, 'Magic Accuracy Skill':242,'Daken':8, 'Jobs':[]}
Tsuru30 = {'Name': 'Tsuru', 'Name2': 'Tsuru R30', 'Skill Type': 'Katana', 'Type':'Weapon', 'DMG':131, 'Delay':190,'VIT':15,'AGI':15,'Accuracy':40,'Ranged Accuracy':40, 'Katana Skill':242, 'Magic Accuracy Skill':242,'Daken':10, 'Jobs':[]}
MalevolenceA = {'Name': "Malevolence",'Name2': "MalevolenceA", 'Skill Type':'Dagger','Type':'Weapon','DMG':94,'Delay':201,'INT':0+10,'Magic Accuracy':25+10, 'Magic Attack':34+10, 'Magic Damage':118, 'Magic Accuracy Skill':201, 'Dagger Skill':242}
MalevolenceB = {'Name': "Malevolence",'Name2': "MalevolenceB", 'Skill Type':'Dagger','Type':'Weapon','DMG':94,'Delay':201,'INT':0+10,'Magic Accuracy':25+10, 'Magic Attack':34+10, 'Magic Damage':118, 'Magic Accuracy Skill':201, 'Dagger Skill':242}
#Karambit = {'Name': 'Karambit' 'Skill Type':'Hand-to-Hand', 'Type':'Weapon', 'DMG':'Base+180','Delay':'base+96', 'STR':20, 'DEX':20,'VIT':20,'Accuracy':40,'Attack':30,'Magic Accuracy':40,'Hand-to-Hand Skill':250, 'Magic Accuracy Skill':250}

Alber_Strap = {'Name': 'Alber Strap', 'Type': 'Grip', 'Magic Attack':7, "DA":2}
Rigorous_Grip = {'Name': 'Rigorous Grip +1', 'Name2': 'Rigorous Grip +1 R15', 'STR':4+15, 'Attack':13+30, 'Accuracy':3}
Utu_Grip = {'Name': 'Utu Grip', 'Type': 'Grip', 'Accuracy':30, 'Attack':30}

mains = [Heishi, Kannagi, Kikoku, Nagi, Gokotai, MalevolenceA, Tauret]
subs = [Ternion, Kunimitsu, Gleti_Knife, Tauret, Gokotai, Crepuscular_Knife, MalevolenceB]
grips = [Alber_Strap, Rigorous_Grip]


Aurgelmir_Orb = {'Name': 'Aurgelmir Orb +1', 'STR':7, 'DEX':7, 'VIT':7, 'Attack':10, 'Store TP':5, 'Jobs':[]}
Cath_Palug_Stone = {'Name': 'Cath Palug Stone', 'DEX':10, 'AGI':10, 'Accuracy':15, 'Jobs':[]}
Coiste_Bodhar = {'Name': 'Coiste Bodhar', 'Name2': 'Coiste Bodhar R25', "Attack":15,'STR':8,"DA":3,'Store TP':3}
Crepuscular_Pebble = {'Name': 'Ghastly Tathlum', 'Name2': 'Crepuscular Pebble', 'STR':3, 'VIT':3, 'PDL':3, 'Jobs':[]}
Date = {'Name': 'Date Shuriken', 'Skill Type': 'Throwing', 'DMG': 125, 'Delay': 192, 'Accuracy': 5, 'Ranged Accuracy': 5, 'Throwing Skill': 242, 'DEX': 5, 'AGI': 5, 'Jobs':[]}
Donar_Gun = {'Name': 'Donar Gun', 'DEX':5, 'AGI':5, 'Lightning Affinity': 15, 'Jobs':[]} # "Lightning Affinity" may need to be changed to "Lightning Elemental Bonus" for it to properly work; see Pixie Hairpin +1
Ghastly_Tathlum = {'Name': 'Ghastly Tathlum +1', 'Name2': 'Ghastly Tathlum +1 R15', 'Magic Damage':11+10, 'INT':6+5, 'Jobs':[]}
Happo = {'Name': 'Happo Shuriken', 'Skill Type': 'Throwing', 'DMG':  99, 'Delay': 188, 'Accuracy': 6, 'Attack': 6, 'Ranged Accuracy': 11, 'Throwing Skill': 228, 'Crit Rate': 2, 'Jobs':[]}
Knobkierrie = {'Name': 'Knobkierrie', 'Attack':23, 'Weaponskill Damage':6, 'Jobs':[]}
Pemphredo_Tathlum = {'Name': 'Pemphredo Tathlum', 'INT':4, 'Magic Accuracy':8, 'Magic Attack':4, 'Jobs':[]}
Seething_Bomblet = {'Name': 'Seething Bomblet +1', 'Name2': 'Seeth. Bomblet +1 R15', 'Accuracy':13, 'Attack':13, 'Magic Attack':7, 'STR':4+10, 'Gear Haste':0+4, 'Jobs':[]}
Seki = {'Name': 'Seki Shuriken', 'Skill Type': 'Throwing', 'DMG': 101, 'Delay': 192, 'Attack': 13, 'Store TP': 2, 'Throwing Skill': 242, 'Jobs':[]}
Yetshila = {'Name': 'Yetshila +1', 'Crit Rate':2, 'Crit Damage':6, 'Jobs':[]}
ammos = [Yetshila, Seething_Bomblet, Cath_Palug_Stone, Aurgelmir_Orb, Pemphredo_Tathlum, Ghastly_Tathlum, Crepuscular_Pebble, Coiste_Bodhar]

Adhemar_Bonnet_A = {'Name': 'Adhemar Bonnet +1', 'Name2': 'Adhemar Bonnet +1 A', 'STR':19, 'DEX':21+12, 'VIT':15, 'AGI':19+12, 'INT':14, 'MND':14, 'CHR':14, 'Accuracy':0+20, 'Attack':36, 'Ranged Attack':36, 'Gear Haste':8, "TA":4, 'Crit Damage':6,'Jobs':[]}
Adhemar_Bonnet_B = {'Name': 'Adhemar Bonnet +1', 'Name2': 'Adhemar Bonnet +1 B', 'STR':19+12, 'DEX':21+12, 'VIT':15, 'AGI':19, 'INT':14, 'MND':14, 'CHR':14, 'Attack':36+20, 'Ranged Attack':36, 'Gear Haste':8, "TA":4, 'Crit Rate': 6,'Jobs':[]}
Blistering_Sallet = {'Name': 'Blistering Sallet +1', 'Name2': 'Blistering Sallet +1 R15', 'STR':16+25, 'DEX':16+25, 'VIT':16, 'AGI':16, 'INT':16, 'MND':16, 'CHR':16, 'Accuracy':6+45, 'Magic Accuracy':0+45, 'Gear Haste':8, "DA":3, 'Crit Rate':10,'Jobs':[]}
Dampening_Tam = {'Name': 'Dampening Tam', 'STR':18, 'DEX':24+10, 'VIT':18, 'AGI':20, 'INT':18, 'MND':22, 'CHR':18, 'Accuracy':20+15,'Ranged Accuracy':20,'Magic Accuracy':20+15,'Gear Haste':7,'QA':3,'Jobs':[]}
Flamma_Zucchetto = {'Name': 'Flamma Zucchetto +2', 'STR':36,'DEX':32,"VIT":24,"AGI":16,'INT':12,'MND':12,'CHR':12,'Accuracy':44,'Magic Accuracy':44,'Gear Haste':4,'Store TP':6,"TA":5}
Hachiya_Hatsuburi = {'Name': 'Hachiya Hatsuburi +3', 'STR': 33, 'DEX': 33, 'VIT':32, 'AGI':32, 'INT':31, 'MND':31, 'CHR': 31, 'Magic Accuracy': 54, 'Ninjutsu Skill': 17, 'Gear Haste': 8, 'Weaponskill Damage':10,'Jobs':[]}
Hizamaru_Somen = {'Name': 'Hizamaru Somen +2', 'STR':33, 'DEX':29, 'VIT':27, 'AGI':24, 'INT':12, 'MND':10, 'CHR':20, 'Accuracy':20, 'Attack':26, 'Gear Haste':6,'Jobs':[]}
Kendatsuba_Jinpachi = {'Name': 'Kendatsuba Jinpachi +1', 'STR':23,'DEX':47,'VIT':32,'AGI':34,'INT':19,'MND':17,'CHR':19,'Accuracy':50,'Ranged Accuracy':45,'Gear Haste':6,"TA":4,'Crit Rate':5,'Jobs':[]}
Malignance_Chapeau = {'Name': 'Malignance Chapeau', 'STR':11,'DEX':40,'VIT':19,'AGI':33,'INT':25,'MND':16,'CHR':17,'Accuracy':50,'Ranged Accuracy':50,'Magic Accuracy':50,'Gear Haste':6,'Store TP':8,'PDL':3,'Jobs':[]}
Mochizuki_Hatsuburi = {'Name': 'Mochizuki Hatsuburi +3', 'STR':31, 'DEX':31, 'VIT':33, 'AGI':33, 'INT':32, 'MND':32, 'CHR':32, 'Accuracy':44,'Attack':62,'Magic Accuracy': 37, 'Magic Attack': 61, 'Gear Haste': 8, 'Ninjutsu Magic Attack': 21,'Jobs':[]}
Mpaca_Cap = {'Name': 'Mpaca\'s Cap', 'Name2': 'Mpaca\'s Cap R25', 'STR':33, 'DEX':30, 'VIT':26, 'AGI':24, 'INT':20, 'MND':17, 'CHR':20,'Accuracy':40+10,'Attack':40+25,'Magic Accuracy':40+10,'Gear Haste':6,"TA":3,'Crit Rate':4,'TP Bonus':200,'Jobs':[]}
Mpaca_Cap30 = {'Name': 'Mpaca\'s Cap', 'Name2': 'Mpaca\'s Cap R30', 'STR':33, 'DEX':30, 'VIT':26, 'AGI':24, 'INT':20, 'MND':17, 'CHR':20,'Accuracy':40+15,'Attack':40+30,'Magic Accuracy':40+15,'Gear Haste':6,"TA":3,'Crit Rate':4,'TP Bonus':200,'Jobs':[]}
Mummu_Bonnet = {'Name': 'Mummu Bonnet +2', 'STR':20,'DEX':39,'VIT':16,'AGI':34,'INT':15,'MND':14,'CHR':17,'Accuracy':44,'Ranged Accuracy':44,'Magic Accuracy':44,'Gear Haste':8,'Crit Rate':5,'Jobs':[]}
Nyame_Helm = {'Name': 'Nyame Helm', 'Name2': 'Nyame Helm R25 B', 'STR':26, 'DEX':25, 'VIT':24, 'AGI':23, 'INT':28, 'MND':26, 'CHR':24,'Accuracy':40,'Attack':30+30, 'Gear Haste':6,'Weaponskill Damage':0+10,"DA":0+4,'Magic Accuracy':40,'Magic Attack':30,'Ranged Accuracy':40,'Ranged Attack':30+30,'Magic Burst Damage':5,'Jobs':[]}
Nyame_Helm30 = {'Name': 'Nyame Helm', 'Name2': 'Nyame Helm R30 B', 'STR':26, 'DEX':25, 'VIT':24, 'AGI':23, 'INT':28, 'MND':26, 'CHR':24,'Accuracy':40,'Attack':30+35, 'Gear Haste':6,'Weaponskill Damage':0+11,"DA":0+5,'Magic Accuracy':40,'Magic Attack':30,'Ranged Accuracy':40,'Ranged Attack':30+35,'Magic Burst Damage':5,'Jobs':[]}
Pixie_Hairpin = {'Name': 'Pixie Hairpin +1', 'INT':27, 'Dark Elemental Bonus':28,'Jobs':[]}
Ratri_Sallet = {'Name': 'Ratri Sallet +1', 'STR':40, 'DEX':33, 'VIT':26, 'AGI':21, 'INT':26, 'MND':23, 'CHR':22, 'Magic Accuracy':45, 'Scythe Skill':54, 'Gear Haste':7, 'Weapon Skill Damage':8}
Ryuo_Somen_A = {'Name': 'Ryuo Somen +1', 'Name2': 'Ryuo Somen +1 A', 'STR':21+12, 'DEX':17+12, 'VIT':14, 'AGI':20, 'INT':11, 'MND':11, 'CHR':11, 'Accuracy':35+20,'Ranged Accuracy':35,'Gear Haste':7,'Store TP':7,'Dual Wield':9,'Jobs':[]}
Sakpata_Helm = {'Name': 'Sakpata\'s Helm', 'Name2': 'Sakpata\'s Helm R15', 'STR':33,'DEX':20,"VIT":40,"AGI":21,'INT':19,'MND':23,'CHR':21,'Accuracy':40+5,'Magic Accuracy':40+5,'Attack':40+20,'Gear Haste':4,"DA":5,'PDL':5,'DA DMG':10}
Sulevia_Mask = {'Name': 'Sulevia\'s Mask +2', 'STR':33,'DEX':19,"VIT":40,"AGI":12,'INT':11,'MND':22,'CHR':22,'Accuracy':44,'Attack':48,'Gear Haste':3,'Store TP':10}
Hattori_Zukin = {'Name': 'Hattori Zukin +1', 'STR':19,'DEX':31,'VIT':18,'AGI':22,'INT':17,'MND':17,'CHR':17,'Gear Haste':10,'Dual Wield':7}
heads = [Adhemar_Bonnet_A, Adhemar_Bonnet_B, Hachiya_Hatsuburi, Mochizuki_Hatsuburi, Malignance_Chapeau, Kendatsuba_Jinpachi, Mummu_Bonnet, Nyame_Helm, Mpaca_Cap, Blistering_Sallet]

Abyssal_Beads = {'Name': 'Abyssal Beads +2', 'Name2':'Abyssal Beads +2 R25','Accuracy':15,'Magic Accuracy':15,'Attack':40,'Store TP':0+7,'STR':0+25,'Crit Rate':4,'PDL':0+10,'Jobs':['drk']}
Baetyl_Pendant = {'Name': 'Baetyl Pendant', 'Magic Attack':13, 'Jobs':all_jobs}
Caro_Necklace = {'Name': 'Caro Necklace', 'STR':6,'DEX':6,'Attack':10, 'Jobs':all_jobs}
Fotia_Gorget = {'Name': 'Fotia Gorget', 'Weaponskill Accuracy': 10, 'ftp': 25./256., 'Jobs':all_jobs}
Ninja_Nodowa = {'Name': 'Ninja Nodowa +2', 'Name2': 'Ninja Nodowa +2 R25', 'Accuracy': 25, 'Ranged Accuracy': 25, 'Store TP': 7, 'DEX':15, 'AGI':15, 'Daken':25, 'PDL':10, 'Jobs':['nin']}
Rep_Plat_Medal = {'Name': 'Republican Platinum Medal', 'STR':10, 'Attack':30, 'Ranged Attack':30}
Samurai_Nodowa = {'Name': 'Samurai Nodowa +2', 'Name2':'Samurai Nodowa +2 R25', 'Accuracy':30, 'Store TP':7+7, 'STR':0+25, 'PDL':0+10, 'Jobs':['sam']}
Sanctity_Necklace = {'Name': 'Sanctity Necklace', 'Attack':10,'Ranged Attack':10,'Ranged Accuracy':10,'Magic Accuracy':10,'Magic Attack':10, 'Jobs':all_jobs}
Sibyl_Scarf = {'Name': 'Sibyl Scarf', 'INT':10, 'Magic Attack':10}
Warders_Charm = {'Name': 'Warders Charm +1', 'Name2': "Warder's Charm +1 R15",'Magic Burst Damage':10}
necks = [Ninja_Nodowa, Fotia_Gorget, Caro_Necklace, Baetyl_Pendant, Rep_Plat_Medal,Sibyl_Scarf,Warders_Charm]

Balder_Earring = {'Name': 'Balder Earring +1', 'Attack':10, 'Store TP':3, 'QA':1, 'Jobs':all_jobs}
Brutal_Earring = {'Name': 'Brutal Earring', "DA":5,'Store TP':1, 'Jobs':all_jobs}
Cessance_Earring = {'Name': 'Cessance Earring', 'Accuracy':6, "DA":3, 'Store TP':3, 'Jobs':all_jobs}
Crematio_Earring = {'Name': 'Crematio Earring', 'Magic Attack':6,'Magic Damage':6, 'Jobs':all_jobs}
Crepuscular_Earring = {'Name': 'Crepuscular Earring', 'Accuracy':10, 'Ranged Accuracy':10, 'Magic Accuracy':10, 'Store TP':5}
Dedition_Earring = {'Name': 'Dedition Earring', 'Accuracy':-10, 'Ranged Accuracy':-10, 'Attack':-10, 'Ranged Attack':-10, 'Store TP':8, 'Jobs':all_jobs}
Dignitary_Earring = {'Name': 'Dignitarty\'s Earring', 'Accuracy':10,'Magic Accuracy':10,'Store TP':3, 'Jobs':all_jobs}
Eabani_Earring = {'Name': 'Eabani Earring', 'Dual Wield':4, 'Jobs':all_jobs}
Friomisi_Earring = {'Name': 'Friomisi Earring', 'Magic Attack':10, 'Jobs':all_jobs}
Ishvara_Earring = {'Name': 'Ishvara Earring', 'Weaponskill Damage':2, 'Jobs':all_jobs}
Lugra_Earring_Aug = {'Name': 'Lugra Earring +1', 'Name2': 'Lugra Earring +1 R15 (day)', 'STR':0+8,'DEX':0+8,'VIT':0+8,'INT':0+8,"DA":3, 'Jobs':['war','pld','drk','bst','sam','nin']}
Mache_Earring1 = {'Name': 'Mache Earring +1', 'Name2': 'Mache Earring +1A', 'DEX':8,'Accuracy':10,"DA":2, 'Jobs':all_jobs}
Mache_Earring2 = {'Name': 'Mache Earring +1', 'Name2': 'Mache Earring +1B', 'DEX':8,'Accuracy':10,"DA":2, 'Jobs':all_jobs}
Moonshade_Earring = {'Name': 'Moonshade Earring', 'Accuracy':4, 'TP Bonus':250, 'Jobs':all_jobs}
Odr_Earring = {'Name': 'Odr Earring', 'DEX':10,'Accuracy':10,'Crit Rate':5, 'Jobs':['mnk','thf','rng','nin','blu','cor','dnc','run']}
Schere_Earring = {'Name': 'Schere Earring', 'Schere Earring R25' 'STR':5, "DA":6, 'Accuracy':15, 'Attack':10, 'Jobs':['war','mnk','drk','sam','pup']}
Schere_Earring30 = {'Name': 'Schere Earring', 'Schere Earring R30' 'STR':5, "DA":6, 'Accuracy':15, 'Attack':15, 'Jobs':['war','mnk','drk','sam','pup']}
Static_Earring = {'Name': 'Static Earring', 'MND':2, 'Magic Burst Damage':5, 'Jobs':all_jobs}
Suppanomimi = {'Name': 'Suppanomimi', 'AGI':2,'Dual Wield':5,'Sword Skill':5, 'Jobs':all_jobs}
Telos_Earring = {'Name': 'Telos Earring', 'Accuracy':10, 'Attack':10, 'Ranged Accuracy':10, 'Ranged Attack':10, "DA":1, 'Store TP':5, 'Jobs':all_jobs}
Thrud_Earring = {'Name': 'Thrud Earring', 'STR':10, 'VIT':10, 'Weaponskill Damage':3, 'Jobs':['war','pld','drk','bst','sam','drg']}
ears = [Static_Earring,Ishvara_Earring, Lugra_Earring_Aug, Moonshade_Earring, Brutal_Earring, Friomisi_Earring, Crematio_Earring, Balder_Earring, Mache_Earring1, Mache_Earring2, Odr_Earring, Crepuscular_Earring]
ears2 = [Static_Earring,Ishvara_Earring, Lugra_Earring_Aug, Moonshade_Earring, Brutal_Earring, Friomisi_Earring, Crematio_Earring, Balder_Earring, Mache_Earring1, Mache_Earring2, Odr_Earring, Crepuscular_Earring]

Abnoba_Kaftan = {'Name': 'Abnoba Kaftan', 'STR':25, 'DEX':38, 'VIT':24, 'AGI':28, 'INT':21, 'MND':21, 'CHR':21, 'Accuracy':22, 'Attack':22, 'Gear Haste':4, 'Crit Rate':5, 'Crit Damage':5,'Jobs':[]}
Adhemar_Jacket_A = {'Name': 'Adhemar Jacket +1', 'Name2': 'Adhemar Jacket +1 A', 'STR':26, 'DEX':33+12, 'VIT':23, 'AGI':29+12, 'INT':20, 'MND':20, 'CHR':20, 'Accuracy':35+20, 'Attack':35, 'Ranged Accuracy':35, 'Ranged Attack':35, 'Gear Haste':4, "TA":4, 'Dual Wield':6,'Jobs':[]}
Adhemar_Jacket_B = {'Name': 'Adhemar Jacket +1', 'Name2': 'Adhemar Jacket +1 B', 'STR':26+12, 'DEX':33+12, 'VIT':23, 'AGI':29, 'INT':20, 'MND':20, 'CHR':20, 'Accuracy':35, 'Attack':35+20, 'Ranged Accuracy':35, 'Ranged Attack':35, 'Gear Haste':4, "TA":4, 'Dual Wield':6,'Jobs':[]}
Agony_Jerkin = {'Name': 'Agony Jerkin +1', 'Name2': 'Agony Jerkin +1 R15', 'STR':24+10, 'DEX':35+10, 'VIT':24+10, 'AGI':28+10, 'INT':23+10, 'MND':23+10, 'CHR':23+10, 'Attack':23+60, 'Gear Haste':4, 'Accuracy':14, 'Store TP':0+10,'Jobs':[]}
Ashera_Harness = {'Name': 'Ashera Harness', 'STR':30, 'DEX':40, 'VIT':30, 'AGI':30, 'INT':30, 'MND':30, 'CHR':40, 'Accuracy':45, 'Attack':45, 'Gear Haste':4, 'STP':10}
Dagon_Breastplate = {'Name': 'Dagon Breastplate', 'STR':40,'DEX':30,"VIT":40,"AGI":30,'INT':30,'MND':30,'CHR':30,'Accuracy':45,'Attack':45,'Gear Haste':1,'Crit Rate':4, "TA":5}
Flamma_Korazin = {'Name': 'Flamma Korazin +2', 'STR':43,'DEX':39,"VIT":32,"AGI":20,'INT':20,'MND':20,'CHR':20,'Accuracy':46,'Magic Accuracy':46,'Gear Haste':2,'Store TP':9}
Gyve_Doublet = {'Name': 'Gyve Doublet', 'STR':19, 'DEX':19, 'VIT':19, 'AGI':19, 'INT':39, 'MND':33, 'CHR':33, 'Magic Attack':42, 'Gear Haste':3,'Jobs':[]}
Hachiya_Chainmail = {'Name': 'Hachiya Chainmail +3', 'STR':39, 'DEX':35, 'VIT':36, 'AGI':35, 'INT':34, 'MND':34, 'CHR':34, 'Accuracy':50, 'Gear Haste':4,'Dual Wield':10,'Crit Rate':8,'Jobs':[]}
Herculean_Vest = {'Name': 'Herculean Vest', 'STR':28, 'DEX':34, 'VIT':24, 'AGI':30, 'INT':21, 'MND':20, 'CHR':21, 'Accuracy':15, 'Ranged Accuracy':15, 'Gear Haste':4, 'Store TP':3, 'Crit Rate':3,'Jobs':[]}
Hizamaru_Haramaki = {'Name': 'Hizamaru Haramaki +2', 'STR':40, 'DEX':36, 'VIT':34, 'AGI':28, 'INT':20, 'MND':17, 'CHR':28, 'Accuracy':46, 'Attack':28, 'Gear Haste':4,'Jobs':[]}
Ignominy_Cuirass = {'Name': 'Ignominy Cuirass +3', 'STR':46,'DEX':29,"VIT":39,"AGI":29,'INT':29,'MND':29,'CHR':29,'Accuracy':50,'Attack':48,'Gear Haste':3,'Weapon Skill Damage':10}
Kendatsuba_Samue = {'Name': 'Kendatsuba Samue +1', 'STR':33, 'DEX':39, 'VIT':21, 'AGI':37, 'INT':24, 'MND':23, 'CHR':21, 'Accuracy': 52, 'Ranged Accuracy': 47, 'Gear Haste': 4, "TA": 6, 'Crit Rate': 9,'Jobs':[]}
Malignance_Tabard = {'Name': 'Malignance Tabard', 'STR':19, 'DEX':49, 'VIT':25, 'AGI':42, 'INT':19, 'MND':24, 'CHR':24, 'Accuracy':50, 'Ranged Accuracy':50, 'Magic Accuracy':50, 'Gear Haste':4, 'Store TP':11, 'PDL':6,'Jobs':[]}
Mochizuki_Chainmail = {'Name': 'Mochizuki Chainmail +3', 'STR':34, 'DEX':35, 'VIT':31, 'AGI':35, 'INT':34, 'MND':34, 'CHR':34, 'Accuracy':51, 'Attack':87, 'Ranged Accuracy':47, 'Ranged Attack':79, 'Magic Accuracy':40,'Gear Haste':4,'Dual Wield':9,'Daken':10,'Jobs':[]}
Mpaca_Doublet = {'Name': "Mpaca's Doublet", 'Name2': "Mpaca's Doublet R25", 'STR':39, 'DEX':37, 'VIT':34, 'AGI':28, 'INT':28, 'MND':25, 'CHR':28,'Accuracy':40+10,'Attack':40+25,'Magic Accuracy':40+10,'Gear Haste':4,"TA":4,'Crit Rate':7, 'Store TP':0+7,'Jobs':[]}
Mpaca_Doublet30 = {'Name': "Mpaca's Doublet", 'Name2': "Mpaca's Doublet R30", 'STR':39, 'DEX':37, 'VIT':34, 'AGI':28, 'INT':28, 'MND':25, 'CHR':28,'Accuracy':40+15,'Attack':40+30,'Magic Accuracy':40+15,'Gear Haste':4,"TA":4,'Crit Rate':7, 'Store TP':0+8,'Jobs':[]}
Mummu_Jacket = {'Name': 'Mummu Jacket +2', 'STR':25, 'DEX':48, 'VIT':24, 'AGI':44, 'INT':21, 'MND':20, 'CHR':24, 'Accuracy':46, 'Ranged Accuracy':46, 'Magic Accuracy':46, 'Gear Haste':4, 'Store TP':6, 'Crit Rate': 6,'Jobs':[]}
Nyame_Mail = {'Name': 'Nyame Mail', 'Name2': 'Nyame Mail R25 B', 'STR':35, 'DEX':24, 'VIT':35, 'AGI':33, 'INT':42, 'MND':37, 'CHR':35, 'Accuracy':40, 'Attack':30+30, 'Gear Haste':3, 'Weaponskill Damage':0+12, 'Magic Accuracy':40, 'Magic Attack':30, 'Ranged Accuracy':40, 'Ranged Attack':30+30,"DA":0+5,'Magic Burst Damage':7,'Jobs':[]}
Nyame_Mail30 = {'Name': 'Nyame Mail', 'Name2': 'Nyame Mail R30 B', 'STR':35, 'DEX':24, 'VIT':35, 'AGI':33, 'INT':42, 'MND':37, 'CHR':35, 'Accuracy':40, 'Attack':30+35, 'Gear Haste':3, 'Weaponskill Damage':0+13, 'Magic Accuracy':40, 'Magic Attack':30, 'Ranged Accuracy':40, 'Ranged Attack':30+35,"DA":0+7,'Magic Burst Damage':7,'Jobs':[]}
Ratri_Breastplate = {'Name': 'Ratri Breastplate +1', 'STR':48, 'DEX':34, 'VIT':30, 'AGI':21, 'INT':25, 'MND':25, 'CHR':24, 'Magic Accuracy':47, 'Scythe Skill':56, 'Gear Haste':3, 'Weapon Skill Damage':10}
Ryuo_Domaru_A = {'Name': 'Ryuo Domaru +1', 'Name2': 'Ryuo Domaru +1 A', 'STR':28+12, 'DEX':24+12, 'VIT':23, 'AGI':29, 'INT':19, 'MND':19, 'CHR':19,'Accuracy':37+20,'Attack':37,'Gear Haste':3,'Crit Rate':5,'Jobs':[]}
Sakonji_Domaru = {'Name':'Sakonji Domaru +3', 'STR':42, 'DEX':37, 'VIT':36, 'AGI':31, 'INT':31, 'MND':31, 'CHR':31, 'Accuracy':47, 'Attack':80, 'Magic Accuracy':40, 'Gear Haste':3, 'Store TP':10, 'Weaponskill Damage':10,'Jobs':[]}
Sakpata_Breastplate = {'Name': 'Sakpata\'s Breastplate', 'Name2': 'Sakpata\'s Breastplate R15', 'STR':42,'DEX':25,"VIT":42,"AGI":25,'INT':24,'MND':28,'CHR':26,'Accuracy':40+5,'Magic Accuracy':40+5,'Attack':40+20,'Gear Haste':2,"DA":8,'PDL':8}
Samnuha_Coat = {'Name': 'Samnuha Coat', 'STR':26, 'DEX':33, 'VIT':23, 'AGI':29, 'INT':20, 'MND':20, 'CHR':20, 'Accuracy':23, 'Magic Accuracy':23+15, 'Magic Attack':20+15, 'Gear Haste':4, 'Dual Wield':5, 'Magic Burst Damage II': 8,'Jobs':[]}
Sulevia_Platemail = {'Name': 'Sulevia\'s Platemail +2', 'STR':41,'DEX':24,"VIT":41,"AGI":16,'INT':16,'MND':27,'CHR':27,'Accuracy':46,'Attack':50,'Gear Haste':1}
Tatenashi_Haramaki = {'Name': 'Tatenashi Haramaki', 'Name2': 'Tatenashi Haramaki R15', 'STR':28+10, 'DEX':24+10, 'VIT':28+10, 'AGI':19+10, 'INT':19+10, 'MND':19+10, 'CHR':19+10,'Accuracy':35+30,'Attack':35,'Gear Haste':3,'Crit Rate':6,'Store TP':8,"TA":0+5,'Jobs':[]}
Hattori_Ningi = {'Name': 'Hattori Ningi +1', 'STR':30,'DEX':37,'VIT':24,'AGI':28,'INT':21,'MND':21,'CHR':21,'Gear Haste':4,'Crit Rate':6, 'Accuracy':24, 'Attack':24}
bodies = [Kendatsuba_Samue, Adhemar_Jacket_A, Adhemar_Jacket_B, Malignance_Tabard, Nyame_Mail, Samnuha_Coat, Gyve_Doublet, Abnoba_Kaftan, Mpaca_Doublet, Tatenashi_Haramaki, Ryuo_Domaru_A, Agony_Jerkin]

Adhemar_Wristbands_A = {'Name': 'Adhemar Wristbands +1', 'Name2': 'Adhemar Wristbands +1 A', 'STR':15, 'DEX':44+12, 'VIT':29, 'AGI':7+12, 'INT':12, 'MND':30, 'CHR':17, 'Accuracy':32+20, 'Ranged Accuracy':32, "TA":4, 'Store TP':7, 'Gear Haste':5, 'Jobs':[]}
Adhemar_Wristbands_B = {'Name': 'Adhemar Wristbands +1', 'Name2': 'Adhemar Wristbands +1 B', 'STR':15+12, 'DEX':44+12, 'VIT':29, 'AGI':7, 'INT':12, 'MND':30, 'CHR':17, 'Accuracy':32, 'Ranged Accuracy':32, "TA":4, 'Store TP':7, 'Attack':0+20, 'Gear Haste':5, 'Jobs':[]}
Flamma_Manopolas = {'Name': 'Flamma Manopolas +2', 'STR':23,'DEX':46,"VIT":35,"AGI":8,'INT':7,'MND':24,'CHR':17,'Accuracy':43,'Magic Accuracy':43,'Gear Haste':4,'Store TP':6,'Crit Rate':8}
Floral_Gauntlets = {'Name': 'Floral Gauntlets', 'STR':16, 'DEX':35,'VIT':29,'AGI':12,'INT':12,'MND':30,'CHR':17,'Accuracy':21+15,'Ranged Accuracy':21+15,'Gear Haste':5,'Dual Wield':5,"TA":3, 'Jobs':[]}
Hachiya_Tekko = {'Name': 'Hachiya Tekko +3', 'STR':20, 'DEX':44, 'VIT':38, 'AGI':26, 'INT':20, 'MND':38, 'CHR':26, 'Accuracy':48, 'Ranged Accuracy':48, 'Ranged Attack':48, 'Throwing skill':14, 'Gear Haste':5,'Daken':10, 'Jobs':[]}
Herculean_Gloves = {'Name': 'Herculean Gloves', 'STR':16, 'DEX':39, 'VIT':30, 'AGI':8, 'INT':14, 'MND':26, 'CHR':19, 'Accuracy':12, 'Ranged Accuracy':12, 'Gear Haste':5,"TA":2, 'Jobs':[]}
Hizamaru_Kote = {'Name': 'Hizamaru Kote +2', 'STR':20, 'DEX':43, 'VIT':38, 'AGI':16, 'INT':7, 'MND':21, 'CHR':25, 'Accuracy':43, 'Attack':23, 'Gear Haste':4, 'Jobs':[]}
Kendatsuba_Tekko = {'Name': 'Kendatsuba Tekko +1', 'STR':14, 'DEX':62, 'VIT':37, 'AGI':5, 'INT':14, 'MND':28, 'CHR':21, 'Accuracy':49, 'Ranged Accuracy':44, 'Gear Haste':4,"TA":4, 'Crit Rate':5, 'Jobs':[]}
Leyline_Gloves = {'Name': 'Leyline Gloves', 'STR':11, 'DEX':35,'VIT':32,'AGI':5,'INT':12,'MND':30,'"CHR':17,'Accuracy':18+15,'Magic Accuracy':18+15,'Magic Attack':15+15,'Gear Haste':5, 'Jobs':[]}
Malignance_Gloves = {'Name': 'Malignance Gloves', 'STR':25, 'DEX':56, 'VIT':32, 'AGI':24, 'INT':11, 'MND':42, 'CHR':21, 'Accuracy':50, 'Ranged Accuracy':50, 'Magic Accuracy':50, 'Gear Haste':4,'Store TP':12,'PDL':4, 'Jobs':[]}
Mochizuki_Tekko = {'Name': 'Mochizuki Tekko +3', 'STR':30, 'DEX':44,'VIT':37,'AGI':16,'INT':20,'MND':38,'CHR':26,'Accuracy':38,'Attack':79,'Magic Accuracy':38,'Gear Haste':5, 'Jobs':[]}
Mpaca_Gloves = {'Name': "Mpaca's Gloves", 'Name2': "Mpaca's Gloves R25", "STR":20, "DEX":44,"VIT":38,"AGI":16,"INT":15,"MND":29,"CHR":25,"Accuracy":40+10,"Attack":40+25,"Magic Accuracy":40+10,'Gear Haste':4,"TA":3,'Crit Rate':5, "TA DMG":0+9, 'Jobs':[]}
Mpaca_Gloves30 = {'Name': "Mpaca's Gloves", 'Name2': "Mpaca's Gloves R30", "STR":20, "DEX":44,"VIT":38,"AGI":16,"INT":15,"MND":29,"CHR":25,"Accuracy":40+15,"Attack":40+30,"Magic Accuracy":40+15,'Gear Haste':4,"TA":3,'Crit Rate':5, "TA DMG":0+10, 'Jobs':[]}
Mummu_Wrists = {'Name': 'Mummu Wrists +2', 'STR':16, 'DEX':53,'VIT':30,'AGI':22,'INT':14,'MND':26,'CHR':21,'Accuracy':43,'Ranged Accuracy':43,'Magic Accuracy':43,'Gear Haste':5,"DA":6,'Crit Rate':6, 'Jobs':[]}
Nyame_Gauntlets = {'Name': 'Nyame Gauntlets', 'Name2': 'Nyame Gauntlets R25 B', 'STR':17, 'DEX':42, 'VIT':39, 'AGI':12, 'INT':28, 'MND':40, 'CHR':24, 'Accuracy':40, 'Attack':30+30, 'Gear Haste':3, 'Weaponskill Damage':0+10, 'Magic Accuracy':40, 'Magic Attack':30, 'Ranged Accuracy':40, 'Ranged Attack':30+30,"DA":0+4,'Magic Burst Damage':5, 'Jobs':[]}
Nyame_Gauntlets30 = {'Name': 'Nyame Gauntlets', 'Name2': 'Nyame Gauntlets R30 B', 'STR':17, 'DEX':42, 'VIT':39, 'AGI':12, 'INT':28, 'MND':40, 'CHR':24, 'Accuracy':40, 'Attack':30+35, 'Gear Haste':3, 'Weaponskill Damage':0+11, 'Magic Accuracy':40, 'Magic Attack':30, 'Ranged Accuracy':40, 'Ranged Attack':30+35,"DA":0+5,'Magic Burst Damage':5, 'Jobs':[]}
Ratri_Gadlings = {'Name': 'Ratri Gadlings +1', 'STR':28, 'DEX':48, 'VIT':34, 'AGI':0, 'INT':14, 'MND':32, 'CHR':24, 'Magic Accuracy':44, 'Scythe Skill':53, 'Gear Haste':4, 'Weapon Skill Damage':8}
Ryuo_Tekko_A = {'Name': 'Ryuo Tekko +1', 'Name2': 'Ryuo Tekko +1 A', 'STR':12+12, 'DEX':38+12, 'VIT':30, 'AGI':13, 'INT':12, 'MND':30, 'CHR':17,'Accuracy':33+20,'Ranged Accuracy':33,'Gear Haste':4,'Crit Rate':5,'Crit Damage':5, 'Jobs':[]}
Ryuo_Tekko_D = {'Name': 'Ryuo Tekko +1', 'Name2': 'Ryuo Tekko +1 D', 'STR':12, 'DEX':38+12, 'VIT':30, 'AGI':13, 'INT':12, 'MND':30, 'CHR':17,'Accuracy':33+25,'Ranged Accuracy':33,'Gear Haste':4,'Crit Rate':5,'Crit Damage':5, "DA":0+4, 'Jobs':[]}
Sakpata_Gauntlets = {'Name': 'Sakpata\'s Gauntlets', 'Name2': 'Sakpata\'s Gauntlets R15', 'STR':24,'DEX':35,"VIT":46,"AGI":0,'INT':14,'MND':33,'CHR':26,'Accuracy':40+5,'Magic Accuracy':40+5,'Attack':40+20,'Gear Haste':4,"DA":6,'PDL':6,'Store TP':5}
Sulevia_Gauntlets = {'Name': 'Sulevia\'s Gauntlets +2', 'STR':23,'DEX':34,"VIT":45,"AGI":0,'INT':6,'MND':32,'CHR':27,'Accuracy':43,'Attack':47,'Gear Haste':3,"DA":6}
Tatenashi_Gote = {'Name': 'Tatenashi Gote', 'Name2': 'Tatenashi Gote R15', 'STR':8+10, 'DEX':40+10, 'VIT':32+10, 'AGI':7+10, 'INT':6+10, 'MND':23+10, 'CHR':16+10,'Accuracy':21+40,'Gear Haste':4,'Store TP':7,"TA":0+4, 'Jobs':[]}
Hattori_Tekko = {'Name': 'Hattori Tekko +1', 'STR':12,'DEX':45,'VIT':29,'AGI':14,'INT':12,'MND':30,'CHR':17,'Gear Haste':5,'Accuracy':23,'Ninjutsu Magic Attack':14}
hands = [Adhemar_Wristbands_A, Adhemar_Wristbands_B, Mochizuki_Tekko, Mummu_Wrists, Malignance_Gloves, Kendatsuba_Tekko, Nyame_Gauntlets, Mpaca_Gloves, Tatenashi_Gote, Ryuo_Tekko_A, Ryuo_Tekko_D,Hattori_Tekko]

Apate_Ring = {'Name': 'Apate Ring', 'STR':6, 'DEX':6, 'AGI':6, 'Store TP':3,'Jobs':[]}
Archon_Ring = {'Name': 'Archon Ring', 'Dark Elemental Bonus':5,'Jobs':[]}
Archon_Ring = {'Name': 'Archon Ring', 'Dark Affinity': 5,'Jobs':[]}
Begrudging_Ring = {'Name': 'Begrudging Ring', 'Accuracy':7, 'Attack': 7, 'Crit Rate':5,'Jobs':[]}
Beithir_Ring = {'Name': 'Beithir Ring', 'Name2': 'Beithir Ring R25', 'STR':3, 'DEX':3, 'VIT':3, 'AGI':3, 'Weaponskill Accuracy':0+15, 'Attack':0+10, 'Weaponskill Damage':2,'Jobs':[]}
Beithir_Ring30 = {'Name': 'Beithir Ring', 'Name2': 'Beithir Ring R30', 'STR':3, 'DEX':3, 'VIT':3, 'AGI':3, 'Weaponskill Accuracy':0+15, 'Attack':0+15, 'Weaponskill Damage':2,'Jobs':[]}
Chirich_Ring = {'Name': 'Chirich Ring +1', 'Accuracy':10, 'Store TP':6,'Jobs':[]}
Crepuscular_Ring = {'Name': 'Crepuscular Ring', 'Ranged Accuracy':10, 'Magic Accuracy':10, 'Store TP':6}
Dingir_Ring = {'Name': 'Dingir Ring', 'AGI':10, 'Ranged Attack':25, 'Magic Attack':10,'Jobs':[]}
Epaminondas_Ring = {'Name': "Epaminondas's Ring", 'Weaponskill Damage':5, 'Store TP':-10,'Jobs':[]}
Epona_Ring = {'Name': 'Epona\'s Ring', "DA":3,"TA":3,'Jobs':[]}
Flamma_Ring = {'Name': 'Flamma Ring', 'Accuracy':6, 'Magic Accuracy':6, 'STP':5}
Gere_Ring = {'Name': 'Gere Ring', 'STR':10, 'Attack':16, "TA":5,'Jobs':[]}
Hetairoi_Ring = {'Name': 'Hetairoi Ring', 'Crit Rate':1, "TA":2, 'TA DMG':5,'Jobs':[]}
Ilabrat_Ring = {'Name': 'Ilabrat Ring', 'DEX':10, 'AGI':10, 'Attack':25, 'Store TP':5,'Jobs':[]}
Karieyh_Ring = {'Name': 'Karieyh Ring', 'Weaponskill Accuracy':10, 'Weaponskill Damage':4,'Jobs':[]}
Locus_Ring = {'Name': 'Locus Ring', 'Magic Burst Damage':5,'Jobs':[]}  # Ignoring the Magic Crit Rate +5 stat since we do not know how it behaves.
Metamorph_Ring = {'Name': 'Metamorph Ring +1', 'Name2': 'Metamorph Ring +1 R15', 'INT':6+10, 'MND':6+10, 'CHR':6+10, 'Magic Accuracy':4+10,'Jobs':[]}
Mujin_Band = {'Name': 'Mujin Band', 'Skillchain Bonus': 5, 'Magic Burst Damage II':5,'Jobs':[]}
Mummu_Ring = {'Name': 'Mummu Ring', 'Accuracy':6, 'Ranged Accuracy':6, 'Magic Accuracy':6, 'Crit Rate':3,'Jobs':[]}
Niqmaddu_Ring = {'Name': 'Niqmaddu Ring', 'STR':10, 'DEX':10, 'VIT':10, 'QA':3,'Jobs':[]}
Petrov_Ring = {'Name': 'Petrov Ring', 'STR':3, 'DEX':3, 'VIT':3, 'AGI':3, "DA":1,'Store TP':5,'Jobs':[]}
Regal_Ring = {'Name': 'Regal Ring', 'STR':10, 'DEX':10, 'VIT':10, 'AGI':10, 'Attack':20, 'Ranged Attack':20,'Jobs':[]}
Rufescent_Ring = {'Name': 'Rufescent Ring', 'STR':6, 'MND':6, 'Weaponskill Accuracy': 7,'Jobs':[]}
Shiva_Ring1 = {'Name': 'Shiva Ring +1', 'Name': 'Shiva Ring +1A', 'INT':9, 'Magic Attack':3,'Jobs':[]}
Shiva_Ring2 = {'Name': 'Shiva Ring +1', 'Name': 'Shiva Ring +1B', 'INT':9, 'Magic Attack':3,'Jobs':[]}
Shukuyu_Ring = {'Name': 'Shukuyu Ring', 'STR':7, 'Attack':15,'Jobs':[]}
Sroda_Ring = {'Name': 'Sroda Ring', 'STR':15, 'DEX':-20, 'PDL':3}
Weatherspoon_Ring = {'Name': 'Weatherspoon Ring +1', 'Light Elemental Bonus':11, 'Magic Accuracy':13,'Jobs':[]}

rings = [Mujin_Band, Sroda_Ring, Gere_Ring, Hetairoi_Ring, Shukuyu_Ring, Apate_Ring, Ilabrat_Ring, Regal_Ring, Epona_Ring, Petrov_Ring, Rufescent_Ring, Begrudging_Ring, Epaminondas_Ring, Mummu_Ring, Beithir_Ring, Dingir_Ring, Metamorph_Ring, Shiva_Ring1, Shiva_Ring2, Weatherspoon_Ring]
rings2 = [Mujin_Band, Sroda_Ring, Gere_Ring, Hetairoi_Ring, Shukuyu_Ring, Apate_Ring, Ilabrat_Ring, Regal_Ring, Epona_Ring, Petrov_Ring, Rufescent_Ring, Begrudging_Ring, Epaminondas_Ring, Mummu_Ring, Beithir_Ring, Dingir_Ring, Metamorph_Ring, Shiva_Ring1, Shiva_Ring2, Weatherspoon_Ring]

Andartia_Critagi = {'Name': 'Andartia\'s Mantle', 'Name2': 'Andartia\'s Mantle AGI Crit Rate', 'AGI':30, 'Accuracy':20, 'Attack':20, 'Crit Rate':10, 'Jobs':['nin']}
Andartia_Critdex = {'Name': 'Andartia\'s Mantle', 'Name2': 'Andartia\'s Mantle DEX Crit Rate', 'DEX':30, 'Accuracy':20, 'Attack':20, 'Crit Rate':10, 'Jobs':['nin']}
Andartia_DAagi = {'Name': 'Andartia\'s Mantle', 'Name2': 'Andartia\'s Mantle STR DA', 'AGI':30, 'Accuracy':20, 'Attack':20, "DA":10, 'Jobs':['nin']}
Andartia_DAdex = {'Name': 'Andartia\'s Mantle', 'Name2': 'Andartia\'s Mantle DEX DA', 'DEX':30, 'Accuracy':20, 'Attack':20, "DA":10, 'Jobs':['nin']}
Andartia_DAstr = {'Name': 'Andartia\'s Mantle', 'Name2': 'Andartia\'s Mantle STR DA', 'STR':30, 'Accuracy':20, 'Attack':20, "DA":10, 'Jobs':['nin']}
Andartia_Nuke = {'Name': 'Andartia\'s Mantle', 'Name2': 'Andartia\'s Mantle INT Magic Attack', 'INT':30, 'Magic Attack':10, 'Magic Accuracy':20, 'Magic Damage':20, 'Jobs':['nin']}
Andartia_WSDstr_mdmg = {'Name': 'Andartia\'s Mantle', 'Name2': 'Andartia\'s Mantle STR WSD MDMG', 'INT':30, 'Weaponskill Damage':10, 'Magic Accuracy':20, 'Magic Damage':20, 'Jobs':['nin']}
Andartia_STP = {'Name': 'Andartia\'s Mantle', 'Name2': 'Andartia\'s Mantle DEX Store TP', 'DEX':30, 'Accuracy':20, 'Attack':20, 'Store TP':10, 'Jobs':['nin']}
Andartia_WSDagi = {'Name': 'Andartia\'s Mantle', 'Name2': 'Andartia\'s Mantle AGI WSD', 'AGI':30, 'Accuracy':20, 'Attack':20, 'Weaponskill Damage':10, 'Jobs':['nin']}
Andartia_WSDdex = {'Name': 'Andartia\'s Mantle', 'Name2': 'Andartia\'s Mantle DEX WSD', 'DEX':30, 'Accuracy':20, 'Attack':20, 'Weaponskill Damage':10, 'Jobs':['nin']}
Andartia_WSDstr = {'Name': 'Andartia\'s Mantle', 'Name2': 'Andartia\'s Mantle STR WSD', 'STR':30, 'Accuracy':20, 'Attack':20, 'Weaponskill Damage':10, 'Jobs':['nin']}
Ankou_Mantle_WSDstr = {'Name': 'Ankou\'s Mantle', 'Name2': 'Ankou\'s Mantle STR WSD', 'STR':30, 'Accuracy':20, 'Attack':20, 'Weaponskill Damage':10, 'Jobs':['drk']}
Ankou_Mantle_DAstr = {'Name': 'Ankou\'s Mantle', 'Name2': 'Ankou\'s Mantle STR DA', 'STR':30, 'Accuracy':20, 'Attack':20, "DA":10, 'Jobs':['drk']}
Ankou_Mantle_STPdex = {'Name': 'Ankou\'s Mantle', 'Name2': 'Ankou\'s Mantle DEX Store TP', 'DEX':30, 'Accuracy':20, 'Attack':20, 'Store TP':10, 'Jobs':['drk']}
Smirtrios_DAstr = {'Name': 'Smirtrios\'s Mantle', 'Name2': 'Smirtrios\'s Mantle STR DA', 'STR':30, 'Attack':20, 'Accuracy':20, "DA":10, "Skillchain Bonus":3,'Jobs':['sam']}
Smirtrios_WSDstr = {'Name': 'Smirtrios\'s Mantle', 'Name2': 'Smirtrios\'s Mantle STR WSD', 'STR':30, 'Attack':20, 'Accuracy':20, 'Weaponskill Damage':10, "Skillchain Bonus":3,'Jobs':['sam']}
capes = [Andartia_DAdex, Andartia_DAstr, Andartia_DAagi, Andartia_Critagi, Andartia_Critdex, Andartia_WSDstr, Andartia_WSDdex, Andartia_WSDagi, Andartia_Nuke, Andartia_WSDstr_mdmg]

Eschan_Stone = {'Name': 'Eschan Stone', 'Accuracy':15, 'Ranged Accuracy':15, 'Attack':15, 'Ranged Attack':15, 'Magic Accuracy':7, 'Magic Attack':7,'Jobs':[]}
Fotia_Belt = {'Name': 'Fotia Belt', 'Weaponskill Accuracy': 10, 'ftp': 25./256.,'Jobs':[]}
Grunfeld_Rope = {'Name': 'Grunfeld Rope', 'STR':5, 'DEX':5, 'Accuracy':10, 'Attack':20, "DA":2,'Jobs':[]}
Hachirin_no_Obi = {'Name': 'Hachirin-no-Obi', 'Weather':1,'Jobs':[]}
Ioskeha_Belt = {'Name': 'Ioskeha Belt +1', 'Accuracy':17, "DA":9, 'Gear Haste':8,'Jobs':[]}
Kentarch_Belt = {'Name': 'Kentarch Belt +1', 'Name2': 'Kentarch Belt +1 R15', 'STR':0+10, 'DEX':0+10, 'Accuracy':14, "DA":3, 'Store TP':5,'Jobs':[]}
Orpheus_Sash = {'Name': "Orpheus's Sash", 'Elemental Bonus': 15,'Jobs':[]}
Reiki_Yotai = {'Name': 'Reiki Yotai', 'Accuracy':10, 'Ranged Accuracy':10, 'Store TP':4, 'Dual Wield':7,'Jobs':[]}
Sailfi_Belt = {'Name': 'Sailfi Belt +1', 'Name2': 'Sailfi Belt +1 R15', 'Gear Haste':9, "TA":2, 'Attack':14, 'STR':0+15, "DA":0+5,'Jobs':[]}
Windbuffet_Belt = {'Name': 'Windbuffet Belt +1', 'Accuracy':2, "TA":2, 'QA':2,'Jobs':[]}
Skymir_Cord = {'Name':'Skymir Cord +1', 'Magic Accuracy':7, 'Magic Attack':7, 'Magic Damage':35}
belts = [Windbuffet_Belt, Fotia_Belt, Grunfeld_Rope, Kentarch_Belt, Sailfi_Belt, Orpheus_Sash,Skymir_Cord]

Adhemar_Kecks_A = {'Name': 'Adhemar Kecks +1', 'Name2': 'Adhemar Kecks +1 A', 'STR':32, 'DEX':0+12, 'VIT':15, 'AGI':30+12, 'INT':28, 'MND':16, 'CHR':8, 'Accuracy':34+20, 'Ranged Accuracy':34, 'Gear Haste':6, 'Store TP':8,'Jobs':[]}
Adhemar_Kecks_B = {'Name': 'Adhemar Kecks +1', 'Name2': 'Adhemar Kecks +1 B', 'STR':32+12, 'DEX':0+12, 'VIT':15, 'AGI':30, 'INT':28, 'MND':16, 'CHR':8, 'Accuracy':34, 'Ranged Accuracy':34, 'Attack':20, 'Gear Haste':6, 'Store TP':8,'Jobs':[]}
Fallen_Flanchard = {'Name': 'Fallen\'s Flanchard +3', 'STR':45,'DEX':0,"VIT":31,"AGI":26,'INT':40,'MND':27,'CHR':20,'Accuracy':39,'Attack':64,'Gear Haste':5,'Weapon Skill Damage':10}
Flamma_Dirs = {'Name': 'Flamma Dirs +2', 'STR':53,'DEX':11,"VIT":29,"AGI":16,'INT':24,'MND':14,'CHR':11,'Accuracy':45,'Magic Accuracy':45,'Gear Haste':4,'Store TP':8}
Gyve_Trousers = {'Name': 'Gyve Trousers', 'STR':19, 'DEX':12, 'VIT':19, 'AGI':5, 'INT':35, 'MND':25, 'CHR':23, 'Magic Attack':40, 'Gear Haste':5,'Jobs':[]}
Hachiya_Hakama = {'Name': 'Hachiya Hakama +3', 'STR':42, 'DEX':0, 'VIT':24, 'AGI':31, 'INT':42, 'MND':27, 'CHR':20, 'Accuracy':56, 'Ranged Accuracy':35, 'Gear Haste':6, 'Store TP':6, 'Dual Wield':5,'Jobs':[]}
Herculean_Trousers = {'Name': 'Herculean Trousers', 'STR':33, 'DEX':0, 'VIT':16, 'AGI':32, 'INT':29, 'MND':15, 'CHR':10, 'Attack':15, 'Ranged Attack':15,'Gear Haste':6, 'Store TP':4,'Jobs':[]}
Hizamaru_Hizayoroi = {'Name': 'Hizamaru Hizayoroi +2', 'STR':50, 'DEX':0, 'VIT':32, 'AGI':24, 'INT':24, 'MND':11, 'CHR':19, 'Accuracy':45, 'Attack':27, 'Gear Haste':9, 'Weaponskill Damage':7,'Jobs':[]}
Ignominy_Flanchard = {'Name': 'Ignominy Flanchard +3', 'STR':50,'DEX':15,"VIT":31,"AGI":26,'INT':40,'MND':22,'CHR':20,'Accuracy':49,'Attack':45,'Gear Haste':5,"DA":10}
Jokushu_Haidate = {'Name': 'Jokushu Haidate', 'STR':29, 'DEX':35, 'VIT':15, 'AGI':21, 'INT':30, 'MND':17, 'CHR':11, 'Gear Haste':20, 'Crit Rate':4,'Jobs':[]}
Kendatsuba_Hakama = {'Name': 'Kendatsuba Hakama +1', 'STR':37, 'DEX':5, 'VIT':25, 'AGI':33, 'INT':32, 'MND':16,'CHR':12,'Accuracy':51,'Ranged Accuracy':46,'Gear Haste':9,"TA":5,'Crit Rate':7,'Jobs':[]}
Malignance_Tights = {'Name': 'Malignance Tights', 'STR':28, 'DEX':0, 'VIT':17, 'AGI':42, 'INT':26, 'MND':19, 'CHR':12, 'Accuracy':50, 'Ranged Accuracy':50, 'Magic Accuracy':50, 'Gear Haste':9, 'Store TP':10, 'PDL':5,'Jobs':[]}
Mochizuki_Hakama = {'Name': 'Mochizuki Hakama +3', 'STR':42, 'DEX':0, 'VIT':24, 'AGI':36, 'INT':42, 'MND':27, 'CHR':20, 'Accuracy':39, 'Attack':64, 'Magic Accuracy':39, 'Gear Haste':6, "Dual Wield":10, 'Weaponskill Damage':10,'Jobs':[]}
Mpaca_Hose = {'Name': 'Mpaca\'s Hose', 'Name2': 'Mpaca\'s Hose R25', "STR":49, "DEX":0, "VIT":32, "AGI":25, "INT":32,"MND":19,"CHR":19,"Accuracy":40+10,"Attack":40+25,"Magic Accuracy":40+10,"Gear Haste":9,"TA":4,"Crit Rate":6,'PDL':0+7,'Jobs':[]}
Mpaca_Hose30 = {'Name': 'Mpaca\'s Hose', 'Name2': 'Mpaca\'s Hose R30', "STR":49, "DEX":0, "VIT":32, "AGI":25, "INT":32,"MND":19,"CHR":19,"Accuracy":40+15,"Attack":40+30,"Magic Accuracy":40+15,"Gear Haste":9,"TA":4,"Crit Rate":6,'PDL':0+8,'Jobs':[]}
Mummu_Kecks = {'Name': 'Mummu Kecks +2', 'STR':33, 'DEX':11, 'VIT':16, 'AGI':45, 'INT':29, 'MND':15, 'CHR':12, 'Accuracy':45, 'Ranged Accuracy':45, 'Magic Accuracy': 45, 'Gear Haste':6, 'Crit Rate': 7,'Jobs':[]}
Nyame_Flanchard = {'Name': 'Nyame Flanchard', 'Name2': 'Nyame Flanchard R25 B', 'STR':43, 'DEX':0, 'VIT':30, 'AGI':34, 'INT':44, 'MND':32, 'CHR':24, 'Accuracy':40, 'Attack':30+30, 'Gear Haste':3, 'Weaponskill Damage':0+11, 'Magic Accuracy':40, 'Magic Attack':30, 'Ranged Accuracy':40, 'Ranged Attack':30+30,"DA":0+5,'Magic Burst Damage':6,'Jobs':[]}
Nyame_Flanchard30 = {'Name': 'Nyame Flanchard', 'Name2': 'Nyame Flanchard R30 B', 'STR':43, 'DEX':0, 'VIT':30, 'AGI':34, 'INT':44, 'MND':32, 'CHR':24, 'Accuracy':40, 'Attack':30+35, 'Gear Haste':3, 'Weaponskill Damage':0+12, 'Magic Accuracy':40, 'Magic Attack':30, 'Ranged Accuracy':40, 'Ranged Attack':30+35,"DA":0+6,'Magic Burst Damage':6,'Jobs':[]}
Rao_Haidate_B = {'Name': 'Rao Haidate +1', 'Name2': 'Rao Haidate +1 B', 'STR':46+12, 'DEX':0+12, 'VIT':15, 'AGI':21, 'INT':30, 'MND':31, 'CHR':8, 'Attack':43+20, 'Gear Haste':6, 'Store TP':8,'Jobs':[]}
Ratri_Cuisses = {'Name': 'Ratri Cuisses +1', 'STR':52, 'DEX':0, 'VIT':21, 'AGI':19, 'INT':37, 'MND':19, 'CHR':15, 'Magic Accuracy':46, 'Scythe Skill':55, 'Gear Haste':5, 'Weapon Skill Damage':9, 'Store TP':10}
Ryuo_Hakama_A = {'Name': 'Ryuo Hakama +1', 'Name2': 'Ryuo Hakama +1 A', 'STR':29+12, 'DEX':0+12, 'VIT':15, 'AGI':21, 'INT':30, 'MND':17, 'CHR':11,'Accuracy':0+20,'Attack':33,'Ranged Attack':33, 'Gear Haste':5,'Store TP':8,"DA":4,'Jobs':[]}
Sakpata_Cuisses = {'Name': 'Sakpata\'s Cuisses', 'Name2': 'Sakpata\'s Cuisses R15', 'STR':48,'DEX':0,"VIT":34,"AGI":23,'INT':32,'MND':21,'CHR':17,'Accuracy':40+5,'Magic Accuracy':40+5,'Attack':40+20,'Gear Haste':4,"DA":7,'PDL':7}
Samnuha_Tights = {'Name': 'Samnuha Tights', 'STR':38+10, 'DEX':6+10, 'VIT':15, 'AGI':30, 'INT':28, 'MND':16, 'CHR':8, 'Accuracy':15, 'Ranged Accuracy':15, 'Gear Haste':6, 'Store TP':7, "DA":3, "TA":3,'Jobs':[]}
Sulevia_Flanchard = {'Name': 'Sulevia\'s Flanchard +2', 'STR':47,'DEX':0,"VIT":33,"AGI":14,'INT':24,'MND':20,'CHR':18,'Accuracy':45,'Attack':49,'Gear Haste':2,"TA":4}
Tatenashi_Haidate = {'Name': 'Tatenashi Haidate', 'Name2': 'Tatenashi Haidate R15', 'STR':45+10, 'DEX':0+10, 'VIT':25+10, 'AGI':15+10, 'INT':23+10, 'MND':12+10, 'CHR':10+10,'Accuracy':0+60,'Attack':31,'Gear Haste':5,'Store TP':7,"TA":0+3,'Jobs':[]}
Wakido_Haidate = {'Name': 'Wakido Haidate +3', 'STR':44, 'DEX':0, 'VIT':29, 'AGI':25, 'INT':37, 'MND':26, 'CHR':20, 'Accuracy':49, 'Attack':40, 'Ranged Attack':40, 'Gear Haste':5, 'Store TP':9, 'Weaponskill Damage':10,'Jobs':[]}
Hattori_Hakama = {'Name': 'Hattori Hakama +1', 'STR':29,'DEX':0,'VIT':16,'AGI':20,'INT':30,'MND':17,'CHR':11,'Gear Haste':8,'Katana Skill':23,'Accuracy':20}
legs = [Kendatsuba_Hakama, Adhemar_Kecks_A, Adhemar_Kecks_B, Mochizuki_Hakama, Samnuha_Tights, Jokushu_Haidate, Malignance_Tights, Mummu_Kecks, Gyve_Trousers, Hizamaru_Hizayoroi, Nyame_Flanchard, Mpaca_Hose, Tatenashi_Haidate, Ryuo_Hakama_A, Rao_Haidate_B]

Adhemar_Gamashes_A = {'Name': 'Adhemar Gamashes +1', 'Name2': 'Adhemar Gamashes +1 A', 'STR':15, 'DEX':23+12, 'VIT':8, 'AGI':42+12, "INT":0, 'MND':11, 'CHR':25, 'Accuracy':20, 'Attack':34, 'Ranged Attack':34, 'Magic Attack':35, 'Gear Haste':4, 'Crit Rate':4, 'Jobs':[]}
Adhemar_Gamashes_B = {'Name': 'Adhemar Gamashes +1', 'Name2': 'Adhemar Gamashes +1 B', 'STR':15+12, 'DEX':23+12, 'VIT':8, 'AGI':42, "INT":0, 'MND':11, 'CHR':25, 'Attack':34+20, 'Ranged Attack':34, 'Magic Attack':35, 'Gear Haste':4, 'Crit Rate':4, 'Jobs':[]}
Flamma_Gambieras = {'Name': 'Flamma Gambieras +2', 'STR':31,'DEX':34,"VIT":20,"AGI":26,'INT':0,'MND':6,'CHR':20,'Accuracy':42,'Magic Accuracy':42,'Gear Haste':2,'Store TP':6,"DA":6}
Hachiya_Kyahan = {'Name': 'Hachiya Kyahan +3', 'STR':24, 'DEX':25, 'VIT':21, 'AGI':44, 'INT':20, 'MND':22, 'CHR':39, 'Magic Accuracy':52, 'Magic Attack':23, 'Gear Haste':4, 'Magic Burst Damage': 10, 'Jobs':[]}
Herculean_Boots = {'Name': 'Herculean Boots', 'STR':16, 'DEX':24, 'VIT':10, 'AGI':43, "INT":0, 'MND':11, 'CHR':26, 'Accuracy':10, 'Attack':10,'Ranged Accuracy':10,'Ranged Attack':10,'Magic Accuracy':10,'Magic Attack':10,'Gear Haste':4,"TA":2, 'Jobs':[]}
Herculean_Boots_QA = {'Name': 'Herculean Boots', 'STR':16, 'DEX':24, 'VIT':10, 'AGI':43, "INT":0, 'MND':11, 'CHR':26, 'Accuracy':10+35, 'Attack':10+18,'Ranged Accuracy':10,'Ranged Attack':10,'Magic Accuracy':10+3,'Magic Attack':10+3,'Gear Haste':4,"TA":2,'QA':3, 'Jobs':[]}
Herculean_Boots_WSDdex = {'Name': 'Herculean Boots', 'STR':16, 'DEX':24+14, 'VIT':10, 'AGI':43, "INT":0, 'MND':11, 'CHR':26, 'Accuracy':10+3, 'Attack':10+17,'Ranged Accuracy':10,'Ranged Attack':10,'Magic Accuracy':10,'Magic Attack':10,'Gear Haste':4,"TA":2,'Weaponskill Damage':0+4, 'Jobs':[]}
Hizamaru_Sune_Ate = {'Name': 'Hizamaru Sune-ate +2', 'STR':28, 'DEX':31, 'VIT':23, 'AGI':34, "INT":0, 'MND':3, 'CHR':28, 'Accuracy':42, 'Attack':24, 'Gear Haste':3, 'Dual Wield':8, 'Jobs':[]}
Kendatsuba_Sune_Ate = {'Name': 'Kendatsuba Sune-ate +1', 'STR':20, 'DEX':44, 'VIT':21, 'AGI':44, "INT":0, 'MND':14, 'CHR':26, 'Accuracy':48, 'Ranged Accuracy':43, 'Gear Haste':3, "TA":4, 'Crit Rate':5, 'Jobs':[]}
Malignance_Boots = {'Name': 'Malignance Boots', 'STR':6, 'DEX':40, 'VIT':12, 'AGI':49, "INT":0, 'MND':15, 'CHR':40, 'Accuracy':50, 'Ranged Accuracy':50, 'Magic Accuracy':50, 'Gear Haste':3, 'Store TP':9, 'PDL':2, 'Jobs':[]}
Mochizuki_Kyahan = {'Name': 'Mochizuki Kyahan +3', 'STR':28, 'DEX':29, 'VIT':25, 'AGI':48, "INT":0, 'MND':22, 'CHR':39, 'Accuracy':43, 'Attack':76, 'Magic Accuracy':36, 'Ninjutsu Skill':23, 'Gear Haste':4, 'Ninjutsu Damage':25, 'Jobs':[]}
Mpaca_Boots = {'Name': "Mpaca\'s Boots", 'Name2': "Mpaca\'s Boots R25","STR":28,"DEX":32,"VIT":23,"AGI":34,"INT":0,"MND":11,"CHR":28,"Accuracy":40+10,"Attack":40+25,"Magic Accuracy":40+10,"Gear Haste":3,"TA":3,"Crit Rate":3,"Magic Attack":0+40, 'Jobs':[]}
Mpaca_Boots30 = {'Name': "Mpaca\'s Boots", 'Name2': "Mpaca\'s Boots R30", "STR":28,"DEX":32,"VIT":23,"AGI":34,"INT":0,"MND":11,"CHR":28,"Accuracy":40+10,"Attack":40+30,"Magic Accuracy":40+15,"Gear Haste":3,"TA":3,"Crit Rate":3,"Magic Attack":0+45, 'Jobs':[]}
Mummu_Gamashes = {'Name': 'Mummu Gamashes +2', 'STR':16, 'DEX':37, 'VIT':10, 'AGI':57, "INT":0, 'MND':11, 'CHR':29, 'Accuracy':42, 'Ranged Accuracy': 42, 'Magic Accuracy': 42, 'Gear Haste':4, 'Crit Rate':5, 'Jobs':[]}
Nyame_Sollerets = {'Name': 'Nyame Sollerets', 'Name2': 'Nyame Sollerets R25 B', 'STR':23, 'DEX':26, 'VIT':24, 'AGI':46, 'INT':25, 'MND':26, 'CHR':38, 'Accuracy':40, 'Attack':30+30, 'Gear Haste':3, 'Weaponskill Damage':0+10, 'Magic Accuracy':40, 'Magic Attack':30, 'Ranged Accuracy':40, 'Ranged Attack':30+30,"DA":0+4,'Magic Burst Damage':5, 'Jobs':[]}
Nyame_Sollerets30 = {'Name': 'Nyame Sollerets', 'Name2': 'Nyame Sollerets R30 B', 'STR':23, 'DEX':26, 'VIT':24, 'AGI':46, 'INT':25, 'MND':26, 'CHR':38, 'Accuracy':40, 'Attack':30+35, 'Gear Haste':3, 'Weaponskill Damage':0+11, 'Magic Accuracy':40, 'Magic Attack':30, 'Ranged Accuracy':40, 'Ranged Attack':30+35,"DA":0+5,'Magic Burst Damage':5, 'Jobs':[]}
Rao_SuneAte_D = {'Name': 'Rao Sune-ate +1', 'Name2': 'Rao Sune-ate +1 D', 'STR':17, 'DEX':26, 'VIT':12, 'AGI':34, 'INT':0, 'MND':16, 'CHR':28,'Accuracy':41,'Crit Rate':0+4,'Gear Haste':4,"DA":0+4, 'Jobs':[]}
Ratri_Sollerets = {'Name': 'Ratri Sollerets +1', 'STR':29, 'DEX':26, 'VIT':17, 'AGI':32, 'INT':0, 'MND':16, 'CHR':31, 'Magic Accuracy':43, 'Scythe Skill':52, 'Gear Haste':3, 'Weapon Skill Damage':8}
Ryuo_SuneAte_D = {'Name': 'Ryuo Sune-Ate +1', 'Name2': 'Ryuo Sune-ate +1 D', 'STR':27+12, 'DEX':19, 'VIT':11, 'AGI':38, 'INT':0, 'MND':5, 'CHR':19,'Attack':32+25,'Ranged Attack':32,'Crit Rate':0+4,'Gear Haste':3, 'Jobs':[]}
Sakpata_Leggings = {'Name': 'Sakpata\'s Leggings', 'Name2': 'Sakpata\'s Leggings R15', 'STR':29,'DEX':20,"VIT":30,"AGI":35,'INT':0,'MND':19,'CHR':32,'Accuracy':40+5,'Magic Accuracy':40+5,'Attack':40+20,'Gear Haste':2,"DA":4,'PDL':4}
Sulevia_Leggings = {'Name': 'Sulevia\'s Leggings +2', 'STR':29,'DEX':19,"VIT":29,"AGI":26,'INT':0,'MND':18,'CHR':32,'Accuracy':42,'Attack':46,'Gear Haste':1,'Weapon Skill Damage':7}
Tatenashi_SuneAte = {'Name': 'Tatenashi Sune-ate', 'Name2': 'Tatenashi Sune-ate R15', 'STR':16+10, 'DEX':19+10, 'VIT':16+10, 'AGI':32+10, 'INT':0+10, 'MND':5+10, 'CHR':19+10,'Accuracy':0+60,'Gear Haste':3,'Store TP':7,"TA":0+3, 'Jobs':[]}
Hattori_Kyahan = {'Name': 'Hattori Kyahan +1', 'STR':14,'DEX':26,'VIT':12,'AGI':39,'INT':0,'MND':12,'CHR':30,'Gear Haste':5}
feet = [Mochizuki_Kyahan, Adhemar_Gamashes_A, Adhemar_Gamashes_B, Malignance_Boots, Mummu_Gamashes, Kendatsuba_Sune_Ate, Nyame_Sollerets, Mpaca_Boots, Tatenashi_SuneAte, Ryuo_SuneAte_D, Rao_SuneAte_D]


# Confirm that the stats for each piece of gear being checked are spelled correctly.
# Compare each stat against a pre-made list of accepted stats.
available_stats = ['Accuracy', 'AGI', 'Attack', 'Axe Skill', 'CHR', 'Club Skill', 'Crit Damage', 'Crit Rate', "DA", 'DA DMG', 'Dagger Skill', 'Daken', 'Dark Affinity', 'Dark Elemental Bonus', 'Delay', 'DEX', 'DMG', 'Dual Wield', 'Earth Affinity', 'Earth Elemental Bonus', 'Elemental Bonus', 'Fire Affinity', 'Fire Elemental Bonus', 'ftp', 'Gear Haste', 'Great Axe Skill', 'Great Katana Skill', 'Great Sword Skill', 'Hand-to-Hand Skill', 'Ice Affinity', 'Ice Elemental Bonus', 'INT', 'Jobs', 'Katana Skill', 'Light Affinity', 'Light Elemental Bonus', 'Magic Accuracy Skill', 'Magic Accuracy', 'Magic Attack', 'Magic Burst Damage II', 'Magic Burst Damage', 'Magic Damage', 'MND', 'Name', 'Name2', 'Ninjutsu Damage', 'Ninjutsu Magic Attack', 'Ninjutsu Skill', 'OA2', 'OA3', 'OA4', 'OA5', 'OA6', 'OA7', 'OA8', 'PDL', 'Polearm Skill', 'QA', 'Ranged Accuracy', 'Ranged Attack', 'Scythe Skill', 'Skill Type', 'Skillchain Bonus', 'Staff Skill', 'Store TP', 'STR', 'Sword Skill', "TA", 'TA DMG', 'Throwing Skill', 'Thunder Affinity', 'Thunder Elemental Bonus', 'TP Bonus', 'Type', 'Utu CHR', 'VIT', 'Water Affinity', 'Water Elemental Bonus', 'Weaponskill Accuracy', 'Weaponskill Damage', 'Wind Affinity', 'Wind Elemental Bonus']

typo = False
slots = [mains, subs, grips, ammos, heads, necks, ears, ears2, bodies, hands, rings, rings2, capes, belts, legs, feet]
for slot in slots:
  for gear in slot:
    keys = gear.keys()
    for key in keys:
      if key not in available_stats:
        print(f"Incorrect stat name found on \"{gear.get('Name2',gear['Name'])}\":  \"{key}\"")
        typo = True
if typo:
  print("Check the \"available_stats\" list at the end of the gear.py file for a list of accepted stat names.")
  import sys ; sys.exit()
