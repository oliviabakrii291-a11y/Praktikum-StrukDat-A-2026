#dictionaries
thisdict = {
  "name": "olivia",
  "gender": "female",
  "age": 20
}
print(thisdict)

#items
thisdict = {
  "name": "olivia",
  "gender": "female",
  "age": 20
}
print(thisdict["gender"])

#duplikat
thisdict = {
  "name": "olivia",
  "gender": "female",
  "age": 20,
  "age": 25
}
print(thisdict)


#length
thisdict = {
  "name": "olivia",
  "gender": "female",
  "age": 20
}
print(len(thisdict))


#type
thisdict = {
  "name": "olivia",
  "gender": "female",
  "age": 20
}
print(type(thisdict))

#get
thisdict = {
  "name": "olivia",
  "gender": "female",
  "age": 20
}
x = thisdict["age"]
print(x)

thisdict = {
  "name": "olivia",
  "gender": "female",
  "age": 20
}
x = thisdict.get("age")
print(x)

#keys
thisdict = {
  "name": "olivia",
  "gender": "female",
  "age": 20
}
x = thisdict.keys()
print(x)


#values
thisdict = {
  "name": "olivia",
  "gender": "female",
  "age": 20
}
x = thisdict.values()
print(x)


#items
thisdict = {
  "name": "olivia",
  "gender": "female",
  "age": 20
}
x = thisdict.items()
print(x)


#keyword
thisdict = {
  "name": "olivia",
  "gender": "female",
  "age": 20
}
if "age" in thisdict:
  print("Yes, 'age' is one of the keys in the thisdict dictionary")


#change values
thisdict = {
  "name": "Yoyo",
  "animal": "Cat",
  "age": 2
}
thisdict["gender"] = "male"
print(thisdict)


#update
thisdict = {
  "name": "Yoyo",
  "animal": "Cat",
  "age": 2
}
thisdict.update({"age": 3})

print(thisdict)


#add items
thisdict = {
  "name": "Yoyo",
  "animal": "Cat",
  "age": 2
}
thisdict["color"] = "yellow"
print(thisdict)

#update add
thisdict = {
  "name": "Yoyo",
  "animal": "Cat",
  "age": 2
}
thisdict.update({"color": "yellow"})
print(thisdict)


#remove pop
thisdict = {
  "name": "Yoyo",
  "animal": "Cat",
  "age": 2
}
thisdict.pop("age")
print(thisdict)


#remove popitem
thisdict = {
  "name": "Yoyo",
  "animal": "Cat",
  "colour": "yellow"
}
thisdict.popitem()
print(thisdict)


#remove del
thisdict = {
  "name": "Yoyo",
  "animal": "Cat",
  "colour": "yellow"
}
del thisdict["name"]
print(thisdict)


#clear
thisdict = {
  "name": "Yoyo",
  "animal": "Cat",
  "colour": "yellow"
}
thisdict.clear()
print(thisdict)


#loop
#cetak nama kunci
thisdict =	{
    "name": "Yoyo",
    "animal": "Cat",
    "colour": "yellow"
}
for x in thisdict:
  print(x)


#salinan copy()
thisdict = {
      "name": "Yoyo",
      "animal": "Cat",
      "colour": "yellow",
      "age" : 2
}
mydict = thisdict.copy()
print(mydict)


#salinan dict()
thisdict = {
      "name": "Yoyo",
      "animal": "Cat",
      "colour": "yellow",
      "age" : 2
}
mydict = dict(thisdict)
print(mydict)


#nested
myFriend = {
    "friend1" : {
    "name" : "Putri",
    "year" : 2000
  },
    "friend2" : {
    "name" : "Ghea",
    "year" : 2002
  },
    "friend3" : {
    "name" : "Syerin",
    "year" : 2015
  }
}

print(myFriend)


friend1 = {
  "name" : "Putri",
  "year" : 2000
}
friend2 = {
  "name" : "Ghea",
  "year" : 2002
}
friend3 = {
  "name" : "Syerin",
  "year" : 2015
}

myFriend = {
  "friend1" : friend1,
  "friend2" : friend2,
  "friend3" : friend3
}
print (myFriend)


#acces nested
myFriend = {
    "friend1" : {
    "name" : "Putri",
    "year" : 2000
  },
    "friend2" : {
    "name" : "Ghea",
    "year" : 2002
  },
    "friend3" : {
    "name" : "Syerin",
    "year" : 2015
  }
}
print(myFriend["friend2"]["name"])
