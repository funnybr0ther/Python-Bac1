class CircularLinkedList :
    class Node :
        def __init__ ( self , cargo = None , next = None ) :
            """ Initialises a new Node object . """
            self . __cargo = cargo
            self . __next = next
        def value ( self ) :
            """ Returns the value of the cargo contained in this node . """
            return self . __cargo
        def next ( self ) :
            """ Returns the next node to which this node links . """
            return self . __next
        def set_next ( self , node ) :
            """ Sets the next node to which this node links to a new node . """
            self . __next = node
    def __init__ ( self ) :
        """ Initialises a new empty circular linked list .
        """
        self . __first = None
        # pointer to the first node
        self . __last = None
        # pointer to the last node
    def first ( self ) :

        return self . __first
    def last ( self ) :
        return self . __last
    def add ( self , cargo ) :                
        node = self . Node ( cargo , self . first () )
        self.__first = node
        if self.last() == None :
        # when this wa s the first element being added ,
            self.__last = node
        # set the last pointer to this new node
        self.last().set_next(node)
    def remove(self, cargo):
        if self.first == None:
            return None
        def remove_cargo_recursive(self, node, cargo):
            if node.next().value() == cargo:
                node.__cargo = node.next().value()
                node.__next = node.next().next()
            if node == self.first:
                return None
            else:
                remove_cargo_recursive(self, node.next(), cargo)
        remove_cargo_recursive(self, self.first(), cargo)
                
class TourdeRole:

    @classmethod
    def main(cls):
        l = CircularLinkedList ()
        l . add ( " Charles " )
        l . add ( " Kim " )
        l . add ( " Siegfried " )
        l . add ( " S é bastien " )
        l . add ( " Charles " )
        l . add ( " Siegfried " )
        l . remove ( " Kim " )
        l . add ( " Charles " )

TourdeRole.main()