import BinarySearchTree
import math

class AVLNode(BinarySearchTree.Node):
    def __init__(self,key,value):
        BinarySearchTree.Node.__init__(self,key,value)
        self.height=1
    def __repr__(self):
        return "Node{ key : " + str(self.key) + ", value : " + str(self.value) + "}"

 



class AVLTree(BinarySearchTree.BST):
    def __init__(self):
        BinarySearchTree.BST.__init__(self)
    def __repr__(self):
        return self.printPart(self.root)

    def printPart(self,node):
        if(node==None):
             return "X"

        leftString=self.printPart(node.left)
        rightString=self.printPart(node.right)


        sideWidth=max(len(leftString.split("\n")[0]),len(rightString.split("\n")[0]))
        width=sideWidth+len(str(node.key))+sideWidth
        halfWidth=math.floor(sideWidth/2)

        string=halfWidth*" "+"/"+(sideWidth-halfWidth-1)*"-"+str(node.key)+(sideWidth-halfWidth-1)*"-"+"\\"+halfWidth*" "+"\n"

        leftArr=leftString.split('\n')
        rightArr=rightString.split("\n")
        for i in range(0,max(len(leftArr),len(rightArr))):
            if(len(leftArr)>i):
                smallSideWidth=math.floor((sideWidth-len(leftArr[i]))/2)
                string+=smallSideWidth*" "
                string+=leftArr[i]
                string+=(sideWidth-len(leftArr[i])-smallSideWidth)*" "
            else:
                string+=" "*(sideWidth)

            string+=(width-sideWidth*2)*" "

            if(len(rightArr)>i):
                smallSideWidth=math.floor((sideWidth-len(rightArr[i]))/2)
                string+=smallSideWidth*" "
                string+=rightArr[i]
                string+=(sideWidth-len(rightArr[i])-smallSideWidth)*" "
            else:
                string+=" "*(sideWidth)
            string+="\n"

        return string[:-1]


    def put(self, keyIn, valueIn):
        if self.root.getKey() == None:
            self.root = AVLNode(keyIn, valueIn)
        else:
            self.root = self.__put(self.root, keyIn, valueIn)
    def __put(self, nodeIn, keyIn, valueIn):
        if nodeIn == None or nodeIn.getKey() == None:
            return AVLNode(keyIn, valueIn)
        
        if keyIn > nodeIn.getKey():
            nodeIn.setRight(self.__put(nodeIn.getRight(), keyIn, valueIn))
        else:
            nodeIn.setLeft(self.__put(nodeIn.getLeft(), keyIn, valueIn))


        nodeIn.height=1+(getHeight(nodeIn.left)+getHeight(nodeIn.right))

        heightDiff=self.getHeightDiff(nodeIn)




        if heightDiff>1 and keyIn<nodeIn.left.key:
            return rotateRight(nodeIn)
        if heightDiff<-1 and keyIn>nodeIn.right.key:
            return rotateLeft(nodeIn)
        if heightDiff>1 and keyIn>nodeIn.left.key:
            nodeIn.left=rotateLeft(nodeIn.left)
            return rotateRight(nodeIn)
        if heightDiff<-1 and keyIn<nodeIn.right.key:
            nodeIn.right=rotateRight(nodeIn.right)
            return rotateLeft(nodeIn)
        
        return nodeIn
    def getHeightDiff(self, node):
        if(node!=None):
            return getHeight(node.left)-getHeight(node.right)
        else:
            return 0
def getHeight(node):
    if(node==None):
        return 0
    return 1+max(getHeight(node.left),getHeight(node.right))
    
def rotateRight(node):
    if(node==None or node.left==None):
        return None

    
    l=node.left
    lr=l.right
    l.right=node
    node.left=lr

    node.height=1+max(getHeight(node.left), getHeight(node.right))
    l.height=1+max(getHeight(l.left), getHeight(l.right))

    return l
def rotateLeft(node):
    if(node==None or node.right==None):
        return None

    
    r=node.right
    rl=r.left
    r.left=node
    node.right=rl

    node.height=1+max(getHeight(node.left), getHeight(node.right))
    r.height=1+max(getHeight(r.left), getHeight(r.right))

    return r






x = AVLTree()
x.put(10,1)
x.put(20,1)
x.put(30,1)
x.put(40,1)
x.put(50,1)
x.put(25,1)

x.put(10,1)
x.put(5,2)
print(x)

x.put(15,3)

x.put(4,4)
x.put(6,5)
x.put(14,6)
x.put(16,7)
print(x)

