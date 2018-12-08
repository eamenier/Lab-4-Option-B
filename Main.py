class HTNode(object):
    def __init__(self, item, next):
        self.item = item
        self.next = next

class hash_table(object):
    def __init__(self, table_size):
        self.size = 0
        self.table = [None] * table_size
    # hash function using the first letter in each word to place words
    def hash_func(self, word, letter):
        return (word ** letter) % len(self.table)
    # average number of comparisons 
    def avg_comps(self):
        total_nodes = 0
        compd_nodes = 0
        for i in range(len(self.table)):
            temp = self.table[i]
            # increase compared nodes for each extra node in a index
            if temp is not None:
                compd_nodes += 1
            # increase total nodes and increment temp
            while temp is not None:
                total_nodes += 1 
                temp = temp.next
        # calculate average comparisons
        avg = total_nodes / compd_nodes
        print(avg)
    # calculate load factor
    def load_factor(self):
        lf = self.size / len(self.table)
        print(lf)
    # find the ascii value of words 
    def ascii(self, word):
        ascii_value = 0
        # loop through each character in word
        for char in word:
            # use ord() to get the ascii value of each char and then add chars together
            ascii_value += ord(char)
        return ascii_value
    
    def insert(self, item):
        self.size += 1
        ascii_word = self.ascii(item)
        # set first letter of the word
        letter = self.ascii(item[:1])
        i = self.hash_func(ascii_word, letter)
        self.table[i] = HTNode(item, self.table[i])

class hash_table2(object):
    def __init__(self, table_size):
        self.size = 0
        self.table = [None] * table_size
    # hash function using the first letter in each word to place words
    def hash_func(self, word, length):
        return (word ** length) % len(self.table)
    # average number of comparisons 
    def avg_comps(self):
        total_nodes = 0
        compd_nodes = 0
        for i in range(len(self.table)):
            temp = self.table[i]
            # increase compared nodes for each extra node in a index
            if temp is not None:
                compd_nodes += 1
            # increase total nodes and increment temp
            while temp is not None:
                total_nodes += 1 
                temp = temp.next
        # calculate average comparisons
        avg = total_nodes / compd_nodes
        print(avg)
    # calculate load factor
    def load_factor(self):
        lf = self.size / len(self.table)
        print(lf)
    # find the ascii value of words 
    def ascii(self, word):
        ascii_value = 0
        # loop through each character in word
        for char in word:
            # use ord() to get the ascii value of each char and then add chars together
            ascii_value += ord(char)
        return ascii_value
    
    def insert(self, item):
        self.size += 1
        ascii_word = self.ascii(item)
        # set length of the word
        length = len(item)
        i = self.hash_func(ascii_word, length)
        self.table[i] = HTNode(item, self.table[i])
# set table size to 26
hashtable = hash_table(26)
hashtable2 = hash_table2(10)
#open word file and insert into hash table
with open("words.txt", "r") as file:
    for line in file:
        hashtable.insert(line)
        hashtable2.insert(line)
# print avg comparisons and load factor
print("")
print("Average comparisons:")
hashtable.avg_comps()
hashtable2.avg_comps()
print("Load factor: ")
hashtable.load_factor()
hashtable2.load_factor()