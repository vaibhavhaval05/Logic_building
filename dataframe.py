import pandas as p
data = {
    "a":[230,310,490],
    "b":[111111111,22,112]
}

saee = p.DataFrame(data,index=["x","y","z"])

print(saee)
print(saee.loc[["x","y","z"]])
