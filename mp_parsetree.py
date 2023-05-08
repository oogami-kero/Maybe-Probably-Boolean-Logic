"""
Program to test student understanding 
by using binary trees, stacks, unittest, and random.
Goal: Implement functions to build, evaluate, and print expressions 
using our (made-up) maybe-probably logic.
"""

from binarytree import BinaryTree
from stack import Stack
import unittest
import random


def buildMPLogicParseTree(s):
    """ 
    This function takes a string as input (s = ('T OR P_0.9")) and returns the binary tree representing the binary tree
    """
	# split the string as input 
	slist = s.split()
	sStack = Stack()
	eTree = BinaryTree('')
	pStack.push(eTree)
	currentTree = eTree
	#eTree.printTree()

	for i in slist: 

		if i == '(' :
			#If '( ' create an empty root node and left child node 
			currentTree.insertLeft('')
			sStack.push(currentTree)
			currentTree = currentTree.getLeftChild()
        
        elif i in [ 'AND' , 'OR' ]:
			#Set 'AND' or 'OR' as a root node and create an emty right child node
			currentTree.setRootVal(i)
			currentTree.insertRight('')
			sStack.push(currentTree)
			currentTree = currentTree.getRightChild()
			#eTree.printTree()
			
		elif i == 'M_x':
			ilist = i.split('_')
			x = ilist[1]
			if 0.0 <= x <= 0.75:
				currentTree.setRootVal(int(x))
				parent = sStack.pop()
				currentTree = parent 
			else:
				("token '{}' is out of bounds.")

		elif i == 'P_x': 
			ilist = i.split('_')
			x = ilist[1]
			if 0.75 <= x <= 1.00:
				currentTree.setRootVal(int(x))
				parent= sStack.pop()
				currentTree = parent 
			else:
				("token '{}' is out of bounds.")

		elif i == ['T','F']: 
			currentTree.setRootVal('')
			parent = sStack.pop()
			currentTree = parent

		elif i == ')': 
			currentTree = sStack.pop()

		else: 
			print("token '{}' is not valid integer".format(i))
			return None

		#print(pStack)
		return eTree

def evaluateMPLogicParseTree(t):
    """ 
    This function takes a binary tree as input and should return a T or an F that is based on the input statement
    """
    #Generate random number in the decimals place
    a = random.randint(1, 9)
    b = a / 10 
    print(b)
    leftC = t.getLeftChild() 
    rightC = t.getRightChild()
    #print(leftC, rightC)
    '''
    ilist = [ 'M_x' , 'P_x']
	for i in find:
		ilist.split('_')
		print(ilist)
		x = ilist[1]
        if b < x:
            return True
        else:
            return False
            '''

def printMPLogicExpression(t):
    """ 
    This function should take a binary tree as input and should return the string that looks like the original string (With extra parentheses)
    """
    sVal = ""
    if t:
        sVal = '(' + printMPLogicExpression(t.getLeftChild())
        sVal = sVal + str(t.getRootVal())
        sVal = sVal + printMPLogicExpression(t.getRightChild())+')'
    return sVal


class TestParseTree(unittest.TestCase):
    """ 
    An example on how the functions work (inside of def main()) and tests taht each of the functions work correctly
    ADD METHODS TO TEST PARSE/EVAL/PRINT FUNCTIONS """
    pass
    def testDataAfterBuild(self):
        """ Check if the build was successful focusing if all the elements make it their expected places"""
        buildTest = buildMPLogicParseTree('( T AND M_0.3)')
        expected = [ 'AND' , 'T', 'M_0.3']
        self.assertEqual(buildtest, expected)

    def testDataAfterBuild2(self):
        """ Check if the build was successful focusing if all the elements make it their expected places"""
        buildTest = buildMPLogicParseTree('( T AND P_1.5)')
        expected = ["token P_1.5 is out of bounds."]
        self.assertEqual(buildtest, expected)

    def testDataAfterBuild3(self):
        """ Check if the build was successful focusing if all the elements make it their expected places"""
        buildTest = buildMPLogicParseTree('( W AND P_0.9)')
        expected = ["token '(W AND P_0.9' is not valid integer"]
        self.assertEqual(buildtest, expected)   

def unittest_main():
    """
    Run unittest's main, which runs TestMPLogicParseTreeFunction's methods
    """
    unittest.main()

def main():
    """
    Code you want to run when this is exectuted as a standalone program should be in here
    """
    pt = buildMPLogicParseTree('( ( T AND F ) OR M_0.3 )')
    ans = print("Evaluating parse tree: ", evaluateMPLogicParseTree(pt))
    exp = printMPLogicExpression(pt)
    # pt, ans, and exp will all be checked to ensure they are correct
    

# Only executed if run as a standalone program
if __name__ == '__main__':
    main()
    unittest_main()
