def find_anagrams(word,anagram ):
    # [assignment] Add your code here
    #user input
     word = input ("Your first word: ")
     anagram = input ("The anagram: ")
     string1= word
     string2 = anagram
     sorted_string1 = sorted(string1)
     sorted_string2 = sorted(string2)

     #check if length words are the same
     if len(string1) == len(string2):
        
       #checking sorted stings are the same
        if sorted_string1 == sorted_string2:
         return True
     else:
             return False
            
print (find_anagrams(' ', ' '))
                   
