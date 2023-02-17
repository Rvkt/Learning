def strs_to_chars(lst):
    result = [i for element in lst for i in element]
    return result

colors = ["red", "white", "a", "b", "black", "f"]
print("Original list:")
print(colors)
print("\nConvert the said list of strings and characters to a single list of characters:")
print(strs_to_chars(colors))
