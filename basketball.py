s1=5
s2= 3



diff = abs( s2-s1)
diff = diff-3 
hasball  = input('Y / N')

if hasball == 'Y' :
        diff += 1/2
else:
    diff -=1/2

diff = diff **2
        
t = float(input (' no of sec left'))

if diff > t:
    print ( ' The lead team is safe')
else:
    ('lead team is not safe')
             
