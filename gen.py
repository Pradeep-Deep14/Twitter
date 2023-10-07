def generator_function():
    for i in range(5):
        yield i
gen=generator_function()
next(gen)
print(list(gen))