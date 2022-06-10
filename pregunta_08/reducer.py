#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    suma = 0
    promedio = 0
    i=0
    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:
            #
            # No se ha cambiado de clave. Aca se acumulan los valores para la misma
            # clave.
            #
            i=i+1
            suma = suma + val

        else:
            #
            # Se cambio de clave. Se reinicia el acumulador.
            #
            if curkey is not None:
                #
                # una vez se han reducido todos los elementos
                # con la misma clave se imprime el resultado en
                # el flujo de salida
                #
                promedio=suma/i
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, promedio))

            curkey = key
            suma = val
            i=1
            promedio = suma/i
    promedio=suma/i
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, promedio))