import pandas as pd

df = pd.read_csv('data/data.csv')

df.columns = [column.replace(" ", "_") for column in df.columns]

df['Pedigree_Status'] = df['Pedigree_Status'].str.replace(" ", "_")

unverified = df.query("Pedigree_Status == 'Birth_Notified'")

print(unverified)

#searchID = input("Please enter the ID of a sheep (NSIS or PedigreeID): ")

#print("Search Results for "+searchID+":\n-------")

def flatten_sum(matrix):
    return sum(matrix, [])

def getFamilyTree(root):
    output = []

    parentage = getParentage(root)
    output.append(parentage)


    for sheep in parentage:
        output.append(getParentage(sheep))

    output = flatten_sum(output)

    return output

def checkFamilyTree(tree):
    for sheep in tree:
        if not(isPedigree(sheep)):
            print("Sheep",sheep,"is not pedigree")
            return False
    return True

def showFamilyTree(tree):
    print("-------------\nParentage\n-------------")
    print("Dam:",tree[0],"Sire:",tree[1])
    print("-------------\nGrand-Parentage\n-------------")
    print("Dam:",tree[2],"Sire:",tree[3],"  |  Dam:",tree[4],"Sire:",tree[5])

def getParentage(id):
    return [dam(id),sire(id)]

# get dam id
def dam(id):
    return df.query("NSIS == '"+id+"' or Pedigree_ID == '"+id+"'")["Dam_Pedigree_ID"].iloc[0]

# get sire id
def sire(id):
    return df.query("NSIS == '"+id+"' or Pedigree_ID == '"+id+"'")["Sire_Pedigree_ID"].iloc[0]

def isPedigree(id):
    if df.query("NSIS == '"+id+"' or Pedigree_ID == '"+id+"'")["Pedigree_Status"].iloc[0] == "Pedigree":
        return True
    else:
        return False


familyTree = getFamilyTree('')
print(showFamilyTree(familyTree))
print("Is this sheep pedigree:",checkFamilyTree(familyTree))


# sample