# 1: This interpreter works by creating a file with vole instructions and
     prestablished memory values (if wanted)

# 2: for the file, it has to be a txt file, like 'lets_see.txt', and has to
     be inputed between '' like 'demofile.txt'. To start your code first use
     the keyword 'main(){' and to mark the end of your insructions close the
     bracket '}'. the instructions are read one line at the time and  each has
     to be on a separate lines, there can belines left in blank the interpreter
     will ignore any line that is empty or starts with the symbol '#', and also
     after the instrucction nothing will be compilled so you can use that space
     for commentaries and also entire lines putting the symbol '#' before the
     commentary.

# 2.1: the way to input memory is by  the keyword 'memory inizializa(){' and at
       the end  closing with '}',for putting the memory location, it follows the
       same rules as the instructions for spaces and commentaries, put the space
       in memory you want to write to in upper case and in hexadecimal then to
       asssigned the value put a '=' and the value to be assigned to that memory
       space like "A0 = 1A" the value '1A' will be stored in the memory position 'A0'.

#    Keep In Mind   #
1. Every characther has to be upper case exept for instructions like: '0xdA05'
2. At the end of the program the register that were used and the memory that was
   used will be printed
3. As a recommendation the instruction_file should be in the same directory(folder)
   that you're in
4. The format that is used with floating point is with a bias of -3.
### that's all (I think)###

#####To take a look on how it works you can run it with the lets_see.txt and see the process####
