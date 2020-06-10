class Opening():
    battles = {'Arantara', 'Christophsis', 'Corvair Sector', 'Geonosis', 'Murkhana', 'Teth'}

    count = 1
    for battle in battles:
        print("%s. %s" % (count, battle))
        count += 1
  
    openingSelection = input("Pick a battle to start:\n")
     
Opening()
