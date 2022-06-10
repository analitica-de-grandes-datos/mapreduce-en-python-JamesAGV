#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':

    letters=[]
    dates=[]
    values=[]
    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        key, date, val = line.split("\t")
        val = int(val)

        letters.append(key)
        dates.append(date)
        values.append(val)

    ordenado=sorted(enumerate(values), key=lambda x: x[1])

    for i in ordenado[:6]:
        sys.stdout.write("{}\t{}\t{}\n".format(letters[i[0]], dates[i[0]], values[i[0]]))
