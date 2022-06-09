#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

   for line in sys.stdin:
      letter, value = line.split('   ')[::2]
      sys.stdout.write("{}\t{}".format(letter, value))
