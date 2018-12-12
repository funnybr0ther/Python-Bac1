import mission

duree1 = mission.Duree(1,59,45)
duree2 = mission.Duree(0,42,70)
duree3 = mission.Duree(1,1,1)

if duree3.toSecondes() == 3721:
    print("Test 1 Ok")
if duree3.delta(duree1) == 3524:
    print("Test 2 Ok")
if duree1.ajouter(duree3).seconds == 46 and duree1.ajouter(duree3).minutes == 0 and duree1.ajouter(duree3).hours == 3:
    print("Test 4 Ok")
if str(duree1) == "01:59:45":
    print("Test 5 Ok")

file = open("testfile.txt","w")
file.write("Remix_Dubstep_Ave_Maria Roland_Keunings 14 50\n")
file.write("Two_Girls_One_Cup_Music David_Guetta 3 16\n")
file.write("Screaming_Goat Chèvre 4 5\n")
file.write("Tournevis_ASMR JMJ 45 30\n")
file.write("Bruit_Tracteur Michel_Vergautier 10 30\n")
file.close()

