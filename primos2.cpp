#include <iostream>
#include <vector>
#include <ctime>
#include <chrono>
using namespace std;
using namespace std::chrono;

//integrantes: Brian Morera Ramirez Carnet: A84375                   
//             Boanerges Martínez Cortez Carnet: A73791
//Calcula los números primos entre 0 a 5000, utilizando la Criba de Eratóstenes.
// VErsion 2.0

//Compile: g++ -std=c++11 -Wall -c "%f"
//Build: g++ -std=c++11 -Wall -o "%e" "%f"
//run: "./%e"

//declaracion de variables y metodos 
vector<bool> primos(5000,true);

void erasto();
void prim_print();

int main(){//se inicializa un reloj
	high_resolution_clock::time_point t1 = high_resolution_clock::now();
	primos[0]=false;
	primos[1]=false;
	erasto();
	prim_print();
	//se mide por seguda vez el tiempo de finalización
	high_resolution_clock::time_point t2 = high_resolution_clock::now();
	auto duration0 = duration_cast<milliseconds>( t2 - t1 ).count();
	auto duration = duration_cast<microseconds>( t2 - t1 ).count();
	auto duration1 = duration_cast<nanoseconds>( t2 - t1 ).count();
	cout <<"Tiempo en mili segundos: "<< duration0 << endl;
	cout <<"Tiempo en micro segundos: "<< duration << endl;
	cout <<"Tiempo en nano segundos: "<< duration1 << endl;
}
//calcula los primos usando erastones
void erasto(){
	int i,j;
	for(i=2; i<5000;i++){
		//tachar multiplos: i*2, i*3, i*4, i*5, i*6 ...
		for(j=2;i*j<5000;j++){
			primos[i*j]=false;
		}
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
