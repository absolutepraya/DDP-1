keyword = "iphone x"
keyword = keyword.lower()

with open("tc1.txt", "r") as file:
    contents = file.readlines()

contents = [content.strip().split("\t") for content in contents]

print(contents)

# for i in range(len(contents)):
#     if keyword in contents[i][0].lower():
#         print(contents[i])