class Model:
    def __init__(self):
        self.value = ""
        self.prev_val = ""
        self.operator = ""

    def calculate(self, caption):
        if caption == "C":
            self.value = ""
            self.prev_val = ""
            self.operator = ""
        elif isinstance(caption, int): # if it is a number
            self.value += str(caption)
        elif caption == "+/-":
            self.value = str(float(self.value)*-1)
        elif caption == "%":
            s = str(float(self.value)/100)
            self.value = s.rstrip("0").rstrip(".") if "." in s else s
        elif caption == "=":
            s = str(self._evaluate())
            self.value = s.rstrip("0").rstrip(".") if "." in s else s
        elif caption == ".":
            if caption not in self.value:
                self.value += caption
        else: # if it is operator +, -, /, *
            if self.value:
                self.operator = caption
                self.prev_val = self.value
                self.value = ""
        return self.value

    def _evaluate(self):
        if self.operator:
            if self.value:
                return eval(self.prev_val + self.operator + self.value)
            else:
                return self.prev_val
        else:
            return self.value
