#! /usr/bin/python
# coding: utf-8
import sys
import math
import os
import random
#Este programa simula el comportamiento de una cache con WB que hace uso
#del protocolo MESI para mantener la coerencia entre caches.
 # Integrantes: 
 # Boanerges Martinez Cortez
 # Brayan Morera Ramirez
 # Version: 2.0
#L1 8 KB.
#L2 compartido, 64 KB.
#Se debe asumir que las líneas impares son instrucciones del CPU0 y las pares son
#instrucciones del CPU1.
#El programa se probo en un archivo que contenia las ultimas 1 000 192 instrucciones
# del archivo 'aligned.trace', no se considero necesario correr el programa
# con las 49 642 128 instrucciones. Esto tomando en consideracion que en el enunciado
# se solicitaba los estados correspondientes a las ultimas 10 instrucciones del archivo 
#'aligned.trace'
# en la carpeta correspondiente al trabajo encontrara el archivo 'aligned3.trace' 
# que se utilizo
#▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀

# Se extraen los valores y se asignan a las varibles de trabajo
asociat = 1           #puede ser de 1 2 4
tamcacheL1 = 8*1024
tamL2 = 64*1024
tambloque = 16           #pueden ser de 16 32 64 128

#▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀
#Hacemos los calculos de las parametros que utilizaremos
boffset = int(math.log(tambloque, 2))
cantidadbloquesL1 = tamcacheL1/tambloque
cantidadbloquesL2 = tamL2/tambloque
indexL1 = int(math.log(cantidadbloquesL1, 2))
indexL2 = int(math.log(cantidadbloquesL2, 2))
print "la asociatividad es de: ", asociat,"way"
print "El tamano de los caches L1 es de: ", tamcacheL1," bytes"
print "El tamano del cache L2 es de: ", tamL2," bytes"
print "El tamano del bloque es de: ", tambloque,"bytes"
print "El cache L1 tiene ",cantidadbloquesL1,"bloques."
print "El cache L2 tiene ",cantidadbloquesL2,"bloques."
print "El byte offset es de", boffset ,"bytes"
print "El index para L1 esta compuesto de", indexL1 ,"bytes"
print "El index para L2 esta compuesto de", indexL2 ,"bytes"
print "El tag para L1 esta compuesto de", 32-indexL1-boffset,"bytes"
print "El tag para L2 esta compuesto de", 32-indexL2-boffset,"bytes"
#▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀
#Preparamos los parametros que utilizaremos en para la simulacion del cache
#se declara como tranformar a binario
binary = lambda x: "".join(reversed( [i+j for i,j in zip( *[ ["{0:04b}".format(int(c,16)) for c in reversed("0"+x)][n::2] for n in [1,0] ] ) ] ))
L10=[]
L11=[]
L2=[]
#defimos cada chache como  una lista de listas, cada posicion de la lista,
#tendra una sublista de 2 posiciones que representaran el la direccion y 
# el la bandera {1,2,3,4} que correspondera a {M,E,S,I},
#el cache se inicializara en cero en todas las posiciones
for i in range(cantidadbloquesL1) :
	L10.append( [0, 0] )
	L11.append( [0, 0] )
for i in range(cantidadbloquesL2) :
	L2.append( [0, 0] )
#nImprimir=49642110
nImprimir=1000180
n=0
M='M'
E='E'
S='S'
I='I'
print "Numero desde el cual imprimir",nImprimir
#▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀
#Inicio de la selecion de caches
#Cache de mapeo directo

#with open('aligned.trace') as f:
with open('aligned3.trace') as f:
	for line in f:
		n=n+1
		#print n
		#print line
		ddd = line.split(" ")
		ddd = [x for x in ddd if x.strip()]
		#print ddd, "linea dividida"
		direccion=ddd[0]
		accion=ddd[1].strip('\n')
		#print direccion, " direccionn"
		#print accion, " accion"
		dirbin=binary(direccion)
		#print dirbin, "Este la direccion en binario"
		dirdeci=int(dirbin,2)
		#print dirdeci, "Este la direccion en decimal"
		#Posicion en cache: Address%BlocksInCache
		idxL1= int(dirdeci%cantidadbloquesL1)
		idxL2= int(dirdeci%cantidadbloquesL2)
		#print idxL1, "index para el mapeo directo para L1"
		#print idxL2, "index para el mapeo directo para L2"
#▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀		
#Revisamos si la cantidad de instrucciones es par, si es par, 
#la "ejecuta" CPU0, y hay que cargarla en L10
#Las banderas son {1,2,3,4} que corresponden a {M,E,S,I},
#.......................................................................
		#es par, trabajamos con L10:
#.......................................................................
		if (n%2 == 0):
			#revisamos si es lectura o escritura 
#....................................................................... 
		#Estamos trabajando con L10, la accion es L = lectura:
#.......................................................................			
			if accion=='L':
				#Nos movemos directamente a la posicion del indice y 
				#revisamos si es hit(si esta en esa posicion) o miss(si no esta en esa posicion)
				#Si hit:
				if (L10[idxL1][0]==dirdeci)and(L10[idxL1][1]!=I):
					if (n>nImprimir):
						print "Para n= ",n 
						print "El estado en L10: ",L10[idxL1][1]
						print "El estado en L2: ",L2[idxL2][1]
						#print "p1"
				#es miss:
				else:
					#revisa en L11 si esta el dato y su estatus
					#si hay una copia del dato(bandera: M=1 o E=2):
					if ((L11[idxL1][0]==dirdeci) and ((L11[idxL1][1]==M) or (L11[idxL1][1]==E))):
						#estado M=1, se escribe el valor desde el CPU1 a L2 con estado S=3,
						#se carga el valor a L10 con estado S=3 y se coloca en L1 el estado S=3:
						if L11[idxL1][1]==M:
							L11[idxL1][1]=S
							L2[idxL2][0]=dirdeci
							L2[idxL2][1]=S
							L10[idxL1][0]=L2[idxL2][0]
							L10[idxL1][1]=S
							if n>nImprimir: 
								print "Para n= ",n 
								print "El estado en L10: ",L10[idxL1][1]
								print "El estado en L2: ",L2[idxL2][1]
								#print "p2"
						#estado E=2:	
						else:
							L11[idxL1][1]=S
							#L2[idxL2][1]=S
							L10[idxL1][0]=L11[idxL1][0]
							L10[idxL1][1]=S
							if n>nImprimir:
								print "Para n= ",n 
								print "El estado en L10: ",L10[idxL1][1]
								print "El estado en L2: ",L2[idxL2][1]
								#print "p3"
					#si hay mas de una copia del dato(bandera: S=3) 
					elif(((L11[idxL1][0]==dirdeci) and (L11[idxL1][1]==S))or ((L2[idxL2][0]==dirdeci)and(L2[idxL2][1]==S))):
						L10[idxL1][0]=L2[idxL2][0]
						L10[idxL1][1]=S
						if n>nImprimir:
								print "Para n= ",n 
								print "El estado en L10: ",L10[idxL1][1]
								print "El estado en L2: ",L2[idxL2][1]
								#print "p4"
					#no hay copias del dato
					#se carga el valor al cache y se pone la bandera en E=2
					else:
						L2[idxL2][0]=dirdeci
						L2[idxL2][1]=I
						L10[idxL1][0]=L2[idxL2][0]
						L10[idxL1][1]=E
						if n>nImprimir:
							print "Para n= ",n 
							print "El estado en L10: ",L10[idxL1][1]
							print "El estado en L2: ",L2[idxL2][1]
							#print "p5"
											
#.......................................................................
		#Estamos trabajando con L10, la accion es S = escritura
#.......................................................................			
			else:
				#Nos movemos directamente a la posicion del indice y 
				#revisamos si es hit(si esta en esa posicion) o miss(si no esta en esa posicion)
				#Si hit:
				if (L10[idxL1][0]==dirdeci)and(L10[idxL1][1]!=I):
					#estado M=1
					if((L10[idxL1][1]==M)):
						if n>nImprimir:
							print "Para n= ",n 
							print "El estado en L10: ",L10[idxL1][1]
							print "El estado en L2: ",L2[idxL2][1]
							#print "p6"
					#estado E=2
					elif((L10[idxL1][1]==E)):
						L10[idxL1][1]=M
						if n>nImprimir:
							print "Para n= ",n 
							print "El estado en L10: ",L10[idxL1][1]
							print "El estado en L2: ",L2[idxL2][1]
							#print "p7"
					#estado S=3
					else:
						if L11[idxL1][0]==dirdeci:
							L11[idxL1][1]=I
						if L2[idxL2][0]==dirdeci:
							L2[idxL2][1]=I
						L10[idxL1][1]=M
						if n>nImprimir:
							print "Para n= ",n 
							print "El estado en L10: ",L10[idxL1][1]
							print "El estado en L2: ",L2[idxL2][1]
							#print "p8"
								
				#es miss:
				else:
					#se revisa si hay copas validas del dato
					#hay copias del dato
					if (L11[idxL1][0]==dirdeci) and (L11[idxL1][1]!=I):
						#estado M=1
						if ((L11[idxL1][1]==M)):
							L2[idxL2][0]=L11[idxL1][0]
							L2[idxL2][1]=I
							L11[idxL1][1]=I
							L10[idxL1][0]=L2[idxL2][0]
							L10[idxL1][1]=M
							if n>nImprimir:
								print "Para n= ",n 
								print "El estado en L10: ",L10[idxL1][1]
								print "El estado en L2: ",L2[idxL2][1]
								#print "p9"
						#estado E=1 o S=3	
						else:
							L2[idxL2][0]=dirdeci
							L2[idxL2][1]=I
							L11[idxL1][1]=I
							L10[idxL1][0]=L2[idxL2][0]
							L10[idxL1][1]=M	
							if n>nImprimir:
								print "Para n= ",n 
								print "El estado en L10: ",L10[idxL1][1]
								print "El estado en L2: ",L2[idxL2][1]
								#print "p10"
					#no hay copias del dato
					else:
						L2[idxL2][0]=dirdeci
						L2[idxL2][1]=I
						L10[idxL1][0]=L2[idxL2][0]
						L10[idxL1][1]=M	
						if n>nImprimir:
							print "Para n= ",n 
							print "El estado en L10: ",L10[idxL1][1]
							print "El estado en L2: ",L2[idxL2][1]
							#print "p11"
					
#▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀
#Revisamos si la cantidad de instrucciones es par, si es impar, 
#la "ejecuta" CPU1, y hay que cargarla en L11	
#.......................................................................
		#es impar, trabajamos con L11:
#.......................................................................

		else:
#.......................................................................			
#
#.......................................................................			

			#print n, " instruccion impar, trabajamos con L11"	
#....................................................................... 
		#Estamos trabajando con L11, la accion es L = lectura:
#.......................................................................			

			if accion=='L':
				#Nos movemos directamente a la posicion del indice y 
				#revisamos si es hit(si esta en esa posicion) o miss(si no esta en esa posicion)
				#Si hit:
				if (L11[idxL1][0]==dirdeci)and(L11[idxL1][1]!=I):
					if (n>nImprimir):
						print "Para n= ",n 
						print "E1 estado en L11: ",L11[idxL1][1]
						print "El estado en L2: ",L2[idxL2][1]
				#es miss:
				else:
					#revisa en L10 si esta el dato y su estatus
					#si hay una copia del dato(bandera: M=1 o E=2):
					if ((L10[idxL1][0]==dirdeci) and ((L10[idxL1][1]==M) or (L10[idxL1][1]==E))):
						#se escribe el valor desde el CPU0 a L2 con estado S=3,
						#se carga el valor a L11 con estado S=3 y se coloca en L10 el estado S=3:
						#estado M=1:
						if L10[idxL1][1]==M: ###*******
							L10[idxL1][1]=S
							L2[idxL2][0]=L10[idxL1][0]
							L2[idxL2][1]=S
							L11[idxL1][0]=L2[idxL2][0]
							L11[idxL1][1]=S
							if n>nImprimir: 
								print "Para n= ",n 
								print "E1 estado en L11: ",L11[idxL1][1]
								print "El estado en L2: ",L2[idxL2][1]
						#estado E=2:	
						else:
							L10[idxL1][1]=S
							L11[idxL1][0]=L10[idxL1][0]
							L11[idxL1][1]=S
							if n>nImprimir:
								print "Para n= ",n 
								print "E1 estado en L11: ",L11[idxL1][1]
								print "El estado en L2: ",L2[idxL2][1]
					#si hay mas de una copia del dato(bandera: S=3) 
					elif(((L10[idxL1][0]==dirdeci) and (L10[idxL1][1]==S))or ((L2[idxL2][0]==dirdeci)and(L2[idxL2][1]==S))):
						L11[idxL1][0]=L2[idxL2][0]
						L11[idxL1][1]=S
						if n>nImprimir:
								print "Para n= ",n 
								print "E1 estado en L11: ",L11[idxL1][1]
								print "El estado en L2: ",L2[idxL2][1]
					#no hay copias del dato
					#se carga el valor al cache y se pone la bandera en E=2
					else:
						L2[idxL2][0]=dirdeci
						L2[idxL2][1]=I
						L11[idxL1][0]=L2[idxL2][0]
						L11[idxL1][1]=E
						if n>nImprimir:
							print "Para n= ",n 
							print "E1 estado en L11: ",L11[idxL1][1]
							print "El estado en L2: ",L2[idxL2][1]
											
#.......................................................................
		#Estamos trabajando con L11, la accion es S = escritura
#.......................................................................			
			else:
				#Nos movemos directamente a la posicion del indice y 
				#revisamos si es hit(si esta en esa posicion) o miss(si no esta en esa posicion)
				#Si hit:
				if (L11[idxL1][0]==dirdeci)and(L11[idxL1][1]!=I):
					#estado M=1
					if((L11[idxL1][1]==M)):
						if n>nImprimir:
							print "Para n= ",n 
							print "E1 estado en L11: ",L11[idxL1][1]
							print "El estado en L2: ",L2[idxL2][1]
					#estado E=2
					elif((L11[idxL1][1]==E)):
						L11[idxL1][1]=M
						if n>nImprimir:
							print "Para n= ",n 
							print "E1 estado en L11: ",L11[idxL1][1]
							print "El estado en L2: ",L2[idxL2][1]
					#estado S=3
					else:
						if L10[idxL1][0]==dirdeci:
							L10[idxL1][1]=I
						if L2[idxL2][0]==dirdeci:
							L2[idxL2][1]=I
						L11[idxL1][1]=M
						if n>nImprimir:
							print "Para n= ",n 
							print "E1 estado en L11: ",L11[idxL1][1]
							print "El estado en L2: ",L2[idxL2][1]
								
				#es miss:
				else:
					#se revisa si hay copas validas del dato
					#hay copias del dato
					if (L10[idxL1][0]==dirdeci) and (L10[idxL1][1]!=I):
						#estado M=1
						if ((L10[idxL1][1]==M)):
							L2[idxL2][0]=L11[idxL1][0]
							L2[idxL2][1]=I
							L10[idxL1][1]=I
							L11[idxL1][0]=L2[idxL2][0]
							L11[idxL1][1]=M
							if n>nImprimir:
								print "Para n= ",n 
								print "E1 estado en L11: ",L11[idxL1][1]
								print "El estado en L2: ",L2[idxL2][1]
						#estado E=1 o S=3	
						else:
							L2[idxL2][0]=dirdeci
							L2[idxL2][1]=I
							L10[idxL1][1]=I
							L11[idxL1][0]=L2[idxL2][0]
							L11[idxL1][1]=M	
							if n>nImprimir:
								print "Para n= ",n 
								print "E1 estado en L11: ",L11[idxL1][1]
								print "El estado en L2: ",L2[idxL2][1]
					#no hay copias del dato
					else:
						L2[idxL2][0]=dirdeci
						L2[idxL2][1]=I
						L11[idxL1][0]=L2[idxL2][0]
						L11[idxL1][1]=M	
						if n>nImprimir:
							print "Para n= ",n 
							print "E1 estado en L11: ",L11[idxL1][1]
							print "El estado en L2: ",L2[idxL2][1]
		





