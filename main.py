import pandas as pd

df = pd.read_csv('data/data.csv')

df.columns = [column.replace(" ", "_") for column in df.columns]

df['Pedigree_Status'] = df['Pedigree_Status'].str.replace(" ", "_")

unverified = df.query("Pedigree_Status == 'Birth_Notified'")

print(unverified)

#searchID = input("Please enter the ID of a sheep (NSIS or PedigreeID): ")

#print("Search Results for "+searchID+":\n-------")

def getFamilyTree():
    return []

# get dam id
def dam(id):
    return df.query("NSIS == '"+id+"' or Pedigree_ID == '"+id+"'")["Dam_Pedigree_ID"].iloc[0]

# get sire id
def sire(id):
    return df.query("NSIS == '"+id+"' or Pedigree_ID == '"+id+"'")["Sire_Pedigree_ID"].iloc[0]


'''
print("Target sheep\n-------")
searchedDf = df.query("NSIS == '"+searchID+"' or Pedigree_ID == '"+searchID+"'")
print("Pedigree Status: "+searchedDf["Pedigree_Status"].iloc[0])

sireID = searchedDf["Sire_Pedigree_ID"].iloc[0]
sireDf = df.query("NSIS == '"+sireID+"' or Pedigree_ID == '"+sireID+"'")
sirePedStatus = sireDf["Pedigree_Status"].iloc[0]

print("-------\nSire\n-------")
print("Pedigree Status: "+sirePedStatus)

grandSireID = sireDf["Sire_Pedigree_ID"].iloc[0]
grandSireDf = df.query("NSIS == '"+grandSireID+"' or Pedigree_ID == '"+grandSireID+"'")
grandSirePedStatus = grandSireDf["Pedigree_Status"].iloc[0]

print("-------\nGrand Sire\n-------")
print("Pedigree Status: "+grandSirePedStatus)

print("************\nRESULT\n************")
if (sirePedStatus == "Pedigree" and grandSirePedStatus == "Pedigree"):
    print("Sheep",searchID,"is Pedigree")
else:
    print("Sheep",searchID,"is NOT Pedigree")
'''