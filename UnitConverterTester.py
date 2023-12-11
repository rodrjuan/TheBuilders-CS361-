import UnitConverter

def main():
    converter = UnitConverter.UnitConverter()

    # test metric length converter
    val = "1"
    for c1 in UnitConverter.PREFIXES:
        for c2 in UnitConverter.PREFIXES:
            curr = val + " m " + c1
            print(converter.convertLength(curr, "1 m " + c2))
    
    # test imperial lengths
    val = "1"
    for c1 in UnitConverter.IM_LENGTHS:
        for c2 in UnitConverter.IM_LENGTHS:
            curr = val + " " + c1
            print(converter.convertLength(curr, "1.0 " + c2))


    # test temperature converter
    # print(converter.__convertTemps("2 F", "C"))
    # print(converter.__convertTemps("5 F", "K"))
    # print(converter.__convertTemps("200 K", "F"))
    return None

if __name__ == "__main__":
    main()