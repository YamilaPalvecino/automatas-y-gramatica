from automata.fa.nfa import NFA

#AFN - (a|b)*

afn = NFA(
    states={'0', '1', '2', '3'},
    input_symbols={'a', 'b'},
    transitions={
        '0': {'a': {'1'}, 'b': {'2'}, '': {'3'}},
        '1': {'': {'3'}},
        '2': {'': {'3'}},
        '3': {'': {'0'}},
    },
    initial_state='0',
    final_states={'0', '3'}
)

string = input("Enter your string: ")
print(afn.accepts_input(string))
