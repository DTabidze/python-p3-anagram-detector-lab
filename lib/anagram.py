# your code goes here!
class Anagram:
    
    def __init__(self,word):
        self.word = word

    def match(self,my_list):
        result = []
        for i in range (len(my_list)):
            if sorted(self.word) == sorted(my_list[i]):
                result.append (my_list[i])
        return result