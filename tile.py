class Tile:
    def __init__(self):
        self.__value = " "
        self.__displayValue = " "
        self.__mode = 1

    def getValue(self):
        return self.__value

    def setValue(self, value):
        self.__value = value

    def setMode(self, mode):
        self.__mode = mode

    def getDisplayValue(self):
        mode1Dic = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K"}
        if self.__mode == 1 and self.__value != " ":  # modo letra
            if self.__value == "*":
                self.__displayValue = "*"
            else:
                self.__displayValue = mode1Dic[self.__value]
            return self.__displayValue
        if self.__mode == 2 and self.__value != " ":    # modo niveles
            if self.__value == "*":
                self.__displayValue = "**"
            else:
                self.__displayValue = self.__value
            return self.__displayValue
        if self.__mode == 3 and self.__value != " ":    # modo 1024
            if self.__value == "*":
                self.__displayValue = "****"
            else:
                self.__displayValue = int(pow(2, int(self.__value)) / 2)
            return self.__displayValue
        if self.__mode == 4 and self.__value != " ":    # modo 2048
            if self.__value == "*":
                self.__displayValue = "****"
            else:
                self.__displayValue =  pow(2, int(self.__value))
            return self.__displayValue
        else:
            return " "


