class Grid:

    def __init__(self):

        with open("grid.txt","r") as file:

            liste = file.readlines()

            self.satırlar = list()
            self.sütunlar = list()
            for i in liste:
                i = i.rstrip("\n")
                i = i.split(" ")

                self.satırlar.append(i)

            for x in range(len(self.satırlar)):
                geçici = list()
                for i in self.satırlar:
                    geçici.append(i[x])
                self.sütunlar.append(geçici)


    def lineproduct(self):

        productlist = list()

        for i in self.satırlar:
            for x in range(len(i)-3):
                product=1
                for j in i[x:x+4]:
                    product *= int(j)
                productlist.append(product)
        return max(productlist)

    def columnproduct(self):

        productlist = list()

        for i in self.sütunlar:
            for x in range(len(i) - 3):
                product = 1
                for j in i[x:x + 4]:
                    product *= int(j)
                productlist.append(product)
        return max(productlist)

    def diagonalproduct1(self):
        liste = [i for i in self.satırlar]

        a = len(liste)-3

        productlist = list()

        for i in range(a):
            for j in range(a):
                product=1
                for k in range(4):
                    product *= int(liste[k][k+j])
                productlist.append(product)
            liste.pop(0)
        return max(productlist)

    def diagonalproduct2(self):
        liste = [i for i in self.satırlar]

        list1 = liste[::-1]
        a = len(list1) - 3

        productlist = list()

        for i in range(a):
            for j in range(a):
                product = 1
                for k in range(4):
                    product *= int(list1[k][k + j])
                productlist.append(product)
            list1.pop(0)
        return max(productlist)


grid1 = Grid()


print(grid1.lineproduct())

print(grid1.columnproduct())

print(grid1.diagonalproduct1())

print(grid1.diagonalproduct2())
