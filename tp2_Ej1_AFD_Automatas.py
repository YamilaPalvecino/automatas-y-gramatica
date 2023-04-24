from automata.fa.dfa import DFA

#AFD - (a|b)*

afd = DFA(
    states={'A', 'B', 'C'},
    input_symbols={'a', 'b'},
    transitions={
        'A': {'a': 'B', 'b': 'C'},
        'B': {'a': 'B', 'b': 'C'},
        'C': {'a': 'B', 'b': 'C'},
    },
    initial_state='A',
    final_states={'A', 'B', 'C'}
)

string = input("Enter your string: ")
print(afd.accepts_input(string))
