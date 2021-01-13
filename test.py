
with open("passy", "r") as file:
    output = file.read().split("\n")
    output = output[:-1]
    print(output)
