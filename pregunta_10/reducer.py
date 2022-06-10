#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    lista=[]

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        key, val = line.split("\t")
        key=key.strip()
        val=int(val)
        #sys.stdout.write("{}\n".format(len(key)))

        if key == curkey:
            #
            # No se ha cambiado de clave. Aca se acumulan los valores para la misma
            # clave.
            #
            lista.append(val)
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
                sys.stdout.write("{} {}\n".format(curkey, ','.join(str(i) for i in sorted(lista))))
                
                lista=[]

            curkey = key
            lista.append(val)

    sys.stdout.write("{}  {}\n".format(curkey, ','.join(str(i) for i in sorted(lista))))
