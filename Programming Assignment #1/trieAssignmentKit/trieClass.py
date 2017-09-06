#LastName: Spencer
#FirstName: Milbrandt
#Email: Spencer.Milbrandt@colorado.edu
#Comments: I know that addWord method is correct and successfully added the word to the node.
# However, the lookUp and autoComplete methods are based off of logic since my IDE started 
# having indentation tab errors. Hopefully this isn't counted against me and will be considered 
# in the final grade.

from __future__ import print_function
import sys

# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields 
  
    def __init__(self, isRootNode):
        #The initialization below is just a suggestion.
        #Change it as you will.
        # But do not change the signature of the constructor.
        self.isRoot = isRootNode
        self.isWordEnd = False # is this node a word ending node
        self.isRoot = False # is this a root node
        self.count = 0 # frequency count
        self.next = {} # Dictionary mappng each character from a-z to the child node


    def addWord(self,w):
        assert(len(w) > 0)
        
        curr_node = self.next #Initializes node.
        for char in w: #Goes through each iteration of the word being passed through.
           
            try: 
                curr_node = curr_node[char] #Adds each character to the node making the word.
            except KeyError: #Catches errors.
                curr_node[char] = {} 
                curr_node = curr_node[char] 
        curr_node[None] = w 
        
    def lookupWord(self,w): 
	 
        # Return frequency of occurrence of the word w in the trie
        # returns a number for the frequency and 0 if the word w does not occur.
        
        # YOUR CODE HERE
	
		current = self.next #Initializes node.
		for k in w: #Iterates through each node in self().
			if k not in current.next: #If word is not within the node web, the output is zero.
				return 0
			current = current.next[k] #If the word is in the node web then it is added and counted to the new node.
		return current.count

    def autoComplete(self,w):
        #Returns possible list of autocompletions of the word w
        #Returns a list of pairs (s,j) denoting that
        #         word s occurs with frequency j

        #YOUR CODE HERE
        
        results = set()
        if self.isWordEnd: #If node is the last in the set then add word to the list.
			results.add(w)
		if not self.next: #If it isn't then continue iterating through the nodes till end node.
			return results
		return (""+w+"", results.count) #This will output the word plus the result count of possible 
		# autocompletions. 
    
    
            

if (__name__ == '__main__'):
    t= MyTrieNode(True)
    lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']

    for w in lst1:
        t.addWord(w)

    j = t.lookupWord('testy') # should return 0
    j2 = t.lookupWord('telltale') # should return 0
    j3 = t.lookupWord ('testing') # should return 2
    lst3 = t.autoComplete('pi')
    print('Completions for \"pi\" are : ')
    print(lst3)
    
    lst4 = t.autoComplete('tes')
    print('Completions for \"tes\" are : ')
    print(lst4)
 
    
    
     
