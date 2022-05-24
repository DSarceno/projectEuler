#    2022-05-23
#    collatzSequence.gp
#    Diego Sarceño (dsarceno68@gmail.com)

#    grafica secuencia de collatz

#    Codificación del texto: UTF8
#    Compiladores probados: GNUPLOT (Ubuntu 20.04 Linux) 5.2
#    Instrucciones de compilación: no requere nada mas
#    gnuplot collatzSequence.gp

# PROGRAM
# Idioma
set encoding utf8
# terminal
unset label
clear
set terminal pdf
set output "collatzSequence.pdf"
set grid
set title "Secuencia de Collatz"
set xlabel "Número"
set ylabel "Longitud de la Secuencia"
set key left top box


# se plotean los dos conjuntos de datos en una sola grafica, pero con ejes
# y's independientes.
plot "data.dat" u 1:2 w point t "Iteraciones"
