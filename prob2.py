list_of_strings = ["monkey", "cheese", "nyx", "apricot", "fish", "kiwi"]

sorted_list_of_strings = sorted(list_of_strings, key=lambda x: (len(x), x))

print(sorted_list_of_strings)
