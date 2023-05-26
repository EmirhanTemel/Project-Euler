class LargeSum:

    def __init__(self):

        with open("50digit.txt","r") as file:

            liste = file.readlines()

            self.satırlar = list()

            for i in liste:
                i = i.rstrip("\n")

                self.satırlar.append(int(i))

sum1 = LargeSum()

toplam = sum(sum1.satırlar)

stri = str(toplam)

print(stri[:10])