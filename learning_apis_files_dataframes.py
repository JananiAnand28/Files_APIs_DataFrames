#%%
#### Reading and Writing files

# Read
f = open('sample.txt', mode='r')
contents_read = f.read()
f.close()

print(contents_read)

#%%
# Write
myName = 'Pragith'
someSentence = 'I am a boy'

f = open('new_file_to_write.txt', mode='w')
f.write('My name is: ' + myName + '\n')
f.write(someSentence)
f.close()


#%%
# Append
import random

someRandomNum = random.random()

x = open('new_file_to_write.txt', mode='a')
#x.write('\nI am appending a new sentence')
#x.write('\nA random number is: ' + someRandomNum)
for i in range(1,10):
    someRandomInt = random.randint(5,20)
    x.write('\nThe ' + str(i) + ' random number is: ' + str(someRandomInt))
x.close()


#%%
# Binary
y = open('einstein.jpg', 'rb')
imageContents = y.read()
y.close()

z = open('newEinstein.jpg', 'wb')
z.write(imageContents)
z.close()

#%%
#### APIs






#%%
#### Dataframes




#%%
## Tuples vs Lists
# Tuples - They are immutable lists
a = (1,2,3)
b = [1,2,3]
c = [4,5,6]
d = (4,5,6)
