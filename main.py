# This entrypoint file to be used in development. Start by reading README.md
#from pytest import main

from arithmetic_arranger import arithmetic_arranger


print(arithmetic_arranger(["9999 + 9999", "3801 - 6703", "4 + 3", "1 + 4009"],True))


# Run unit tests automatically
#main(['-vv'])
