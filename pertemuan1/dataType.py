#tipe data bawaan di python
'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''

#mendapatkan tipe data dengan fungsi type()
x = 100
print(type(x))

y = "Hello"
print(type(y))

#mengatur tipe data
x = "Hello guys"	                    #str	
x = 10	                                #int	
x = 21.5                            	#float	
x = 1j	                                #complex	
x = ["ayam", "sapi", "kucing"]	        #list	
x = ("ayam", "sapi", "kucing")	        #tuple	
x = range(5)	                        #range	
x = {"name" : "Olivia", "age" : 20} 	#dict	
x = {"ayam", "sapi", "kucing"}      	#set	
x = frozenset({"ayam", "sapi", "kucing"})	#frozenset	
x = True	                             #bool	
x = b"Hello"                        	#bytes	
x = bytearray(5)                    	#bytearray	
x = memoryview(bytes(5))            	#memoryview	
x = None                            	#NoneType

#menetapkan tipe data spesifik
x = str("Hello guys")	                #str	
x = int(10)	                            #int	
x = float(21.5)	                        #float	
x = complex(1j)	                        #complex	
x = list(("ayam", "sapi", "kucing"))	#list	
x = tuple(("ayam", "sapi", "kucing"))	#tuple	
x = range(5)	                        #range	
x = dict(name="Olivia", age=20)        	#dict	
x = set(("ayam", "sapi", "kucing")) 	#set	
x = frozenset(("ayam", "sapi", "kucing"))	#frozenset
x = bool(5)                              	#bool	
x = bytes(5)                               #bytes	
x = bytearray(5)	                       #bytearray	
x = memoryview(bytes(5))            	#memoryview	





