# Desta Pickering
# 11597781
# Cpts 355: Homework 4 Part 1
# October 26, 2018

import sys
import re
import types
import string
############### Start 0. Helper Function ##############
# Returns the size of the array_stack
# @param array_stack: the list you want to getHelper the size of
def lengthHelper(array_stack):
    counter = 0;
    for index in array_stack:
        counter = counter + 1
    return counter
############## End 1. Helper Function #################

############### Start 1. Operand Stack ################
# The operand stack, which acts as a list
opstack = []

# Removing a operand from the stack 
def opPop():
    # Check the size of the stack
    if(lengthHelper(opstack) > 0):
        return opstack.pop()
    else:
        return {}

# Adding a new operand to the stack
# @param element: the operand to be added
def opPush(element):
    opstack.append(element)
    if((element in opstack) == False):
        raise Exception('Unable to push element')

############### End 1. Operand Stack #################


############### Start 2. Dictionary Stack ################
# The dictionary stack, which is implemented as a list
dictstack = []

# Iterates through the stack looking for index
# @param index: the index looking for
def getHelper(index):
    if(lengthHelperHelper(dictstack) >= index):
        return dictstack[index]
    else:
        raise Exception('Index out of bounds')

# Removing an element from the stack
def dictPop():
    # Check the size of the stack
    if(lengthHelper(dictstack) == 0):
        raise Exception('Stack of dictionary is empty.')
    else:
        return dictstack.pop()

# Adding an element from the stack
# @param pair_value: is pair_value of the new dictionary entry
def dictPush(pair_value = None):
    if(pair_value == None):
        dictstack.append({})
    else:
        dictstack.append(pair_value)
        if((pair_value in dictstack) == False):
            raise Exception('Unable to push pair_value')

# Creating a new dictionary entry
# @param key: the key of the dictionary entry
# @param value: the value of the dictionary key entry
def define(key, value):
    if(lengthHelper(dictstack) > 0 ):
        dictstack[lengthHelper(dictstack)-1][key] = value
    else:
        newDict = {}
        newDict[key] = value
        dictstack.append(newDict)

############### End 2. Dictionary Stack ################	

################# Start 3. Operators ###################

# Addition
def add():
    if(lengthHelper(opstack) > 1):
        value_one = opPop()
        value_two = opPop()
        if((isinstance(value_one, int) or isinstance(value_one, float)) and (isinstance(value_one, int) or isinstance(value_one, float))):
            opPush(value_one + value_two)
        else:
            opPush(value_one)
            opPush(value_two)
            raise Exception('Error: Invalid type')
    else:
        raise Exception('Error: Invalid size')

# Subtraction
def sub():
    if(lengthHelper(opstack) > 1):
        value_one = opPop()
        value_two = opPop()
        if((isinstance(value_one, int) or isinstance(value_one, float)) and (isinstance(value_one, int) or isinstance(value_one, float))):
            opPush(value_two - value_one)
        else:
            opPush(value_two)
            opPush(value_one)
            raise Exception('Error: Invalid types')
    else:
        raise Exception('Error: Invalid size')

# Multiplication 
def mul():
    if(lengthHelper(opstack) > 1):
        value_one = opPop()
        value_two = opPop()
        if((isinstance(value_one, int) or isinstance(value_one, float)) and (isinstance(value_one, int) or isinstance(value_one, float))):
            opPush(value_one * value_two)
        else:
            opPush(value_two)
            opPush(value_one)
            raise Exception('Error: Invalid types')
    else:
        raise Exception('Error: Invalid size')

# Division	
def div():
    if(lengthHelper(opstack) > 1):
        value_one = opPop()
        value_two = opPop()
        if((isinstance(value_one, int) or isinstance(value_one, float)) and (isinstance(value_one, int) or isinstance(value_one, float))):
            if((value_two == 0) or (value_two == 0.0)):
                raise Exception('Error: Dividing by zero')
            else:
                opPush((value_two / value_one))
        else:
            opPush(value_two)
            opPush(value_one)
            raise Exception('Error: Invalid types')
    else:
        raise Exception('Error: Invalid size')

# Less than
def lt():
    if(lengthHelper(opstack) > 1):
        value_one = opPop()
        value_two = opPop()
        if((isinstance(value_one, int) or isinstance(value_one, float)) and (isinstance(value_one, int) or isinstance(value_one, float))):
            if(value_one > value_two):
                opPush(True)
            else:
                opPush(False)
        else:
            opPush(value_two)
            opPush(value_one)
            raise Exception('Error: Invalid types')
    else:
        raise Exception('Error: Invalid size')

# Greater than
def gt():
    if(lengthHelper(opstack) > 1):
        value_one = opPop()
        value_two = opPop()
        if((isinstance(value_one, int) or isinstance(value_one, float)) and (isinstance(value_one, int) or isinstance(value_one, float))):
            if(value_one < value_two):
                opPush(True)
            else:
                opPush(False)
        else:
            opPush(value_two)
            opPush(value_one)
            raise Exception('Error: Invalid types')
    else:
        raise Exception('Error: Invalid size')

# Equal to
def eq():

    if(lengthHelper(opstack) > 1):

        value_one = opPop()
        value_two = opPop()

        if((isinstance(value_one, int) or isinstance(value_one, float)) and (isinstance(value_one, int) or isinstance(value_one, float))):
            if(value_one is value_two):
                opPush(True)
            else:
                opPush(False)
        else:
            opPush(value_two)
            opPush(value_one)
            raise Exception('Error: Invalid types')

    else:
        raise Exception('Error: Invalid size')


# Post Script And		
def psAnd():

    if(lengthHelper(opstack) > 1):

        value_one = opPop()
        value_two = opPop()

        if((isinstance(value_one, bool)) and (isinstance(value_two, bool))):
            if((value_one is True) and (value_two is True)):
                opPush(True)
            else:
                opPush(False)
        else:
            opPush(value_two)
            opPush(value_one)
            raise Exception('Error:invalid input')

    else:
        raise Exception('Error: out of bounds')

#Post Script Or		
def psOr():
    if(lengthHelper(opstack) > 1):

        value_one = opPop()
        value_two = opPop()

        if((isinstance(value_one, bool)) and (isinstance(value_two, bool))):
            if((value_one is True) or (value_two is True)):
                opPush(True)
            else:
                opPush(False)
        else:
            opPush(value_two)
            opPush(value_one)
            raise Exception('Error:invalid input')

    else:
        raise Exception('Error: out of bounds')


# Post Script Not
def psNot():
    global opstack
    if(lengthHelper(opstack) > 0):
        value_one = opPop()
        if(isinstance(value_one, bool)):
            if(value_one is True):
                opPush(False)
            else:
                opPush(True)
        else:
            opPush(value_one)
            raise Exception('Error: out of bounds')

    else:
        raise Exception('Error out of bounds')

# Gets the length of the array
def length():
    is_array = opPop()
    if isinstance(is_array, list):
        opPush(len(is_array))
    else:
        opPush(is_array)
        raise Exception('The inputted value is not of type array')

# Returns the index at a specified position
def get():
    index_value = opPop()
    is_array = opPop()
    if isinstance(index_value, int) and isinstance(is_array, list):
        opPush(is_array[index_value])
    else:
        opPush(is_array)
        opPush(index_value)
        raise Exception('Invalid values in the inputted array')

# Make a duplicate value	
def dup():
    if(lengthHelper(opstack) > 0):
        value = opPop()
        opPush(value)
        opPush(value)

    else:
        raise Exception('Error: out of bounds')

# Switch the first two values
def exch():
    if(lengthHelper(opstack) > 1):

        value_one = opPop()
        value_two = opPop()
        opPush(value_one)
        opPush(value_two)
    else:
        raise Exception('Error: out of bounds')

# pop function
# returns the last element in the stack
def pop():
    if(lengthHelper(opstack) > 0):
        element = opstack[lengthHelper(opstack) - 1]
        opstack.pop(lengthHelper(opstack) - 1)
        return element

# Copies n number of elements and pushes it onto stack
# @param number_of_elements: the number of elements to copy
def copy():
    temp_op_list = []
    copy_value = opPop()
    if(copy_value <= copy_value):
        for index in range(copy_value):
            element = opPop()
            temp_op_list.append(element)
            temp_op_list.reverse()

        for original in temp_op_list:
            opPush(original)

        for copied in temp_op_list:
            opPush(copied)

    else:
        opPush(copy_value)
        raise Exception('Error: size of the table')

# Removes all elemetns from the stack
def clear():
    while(lengthHelper(opstack) is not 0):
        opPop()

def stack():

    if(lengthHelper(opstack) > 0):
        for element in reversed(opstack):
            print(element)

    else:
        raise Exception('Error: Stack is empty')



# Defining the top of the stack
def begin():
    pair_value = opPop()
    dictstack.append(pair_value)

# Defines the end of the stack
def end():
    if(lengthHelper(dictstack) is not 0):
        return dictPop()
    else:
        raise Exception('Error: dictionary is empty')

def psDict():
    if(lengthHelper(dictstack) >= 0):
        opPop()
        opPush({})

    else:
        raise Exception('Error: popping an empty dictionary')

def psDef():
    if(lengthHelper(opstack)) > 1:

        value_one = opPop()
        value_two = opPop()

        if(isinstance(value_one, str)):
            define(value_one, value_two)
        elif(isinstance(value_two, str)):
            define(value_two, value_one)
        else:
            opPush(value_two)
            opPush(value_one)
            raise Exception('Error: Can not make a dictionary entry')
    else:
        raise Exception('Error: out of bounds error')
############## End 3. Operators ###################

############## Start 4. Name Lookup ###############

# Look up the element and returns the value associated
def lookup(key):
    for d in reversed(dictstack):
        if(d.get('/'+key)):
            return d.get('/'+ key)
############# End 4. Name Lookup ###################


############# HOMEWORK PART TWO ####################

### Start Tokenize ###
def tokenize(str1):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[[][a-zA-Z0-9_\s!][a-zA-Z0-9_\s!]*[]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", str1)
### End Tokenize ###

### Start matchingClosingBrace ###
def matchingClosingBrace(elements):
    temp_array = []
    for element in elements:
        if element == '{':
            temp_array.append(matchingClosingBrace(elements))
        elif element == '}':
            return temp_array
        else:
            temp_array.append(checkInput(element))
    return False
### End matchingClosingBrace ###

### Start checkInput ###
def checkInput(element):
    if element == 'true' or element == 'True' or element == 'TRUE':
        return True
    elif element == 'false' or element == 'False' or element == 'FALSE':
        return False
    try:
        return int(element)
    except:
        if element[0] == '[':
            return createValidArray(element)
        else:
            return element
### End checkInput ###

### createValidArray ###
def createValidArray(anElement):
    working_array = anElement[1:-1]
    working_array = working_array.split()
    working_array = [int(x) for x in working_array]
    return working_array

### Start parse ###
def parse(inputted_string):
    temp_array = []
    string_itt = iter(inputted_string)
    for element in string_itt:
        if (element == '{'):
            temp_array.append(matchingClosingBrace(string_itt))
        elif (element == '}'):
            return False
        else:
            temp_array.append(checkInput(element))
    return temp_array
### End parse ###

### Start ifOp ###
def psIf():
    temp_array = opPop()
    is_bool = opPop()
    if isinstance(is_bool, bool):
        if is_bool == True:
            if(isinstance(temp_array, list) and any(isinstance(elem, str)) for elem in temp_array):
                spInterpret(temp_array)
            else:
                raise Exception("psIf temp_array needs a list of str value")
    else:
        raise Exception("psIf is_bool needs a boolean value and none was provided")
### End ifOp ###

### Start ifElseOp ###
def psIfElse():
    array_one = opPop()
    array_two = opPop()
    is_bool = opPop()

    if isinstance(is_bool, bool):
        if is_bool == True:
            if isinstance(array_two, list):
                spInterpret(array_two)
            else:
                raise Exception("psIfElse array_two needs a list of str value")
        else:
            if isinstance(array_one, list):
                spInterpret(array_one)
            else:
                raise Exception("psIfElse array_one needs a list of str value")
    else:
        raise Exception("psIfElse is_bool needs a bool value and none was provided")
### End ifElseOp

### Start psFor ###
def psFor():
    is_code_array = opPop()
    size_of_itt = opPop()
    incrementation = opPop()
    initialization = opPop()

    if(isinstance(is_code_array, list) and isinstance(size_of_itt, int) and isinstance(incrementation, int) and isinstance(initialization, int)):

        for x in range(initialization, (size_of_itt + incrementation), incrementation):
            opPush(x)
            spInterpret(is_code_array)
### End psFor ###

### Start forAll ###
def forall():
    is_code_array = opPop()
    itterate_over_array = opPop()
    if isinstance(itterate_over_array, list):
        if isinstance(is_code_array, list) and any(isinstance(element, str) for element in is_code_array):
            for element in itterate_over_array:
                opPush(element)
                spInterpret(is_code_array)
    else:
        raise Exception("Invalid inputs for forAll function")
### End forAll ###

### Start parseString ###
def parseString(elem):
    if isinstance(elem, list):
        opPush(elem)
    elif isinstance(elem, bool):
        opPush(elem)
    elif isinstance(elem, int):
        opPush(elem)
    elif isinstance(elem, float):
        opPush(elem)
    elif elem == 'mul':
        mul()
    elif elem == 'div':
        div()
    elif elem == 'add':
        add()
    elif elem == 'sub':
        sub()
    elif elem == 'eq':
        eq()
    elif elem == 'lt':
        lt()
    elif elem == 'gt':
        gt()
    elif elem == 'and':
        psAnd()
    elif elem == 'or':
        psOr()
    elif elem == 'not':
        psNot()
    elif elem == 'if':
        psIf()
    elif elem == 'ifelse':
        psIfElse()
    elif elem == 'length':
        length()
    elif elem == 'get':
        get()
    elif elem == 'dup':
        dup()
    elif elem == 'exch':
        exch()
    elif elem == 'pop':
        opPop()
    elif elem == 'copy':
        copy()
    elif elem == 'clear':
        clear()
    elif elem == 'dict':
        psDict()
    elif elem == 'begin':
        begin()
    elif elem == 'end':
        end()
    elif elem == 'for':
        psFor()
    elif elem == 'forall':
        forall()
    elif elem == 'def':
        psDef()
    elif elem == 'stack':
        stack()
    else:
        if elem[0] == '/':
            opPush(elem)
        else:
            is_code_array = lookup(elem)
            if isinstance(is_code_array, list) and any(isinstance(elem, str) for elem in is_code_array):
                spInterpret(is_code_array)
            else:
                opPush(is_code_array)
### End parseString ###

### Start spInterpret ###
def spInterpret(inputted_string):
    for input in inputted_string:
        parseString(input)
### End spInterpret ###

### Start interpreter ###
def interpreter(input):
    tokenized_input = tokenize(input)
    element_arrays = parse(tokenized_input)
    for element in element_arrays:
        parseString(element)
### End interpreter ###

######################################### TESTING ###################################
def testTokenize():
    test = """/helper { add } def [1 2 3 4] forall add stack"""
    output = tokenize(test)
    if output == ['/helper', '{', 'add', '}', 'def', '[1 2 3 4]', 'forall', 'add', 'stack']:
        return True
    return False

def testTokenize2():
    test = """[1 2 3 4 5 6 7] { add mul sub div } False [1 2 3 4 5 6] [6 5 4 3 2 1] ifelse"""
    output = tokenize(test)
    if output == ['/helper', '{', 'add', '}', 'def', '[1 2 3 4]', 'forall', 'add', 'stack']:
        return True
    return False

def testInterpreter():
    clear()
    test = """
 /square {dup mul} def
 [1 2 3 4] {square} forall
 add add add 30 eq true
 stack
"""
    interpreter(test)
    if(opPop() == True):
        return True
    return False

def testInterpreter1():
    clear()
    input4 = """
     [1 2 3 4 5] dup length exch {dup mul} forall
     add add add add
     exch 0 exch -1 1 {dup mul add} for
     eq stack
    """
    interpreter(input4)
    if(opPop() == True):
        return True
    return False

def main():
    print(">>>Testing the tokenize function")
    print("Test One: ", testTokenize())
    print("Test Two: ", testTokenize2())
    print(">>> Testing the interpreter")
    print("Test One: ", testInterpreter())
    print("Test Two: ", testInterpreter1())
if __name__ == '__main__':
    main()