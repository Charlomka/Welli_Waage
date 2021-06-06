

#Start 2: Eine Klasse erstellen
class Vogel:
    def __init__(self, name, schlupfjahr, gender, gewicht, verliebt, art):
        self.name = name
        self.schlupfjahr = schlupfjahr 
        self.gender = gender
        self.gewicht = gewicht
        self.verliebt = verliebt
        self.art = art 

#Bobby erstellen 
Bobby = Vogel("Bobby", 2018, "m", 52, 1, "Welli")

#Start: 6 kleine und 2 große Vögel
Wellensittiche = [Bobby, "Klausi", "Quackie", "Olga", "Tonya", "Melek"]
Nymphensittiche = ["Jahari", "Zari"]