from automata.fa.dfa import DFA

#AFD - (aa|b)*(a|bb)*

afd = DFA(
    states={'A', 'B', 'C', 'D', 'E', 'F'},
    input_symbols={'a', 'b'},
    transitions={
        'A': {'a': 'B', 'b': 'C'},
        'B': {'a': 'D', 'b': 'E'},
        'C': {'a': 'F', 'b': 'E'},
        'D': {'a': 'D', 'b': 'E'},
        'E': {'a': 'D', 'b': 'E'},
        'F': {'a': 'D', 'b': 'E'},
    },
    initial_state='A',
    final_states={'D'}
)

string = input("Enter your string: ")
print(afd.accepts_input(string))
