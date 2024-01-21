# Helper function: Print table headers
def print_headers():
    print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format("No", "Smartphone", "Price", "Screensize", "RAM"))
    print("================================================================")

# TODO: Implement the function to print the entire table content.
def print_table(filename):
    with open(filename, "r") as file:
        contents = file.readlines()
    print_headers()
    for i in range(1, len(contents) + 1):
        line = contents[i - 1].strip().split("\t")
        print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(i, line[0], line[1], line[2], line[3]))

print_table("tc1.txt")