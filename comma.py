
def oxford(list):
    newString = []
    for i in range(len(list)):
        if i < len(list) -1:
            newString.append(list[i] + ',')
        else:
            newString.append('and ' + list[i])        
    print(' '.join(newString))
    
    
oxford(['test', '2', '3', '4','5'])
oxford(['apples', 'pizza', 'dogs', 'cats'])