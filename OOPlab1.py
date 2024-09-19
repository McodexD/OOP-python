# class Matratt:
#     def __init__(self, namn, pris, typ, kalorier):
#         self.namn = namn
#         self.pris = pris
#         self.typ = typ
#         self.kalorier = kalorier

#     def __str__(self):
#         return f"{self.namn} ({self.typ}) - {self.kalorier} kcal - {self.pris} kr"


# matratt1 = Matratt("Spaghetti Bolognese", 85, "Kött", 700)
# matratt2 = Matratt("Falafelwrap", 75, "Vegetarisk", 500)
# matratt3 = Matratt("Veganburgare", 90, "Vegansk", 600)

# lunchmeny = [matratt1, matratt2, matratt3]

# print("Dagens lunchmeny:")
# for matratt in lunchmeny:
#     print(matratt)



# class   person:
#     def __init__(self, data:dict):
#         self.__dict__ = data

#     def __str__(self):
#         str_rep= ""
#         for key, val in self.__dict__.items():
#             str_rep += f"{key} = {val}"
#             return str_rep

# data_dict1 = {

#     "Födelsedatum": "2005-10-02",
#     "Name": "John",
#     "GatuAdress": "solnagatan", # type: ignore
#     "postnummer": 12345,
#     "postort": "Stockholm",
# }

# # data_dict2 = {
# #     "c" : 15,
# #     "d" : 20,
# #     "name" : "John",
# # }

# s1 = person(data_dict1)
# # s2 = Something(data_dict2)

# print (s1)
# print (s2)
class Person:
    def __init__(self, födelsedatum):
        self._födelsedatum = födelsedatum
        self._namn = None
        self._gatu_adress = None
        self._postnummer = None
        self._postort = None

    
    @property
    def födelsedatum(self):
        return self._födelsedatum

    @property
    def namn(self):
        return self._namn

    @property
    def gatu_adress(self):
        return self._gatu_adress

    @property
    def postnummer(self):
        return self._postnummer

    @property
    def postort(self):
        return self._postort


    def namnge(self, namn):
        self._namn = namn

    def byt_adress(self, gatu_adress, postnummer, postort):
        self._gatu_adress = gatu_adress
        self._postnummer = postnummer
        self._postort = postort

    def __str__(self):
        return f"Namn: {self.namn}, Födelsedatum: {self.födelsedatum}, Adress: {self.gatu_adress}, {self.postnummer} {self.postort}"


def main():
    
    person1 = Person("1995-01-01")
    person2 = Person("1996-06-15")

    
    person1.namnge("jude")
    person2.namnge("Kalle")

    
    person1.byt_adress("Solna 1", "12345", "Stockholm")
    person2.byt_adress("Lindholmen 2", "54321", "Göteborg")


    print("Innan flytten:")
    print(person1)
    print(person2)

    person2.byt_adress(person1.gatu_adress, person1.postnummer, person1.postort)

    
    print("\nEfter flytten:")
    print(person1)
    print(person2)

if __name__ == "__main__":
    main()