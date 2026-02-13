#set
thisset = {"yoyo", "ocen", "bams", "cimol", "ciko"}
print(thisset)


#duplikat
thisset = {"yoyo", "ocen", "bams", "cimol", "ciko", "yoyo"}
print(thisset)


#lenght
thisset = {"yoyo", "ocen", "bams", "cimol", "ciko"}
print(len(thisset))


#type()
thisset = {"yoyo", "ocen", "bams", "cimol", "ciko"}
print(type(thisset))


#konstruktor set
thisset = set(("yoyo", "ocen", "bams", "cimol", "ciko")) 
print(thisset)


#access set
thisset = {"cherry", "kiwi", "mango"}

for x in thisset:
  print(x)


thisset = {"cherry", "kiwi", "mango"}
print("kiwi" in thisset)


thisset = {"cherry", "kiwi", "mango"}
print("kiwi" not in thisset)

#add
thisset = {"cherry", "kiwi", "mango"}
thisset.add("orange")

print(thisset)


#add dari set lain
thisset = {"cherry", "kiwi", "mango"}
tropical = {"pineapple", "orange", "papaya"}

thisset.update(tropical)

print(thisset)


#any iterable
thisset = {"cherry", "kiwi", "mango"}
mylist = ["papaya", "apple"]

thisset.update(mylist)

print(thisset)


#remove()
thisset = {"cherry", "kiwi", "mango"}

thisset.remove("mango")
print(thisset)


#discard
thisset = {"cherry", "kiwi", "mango"}

thisset.discard("cherry")

print(thisset)


#pop
thisset = {"cherry", "kiwi", "mango"}

x = thisset.pop()

print(x)
print(thisset)


#clear
thisset = {"cherry", "kiwi", "mango"}

thisset.clear()
print(thisset)


#del
thisset = {"cherry", "kiwi", "mango"}

del thisset
print(thisset)


#loop
thisset = {"cherry", "kiwi", "mango"}

for x in thisset:
  print(x)


#union
set1 = {"x", "y", "z"}
set2 = {7, 8, 9}

set3 = set1.union(set2)
print(set3)


#intersectin()
set1 = {"cherry", "kiwi", "mango"}
set2 = {"banana", "strawwberry", "cherry"}

set3 = set1.intersection(set2)
print(set3)


#pakai operator &
set1 = {"cherry", "kiwi", "mango"}
set2 = {"banana", "strawwberry", "cherry"}

set3 = set1 & set2
print(set3)


#frozenset
x = frozenset({"cherry", "kiwi", "mango"})
print(x)
print(type(x))

