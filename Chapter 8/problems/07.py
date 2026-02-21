def rem(l,word):
    n=[]
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
 
l = ["Joy","Bhan","Kabir","shrey","an"]

print(rem(l,"an"))