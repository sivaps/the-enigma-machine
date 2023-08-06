from Wiring import Wiring


class Rotor:
    def __init__(self, wiring, notch, ring_setting=0):
        self.wiring = Wiring(wiring)
        self.notch = notch
        self.ring_setting = ring_setting
        self.position = 0

    def step(self):
        self.position = (self.position + 1) % 26

    def encrypt(self, char, reverse=False):
        char_num = ord(char) - ord('A')
        char_num = (char_num + self.position - self.ring_setting) % 26

        if reverse:
            transformed_char_num = (self.wiring.reverse(char_num) - self.position + self.ring_setting) % 26
        else:
            transformed_char_num = (self.wiring.forward(char_num) - self.position + self.ring_setting) % 26

        transformed_char = chr(transformed_char_num + ord('A'))
        return transformed_char
