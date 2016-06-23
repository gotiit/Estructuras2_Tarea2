#Reglas a e j e c u t a r cuando se ejecute make
all: 
	mpiCC -O -std=c++11 primos3.cpp -o primos3
	g++ -std=c++11 -Wall -o primos2 primos2.cpp
#Al d i g i t a r make clean se borrarAn todos los archivos compilados ,
#note e l −f en rm , s i no sabe para que s i r v e use e l manual de rm .
clean:
	rm -f *.o primos2 primos3
