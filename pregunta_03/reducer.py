#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys


if __name__ == '__main__':

    letters=[]
    values=[]

    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)
        letters.append(key)
        values.append(val)
        # sys.stdout.write("{}\n".format(lista))
    
    ordered=sorted(enumerate(values), key=lambda x: x[1])
    for i in ordered:
        sys.stdout.write("{},{}\n".format(letters[i[0]],values[i[0]]))
