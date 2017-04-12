class ChessBoard:

    def __init__(self, width, height):
        """ Constructs objects of type Board.
        """
        self.width = width
        self.height = height
        self.data = [[' '] * width for row in range(height)]


    
    def __repr__(self):
        """ Returns a string representation for an object of type Board.
        """
        counter = 8
        s = ''   # the string to return
        for row in range(self.height):
            s += str(counter) + '|'+ ''  # add the spacer character
            counter -=1
            for col in range(self.width):
                s += self.data[row][col] + '|'
        
            s += '\n'
            

        s = s + ' ' + ('-' + ('-'*2*self.width) + '\n')

        result = ' '
        for x in range(self.width):
            result = result + str(chr(x+97)) + " "

        s += " " + result + '\n'

        return s


    def readPieces(self,string):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        black = "abcdefghijklmnopqrstuvwxyz"
        spaces = "0123456789"
        counter = 0
        
        
        for row in range(8):
            for col in range(8):
                self.data[row][col] = string[counter]
                counter +=1
                
                    
                
        
                
            
    def parseString(self, string):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        black = "abcdefghijklmnopqrstuvwxyz"
        spaces = "0123456789"
        newstr = string.replace("/", "")
        for x in newstr:
            if x in spaces:
                replaceStr = int(x)*' '
                newstr = newstr.replace(x, replaceStr)
        return newstr

    def updateBoard(self,string):
        piecesString = self.parseString(string)
        self.readPieces(piecesString)
        




