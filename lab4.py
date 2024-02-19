#In A Galaxy Far Far Away

#Create class 
class Phone:
    def __init__(self):
        #List of commands
        self.command = {"add": self.addContact, 
                   "lookup": self.findContact, 
                   "alias": self.addAlias, 
                   "change": self.changeNum, 
                   "save": self.save, 
                   "load": self.load, 
                   "delete": self.deleteContact, 
                   "quit": self.quit, 
                   "options": self.option}
        self.phone = {}

        

#Function to run the program and start the user input
    def run(self):
        print("Type 'options' for a list of commands")
        while True:
            #input for phonebook
            teleb = input("PhoneBook>").casefold()
            if teleb in self.command:
                match teleb: 
                    case "add":
                        self.addContact()
                    case "lookup":
                        self.findContact()
                    case "alias":
                        self.addAlias()
                    case "change":
                        self.changeNum()
                    case "save":
                        self.save()
                    case "load":
                        self.load()
                    case "delete":
                        self.deleteContact()
                    case "quit":
                        self.quit()
                    case "options":
                        self.option()
                    case _:
                        print("Kommando existerar inte!")
                
            
#Function to add contact in the phone book
    def addContact(self):
        name = input("Name: ")
        phoneN = input("Phone: ")
        if name in self.phone.keys():
            print(name, "finns redan i telefonboken!")
        elif phoneN in self.phone.values():
            print(phoneN, "finns redan i telefonboken!")
        else:
            self.phone[name] = phoneN
            print("Kontakten har lagts till!")
    #klar

#Function to add alias 
    def addAlias(self):
        name = input("Name: ")
        newName =  input("Alias: ")
        if newName not in self.phone.keys():
            if name in self.phone.keys():
                self.phone[newName] = self.phone[name]
                print("Alias har lagts till för", name, "som", newName)
            else: 
                print("Namnet finns inte")
#klar

#Function to search for contact, both name and alias 
    def findContact(self):
        name = input("Namn: ")
        if name in self.phone.keys():
            print(name + ":", self.phone[name])            
        else:
            print(name, "finns inte i telefonboken!")
#klar
#Function to change number
    def changeNum(self):
        name = input("Namn: ")
        newNum = input("Nytt nummer: ")
        if name in self.phone.keys():
            oldNumb = self.phone[name]
            if newNum not in self.phone.values():
                self.phone[name] = newNum
                print("Nummret för ", name, "är uppdaterad från" , oldNumb, "till", newNum)
            else: 
                print("Ny nummer finns redan i telefonboken!")
        else:
            print(name, " finns inte i telefonboken")
#klar
#Function to delete a contact
    def deleteContact(self, b):
        name = input("Namn: ")
        if name in self.phone.keys():
            del self.phone[name]
            print("Kontakten har tagits bort")
        else:
            print(name, "finns inte!")
#klar
#Function to save the phonebook
    def save(self):
        filename = input("Ange namnet på filen: ")
        try:
            with open(filename, "w") as f:
                for name, phoneN in self.phone.items():
                    f.write(phoneN + ";" + name + "\n")
            print("Telefonboken har sparats!")
        except IOError:
            print("Kunde inte spara telefonboken!")

#Function to load up the saved phonebook
    def load(self):
        filename = input("Ange namnet på filen (.txt): ")
        with open(filename, "r") as f:
            for rad in f:
                name , phoneN = rad.strip().split(";") 
                self.phone[name] = phoneN
        print("Telefonboken har laddats!", filename, ":", self.phone)

    def option(self):
        print("OPTIONS", "\n", "add: Add contact", "\n", 
        "lookup: Look up a contact", 
        "\n", "alias: Adds an alias", "\n", 
        "change: Changes number to contact",
        "\n", "save: Save contactfile", "\n", 
        "load: Load contactfile", "\n", "delete: Deletes contacts",
         "\n", "Quit: Exits Program")

#Function to quit the program
    def quit(self):
        print("Hej Då!")
        raise SystemExit


#create a instance of the class
if __name__ == "__main__":
    phone = Phone()
    phone.run()
