# import dependencies


# unit converter constants
LENGTHS = ["in", "ft", "yd"]
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
SUFFIXES = {
    "sq":"sq",
    "cb":"cb"
}

"""
Unit Converter Class
"""
class UnitConverter:
    # Constructor Method
    def __init__(self):
        self.lengths = LENGTHS
        self.prefixes = PREFIXES
        self.suffixes = SUFFIXES

    """
    Function: syntax_parser()
    - expr must be in the correct format. That is, the format should be
    [multiplier] [unit] [prefix(optional)] [suffix(optional)].
    - return a list that has been parsed through so it can be used in
    calculations.
    """
    def syntaxParser(self, expr):
        parse_list = expr.split(" ")
        
        # first element should always be the multiplier, convert to number 
        parse_list[0] = float(parse_list[0])

        # if the expression has a prefix, convert to its table value, i.e. a number.
        if len(parse_list) > 2:
            parse_list[2] = float(PREFIXES[parse_list[2]])
        else:
            parse_list.extend(["",""])
        return parse_list
    
    """
     Function: tempSyntaxParser()
     expr must be in the correct format: [multiplier] [unit]
     return a lost that has been parsed through to be used in calculations.
    """
    def tempSyntaxParser(self,expr):
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
    def toCelcius(self, val, unit):
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
    def toFahrenheit(self, val, unit):
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
    def toKelvin(self, val, unit):
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
        parse = self.tempSyntaxParser(temp)

        if to_unit == "C":
            val = self.toCelcius(parse[0], parse[1])
        elif to_unit == "F":
            val = self.toFahrenheit(parse[0], parse[1])
        else:
            val = self.toKelvin(parse[0], parse[1])

        return str(val) + to_unit
    
    def convertSameSystemLength(self, parse1, parse2):
        return float(parse1[0] * parse1[1]/(parse2[0] * parse2[1]))
    

    def convertUnits(self, expr1, expr2):
        parse1 = self.syntaxParser(expr1)
        parse2 = self.syntaxParser(expr2)

        # case 1: both metric
        if parse1[1] == parse2[1] == "m":
            return str(self.convertSameSystemLength(parse1, parse2)) + parse2[2] + "m"

    
        return None


