#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

   for line in sys.stdin:
      number, letters = line.replace('\n','').split('\t')
      #sys.stdout.write("{}\t{}".format(number, letters))
      for letter in letters.split(','):
        sys.stdout.write("{}\t{}\n".format(letter, number))
        #tupla=(number,letter)
        #rite("{}\n".format(tupla))