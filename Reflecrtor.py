from Wiring import Wiring


class Reflector:
    def __init__(self, wiring):
        self.wiring = Wiring(wiring)

    def reflect(self, char):
        char_num = ord(char) - ord('A')
        reflected_char_num = self.wiring.forward(char_num)
        reflected_char = chr(reflected_char_num + ord('A'))
        return reflected_char
