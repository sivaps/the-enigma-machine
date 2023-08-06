class Wiring:
    def __init__(self, connections):
        self.connections = connections

    def forward(self, char_num):
        return self.connections[char_num]

    def reverse(self, char_num):
        return self.connections.index(char_num)