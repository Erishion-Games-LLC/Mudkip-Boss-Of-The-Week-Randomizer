import pandas as pd
import random

normalBosses = ["Gauntlet","Corrupted","Jad","Zuk","Barrows","Mole","Deranged Arch","Solo Prime","Solo Rex","Solo Supreme","Tribrid DKS","Sarachnis","KQ","kreeara","Zilyana","Graardor","Kril","Zulrah","Vorkath","Muspah","Corp","Nightmare","Phosani NM","Nex"]
slayerBosses = ["Grotesque Guardians","Abyssal Sire","Kraken","Cerberus","Thermy","Hydra"]
wildyBosses = ["Chaos Fanatic","Crazy Arch","Scorpia","Chaos Ele","KBD","Vetion","Calvarion","Venenatis","Spindel","Calisto","Artio"]
skillingBosses = ["Tempoross","Wintertodt","Zalcano"]
raids = ["COX Normal","COX CM","TOB Entry","TOB Normal","TOB Hard","TOA Entry","TOA Normal","TOA Expert"]
sporadicBosses = ["Obor","Bryo","Mimic","Hespori","Skotizo"]
ba = ["Yes","No"]

passingBosses = []

normalColumn =  'Which of these bosses should be included?'
slayerColumn =  'What slayer bosses should be included?'
wildyColumn =  'What wildy bosses should be included?'
skillingColumn =  'What skilling bosses should be included?'
raidsColumn =  'What raids should be included?'
sporadicColumn = 'What sporadic bosses should be included?'
baColumn = 'Should BA be included?'
  
FILE_NAME = 'Boss of the Week Bosses (Responses).xlsx'
data = pd.read_excel(FILE_NAME, header=0)
totalResponses = len(data)
passingPercentage = 0.70

#get all bosses above the passingPercentage and add to the passingBosses List
def findPassingBosses():

    for boss in normalBosses:
        if sum(data[normalColumn].str.contains(boss) * 1) / totalResponses >= passingPercentage:
            passingBosses.append(boss)
        
    for boss in slayerBosses:
        if sum(data[slayerColumn].str.contains(boss) * 1) / totalResponses >= passingPercentage:
            passingBosses.append(boss)

    for boss in wildyBosses:
        if sum(data[wildyColumn].str.contains(boss) * 1) / totalResponses >= passingPercentage:
            passingBosses.append(boss)

    for boss in skillingBosses:
        if sum(data[skillingColumn].str.contains(boss) * 1) / totalResponses >= passingPercentage:
            passingBosses.append(boss)

    for boss in raids:
        if sum(data[raidsColumn].str.contains(boss) * 1) / totalResponses >= passingPercentage:
            passingBosses.append(boss)

    for boss in sporadicBosses:
        if sum(data[sporadicColumn].str.contains(boss) * 1) / totalResponses >= passingPercentage:
            passingBosses.append(boss)

    for boss in ba:
        if sum(data[baColumn].str.contains(boss) * 1) / totalResponses >= passingPercentage:
            passingBosses.append(boss)
findPassingBosses()

print("The boss of the week is: " + random.choice(passingBosses))
