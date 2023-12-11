# import dependencies


# unit converter constants
IM_LENGTHS = {
    "in": 1.00,
    "ft": 12.00,
    "yd": 36.00,
    "mi": 63360.00,
    "m": "m"
}
# WEIGHTS = ["g","pd","oz","ton"]
PREFIXES = {
    "T":pow(10,12),
    "G":pow(10,9),
    "M":pow(10,6),
    "k":pow(10,3),
    "h":pow(10,2),
    "da":pow(10,1),
    "d":pow(10,-1),
    "c":pow(10,-2),
    "m":pow(10,-3),
    "mu":pow(10,-6),
    "n":pow(10,-9),
    "p":pow(10,-12)
}

"""
Unit Converter Class
"""
class UnitConverter:
    # Constructor Method
    def __init__(self):
        self.__lengths = IM_LENGTHS
        self.__prefixes = PREFIXES

    """
    Function: syntax_parser()
    - expr must be in the correct format. That is, the format should be
    [multiplier] [unit] [prefix(optional)] [suffix(optional)].
    - return a list that has been parsed through so it can be used in
    calculations.
    """
    def __syntaxParser(self, expr):
        parse_list = expr.split(" ")
        
        # first element should always be the multiplier, convert to number 
        parse_list[0] = float(parse_list[0])

        # if second element is an imperial unit, convert to its table value
        # otherwise, leave as is.
        parse_list[1] = self.__lengths[parse_list[1]]

        # if the expression has a prefix, convert to its table value, i.e. a number.
        if len(parse_list) > 2:
            parse_list[2] = float(self.__prefixes[parse_list[2]])
        else:
            parse_list.extend([1,""])
        return parse_list
    
    """
     Function: tempSyntaxParser()
     expr must be in the correct format: [multiplier] [unit]
     return a lost that has been parsed through to be used in calculations.
    """
    def __tempSyntaxParser(self,expr):
        parse_list = expr.split(" ")

        # first element should always be the multiplier, convert to number
        parse_list[0] = float(parse_list[0])

        # second element should be the unit, leave as is.
        # return the parse_list
        return parse_list

    """
     Function: toCelcius()
     Return the conversion from one unit to celcius
    """
    def __toCelcius(self, val, unit):
        if unit == "F":
            return float((val - 32.0) * (5.0/9.0))
        elif unit == "K":
            return float(val - 273.15)
        else:
            return val
    """
     Function: toFehrinheit()
     Return the conversion from one unit to fahrenheit
    """        
    def __toFahrenheit(self, val, unit):
        if unit == "C":
            return float((val * 9.0/5.0) + 32)
        elif unit == "K":
            return float((val - 273.15) * 9.0/5.0 + 32)
        else:
            return val
    """
     Function: toKelvin()
     Return the conversion from one unit to kelvin
    """        
    def __toKelvin(self, val, unit):
        if unit == "C":
            return float(val + 273.15)
        elif unit == "F":
            return float((val - 32) * 5.0/9.0 + 273.15)
        else:
            return val

    """
     Function: convertTemps()
     Return the tempurature from one tempature unit to another given unit
    """    
    def convertTemps(self, temp, to_unit):
        parse = self.__tempSyntaxParser(temp)

        if to_unit == "C":
            val = self.__toCelcius(parse[0], parse[1])
        elif to_unit == "F":
            val = self.__toFahrenheit(parse[0], parse[1])
        else:
            val = self.__toKelvin(parse[0], parse[1])

        return str(val) + to_unit
    
    def __convertMetric(self, parse1, parse2):
        return float((parse1[0] * parse1[2] /parse2[2]))
    
    def __convertImperial(self, parse1, parse2):
        return float(parse1[0] * parse1[1] / parse2[1])

    def convertLength(self, expr1, expr2):
        parse1 = self.__syntaxParser(expr1)
        parse2 = self.__syntaxParser(expr2)

        # case 1: both metric
        if parse1[1] == parse2[1] == "m":
            x = ""
            for c in self.__prefixes:
                if self.__prefixes[c] == parse2[2]:
                    x = c
            return str(self.__convertMetric(parse1, parse2)) + x + "m"
        elif parse1[1] != "m" and parse2[1] != "m":
            s = str(self.__convertImperial(parse1,parse2))
            for c in self.__lengths:
                if self.__lengths[c] == parse2[1]:
                    s += c

            return s

    
        return None


