import sys
import cowsay


a = sys.argv
text = cowsay.cow(a[1])

print(text)