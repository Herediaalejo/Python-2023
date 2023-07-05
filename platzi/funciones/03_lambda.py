def increment(x):
    return x + 1

increment_v2 = lambda x : x + 1

full_name = lambda name, last_name: f"Full name is {name.title()} {last_name.title()}"

result = increment(10)
print(result)

result = increment_v2(20)
print(result)

result = full_name("alejo", "hEredia")
print(result)
