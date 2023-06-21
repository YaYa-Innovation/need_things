f = open("demo.txt", "w")

f.write("Success Fully Created and This Is Your Text")

f.close()



#open and read the file after the appending:

f = open("demo.txt", "r")

print(f.read())
