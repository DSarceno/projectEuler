#    2022-05-26
#    digitFactorials.gp
#    Diego Sarceño (dsarceno68@gmail.com)

#    grafica secuencia de collatz

#    Codificación del texto: UTF8
#    Compiladores probados: GNUPLOT (Ubuntu 20.04 Linux) 5.2
#    Instrucciones de compilación: no requere nada mas
#    gnuplot digitFactorials.gp

# PROGRAM
# Idioma
set encoding utf8
# terminal
unset label
clear
set terminal pdf
set output "digitFactorials.pdf"
set grid
set title "Digit Factorials"
set xlabel "Número"
set ylabel "Suma de los Factoriales de sus Dígitos"
set key left top box


# se plotean los dos conjuntos de datos en una sola grafica, pero con ejes
# y's independientes.
f(x) = x
plot "data2.dat" u 1:2 w point t "Iteraciones", f(x) lc "black" t "Cota"
