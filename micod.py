from math import *

def modulo(Um,Vm):
	return pow(pow(Um,2) + pow(Vm,2), 0.5)
def polosNpar(fc, fs, n):
	wc = 2*pi*fc
	arg = (wc/fs)*0.5

	for m in range(0, 2*n, 1):
		Um = (1 - pow(tan(arg), 2)) / (1 - 2*tan(arg)*cos((2*m + 1)*pi/(2*n)) + pow(tan(arg), 2))
		Vm = (2 * tan(arg) * sin((2*m + 1)*pi/(2*n))) / (1 - 2*tan(arg)*cos((2*m + 1)*pi/(2*n)) + pow(tan(arg), 2))
		print("Para m=%d ---> Um = %f  Vm= %f ---> modulo= %f" %(m, Um, Vm, modulo(Um, Vm)))

def polosNimpar(fc, fs, n):
	wc = 2*pi*fc
	arg = (wc/fs)*0.5

	for m in range(0, 2*n, 1):
		Um = (1 - pow(tan(arg), 2)) / (1 - 2*tan(arg)*cos(m*pi/n) + pow(tan(arg), 2))
		Vm = (2 * tan(arg) * sin(m*pi/n)) / (1 - 2*tan(arg)*cos(m*pi/n) + pow(tan(arg), 2))
		print("Para m=%d ---> Um = %f  Vm= %f ---> modulo= %f" %(m, Um, Vm, modulo(Um, Vm)))

polosNpar(83.407, 400,6)
