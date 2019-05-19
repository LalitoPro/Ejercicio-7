class Arreglos:
    __Matriz_Marco = []


    def Arreglos(self):
        for i in range(8):
            self.__Matriz_Marco.append([0] * 6)

        for f in range(0, 8):
            for c in range(0, 6):

                if (f == 0 or f == 7):
                    self.__Matriz_Marco[f][c] = 1

                if (c == 0 or c == 5):
                    self.__Matriz_Marco[f][c] = 1

                print(self.__Matriz_Marco[f][c], "\t", end="")
            print("\n")

ejercicio7 = Arreglos()
ejercicio7.Arreglos()

