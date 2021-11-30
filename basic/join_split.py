# join
#print(" ".join(["Hi", "My", "Name", "is", "John"]))
text = "**".join(["Hi", "My", "Name", "is", "John"])
print(text)
#"Hi My name is John"

# split
print("Hi My name is John".split(" "))
print("Hi My name is John".split())
print("Hi/My/name/is/John".split("/"))

filename  = "sample.py"
print(filename.split(".")[0])
print(filename.split(".")[-1])