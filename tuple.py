#//How to access items in tuple

schools =("Nairobi","Kabsabet","Nakuru","Muranga")
print(schools[2])    #output Nakuru

names =("Chemtai","Faith","Aline","Raziah")
print(names[-2])   #output Aline

fruits =("mango","orange","lemon","apple")
print(fruits[2:4])   #output ('lemon','apple')
#checking if item exist
classes =("Lovelace","Ada","Anita")
if "Ada" in classes:
 print("yes,'Ada' is in the classes tuple")  #output   yes,"Ada' is in the classes tuple

# How to change items in tuples
x=(1,2,3,4,5)
y= list(x)
y[2]= 6
x= tuple(y)

print(x)      #output  1,2,6,4,5

#Adding items in tuple by   converting to list
animals = ("Lion","Monkey","Goat","cow")
x= list(animals)
x.append("cat")
animals = tuple(x)

print(animals)      #output ('Lion','Monkey','Goat','cow','cat')

#Adding items in a tuple by using concertination
s=(100,200,300,400)
s_append = s + (500,600)
print(s_append)        #output (100,200,300,400,500,600)

#Adding items in tuple by using the assignment operator
counties = ("kilifi","Nakuru","Baringo")
new_county = ("Narok")
counties += (new_county,)
print(counties)                #output ('Kilifi','Nakuru','Baringo','Narok')


#Removing items in a tuple by converting to list
words = ("class","school","country","county")
y= list(words)
y.remove("class")
words = tuple(y)

print(words)     #output ('school','country','county')

#Removing items in a tuple Through slicing
nums = (20,30,40,50,60)
removeItem = nums[:2]
print(removeItem)   #output  (20,30)

#How to write For-loop
fruits = ("apple","banana","mango","kiwi")
for a in fruits:
  print(a) #output #apple
                   #banana
                   #mango
                   #kiwi
 #how to access elements in a dictionary where the keys are tuples.
fruits = {("sweet",):["mango","apple","banana"]}
print(fruits[("sweet",)][2])