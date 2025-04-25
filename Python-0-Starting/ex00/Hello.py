# Hello.py
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Modifying data structures
ft_list[1] = "World!"
ft_tuple = (ft_tuple[0], "Germany!")
ft_set.remove("tutu!")
ft_set.add("Heilbron!")
ft_dict["Hello"] = "42Heilbronn!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
