def main():
    #escribe tu código abajo de esta línea
    pesoi=float(input("Dame el peso inicial: "))
    pesof=float(input("Dame el peso final: "))
    meses=int(input("Dame la cantidad de meses: "))
    bajar=(pesoi-pesof)/meses
    print("Lo que debes bajar por mes es:", bajar)
    pass



if __name__ == '__main__':
    main()
