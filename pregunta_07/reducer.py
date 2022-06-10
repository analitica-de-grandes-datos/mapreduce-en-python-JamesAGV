#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    letters=[]
    dates=[]
    values=[]
    letters_total=[]
    dates_total=[]
    values_total=[]
    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        letter= line.split("\t")[0]
        date= line.split("\t")[1]
        value= line.split("\t")[2]
        value = int(value)

        if letter == curkey:

            letters.append(curkey)
            dates.append(date)
            values.append(value)

        else:

            if curkey is not None:

                letters_total.append(letters)
                dates_total.append(dates)
                values_total.append(values)
                #sys.stdout.write("{}\n{}\n{}\n".format(letters, dates, values))

            curkey = letter
            letters=[]
            letters.append(curkey)
            dates=[]
            dates.append(date)
            values=[]
            values.append(value)

    letters_total.append(letters)
    dates_total.append(dates)
    values_total.append(values)

    # sys.stdout.write("{}\n{}\n{}\n".format(letters, dates, values))
    #     #sys.stdout.write("{}\n".format(line.split("\t")))
    # sys.stdout.write('\n')
    # sys.stdout.write("{}\n{}\n{}".format(letters_total, dates_total, values_total))

    for i in range(5):
        ordenada=sorted(enumerate(values_total[i]), key=lambda x: x[1])
        for j in ordenada:
            sys.stdout.write("{}\t{}\t{}\n".format(letters_total[i][j[0]], dates_total[i][j[0]], values_total[i][j[0]]))
