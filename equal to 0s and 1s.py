class FiniteStateAutomaton:
    def __init__(self):
        self.states = {'q0', 'q1'}
        self.alphabet = {'0', '1'}
        self.transition = {
            'q0': {'0': 'q1', '1': 'q0'},
            'q1': {'0': 'q0', '1': 'q1'}
        }
        self.initial_state = 'q0'
        self.accepting_states = {'q0'}
    
    def process_input(self, input_string):
        current_state = self.initial_state
        
        for symbol in input_string:
            if symbol not in self.alphabet:
                raise ValueError(f"Symbol '{symbol}' not in the alphabet.")
            
            current_state = self.transition[current_state][symbol]
        
        return current_state in self.accepting_states


if __name__ == "__main__":
    fsa = FiniteStateAutomaton()
    test_strings = ["", "01", "10", "0011", "1100", "000111", "111000", "010101", "101010"]
    
    for test_str in test_strings:
        result = fsa.process_input(test_str)
        print(f"The string '{test_str}' is {'accepted' if result else 'rejected'} by the FSA.")
