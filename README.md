# TareaProgramada1
Primera tarea programada Estructuras II

************** IMPORTANTE **************
Antes de correr cualquier simulación se debe descargar el archivo aligned.trace el cual se puede descargar del link:  
http://ie0521.jsdanielh.org/memory-trace-
gcc.trace.gz

Este archivo se debe ubicar en la raiz de la carpeta.

***************************************** 
**************INSTRUCCIONES**************
*****************************************

1) run_cache.py sirve para simular el cache, la foma de ejecutarlo es:

$run_cache.py <associativity> <cache_size> <block_size>

2) all_test.py sirve para correr todos las posibles combinaciones, variando la asociatividad, tamaño de cache y tamaño de bloque. Considere que ejecutar este programa le tomará su debido tiempo, pues se ejecutan todas y cada una de las posibles combinaciones.

$./all_test.py

3)plot_Miss_Rate.py sirve para graficar el Miss Rate obtenido. Dentro del archivo se debe escribir el tipo de asociatividad deseado y los tamaños de cache y bloque. 

$./plot_miss_rate.py