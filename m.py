a=input("enter string")
i=0
le=len(a)
while i<le:
	if a[i]=="a":
		print(a.find("a",i,le))
	i=i+1
	 
