

vaken = "n" 
print("Du sover djupt som björnen i ide...") 
while vaken == "n": 
    vaken = input("Vaknar du? [y/n] ").lower() 

# duscha
print("Du masar dig upp och släpar dig in i duschen.")
print("Någon har lämnat en brödrost i din dusch")
duscha = input("Flyttar du på brödrosten? [y/n] ").lower()
if duscha == "n":
    exit("Du elchockas och ditt äventyr är slut")
elif duscha == "y":
    print("Friskt vatten sköljer över dig och du börjar äntligen vakna.")
else:
    print("DOES NOT COMPUTE")

# årstid
season = False
while season == False:
    season = input("Vilken årstid är det? [vår, vinter, sommar, höst] ").lower()
    if season == "vår" or season == "vinter" or season == "höst":
        print("Det är kallt och slask, fy tusan!")
        print("Du klär på dig vinterpälsen...")
    elif season == "sommar":
        print("Sommar! Shorts och flip flops")
    else:
        season = False
        