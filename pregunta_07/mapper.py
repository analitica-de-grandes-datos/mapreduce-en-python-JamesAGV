#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

	for line in sys.stdin:

		letter, date, value =line.split('   ')
		sys.stdout.write("{}\t{}\t{}".format(letter, date, value))