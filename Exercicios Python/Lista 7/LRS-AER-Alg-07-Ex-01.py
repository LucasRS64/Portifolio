def repet(stringX) :
    stringD = set(stringX)
    if len(stringD) == len(stringX) :
        return True
    else :
        return False

def main():
    stringA = "azul"
    stringB = "ferramenta"

    print(repet(stringA))
    print(repet(stringB))

if __name__ == "__main__":
    main()