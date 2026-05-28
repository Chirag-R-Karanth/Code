import numpy as np
#impulse response
h = [1,2,3,3,2,1]
#input response
x = [1,2,3,4,5]
y = np.convolve(x,h,mode='full')
print('Linear convolution using NumPy built-in function output response y=\n',y)
