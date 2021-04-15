import numpy as np
import pickle

def get_func(msg):
    text = input(msg)
    def f(x):
        return eval(f"lambda x : {text}")(x)
    return f

def getDDCoeffs(x, y):
    n = np.shape(y)[0]
    pyramid = np.zeros([n, n]) 
    pyramid[::,0] = y 
    for j in range(1,n):
        for i in range(n-j):
            pyramid[i][j] = (pyramid[i+1][j-1] - pyramid[i][j-1]) / (x[i+j] - x[i])
    return pyramid

def make_f(xi, yi):
    n = len(xi)
    def f1(x):
        ans = yi[0]
        for i in range(1,n):
            ans += yi[i] * np.prod([(x - xi[k]) for k in range(i)])
        return ans
    return f1

def approximate(xi, yi):
    ydd, *_ = getDDCoeffs(xi, yi)
    return make_f(xi, ydd)

def main():
    f = get_func('Enter f(x) = ')
    xi = np.array(list(map(float, input("Enter xi:").split())))
    yi = np.array(list(map(f, xi)))
    ydd, *_ = getDDCoeffs(xi, yi)
    x = np.arange(0, np.pi * 2, 0.01)
    f1 = make_f(xi, ydd)
    y = list(map(f1, x))
    with open('data.pickle', 'wb') as f:
        print(x, y)
        pickle.dump((x, y), f)


if __name__ == '__main__':
    main()