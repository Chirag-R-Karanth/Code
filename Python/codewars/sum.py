def sum_array(a):
    b=0;
    for i in range(len(a)):
        if len(a) == 0:
            return b
        else:
            b += a[i];
    print(b)
    return b

def __main():
    sum_array([20,30,40])
