import getopt, sys

def usage():
  print "\nThis is the usage function\n"
  print 'Usage: '+sys.argv[0]+' -i <file1> [option]'

def main(argv):
  try:
    opts, args = getopt.getopt(argv, 'hi:o:tbpms:', ['help', 'input file=', 'number of nodes='])
    if not opts:
      print 'No options supplied'
      usage()
    print opts[0][1]
    print args
  except getopt.GetoptError,e:
    print e
    usage()
    sys.exit(2)

  for opt, arg in opts:
    if opt in ('-h', '--help'):
      usage()
      sys.exit(2)

if __name__ =='__main__':
    main(sys.argv[1:])
