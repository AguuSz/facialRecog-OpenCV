d = {}
for i in range(3):
    d["group" + str(i)] = self.getGroup(selected, header+i)
print(d)