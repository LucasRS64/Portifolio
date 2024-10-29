def simetry(conjN, conjM) :
    diff=[conjN.symmetric_difference(conjM)]
    diff.sort()

    return diff

def main():
    conjN = {2,4,11,12}
    conjM = {2,4,5,9}
    print(simetry(conjN, conjM))


if __name__ == "__main__":
    main()