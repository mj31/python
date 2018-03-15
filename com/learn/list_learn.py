classmate=["张三","李四","王五"]
classmate.insert(4,"黑柳")
print(len(classmate))
print("classmate[0]="+classmate[0])
classmate.pop(3)
for mate in classmate:
    if mate == "none":
        print("none")
    else:
        print(mate)
