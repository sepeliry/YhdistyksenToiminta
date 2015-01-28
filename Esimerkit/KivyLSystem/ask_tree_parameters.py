import json

# Kysy puun yksittäiset parametrit
treeangle = int( input("tree angle? ") )
treelength = int( input("tree length? ") )
treedepth = int( input("tree depth? ") )
axiom = input("axiom? ")

# Sääntöjä voi olla kuinka monta vaan, joten
#  kysytään kunnes annetaan tyhjä sääntö.
rules = {}
while(True):
    loopfrom = input("rule convert this? ")
    if loopfrom=="":
        break
    loopto = input("to this? ")
    rules[loopfrom] = loopto

# Ota tästä kommentit pois jos haluat näyttää kysytyt tiedot ruudulla
#print("ang="+str(treeangle),
#"len="+str(treelength),
#"depth="+str(treedepth))
#print("axiom=", axiom)
#for key in rules:
#    print( key + " -> " + rules[key])

# Rakennetaan Pythonin tietorakenne (dict), jossa kaikki kysytty
#  on samassa nipussa ja viksusti nimettynä.
python_data = {
  "treelength":treelength,
  "treeangle":treeangle,
  "treedepth":treedepth,
  "axiom":axiom,
  "rules":rules
}

# Näytä Python muodossa oleva data
print("dict fmt.", python_data)
# Konvertoi se json muotoon
print("json fmt.", json.dumps(python_data))
