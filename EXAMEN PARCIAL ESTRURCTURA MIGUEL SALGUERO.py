# MIGUEL SALGUERO - 1626923
class Nodo:
    def __init__(self, coeficiente, grado):
        self.coeficiente = coeficiente
        self.grado = grado
        self.siguiente = None

class Polinomio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cabeza = None

    def agregar_componente(self, coeficiente):
        nuevo_nodo = Nodo(coeficiente, 0)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        self.actualizar_grados()

    def agregar_componente_al_principio(self, coeficiente, grado):
        nuevo_nodo = Nodo(coeficiente, grado)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def actualizar_grados(self):
        grado = 0
        nodo_actual = self.cabeza
        while nodo_actual:
            nodo_actual.grado = grado
            grado += 1
            nodo_actual = nodo_actual.siguiente

    def modificar_componente(self, grado, nuevo_coeficiente):
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.grado == grado:
                nodo_actual.coeficiente = nuevo_coeficiente
                return
            nodo_actual = nodo_actual.siguiente
        print(f"No está el término de grado {grado} en el polinomio {self.nombre}.")

    # aqui habia un problema en que me daba al revez los coeficientes, ya los ingresa el revez pero el resultado sigue asi,
    # da los valores al revez, digamos que donde es x^2 escribe el que no tiene x
    def __str__(self):
        polinomio_str = ""
        nodos = []
        nodo_actual = self.cabeza
        while nodo_actual:
            nodos.append(nodo_actual)
            nodo_actual = nodo_actual.siguiente
        nodos.sort(key=lambda x: (x.grado, x.coeficiente), reverse=True)
        for nodo in nodos:
            if nodo.coeficiente != 0:
                if nodo.grado > 1:
                    polinomio_str += f"{nodo.coeficiente}x^{nodo.grado} + "
                elif nodo.grado == 1:
                    polinomio_str += f"{nodo.coeficiente}x + "
                else:
                    polinomio_str += f"{nodo.coeficiente} + "
        return f"{self.nombre} = {polinomio_str[:-3]}"

    def __add__(self, otro):
        resultado = Polinomio("c")
        nodo_self = self.cabeza
        nodo_otro = otro.cabeza
        while nodo_self or nodo_otro:
            coef_self = nodo_self.coeficiente if nodo_self else 0
            coef_otro = nodo_otro.coeficiente if nodo_otro else 0
            grado_self = nodo_self.grado if nodo_self else -1
            grado_otro = nodo_otro.grado if nodo_otro else -1
            if grado_self == grado_otro:
                coef_suma = coef_self + coef_otro
                resultado.agregar_componente_al_principio(coef_suma, grado_self)
                if nodo_self:
                    nodo_self = nodo_self.siguiente
                if nodo_otro:
                    nodo_otro = nodo_otro.siguiente
            elif grado_self > grado_otro:
                resultado.agregar_componente_al_principio(coef_self, grado_self)
                if nodo_self:
                    nodo_self = nodo_self.siguiente
            else:
                resultado.agregar_componente_al_principio(coef_otro, grado_otro)
                if nodo_otro:
                    nodo_otro = nodo_otro.siguiente
        return resultado

    def __sub__(self, otro):
        resultado = Polinomio("c")
        nodo_self = self.cabeza
        nodo_otro = otro.cabeza
        while nodo_self or nodo_otro:
            coef_self = nodo_self.coeficiente if nodo_self else 0
            coef_otro = nodo_otro.coeficiente if nodo_otro else 0
            grado_self = nodo_self.grado if nodo_self else -1
            grado_otro = nodo_otro.grado if nodo_otro else -1
            if grado_self == grado_otro:
                coef_resta = coef_self - coef_otro
                resultado.agregar_componente_al_principio(coef_resta, grado_self)
                if nodo_self:
                    nodo_self = nodo_self.siguiente
                if nodo_otro:
                    nodo_otro = nodo_otro.siguiente
            elif grado_self > grado_otro:
                resultado.agregar_componente_al_principio(coef_self, grado_self)
                if nodo_self:
                    nodo_self = nodo_self.siguiente
            else:
                resultado.agregar_componente_al_principio(-coef_otro, grado_otro)
                if nodo_otro:
                    nodo_otro = nodo_otro.siguiente
        return resultado

    def evaluar(self, valor):
        resultado = 0
        nodo_actual = self.cabeza
        while nodo_actual:
            resultado += nodo_actual.coeficiente * (valor ** nodo_actual.grado)
            nodo_actual = nodo_actual.siguiente
        return resultado

def main():
    polinomios = []
    print("--- EVALUACION PARCIAL - MIGUEL SALGUERO ---")
    print("     ----- Sistema de Polinomios -----")
    while True:
        print("\n1. Ingresar un nuevo polinomio")
        print("2. Mostrar polinomios ingresados")
        print("3. Modificar componente de un polinomio")
        print("4. Suma de polinomios (se guardan con la letra C)")
        print("5. Resta de polinomios (se guardan con la letra C)")
        print("6. Evaluar un polinomio")
        print("7. Salir")

        opcion = input("\nIngrese el número de opción: ")

        if opcion == "1":
            ingresar_polinomio(polinomios)
        elif opcion == "2":
            mostrar_polinomios(polinomios)
        elif opcion == "3":
            modificar_componente(polinomios)
        elif opcion == "4":
            sumar_polinomios(polinomios)
        elif opcion == "5":
            restar_polinomios(polinomios)
        elif opcion == "6":
            evaluar_polinomio(polinomios)
        elif opcion == "7":
            print("---- FIN DE LA EJECUCIÓN ----")
            break
        else:
            print("--- Opción inválida - Vuelva a intentar ---")

def ingresar_polinomio(polinomios):
    print("\nIngrese los coeficientes del polinomio.")
    nombre = input("Ingrese el nombre del polinomio: ")
    grado = int(input("Ingrese el grado del polinomio: "))
    polinomio = Polinomio(nombre)
    for i in range(grado, -1, -1):
        while True:
            try:
                coeficiente = float(input(f"Ingrese el coeficiente para el término de grado {i}: "))
                polinomio.agregar_componente(coeficiente)
                break
            except ValueError:
                print("--- Ingrese un coeficiente válido (número real) ---")
    polinomios.append(polinomio)
    print(f"\nPolinomio '{nombre}' ingresado correctamente")

def mostrar_polinomios(polinomios):
    if not polinomios:
        print("--- No hay polinomios ingresados ---")
    else:
        print("\n- Polinomios ingresados:")
        for polinomio in polinomios:
            print(polinomio)

def modificar_componente(polinomios):
    if not polinomios:
        print("--- No hay polinomios ingresados ---")
        return
    mostrar_polinomios(polinomios)
    idx = int(input("Ingrese el número del polinomio que quiere modificar: ")) - 1
    if 0 <= idx < len(polinomios):
        pol_modificar = polinomios[idx]
        grado = int(input("Ingrese el grado del término que desea modificar: "))
        nuevo_coeficiente = float(input("Ingrese el nuevo coeficiente para ese término: "))
        pol_modificar.modificar_componente(grado, nuevo_coeficiente)
    else:
        print("--- Ingrese un índice válido ---")

def sumar_polinomios(polinomios):
    if len(polinomios) < 2:
        print("-- Se necesitan dos polinomios para hacer una suma --")
        return
    mostrar_polinomios(polinomios)
    indices = input("Ingrese los números de los polinomios que desea sumar separados por coma: ")
    indices = [int(i.strip()) - 1 for i in indices.split(",")]
    if all(0 <= idx < len(polinomios) for idx in indices):
        pol_resultado = polinomios[indices[0]]
        for idx in indices[1:]:
            pol_resultado += polinomios[idx]
        print("El resultado ha sido guardado (C)")
        print(pol_resultado)
        polinomios.append(pol_resultado)
    else:
        print("--- Ingrese un índice válido ---")

def restar_polinomios(polinomios):
    if len(polinomios) < 2:
        print("-- Se necesitan dos polinomios para hacer una resta --")
        return
    mostrar_polinomios(polinomios)
    indices = input("Ingrese los números de los polinomios que desea restar separados por coma: ")
    indices = [int(i.strip()) - 1 for i in indices.split(",")]
    if all(0 <= idx < len(polinomios) for idx in indices):
        pol_resultado = polinomios[indices[0]]
        for idx in indices[1:]:
            pol_resultado -= polinomios[idx]
        print("El resultado ha sido guardado (C)")
        print(pol_resultado)
        polinomios.append(pol_resultado)
    else:
        print("--- Ingrese un índice válido ---")

def evaluar_polinomio(polinomios):
    if not polinomios:
        print("--- No hay polinomios ingresados ---")
        return
    mostrar_polinomios(polinomios)
    idx = int(input("Ingrese el número del polinomio que desea evaluar: ")) - 1
    if 0 <= idx < len(polinomios):
        pol_evaluar = polinomios[idx]
        valor = float(input("Ingrese el valor que desea asignar a la variable: "))
        resultado_evaluacion = pol_evaluar.evaluar(valor)
        print(f"El resultado de '{pol_evaluar.nombre}' evaluado en {valor} es: {resultado_evaluacion}")
    else:
        print("--- Ingrese un índice válido ---")


main()
