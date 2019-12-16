import numpy as np
#crear Matriz donde todos sean unos
unos=np.ones((2,2))
print(unos)

#crear Matriz donde todos sean ceros
ceros=np.zeros((2,2))
print(ceros)

#crear Matriz donde todos sean random
randoms=np.random.random((2,2))
print(randoms)

#crear Matriz una matriz vacia
vacios=np.empty((2,2))
print(vacios)

#crear Matriz una matriz con un solo valor
full=np.full((2,2),10)
print(full)
#crear un matriz dentro de un ragon se incrementa en 5 donde 0 inicia y 30 fin y aumenta de 5 en 5
espacio=np.arange(0,30,5)
print(espacio)

#crear un matriz con 5 valores que se encuentren entre 0 y 2
espacio1=np.linspace(0,10,5)
print(espacio1)

#crear matriz identidad toda la diagonal son iguales
identidat1=np.eye(2,2)
print(identidat1)

identidat1=np.identity(2)
print(identidat1)

#conocer la dimension de una matriz
a=np.array([(1,2,3),(4,5,6)])
print(a.ndim)
#conocer el tipo de datos
a=np.array([(1,2,5,3)])
print(a.dtype)
#tamaño y forma de la matriz
a=np.array([(1,2,5,3,6,9,10,8)])
print(a.size)
print(a.shape)

a=np.array([1,2,3,4,5])
print(a.max())
print(a.min())
print(a.sum())