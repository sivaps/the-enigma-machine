from Enigma import Enigma


def main():
    print("Welcome to the Enigma Machine simulator!")

    # Get rotor settings
    rotor_settings = input("Enter initial rotor positions (e.g., A A A): ").strip().split()

    # Get ring settings
    ring_settings = [int(pos) for pos in input("Enter ring settings (e.g., 0 0 0): ").strip().split()]

    # Define reflector wiring
    reflector_wiring = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0,
                        19]  # Example wiring

    # Get plugboard connections
    plugboard_connections = {}
    connections = input("Enter plugboard connections (e.g., AB CD EF): ").strip().split()
    for pair in connections:
        plugboard_connections[pair[0]] = pair[1]
        plugboard_connections[pair[1]] = pair[0]

    enigma = Enigma(rotor_settings, ring_settings, reflector_wiring, plugboard_connections)

    # Encrypt/Decrypt message
    operation = input("Would you like to encrypt or decrypt? (e/d): ").strip().lower()
    text = input("Enter the plaintext (if encrypting) or ciphertext (if decrypting): ")

    # Reset the rotor positions if decrypting
    if operation == 'd':
        enigma.set_rotor_positions(rotor_settings)

    result = enigma.encrypt(text)
    print("Result:", result)


if __name__ == "__main__":
    main()
