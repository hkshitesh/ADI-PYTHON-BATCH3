def generate_square():
    sq = []
    for i in range(1,6):
        sq.append(i*i)
    return sq

sq_lst = generate_square()
#print(sq_lst)

def generate_square_generator(n):
    yield n*n


for i in range(1,10):
    print(next(generate_square_generator(i)))

