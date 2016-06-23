#include <iostream>
#include <vector>
#include <ctime>
#include <chrono>
#include <mpi.h>
using namespace std;
/*Este programa calcula los numeros primos entre 0 y 5000 utilizando el 
 * algoritmo Criba de Eratóstenes, en el cual se marcan como invalidos
 * todos los multiplos de los valores de entrada.
 * Integrantes: 
 * Boanerges Martinez Cortez
 * Brayan Morera Ramirez
 * Version: 2.0
 *  
 * */
//compilar-construir el programa: mpiCC -O -std=c++11 primos3.cpp -o primos3
// correr el programa: mpirun -np 2 primos3, para crear 2 procesos
/*
mpirun -np <p> <exec> <arg1> ... 
•
-np <p> 
⎯
 numero de procesos
•
<exec>
⎯
 ejecutable
•
<arg1> ...
⎯
 command-line arguments 

Ejecucion en 3 CPUs 
mpirun -np 3 sat 
*/

//Declaracion de variable y metodos
vector<bool> primos(5000,true);
void erastones(int,int);
void prim_print();

//main
int main(int argc, char *argv[]){
	primos[0]=false;
	primos[1]=false;
	int i, ierr; 
	int id; /* Rango del proceso */ 
	int p;  /* Numero de procesos */ 
	//  Inicializar MPI.
	ierr= MPI_Init (&argc, &argv);
	//  Obtener el numero de procesos.
	ierr= MPI_Comm_size (MPI_COMM_WORLD, &p);
	//  Determinar el rango del proceso.
	ierr= MPI_Comm_rank (MPI_COMM_WORLD, &id); 
	std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
	//desabilita las posiciones de los numeros multiplos de los que se envian,
	//false multiplos: i*2, i*3, i*4, i*5, i*6 ...
	for(i=2;i*i<5000;i+=1){
		ierr = MPI_Bcast ( &i, 1, MPI_INT, 0, MPI_COMM_WORLD );
		erastones(id,i);
	}
	MPI_Finalize();
	
	prim_print();
	
	std::chrono::steady_clock::time_point end= std::chrono::steady_clock::now();
	std::cout << "Tiempo en micro segundos= " << std::chrono::duration_cast<std::chrono::microseconds>(end - begin).count() <<std::endl;
	std::cout << "Tiempo en nano segundos= " << std::chrono::duration_cast<std::chrono::nanoseconds> (end - begin).count() <<std::endl;
	std::cout << "Tiempo en mili segundos= " << std::chrono::duration_cast<std::chrono::milliseconds> (end - begin).count() <<std::endl;
}
//calcula los primos usando Eratosthenes, al eleminar los multiplos de los
//numero enviados en paralelo
void erastones(int id,int i){
	for(int j=2;i*j<5000;j++){
			primos[i*j]=false;
		}
}
//imprime los indices de las posiciones validas
void prim_print(){
	for(int i=0; i<5000;i++){
		if(primos[i]){
		cout<< i << endl;
		}
	}	
}
