name = "Daksh" # starting 0 index se hi hogi lekin isme negitive indexing bhi hoti he to -1 se start hota he last end se like h letter pe -1 ayega and d letter pe -5.

name1 = name[0:3] # 0 index se include hoke (length -1) tak include hoga jese yaha  par 3 he to 2nd index tak ayega i.e 0 ,1 ,2 index

print(name1)

ch1 = name[2]# 2nd index gets printed

print(ch1)

print(name[-4:-1]) # -4 yani a se lekar -2 yani s tak

print(name[:4]) # same as print(name[0:4]) 

print(name[1:]) # same as print(name[1:5])

print(name[1:5])

a = "0123456789"

print(a[1:8:2])# 1st index se chalu hoga and then (8-1=7)th index tak jayega and usme 1 jump karke (yani 2nd next index) next index print hoga