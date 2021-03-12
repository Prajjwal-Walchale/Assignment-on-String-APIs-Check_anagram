Write a python function, check_anagram()
Sample Input                 Expected Output
eat, tea                     True
backward, drawback           False
                             (Reason: character 'a' repeats at position 6, not an anagram)
                             
Reductions, discounter        True 
About, table                  False



def check_anagram(data1,data2):
    d1=data1.lower()
    d2=data2.lower()
    if(len(data1)!=len(data2)or(sorted(d1)!=sorted(d2))):
        
        return False
    else:
        
        
        for i in range(len(d1)):
            if(d1[i]==d2[i]):
                return False
        else:
                
                
            return True
            
            
            

print(check_anagram("listen","silent"))
