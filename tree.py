import numpy as np


class node:
    def __init__(self,*w):
        self.array=[]
        for i in w:
            self.array.append(i)
        self.array=np.array(self.array)

        self.parent=None
        self.children=[None]*(2**len(self.array))

    def addChild(self,other,position):
        other.parent = self
        self.children[position]=other
        return other

    def __str__(self):
        return "["+",".join([str(i) for i in self.array])+"]"


class Tree:
    SIZE = 1000000
    def __init__(self,root_node):
        '''
        dimension : number of dimensions
        array : the array of ndimention points
        number_of_splits : the number of splits baced directly on dimentions
        list_of_choices : the list of choices of the points to be stored in the corect tree
        '''
        
        self.root = root_node
        
        self.number_of_splits = 2**len(self.root.array)

        #calculating the diferent choices for sortingthe data to tree
        maxlength=self.number_of_splits
        counter = int('0', 2)
        self.list_of_choices = []
        while counter!=self.number_of_splits:
            string = bin(counter)[2:]
            string = '0'*(maxlength-len(string)-2) + string
            logic_array = [True if i=='1' else False for i in string] # 0: >= , 1: <=
            self.list_of_choices.append(logic_array)
            counter += int('0b1', 2)  
        
    def add(self,obj: node): #add to the tree 

        current_node = self.root
        depth=0
        while True:
            depth +=1
            #print("#")
            for j in range(len(self.list_of_choices)):
                logic = sum([1 for i in range(len(obj.array)) if (self.list_of_choices[j][i] == (obj.array[i]<=current_node.array[i]))]) #True in list_of_choices is : new cord is less or equal to the parent cord 
                #print(logic,j)
                index=j
                if logic==len(obj.array): break

            if current_node.children[j]!=None:
                current_node = current_node.children[j]
                continue

            #put element in current_node
            #print(f'index: {current_node} obj: {obj}')
            current_node = current_node.addChild(obj,j)
            return depth , index

    def select(self,start_cords,end_cords,node=None): 
        mins = [min(start_cords[i],end_cords[i]) for i in range(len(start_cords))]
        maxs = [max(start_cords[i],end_cords[i]) for i in range(len(start_cords))]

        current_node = node
        if node==None: current_node = self.root

        array_output = []
        min_logic = sum([1 for i in range(len(current_node.array)) if (current_node.array[i]>=mins[i])])==len(current_node.array)
        max_logic = sum([1 for i in range(len(current_node.array)) if (current_node.array[i]<=maxs[i])])==len(current_node.array)
        if min_logic and max_logic: array_output.append(current_node)
                

        min_disable_index = []
        max_disable_index = []
        for i in range(len(current_node.array)): #in every dimention 
            if mins[i]>current_node.array[i]: 
                min_disable_index.append(i) #for the dimention ,that is less than start node cord, we append to the disable ones the index of the dimention
            if maxs[i]<current_node.array[i]: 
                max_disable_index.append(i) #for the dimention ,that is less than start node cord, we append to the disable ones the index of the dimention

        disabled_choices_indexes = set([])
        for dimention in min_disable_index:
            for i in range(len(self.list_of_choices)):
                if self.list_of_choices[i][dimention] == True: disabled_choices_indexes.add(i)
        for dimention in max_disable_index:
            for i in range(len(self.list_of_choices)):
                if self.list_of_choices[i][dimention] == False: disabled_choices_indexes.add(i)

        for choice in range(len(self.list_of_choices)):
            if not choice in disabled_choices_indexes: 
                if current_node.children[choice]!=None:
                    result = self.select(start_cords,end_cords,node=current_node.children[choice])
                    if result!=[]:
                        for item in result:  
                            array_output.append(item)
        
        return array_output




            

    def move(self,point_index,newCords): pass
    def search(self,cords): pass

def preorder(current_node: node,depth=0):
    #parent children
    if current_node==None: return
    print(depth," : ",current_node)
    for i in range(len(current_node.children)):
        preorder(current_node.children[i],depth+1)
    return 




