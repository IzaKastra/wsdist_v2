#
# Created by Kastra on Asura.
# Feel free to /tell in game or send a PM on FFXIAH you have questions, comments, or suggestions.
#
# Version date: 2022 January 28
#
from scipy.interpolate import interp1d
from set_stats import *
from get_dex_crit import *

def weaponskill_scaling(ws_name, tp, gearset, equipment, buffs, dStat, dual_wield, enemy_defense, enemy_agi):
    #
    # Setup weaponskill statistics (TP scaling, # of hits, ftp replication, WSC, etc)
    # Placed in separate file to reduce clutter in main file.
    # Need to sort alphabetically later.
    #
    player_str = gearset.playerstats['STR']
    player_dex = gearset.playerstats['DEX']
    player_vit = gearset.playerstats['VIT']
    player_agi = gearset.playerstats['AGI']
    player_int = gearset.playerstats['INT']
    player_mnd = gearset.playerstats['MND']
    player_chr = gearset.playerstats['CHR']
    player_attack1 = gearset.playerstats['Attack1']
    player_attack2 = gearset.playerstats['Attack2']
    player_attack2 = 0 if not dual_wield else player_attack2
    crit_rate = 0

    hybrid = False
    element = "None"
    ftp_hybrid = 0

    base_tp = [1000,2000,3000]
    if ws_name == 'Savage Blade':
        base_ftp = [4.0, 10.25, 13.75] # Base TP bonuses for 1k, 2k, 3k TP
        ftp = interp1d(base_tp, base_ftp)(tp) # Effective TP at WS use
        ftp_rep = False # Does this WS replicate FTP across all hits?
        wsc  = int(0.5*(player_str + player_mnd) + dStat[1]*gearset.playerstats[dStat[0]]) # Stat modifiers, including things like Utu Grip if applicable.
        nhits = 2 # Savage is a 2-hit weaponskill (+1 for offhand)
    elif ws_name == 'Blade: Shun':
        atk_boost = [1.0, 2.0, 3.0]
        ws_atk_bonus = interp1d(base_tp, atk_boost)(tp) - 1.0
        special_set = set_gear(buffs, equipment, ws_atk_bonus) # The attack bonus from Blade: Shun is applied before buffs. I needed to recalculate player attack with a "special set" to deal with this.
        player_attack1 = special_set.playerstats['Attack1'] # Redefine the player's attack1 and attack2 used in the weapon skill based on the FTP scaling value
        player_attack2 = special_set.playerstats['Attack2'] # These boosted attack1 and attack2 values do not show up in the player's stats shown in the final plot.
        ftp = 1.0
        ftp_rep = True
        wsc  = 0.85*player_dex + dStat[1]*gearset.playerstats[dStat[0]] # Assuming 5/5 Blade: Shun merits. Add clickable drop-down menu to adjust merits later.
        nhits = 5
    elif ws_name == 'Blade: Ten':
        base_ftp = [4.5, 11.5, 15.5]
        ftp      = interp1d(base_tp, base_ftp)(tp)
        ftp_rep = False
        wsc      = 0.3*(player_str+player_dex) + dStat[1]*gearset.playerstats[dStat[0]]
        nhits    = 1
    elif ws_name == 'Blade: Kamu':
        ftp  = 1.0
        ftp_rep = False
        wsc = 0.6*(player_int+player_str)
        nhits = 1
        special_set = set_gear(buffs, equipment, 1.25) # The attack bonus from Blade: Kamu is similar to Blade: Shun (see above)
        player_attack1 = special_set.playerstats['Attack1']
        player_attack2 = special_set.playerstats['Attack2']
        enemy_defense *= 0.75
    elif ws_name == 'Blade: Ku':
        acc_boost = [1.0, 1.05, 1.1] # Made these numbers up since it isnt known. It's probably just something like "accuracy+0/20/40".
        acc_bonus = interp1d(base_tp, acc_boost)(tp)
        ftp  = 1.25
        ftp_rep = True
        wsc = 0.3*(player_str+player_dex) + dStat[1]*gearset.playerstats[dStat[0]]
        nhits = 5
    elif ws_name == 'Blade: Metsu':
        ftp  = 5.0
        ftp_rep = False
        wsc = 0.8*player_dex
        nhits = 1
    elif ws_name == 'Blade: Hi':
        crit_rate +=  gearset.playerstats['Crit Rate']/100 # Blade: Hi can crit, so define crit rate now
        crit_boost = [0.15, 0.2, 0.25]
        crit_bonus = interp1d(base_tp, crit_boost)(tp) # Bonus crit rate from TP scaling
        crit_rate += crit_bonus
        crit_rate += get_dex_crit(player_dex, enemy_agi) # Bonus crit rate from the player's DEX stat vs enemy AGI stat
        ftp = 5.0
        ftp_rep = False
        wsc = 0.8*player_agi + dStat[1]*gearset.playerstats[dStat[0]]
        nhits = 1
    elif ws_name == 'Evisceration':
        crit_rate +=  gearset.playerstats['Crit Rate']/100
        crit_boost = [0.1, 0.25, 0.5]
        crit_bonus = interp1d(base_tp, crit_boost)(tp)
        crit_rate += crit_bonus
        crit_rate += get_dex_crit(player_dex, enemy_agi)
        ftp = 1.25
        ftp_rep = True
        wsc = 0.5*player_dex + dStat[1]*gearset.playerstats[dStat[0]]
        nhits = 5
    elif ws_name == 'Blade: Chi':
        hybrid    = True
        base_ftp  = [0.5, 1.375, 2.25]
        ftp_hybrid = interp1d(base_tp, base_ftp)(tp)
        ftp       = 1.0
        ftp_rep   = False
        wsc       = 0.3*(player_str+player_int) + dStat[1]*gearset.playerstats[dStat[0]]
        nhits     = 2
        element   = 'Earth'
    elif ws_name == 'Blade: Teki':
        hybrid    = True
        base_ftp  = [0.5, 1.375, 2.25]
        ftp_hybrid = interp1d(base_tp, base_ftp)(tp)
        ftp       = 1.0
        ftp_rep   = False
        wsc       = 0.3*(player_str+player_int) + dStat[1]*gearset.playerstats[dStat[0]]
        nhits     = 1
        element   = 'Water'
    elif ws_name == 'Blade: To':
        hybrid    = True
        base_ftp  = [0.5, 1.5, 2.5]
        ftp_hybrid = interp1d(base_tp, base_ftp)(tp)
        ftp       = 1.0
        ftp_rep   = False
        wsc       = 0.4*(player_str+player_int) + dStat[1]*gearset.playerstats[dStat[0]]
        nhits     = 1
        element   = 'Ice'
    elif ws_name == 'Blade: Retsu':
        base_ftp  = [0.5, 1.5, 2.5]
        ftp       = 1.0
        ftp_rep   = False
        wsc       = 0.6*player_dex + 0.2*player_str + dStat[1]*gearset.playerstats[dStat[0]]
        nhits     = 2
    elif ws_name == 'Asuran Fists':
        acc_boost = [1.0, 1.1, 1.2] # Made these numbers up, same as Blade: Ku (see above)
        acc_bonus = interp1d(base_tp, acc_boost)(tp)
        ftp       = 1.25
        ftp_rep   = True
        wsc       = 0.15*(player_vit + player_str) + dStat[1]*gearset.playerstats[dStat[0]]
        nhits     = 8
    elif ws_name == 'Impulse Drive':
        base_ftp = [1.0, 3.0, 5.5]
        ftp      = interp1d(base_tp, base_ftp)(tp)
        ftp_rep  = False
        wsc      = 1.0*player_str + dStat[1]*gearset.playerstats[dStat[0]]
        nhits    = 2
    elif ws_name == 'Stardiver':
        base_ftp = [0.75, 1.25, 1.75]
        ftp      = interp1d(base_tp, base_ftp)(tp)
        ftp_rep  = True
        wsc      = 0.85*player_str + dStat[1]*gearset.playerstats[dStat[0]]
        nhits    = 4
    elif ws_name == 'Tachi: Rana':
        acc_boost = [1.0, 1.05, 1.1] # Made these numbers up since it isnt known. It's probably just something like "accuracy+0/20/40".
        acc_bonus = interp1d(base_tp, acc_boost)(tp)
        ftp  = 1.0
        ftp_rep = False
        wsc = 0.5*player_str + dStat[1]*gearset.playerstats[dStat[0]]
        nhits = 3
    elif ws_name == 'Tachi: Fudo':
        base_ftp = [3.75, 5.75, 8.0]
        ftp = interp1d(base_tp, base_ftp)(tp)
        ftp_rep = False
        wsc = 0.8*player_str + dStat[1]*gearset.playerstats[dStat[0]]
        nhits = 1
    elif ws_name == 'Tachi: Kaiten':
        ftp  = 3.0
        ftp_rep = False
        wsc = 0.8*player_str + dStat[1]*gearset.playerstats[dStat[0]]
        nhits = 1
    elif ws_name == 'Tachi: Shoha':
        base_ftp = [1.375, 2.1875, 2.6875]
        ftp = interp1d(base_tp, base_ftp)(tp)
        ftp_rep = False
        special_set = set_gear(buffs, equipment, 1.375) # The attack bonus from Tachi: Shoha is similar to Blade: Shun (see above)
        player_attack1 = special_set.playerstats['Attack1']
        player_attack2 = special_set.playerstats['Attack2']
        wsc = 0.85*player_str + dStat[1]*gearset.playerstats[dStat[0]]
        nhits = 2
    elif ws_name == 'Tachi: Kasha':
        base_ftp = [1.5625, 2.6875, 4.125]
        ftp = interp1d(base_tp, base_ftp)(tp)
        ftp_rep = False
        special_set = set_gear(buffs, equipment, 1.65) # The attack bonus from Tachi: Kasha is similar to Blade: Shun (see above)
        player_attack1 = special_set.playerstats['Attack1']
        player_attack2 = special_set.playerstats['Attack2']
        wsc = 0.75*player_str + dStat[1]*gearset.playerstats[dStat[0]]
        nhits = 1
    elif ws_name == 'Tachi: Gekko':
        base_ftp = [1.5625, 2.6875, 4.125]
        ftp = interp1d(base_tp, base_ftp)(tp)
        ftp_rep = False
        special_set = set_gear(buffs, equipment, 2.0) # The attack bonus from Tachi: Gekko is similar to Blade: Shun (see above)
        player_attack1 = special_set.playerstats['Attack1']
        player_attack2 = special_set.playerstats['Attack2']
        wsc = 0.75*player_str + dStat[1]*gearset.playerstats[dStat[0]]
        nhits = 1
    elif ws_name == 'Tachi: Koki':
        hybrid    = True
        base_ftp  = [0.5, 1.5, 2.5]
        ftp_hybrid = interp1d(base_tp, base_ftp)(tp)
        ftp       = 1.0
        ftp_rep   = False
        wsc       = 0.3*player_mnd + 0.5*player_str + dStat[1]*gearset.playerstats[dStat[0]]
        nhits     = 1
        element   = 'Light'
    elif ws_name == 'Tachi: Kagero':
        hybrid    = True
        base_ftp  = [0.5, 1.5, 2.5]
        ftp_hybrid = interp1d(base_tp, base_ftp)(tp)
        ftp       = 1.0
        ftp_rep   = False
        wsc       = 0.75*player_str + dStat[1]*gearset.playerstats[dStat[0]]
        nhits     = 1
        element   = 'Fire'
    elif ws_name == 'Tachi: Goten':
        hybrid    = True
        base_ftp  = [0.5, 1.5, 2.5]
        ftp_hybrid = interp1d(base_tp, base_ftp)(tp)
        ftp       = 1.0
        ftp_rep   = False
        wsc       = 0.6*player_str + dStat[1]*gearset.playerstats[dStat[0]]
        nhits     = 1
        element   = 'Thunder'
    elif ws_name == 'Tachi: Jinpu':
        hybrid    = True
        base_ftp  = [0.5, 1.5, 2.5]
        ftp_hybrid = interp1d(base_tp, base_ftp)(tp)
        ftp       = 1.0
        ftp_rep   = False
        wsc       = 0.3*player_str + dStat[1]*gearset.playerstats[dStat[0]]
        nhits     = 2
        element   = 'Wind'

    scaling = {'hybrid':hybrid,
               'wsc':wsc,
               'nhits':nhits,
               'element':element,
               'ftp':ftp,
               'ftp_rep':ftp_rep,
               'player_attack1':player_attack1,
               'player_attack2':player_attack2,
               'enemy_def':enemy_defense,
               'crit_rate':crit_rate,
               'ftp_hybrid':ftp_hybrid}
    return(scaling)
