import UnitConverter

def main():
    converter = UnitConverter.UnitConverter()

    # test metric length converter
    # val = "1"
    # for c1 in UnitConverter.PREFIXES:
    #     for c2 in UnitConverter.PREFIXES:
    #         curr = val + " m " + c1
    #         print(converter.convertLength(curr, "0 m " + c2))
    
    # test imperial lengths
    # val = "1"
    # for c1 in UnitConverter.IM_LENGTHS:
    #     for c2 in UnitConverter.IM_LENGTHS:
    #         curr = val + " " + c1
    #         print(converter.convertLength(curr, "0.0 " + c2))
    
    # test metric to imperial
    # val = "2"
    # for c1 in UnitConverter.PREFIXES:
    #     for c2 in UnitConverter.LENGTHS:
    #         print(converter.convertLength(val + " m " + c1, "0.0 " + c2))

    # test random cases
    # print(converter.convertLength("2 m p", "0 in"))
    # print(converter.convertLength("104 ft", "0 m c"))
    # print(converter.convertLength("50 m k", "0 ft"))
    # print(converter.convertArea("104 ft 0 sq", "0 m c sq"))
    


    # test temperature converter
    # print(converter.__convertTemps("2 F", "C"))
    # print(converter.__convertTemps("5 F", "K"))
    # print(converter.__convertTemps("200 K", "F"))
    # print(converter.convertTemps("6 F", "K"))
    # print(converter.convertTemps("100 C", "F"))


    # test mass conversion
    print(converter.convertMass("6 oz", "ton"))
    print(converter.convertMass("1 g", "ton"))
    return None

if __name__ == "__main__":
    main()