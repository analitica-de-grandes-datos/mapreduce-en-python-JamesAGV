#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
   for line in sys.stdin:
      lista=line.split(',')
      letter=lista[0]
      value=lista[1]
      sys.stdout.write("{}\t{}".format(letter, value))
