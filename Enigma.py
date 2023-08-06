# Define the Enigma class
from Reflecrtor import Reflector
from Rotor import Rotor


class Enigma:
    def __init__(self, rotor_settings, ring_settings, reflector_wiring, plugboard_connections):

        rotor1_wiring = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
        rotor2_wiring = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
        rotor3_wiring = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]

        rotor1 = Rotor(wiring=rotor1_wiring, notch=16, ring_setting=ring_settings[0]) # Define rotor wirings
        rotor2 = Rotor(wiring=rotor2_wiring, notch=4, ring_setting=ring_settings[1])
        rotor3 = Rotor(wiring=rotor3_wiring, notch=21, ring_setting=ring_settings[2])
        self.rotors = [rotor1, rotor2, rotor3]
        self.reflector = Reflector(wiring=reflector_wiring)
        self.plugboard = plugboard_connections
        self.set_rotor_positions(rotor_settings)

    def set_rotor_positions(self, positions):
        for rotor, position in zip(self.rotors, positions):
            rotor.position = ord(position) - ord('A')

    def encrypt(self, plaintext):
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                char = char.upper()

                # Step rotors
                self.rotors[0].step()
                if self.rotors[0].position == self.rotors[0].notch:
                    self.rotors[1].step()
                    if self.rotors[1].position == self.rotors[1].notch:
                        self.rotors[2].step()

                # Apply plugboard
                char = self.plugboard.get(char, char)

                # Forward through rotors
                for rotor in self.rotors:
                    char = rotor.encrypt(char)

                # Reflect
                char = self.reflector.reflect(char)

                # Backward through rotors
                for rotor in reversed(self.rotors):
                    char = rotor.encrypt(char, reverse=True)

                # Apply plugboard
                char = self.plugboard.get(char, char)

                ciphertext += char
            else:
                ciphertext += char
        return ciphertext

# Define other classes (Rotor, Reflector) and interactive main function as before
