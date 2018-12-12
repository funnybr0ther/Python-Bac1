This assistant can execute 11 different commands, all listed in the 11th, help().

The first, 'file <filename.(optional extension>', selects <filename> as the basefile for other commands, such as dictionnary, info or search. If the command returns an error, verify that you've specified the right path for the file.

The second, 'info', gives information about the selected file (the file has to be specified with 'file' before). That info consists of the amount of lines and the amount of chars in the file.

The third, 'dictionnary', just switches to dictionnary mode, allowing the use of the 'search' command.

The fourth, 'search <word>', searches the closest-looking word in the file, using Levenshtein's algorithm, calculating the amount of changes needed to be performed on word1 for it to become word2. That algorithm can take a bit of time for longer files or slower pc's.

The fifth, 'sum <number1 number2 number3 ... >' computes the sum of all numbers specified in the list, SEPARATED BY SPACES!

The sixth, 'avg <number1 number2 number3 ... >' computes the arithemetic mean of all numbers specified in the list, SEPARATED BY SPACES!

The seventh, 'product <number1 number2 number3 ... >' computes the product of all numbers specified in the list, SEPARATED BY SPACES!

The eighth, 'morsecode <Sentence>', translates the Sentence into morsecode.

The ninth, 'help', displays a simplified version of this README.

The tenth, 'exit', 'q', 'quit', 'exit()', all exit the assistant.

The eleventh, 'pika', well, just see for yourself. ASCII is beautiful, isn't it?

We didn't have that much trouble creating this program, it just took a lot of time and coordination. Creating the error messages was easy, although we had to create a different one for all the possible file/syntax/... errors. 

