from automata.fa.nfa import NFA

#AFN - (aa|b)*(a|bb)*

afn = NFA(
    states={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'},
    input_symbols={'a', 'b'},
    transitions={
        '0': {'': {'1'}},
        '1': {'a': {'2'}, 'b': {'4'}, '': {'5'}},
        '2': {'a': {'3'}},
        '3': {'': {'5'}},
        '4': {'': {'5'}},
        '5': {'a': {'6'}, 'b': {'7'}, '': {'1'}},
        '6': {'': {'9'}},
        '7': {'b': {'8'}},
        '8': {'': {'9'}},
        '9': {'': {'5'}}
    },
    initial_state='0',
    final_states={'1', '5', '9'}
)

string = input("Enter your string: ")
print(afn.accepts_input(string))