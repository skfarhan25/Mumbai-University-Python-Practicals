YellowDict = {"Jane Doe": "+27 555 5367",
              "John Smith": "+27 555 6254", 
              "Bob Stone": "+27 555 5689"}

YellowDict["Jane Doe"] = "+27 555 1024"
YellowDict.update({"Anna Cooper":"+27 555 3237"})
print("Bob Stone's Number:", YellowDict.get("Bob Stone"))
print(YellowDict.keys())
print(YellowDict.values())