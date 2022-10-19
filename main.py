#indendation(space error)
#colon:
#function

#contents of python

# *primitives-numbers,string,booleans
# *collection-lists,dictionary,sets
# *control staement-if & elif,loops,etc
# *range,in,output,input,tuples

#numbers

#integers 1 2 3 4 5
#float 1.2
#complex 5+2j
print(3/2)

# variables

whatch_price=500+20 # spcial characters la _ mattum tha use pann mudium
custmer_name= "harish"  # entha name kuduthalum double codes (or) single ulla tha kuduanum
print(whatch_price+50)
whatch1, whatch2= 750, 756 #you can stoed more values the variable

#strings means(" kulla vara ellame string including special charactrs) important one

word = 'hi dude'
word2 = "my age is 20 why i can't vote  "
para = """hi
bro how 
are 
you
"""
print(para)

word3 = "     hellow, world"
print(word3[0]) #arrays conccept

#slicing one sertine word mattum cut pannalam
print(word3[1:3]) # start to end
print(word3[-5:-1]) #end to start

#lenght

print(len(word3)) # word oda lenght tha kandupidichi sollu

#strip ( unwanted space ex: frontla irukura edathula space illama kondu varla)
print(word3.strip())

print(word3.upper()) # small letters irukka ellam capital lettrs ku change agidum
#lower na change

#replace
a="raj"
print(a.replace('j', 'ju')) # oru letter a eduthutu innoru lettera mathum

print(a.split('a')) # split panni kamikkum