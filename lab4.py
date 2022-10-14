#In A Galaxy Far Far Away
#Function to create the dictionary to store information 
def dictionary():
    dic = {}
    return dic

#Creating a Alias for dictionary
dicContact = dictionary()

#Fucntion to create the main meny
def mainMeny():
    while True: 
        print("Meny för telefonboken!")
        print("Val 1: Lägg till kontakt")
        print("Val 2: Visa kontakt")
        print("Val 3: Ändra kontakt")
        print("Val 4: Avsluta programmet")
        choice  = input("Välj alternativ: ")
        if choice == "1":
            addContact()
        elif choice == "2":
            findContact()
        elif choice == "3":
            changeContact()
        elif choice == "4":
            print("Hej Då!")
            break
        else: 
            print("Error!")

#Function that adds new contact to the phonebook
def addContact():
    print()
    name = input("Skriv in namn: ")
    phoneN = input("Skriv telefonnummer: ")
    while name not in dicContact:
        dicContact[name] = name, phoneN
        print()
        break
    else:
        print()
        print(name, " finns redan i telefonlistan!")
        print()
    
def findContact():
    print()
    name = input("Skriv in namnet på personen du söker: ")
    if name in dicContact:
        print(dicContact[name])
    else: 
        print("Kontakten finns inte i telefonboken")
        print()

def changeContact():
    name = input("Vilken kontakt vill du ändra: ")
    newName = input("Ändra namn på kontakten: ")
    dicContact[newName] = dicContact.pop(name)
    print(dicContact[newName])

mainMeny()