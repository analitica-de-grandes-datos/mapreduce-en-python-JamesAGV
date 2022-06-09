#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
   n=0
   for line in sys.stdin:
      if n>0:
         lista=line.split(',')
         purpose=lista[3]
         amount=lista[4]
         sys.stdout.write("{}\t{}\n".format(purpose, amount))
      n=1
