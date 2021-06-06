#!/usr/bin/env python3

from heltal import Heltal
import matplotlib.pyplot as plt
from time import perf_counter as pc

def fib_py(n):
	if n<=1:
		return n
	else:
		return (fib_py(n-1)+fib_py(n-2))

def main():
	pytime = []
	ctime = []
	for i in range(30,35):
		t1 = pc()
		f=Heltal(i)
		f.fib()
		t2 = pc()
		fib_py(i)
		t3 = pc()
		pytime.append(t3-t2)
		ctime.append(t2-t1)
	n = [*range(30,35)]
	fig, ax = plt.subplots()
	ax.plot(n,pytime)
	ax.set(xlabel='n',ylabel='seconds (s)',title='C++ vs Python (fib)')
	ax.grid()
	fig.savefig('test.png')
	plt.show()
	f = Heltal(40)
	print(f'Time with n = 47: {f.fib()}')

if __name__ == '__main__':
	main()
