from multiprocessing import Pool

numbers = [1, 2, 3, 4, 5]

def square(x):
    return x * x

if __name__ == "__main__":
    with Pool(processes=4) as pool:
        result = pool.map(square, numbers)

    print(result)