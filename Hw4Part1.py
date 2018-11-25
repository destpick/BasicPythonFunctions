# Desta Pickering
# 11597781
# Cpts 355: Homework 4 Part 1
# October 26, 2018

import sys
import re
import types

############### Start 0. Helper Function ##############
# Returns the size of the array_stack
# @param array_stack: the list you want to get the size of
def length(array_stack):
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
    if(length(opstack) > 0):
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
def get(index):
    if(length(dictstack) >= index):
        return dictstack[index]
    else:
        raise Exception('Index out of bounds')

# Removing an element from the stack
def dictPop():
    # Check the size of the stack
    if(length(dictstack) == 0):
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
    if(length(dictstack) > 0 ):
        dictstack[length(dictstack)-1][key] = value
    else:
        newDict = {}
        newDict[key] = value
        dictstack.append(newDict)

############### End 2. Dictionary Stack ################	

################# Start 3. Operators ###################

# Addition
def add():
    if(length(opstack) > 1):
        value_one = opPop()
        value_two = opPop()
        if((isinstance(value_one, int) or isinstance(value_one, float)) and (isinstance(value_one, int) or isinstance(value_one, float))):
            opPush(value_one + value_two)
        else:
            print(stderr, 'Error: Invalid types')
    else:
        raise Exception('Error: Invalid size')

# Subtraction
def sub():
    if(length(opstack) > 1):
        value_one = opPop()
        value_two = opPop()
        if((isinstance(value_one, int) or isinstance(value_one, float)) and (isinstance(value_one, int) or isinstance(value_one, float))):
            opPush(value_two - value_one)
        else:
            print(stderr, 'Error: Invalid types')
            # WHAT SHOULD BE DONE IF IT IS AN INVALID VALUE
    else:
        raise Exception('Error: Invalid size')

# Multiplication 
def mul():
    if(length(opstack) > 1):
        value_one = opPop()
        value_two = opPop()
        if((isinstance(value_one, int) or isinstance(value_one, float)) and (isinstance(value_one, int) or isinstance(value_one, float))):
            opPush(value_one * value_two)
        else:
            print(stderr, 'Error: Invalid types')
            # WHAT SHOULD BE DONE IF IT IS AN INVALID VALUE
    else:
        raise Exception('Error: Invalid size')

# Division	
def div():
    if(length(opstack) > 1):
        value_one = opPop()
        value_two = opPop()
        if((isinstance(value_one, int) or isinstance(value_one, float)) and (isinstance(value_one, int) or isinstance(value_one, float))):
            if((value_two == 0) or (value_two == 0.0)):
                raise Exception('Error: Dividing by zero')
            else:
                opPush((value_two / value_one))
        else:
            raise Exception('Error: Invalid types')
            # WHAT SHOULD BE DONE IF IT IS AN INVALID VALUE
    else:
        raise Exception('Error: Invalid size')

# Less than
def lt():
    if(length(opstack) > 1):
        value_one = opPop()
        value_two = opPop()
        if((isinstance(value_one, int) or isinstance(value_one, float)) and (isinstance(value_one, int) or isinstance(value_one, float))):
            if(value_one > value_two):
                opPush(True)
            else:
                opPush(False)
        else:
            raise Exception('Error: Invalid types')
    else:
        raise Exception('Error: Invalid size')

# Greater than
def gt():
    if(length(opstack) > 1):
        value_one = opPop()
        value_two = opPop()
        if((isinstance(value_one, int) or isinstance(value_one, float)) and (isinstance(value_one, int) or isinstance(value_one, float))):
            if(value_one < value_two):
                opPush(True)
            else:
                opPush(False)
        else:
            raise Exception('Error: Invalid types')
    else:
        raise Exception('Error: Invalid size')

# Equal to
def eq():

    if(length(opstack) > 1):

        value_one = opPop()
        value_two = opPop()
        
        if((isinstance(value_one, int) or isinstance(value_one, float)) and (isinstance(value_one, int) or isinstance(value_one, float))):
            if(value_one is value_two):
                opPush(True)
            else:
                opPush(False)
        else:
            raise Exception('Error: Invalid types')

    else:
        raise Exception('Error: Invalid size')


# Post Script And		
def psAnd():

    if(length(opstack) > 1):

        value_one = opPop()
        value_two = opPop()

        if((isinstance(value_one, bool)) and (isinstance(value_two, bool))):
            if((value_one is True) and (value_two is True)):
                opPush(True)
            else:
                opPush(False)
        else:
            # WHAT TO DO IF THE VALUSE'S AREN'T CORRECT VALUES
            raise Exception('Error:invalid input')

    else:
        raise Exception('Error: out of bounds')

#Post Script Or		
def psOr():
    if(length(opstack) > 1):

        value_one = opPop()
        value_two = opPop()

        if((isinstance(value_one, bool)) and (isinstance(value_two, bool))):
            if((value_one is True) or (value_two is True)):
                opPush(True)
            else:
                opPush(False)
        else:
            # WHAT TO DO IF THE VALUSE'S AREN'T CORRECT VALUE
            raise Exception('Error:invalid input')

    else:
        raise Exception('Error: out of bounds')


# Post Script Not
def psNot():
    global opstack
    if(length(opstack) > 0):
        value_one = opPop()
        if(isinstance(value_one, bool)):
            if(value_one is True):
                opPush(False)
            else:
                opPush(True)
        else:
            raise Exception('Error: out of bounds')

    else:
        raise Exception('Error out of bounds')

# Make a duplicate value	
def dup():
    if(length(opstack) > 0):
        value = opPop()
        opPush(value)
        opPush(value)

    else:
        raise Exception('Error: out of bounds')

# Switch the first two values
def exch():
    if(length(opstack) > 1):

        value_one = opPop()
        value_two = opPop()
        opPush(value_one)
        opPush(value_two)
    else:
        raise Exception('Error: out of bounds')

# pop function
# returns the last element in the stack
def pop():
    if(length(opstack) > 0):
        element = opstack[length(opstack) - 1]
        opstack.pop(length(opstack) - 1)
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
        raise Exception('Error: size of the table')

# Removes all elemetns from the stack
def clear():
    while(length(opstack) is not 0):
        opPop()

def stack():

    if(length(opstack) > 0):
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
    if(length(dictstack) is not 0):

        return dictPop()

    else:
        raise Exception('Error: dictionary is empty')

def psDict():
    if(length(dictstack) >= 0):
        opPop()
        opPush({})

    else:
        raise Exception('Error: popping an empty dictionary')

def psDef():
    if(length(opstack)) > 1:

        value_one = opPop()
        value_two = opPop()

        if(isinstance(value_one, str)):
            define(value_one, value_two)
        elif(isinstance(value_two, str)):
            define(value_two, value_one)
        else:
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
	return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[[][a-zA-Z0-9_\s!][a-zA-Z0-
9_\s!]*[]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", str1)
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
			res.append(checkInput(element))
	return False
### End matchingClosingBrace ###

### Start checkInput ###
def checkInput(element):
	if element == 'true' or element == 'True' or element == 'TRUE':
		return True
	elif element == 'false' or element == 'False' or element == 'FALSE':
		return False	
	elif not any(not(isinstance(character, int) or character == '-') for character in element)
### End checkInput ###

### Start parse ###
def parse(inputted_string):
	temp_array = []
	string_itt = iter(inputted_string)
	for element in string_itt:
		if (c == '{'):
			temp_array.append(matchingClosingBrace(string_itt))
		elif (c == '}'):
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
			if(isinstance(temp_array, list) && any(isinstance(elem, str)) for elem in temp_array):
				interpretSPS(temp_array)
			else:
				raise.Exception("psIf temp_array needs a list of str value")
	else:
		raise.Exception("psIf is_bool needs a boolean value and none was provided")
### End ifOp ###

### Start ifElseOp ###
def psIfElse():
	array_one = opPop()
	array_two = opPop()
	is_bool = opPop()
	
	if isinstance(is_bool, bool):
		if is_bool == True:
			if(isinstance(array_two, list) and any(isinstance(elem, str) for elem in array_two):
				interpretSPS(array_two)
			else:
				raise.Exception("psIfElse array_two needs a list of str value")
		else:
			if (isinstance(array_one, list) and any(isinstance(elem, str) for elem in array_one):
				interpretSPS(array_one)
			else:
				raise.Exception("psIfElse array_two needs a list of str value")
	else:
		raise.Exception("psIfElse is_bool needs a bool value and none was provided")
### End ifElseOp

### Start psFor ###
def psFor():


### End psFor ###

### Start forAll ###
def forAll():
	is_code_array = opPop()
	itterate_over_array = opPop()
	if(isinstance(itterate_over_array, list):
		if(isinstance(is_code_array, list) and any(isinstance(elem, str) for elemen in is_code_array):
			for elemement in itterate_over_array:
				opPush(element)
				interpretSPS(is_code_array)
	else:
		raise.Exception("Invalid inputs for forAll function")
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
	elif elem.lower() == 'mul':
		mul()
	elif elem.lower() == 'div':
		div()
	elif elem.lower() == 'add':
		add()
	elif elem.lower() == 'sub':
		sub()
	elif elem.lower() == 'eq':
		eq()
	elif elem.lower() == 'lt':
		lt()
	elif elem.lower() == 'gt':
		gt()
	elif elem.lower() == 'and':
		psAnd()
	elif elem.lower() == 'or':
		psOr()
	elif elem.lower() == 'not':
		psNot()
	elif elem.lower() == 'if':
		psIf()
	elif elem.lower() == 'ifelse':
		psIfElse()
	elif elem.lower() == 'length':
		length()
	elif elem.lower() == 'get':
		get()
	elif elem.lower() == 'dup':
		dup()
	elif elem.lower() == 'exch':
		exch()
	elif elem.lower() == 'pop':
		opPop()
	elif elem.lower() == 'copy':
		copy()
	elif elem.lower() == 'clear':
		clear()
	elif elem.lower() == 'dict':
		psDict()
	elif elem.lower() == 'begin':
		begin()
	elif elem.lower() == 'end':
		end()	
	elif elem.lower() == 'for':
		psFor()
	elif elem.lower() == 'forall':
		forall()
	elif elem.lower() == 'def':
		psDef()
	elif elem.lower() == 'stack':
		psStack()
	else:
		if elem[0] == '/':
			opPush(elem)
		else:
			is_code_array = lookup(elem)
			if(isinstance(is_code_array, list) and any(isinstance(elem, str) for elemen in is_code_array):
				interpretSPS(is_code_array)
			else:
				raise.Exception(" An invalid input was entered cannot do anything with ", elem)
### End parseString ###

### Start interpretSPS ###
def interpretSPS(inputted_string):
	for input in inputted_string:
		parseString(input)
### End interpretSPS ###

### Start interpreter ###
def interpreter(input):
	tokenized_input = tokenize(input)
	element_arrays = parse(tokenized_input)
	for element in element_arrays:
		parseString(element)
### End interpreter ###