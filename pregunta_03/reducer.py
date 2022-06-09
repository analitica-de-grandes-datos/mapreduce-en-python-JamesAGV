#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import numpy as np

if __name__ == '__main__':

    letters=[]
    values=[]

    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)
        letters.append(key)
        values.append(val)
        # sys.stdout.write("{}\n".format(lista))
    
    letters=np.array(letters)
    values=np.array(values)
    ordered=np.argsort(values)

    for i in ordered:
        sys.stdout.write("{},{}\n".format(letters[i],values[i]))
