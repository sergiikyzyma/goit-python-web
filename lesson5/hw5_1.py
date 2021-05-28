import time

def factorize(*number):
    res = [[], [], [], []]
    for i in range(len(number)):
        res[i].append(1)
        for n in range(2, number[i] + 1):
            for m in range(2, n):
                if number[i] % m == 0 and m not in res[i]:
                    res[i].append(m)
        res[i].append(number[i])
    return res

def main():
    #----------Закоментовані числа завеликі для моєго процесора та осі----------
    
    time_start = time.process_time()
    a = [1, 2, 4, 8, 16, 32, 64, 128]
    b = [1, 3, 5, 15, 17, 51, 85, 255]
    #c = [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    #d = [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    c = [1, 3, 9, 27, 37, 111, 333, 999]
    d = [1, 3, 9, 11, 33, 99, 101, 303, 909, 1111, 3333, 9999]
    #print(factorize(128, 255, 99999, 10651060))
    x = factorize(128, 255, 999, 9999)
    assert x == [a, b, c, d]
    print(factorize(128, 255, 999, 9999))
    time_end = time.process_time()
    print("CPU time - ", time_end - time_start)

if __name__ == "__main__":
    main()
