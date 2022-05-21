# encuentra-copia
Reto 4 Python - Desarrollo de un programa que detecta la cantidad de laminas repetidas retornando su cantidad.

## Reto:
### Entrada
La entrada estará formada por dos líneas:
La primera línea aparecerán dos números N y K que indican el número de láminas de fútbol 
de colección a verificar y el tamaño de la memoria de la máquina (1≤N≤10000,1≤K≤1000).
La segunda línea contiene N números (entre 1 y 100) separados por espacios que 
representan los números de las láminas de fútbol de colección introducidas en la máquina.
Dos láminas se consideran iguales si están representadas por el mismo número.

### Salida
El programa imprimirá dos números separados por un espacio.
El primero representará el número real de láminas repetidas.
El segundo representará la cantidad de láminas repetidas detectadas por la 
máquina en función de su memoria considerando que esta solo es capaz de guardar 
en memoria las K láminas anteriores.

### Casos de prueba:
Entrada:<br>
5 1<br>
1 2 3 1 2<br>
5 2<br>
1 2 3 1 2<br>
5 3<br>
1 2 3 1 2<br>
5 1<br>
1 1 1 1 1<br><br>
Salida:<br>
2 0<br>
2 0<br>
2 2<br>
4 4<br>

