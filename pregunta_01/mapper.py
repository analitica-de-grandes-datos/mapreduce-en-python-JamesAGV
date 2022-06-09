#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
	n=0

	for line in sys.stdin:

        #
        # genera las tuplas palabra \tabulador 1
        # ya que es un conteo de palabras
        #
       # for word in line.split()[2]:

            #
            # escribe al flujo estandar de salida
            #
		if n == 1:
			word=line.split(',')[2]
			sys.stdout.write("{}\t1\n".format(word))
		n=1
