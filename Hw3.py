# Desta Pickering
# Course 355: Homework 3
# Intro to Python3 in Linux

from functools import reduce

# Problem 1 Dictionaries
# Part a: addDict() 
def addDict (inputted_dic):
    updated_dic = {}
    for course in inputted_dic:
        for day, hour in inputted_dic[course].items():
            updated_dic[day]= updated_dic.get(day, 0) + hour
    return updated_dic

# Part b: addDictN()
def helperDict(inputted_dic, base_case):
    for key, value in base_case.items():
        inputted_dic[key] = inputted_dic.get(key, 0) + value
    return inputted_dic
        
def addDictN (inputted_dic):
    updated_dic = {}
    updated_dic = list(map(addDict, inputted_dic))
    updated_dic = reduce(helperDict, updated_dic)
    return updated_dic

# Problem Two: List and Dictionary
# Part a: lookupVal()
def lookupVal(inputted_dic, desired):
    reversed_dic = reversed(inputted_dic)
    for  cur_dict in reversed_dic:
        for key in cur_dict:
            if key == desired:
                return cur_dict[key]
    return None

# Part b: lookupVal2()
# Recursive helper
def helperLookupVal(tuple_list, key, elem):
    cur_dic = tuple_list[elem][1]
    
    if elem == 0:
        for item in cur_dic:
            if item == key:
                return cur_dic[item]
        return None

    else:
        for item in cur_dic:
            if item == key:
                return cur_dic[item]
        return helperLookupVal(tuple_list, key, tuple_list[elem][0])

# lookupVal2()
def lookupVal2(list_tuple, key):
    elem = list_tuple[-1][0]
    return helperLookupVal(list_tuple, key, elem)

# Problem three -> Recursion numPaths()
def numPaths(m, n, blocks):
    if (m, n) in blocks:
        return 0

    if m is 1 and n is 1:
        return 1

    total = 0
    if m is not 1:
        total += numPaths( m-1, n, blocks)
    if n is not 1:
        total += numPaths(m, n-1, blocks)
    return total


# Problem One -> part a: testing addDict()
def testaddDict():

    test1 = {
                '355' : { 'Mon' : 3, 'Wed' : 2, 'Sat' : 2}, 
                '360' : { 'Mon' : 3, 'Tue' : 2, 'Wed' : 2, 'Fri' : 10}, 
                '321' : { 'Tue' : 2, 'Wed' : 2, 'Thu' : 3}, 
                '322' : { 'Tue' : 1, 'Thu' : 5, 'Sat' : 2}
            }
    
    test2 = {
                '355':{'Mon': 2 }
            }

    test3 = {
                '121': {'Wed': 8},
                '432' : {'Tues' : 1}, 
                '360': {'Mon' : 9}
             }
    
    test4 = {}

    expected1 = {'Mon': 6, 'Wed': 6, 'Sat': 4, 'Tue': 5, 'Fri': 10, 'Thu': 8}
    expected2 = {'Mon' : 2}
    expected3 = {'Wed': 8, 'Tues': 1, 'Mon': 9}
    expected4 = {}

    statement1 = False
    statement2 = False
    statement3 = False
    statement4 = False
    
    result1 = addDict(test1)
    result2 = addDict(test2)
    result3 = addDict(test3)
    result4 = addDict(test4)
    
    if(result1 == expected1):
        statement1 = True
    
    if(result2 == expected2):
        statement2 = True

    if(result3 == expected3):
        statement3 = True
    
    if(result4 == expected4):
        statement4 = True

    print(">>>Testing addDict()")
    print("Test1: " + str(statement1))
    print("Test2: " + str(statement2))
    print("Test3: " + str(statement3))
    print("Test4: " + str(statement4))


# Problem 1 --> part b: Test Cases
def testaddDictN():

    test1 = [
                {'355' : {'Mon' : 3, 'Wed' : 2, 'Sat' : 2}, '360' : { 'Mon' : 3, 'Tue' : 2, 'Wed' : 2, 'Fri' : 10}, 
                    '321' : { 'Tue' : 2, 'Wed' : 2, 'Thu' : 3}, '322' : { 'Tue' : 1, 'Thu' : 5, 'Sat' : 2}},
                { '322' : { 'Mon' : 2}, '360' : { 'Thu' : 2, 'Fri' : 5}, '321' : { 'Mon' : 1, 'Sat' : 3}},
                { '355' : { 'Sun' : 8}, '360' : { 'Fri' : 5}, '321' : { 'Mon' : 4}, '322' : { 'Sat' : 3}}
            ]

    test2 = [
                { '355' : { 'Mon' : 3, 'Mon' : 4}}
            ]

    test3 = [
                {}
            ]

    test4 = [
                {'355' : {'Mon' : 1000}, '360' : {'Tue' : 1}},
                {'355' : {'Tue' : 10}, '360' : {'Mon' : 100}}
            ]

    expected1 = {'Mon' : 13, 'Wed' : 6, 'Sat' : 10, 'Tue' : 5, 'Fri' : 20, 'Thu' : 10, 'Sun' : 8}
    expected2 = {'Mon' : 4}
    expected3 = {}
    expected4 = {'Mon' : 1100, 'Tue' : 11}

    statement1 = False
    statement2 = False
    statement3 = False
    statement4 = False

    results1 = addDictN(test1)
    results2 = addDictN(test2)
    results3 = addDictN(test3)
    results4 = addDictN(test4)

    if(results1 == expected1):
        statement1 = True

    if(results2 == expected2):
        statement2 = True

    if(results3 == expected3):
        statement3 = True

    if(results4 == expected4):
        statement4 = True

    print(">>>Testing addDictNew()")
    print("Test1: " + str(statement1))
    print("Test2: " + str(statement2))
    print("Test3: " + str(statement3))
    print("Test4: " + str(statement4))

#Problem two --> part a: testing lookupVal()
def testlookupVal():
    test1 = [
                {"x":1,"y":True,"z":"found"},{"x":2},{"y":False}
            ]
    
    test2 = [
                {'355' : {'Mon' : 3, 'Wed' : 2, 'Sat' : 2}, '360' : { 'Mon' : 3, 'Tue' : 2, 'Wed' : 2, 'Fri' : 10}, 
                    '321' : { 'Tue' : 2, 'Wed' : 2, 'Thu' : 3}, '322' : { 'Tue' : 1, 'Thu' : 5, 'Sat' : 2}},
                { '322' : { 'Mon' : 2}, '360' : { 'Thu' : 2, 'Fri' : 5}, '321' : { 'Mon' : 1, 'Sat' : 3}},
                { '355' : { 'Sun' : 8}, '360' : { 'Fri' : 5}, '321' : { 'Mon' : 4, 'Tue' : 7}, '322' : { 'Sat' : 3}}
            ]
    statement11 = False
    statement12 = False
    statement13 = False
    statement14 = False
    statement21 = False
    statement22 = False
    statement23 = False
    statement24 = False
    statement25 = False

    expected11 = 2
    expected12 = False
    expected13 = 'found'
    expected14 = None

    expected21 = { 'Sun' : 8} 
    expected22 = { 'Fri' : 5}
    expected23 =  { 'Sat' : 3}  
    expected24 = None
    expected25 = {'Mon' : 4, 'Tue' : 7}

    results11 = lookupVal(test1, 'x')
    results12 = lookupVal(test1, 'y')
    results13 = lookupVal(test1, 'z')
    results14 = lookupVal(test1, 'hello')

    results21 = lookupVal(test2, '355')
    results22 = lookupVal(test2, '360')
    results23 = lookupVal(test2, '322')
    results24 = lookupVal(test2, '121')
    results25 = lookupVal(test2, '321')
   
    if(results11 == expected11):
        statement11 = True

    if(results12 == expected12):
        statement12 = True
    
    if(results13 == expected13):
        statement13 = True
    
    if(results14 == expected14):
        statement14 = True

    if(results21 == expected21):
        statement21 = True
    
    if(results22 == expected22):
        statement22 = True
    
    if(results23 == expected23):
        statement23 = True
    
    if(results24 == expected24):
        statement24 = True

    if(results25 == expected25):
        statement25 = True

    print(">>Testing lookupVal()")
    print("Test 1: " + str(statement11))
    print("Test 2: " + str(statement12))
    print("Test 3: " + str(statement13))
    print("Test 4: " + str(statement14))
    print("Test 5: " + str(statement21))
    print("Test 6: " + str(statement22))
    print("Test 7: " + str(statement23))
    print("Test 8: " + str(statement24))
    print("Test 9: " + str(statement25))

# Problem two --> part b: testing lookupVal2
def testlookupVal2():
    test1 = [
                (0,{"x":0,"y":True,"z":"zero"}),
                (0,{"x":1}),
                (1,{"y":False}),
                (1,{"x":3, "z":"three"}),
                (2,{})
             ]
    
    test2 = [
                (0,{ '355' : 'a', '360' : 'b'}),
                (0,{ '322' : 'A', '321' : 'b'}),
                (1,{ '355' : 'c', '302' : 'd', '321' : 'A'}),
                (2, {}),
                (3, {'x': 6})
            ]

    expected11 = 1
    expected12 = False
    expected13 = 'zero'
    expected14 = None
    expected21 = 'c'
    expected22 = 'b'
    expected23 = 'A'
    expected24 = 'A'
    expected25 = None

    statement11 = False
    statement12 = False
    statement13 = False
    statement14 = False
    statement21 = False
    statement22 = False
    statement23 = False
    statement24 = False

    results11 = lookupVal2(test1, 'x')
    results12 = lookupVal2(test1, 'y')
    results13 = lookupVal2(test1, 'z')
    results14 = lookupVal2(test1, 'hello' )

    results21 = lookupVal2(test2, '355')
    results22 = lookupVal2(test2, '360')
    results23 = lookupVal2(test2, '321')
    results24 = lookupVal2(test2, '322')
    results25 = lookupVal2(test2, '121')

    if(results11 == expected11):
        statement11 = True
    
    if(results12 == expected12):
        statement12 = True
    
    if(results13 == expected13):
        statement13 = True

    if(results14 == expected14):
        statement14 = True
    
    if(results21 == expected21):
        statement21 = True

    if(results22 == expected22):
        statement22 = True

    if(results23 == expected23):
        statement23 = True

    if(results24 == expected24):
        statement24 = True

    if(results25 == expected25):
        statement25 = True

    print(">>>Testing lookupVal2")
    print("Test1: " + str(statement11))
    print("Test2: " + str(statement12))
    print("Test3: " + str(statement13))
    print("Test4: " + str(statement14))
    print("Test5: " + str(statement21))
    print("Test6: " + str(statement22))
    print("Test7: " + str(statement23))
    print("Test8: " + str(statement24))
    print("Test9: " + str(statement25))


# Problem Three: testting pathNum()
def testNumPaths():
    statement1 = False
    statement2 = False
    statement3 = False
    statement4 = False
    statement5 = False

    expected1 = 10
    expected2 = 3
    expected3 = 4
    expected4 = 27
    expected5 = 1

    test1 = numPaths(3,5,[(2,1)])
    test2 = numPaths(3,3, [(2,3)])
    test3 = numPaths(4,3,[(2,2)])
    test4 = numPaths(10,3,[(2,2),(7,1)])
    test5 = numPaths(2,2, [(2,1)])

    if test1 == expected1:
        statement1 = True

    if test2 == expected2:
        statement2 = True

    if test3 == expected3:
        statement3 = True
    
    if test4 == expected4:
        statement4 = True

    if test5 == expected5:
        statement5 = True

    print(">>>Testing numPaths()")
    print("Test1: " + str(statement1))
    print("Test2: " + str(statement2))
    print("Test3: " + str(statement3))
    print("Test4: " + str(statement4))
    print("Test5: " + str(statement5))

def main():
    
    testaddDict()
    print(" ")
    
    testaddDictN()
    print(" ")

    testlookupVal()
    print(" ")

    testlookupVal2()
    print(" ")

    testNumPaths()
    print(" ")
if __name__ == '__main__':
    main()
