lv = 1
lvg = 50
first = 100
sum = 0

 
while lv < 31:
    if lv == 1:
        lv = lv + 1
        sum = 100
    else:
        lv = lv + 1
        first = first + lvg
        sum = sum + first + lvg
print(sum)
        
