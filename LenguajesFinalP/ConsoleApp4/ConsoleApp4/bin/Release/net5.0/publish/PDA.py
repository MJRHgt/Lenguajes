import sys
sys.path.append(r'C:\Python27\Lib')
import os
import time

class FileHandler:

    def __init__(self):
        pass

    def readFile(self, filePath):
        lines=[]
        if(os.path.isfile(filePath)):
            try:
                with open(filePath) as file:
                    lines = [line.rstrip() for line in file]
            except IOError as e:
                print("El archivo no se puede abrir")
                exit(0)
        else:
            print('{} :no existe el archivo en la ruta especificada'.format(filePath))
            exit(0)
        return lines

    def parseFile(self,lines):
        ''' Line 1: Total States
            Line 2: Input Word Symbols
            Line 3: Stack Symbols
            Line 4: Initial State Symbol
            Line 5: Initial Stack Symbol
            Line 6: List of Final States
            Line 7 and onwards: Productions in form of
                    (Current State, Current Input Symbol, Current Top of Stack, Next State, Push/Pop Operation Symbol)
            '''
        
        Estados=lines[0]
        if Estados=='1':
         states='1'
        elif Estados=='2':
            states='1','2'
        elif Estados=='3':
         states='1','2','3'
        elif Estados=='4':
            states='1','2','3','4'
        elif Estados=='5':
            states='1','2','3','4','5'
        elif Estados=='6':
            states='1','2','3','4','5','6'
        elif Estados=='7':
            states='1','2','3','4','5','6','7'
        elif Estados=='8':
            states='1','2','3','4','5','6','7','8'
        elif Estados=='9':
            states='1','2','3','4','5','6','7','8','9'       
        input_symbols = '0','1','a','b'
        stack_symbols = 'Z','0'
        initial_state = lines[1][0]
        initial_stack = 'Z'
        final_states = lines[2].rstrip().split(',')
        productions = lines[3:]
        for i in range(len(productions)):
            productions[i] = productions[i].rstrip().split(',')

        parsedLines = {'states':states,
                        'input_symbols':input_symbols,
                        'stack_symbols':stack_symbols,
                        'initial_state':initial_state,
                        'initial_stack':initial_stack,
                        'final_states':final_states,
                        'productions':productions}
        return parsedLines
class PDA:
    def __init__(self):
        self.stack = []

    def compute(self, inputString, parsedLines):
        #Retrieve all information
        inputString += 'e'
        initStackSymbol = parsedLines['initial_stack']
        self.stack.append(initStackSymbol)
        finalStates = parsedLines['final_states']
        initialState = parsedLines['initial_state']
        stackSymbols = parsedLines['stack_symbols']
        productions = parsedLines['productions']

        currentStackSymbol = initStackSymbol
        currentState = initialState

        print('State\tInput\tStack\tMove')
        print('{}\t {}\t {}\t ({}, {})'.format(currentState, '_', 'Z', currentStackSymbol, self.stack))
        for char in inputString:
            #print('Current TOS', currentStackSymbol)
            for production in productions:
                if ((production[0] == currentState) and (production[1] == char) and (production[2] == currentStackSymbol)):
                    currentState = production[3]
                    if(len(production[4]) == 2):
                        self.stack.append(char)
                    elif(len(production[4]) == 3):
                        self.stack.append(char)
                        self.stack.append(char)
                    elif ((production[4] == 'e') and (len(self.stack) != 1)):
                        self.stack.pop()
                        break
            previousStackSymbol = currentStackSymbol
            currentStackSymbol = self.stack[len(self.stack)-1]
            print('{}\t {}\t {}\t ({}, {})'.format(currentState, char, previousStackSymbol, currentStackSymbol, self.stack))
            #time.sleep(2)

        if(currentState in finalStates):
            print('Cadena aceptada por el PDA.')
        else:
            print('Cadena rechazada por el PDA.')

def main(cadena,entrada):
    fh = FileHandler()
    pda = PDA()
    automataFilePath = cadena
    lines = fh.readFile( automataFilePath)
    #time.sleep(2)
    print('Se ha leido el archivo de forma correcta')
    #time.sleep(2)
    inputString = entrada
    inputString = inputString.rstrip()
    #time.sleep(3)
    parsedLines = fh.parseFile(lines)
    print('Estados: ', parsedLines['states'])
    print('Estado inicial:', parsedLines['initial_state'])
    print('Estados Finales: ', parsedLines['final_states'])
    print('Transiciones:')
    for production in parsedLines['productions']:
        print( production)
    #time.sleep(2)
    pda.compute(inputString, parsedLines)

if __name__ == '__main__':
    main()


