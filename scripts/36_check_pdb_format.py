pdb_file = "../data/2XWR.pdb"

print("First 10 ATOM lines:")
print("--------------------")

count = 0

with open(pdb_file, "r") as file:
    for line in file:
        if line.startswith("ATOM"):
            print(repr(line))
            count += 1

            if count == 10:
                break

print("\nTotal ATOM lines shown:", count)