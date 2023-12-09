import UnitConverter

def main():
    converter = UnitConverter.UnitConverter()

    # test metric length converter
    print(converter.convertUnits("2 m p", "1 m"))
    print(converter.convertUnits("40 m", "1 m k"))
    print(converter.convertUnits("4 m k", "1 m mu"))

    # test temperature converter
    # print(converter.convertTemps("2 F", "C"))
    # print(converter.convertTemps("5 F", "K"))
    # print(converter.convertTemps("200 K", "F"))
    return None

if __name__ == "__main__":
    main()