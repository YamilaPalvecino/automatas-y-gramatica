class DFA:
    def __init__(self):
        self.states = {'q0', 'q1'}
        self.alphabet = {'a', 'b'}
        self.transitions = {
            'q0': {'a': 'q0', 'b': 'q0'},
            'q1': {'a': 'q1', 'b': 'q1'}
        }
        self.start_state = 'q0'
        self.accept_states = {'q1'}

    def run(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            current_state = self.transitions[current_state][symbol]
        return current_state in self.accept_states


# Ejemplo de uso:
dfa = DFA()
print(dfa.run('abbabbab'))  # True
print(dfa.run('aab'))  # False