# marks =[94.3, 87.3, 45.7, 34]
# print(marks)
# print(len(marks))
# print(marks[0])
# print(marks[1])
# print(type(marks))

# student =["vishal", 18, "delhi"]
# print(student[0])
# student[0]="arjun"
# print(student)

# marks=[85, 87, 33, 33,  24]
# print(marks[1:2])
# print(marks)

# marks=[85, 87, 33, 33,  24]
# marks.append(2)

# marks=[85, 87, 33, 33,  24]
# print(marks.sort())
# print(marks)

# marks=[4, 2, 1, 3, 5]
# print(marks.append(6))
# print(marks.sort())
# print(marks)

# marks=[4, 2, 1, 3, 5]
# print(marks.append(6))
# print(marks.sort(reverse=True))
# print(marks)

# marks=["mango", "lichi", "apple", "banana"]
# print(marks.append("amrud"))
# print(marks.sort())
# print(marks)

# marks=["mango", "lichi", "apple", "banana"]
# print(marks.append("amrud"))
# print(marks.sort(reverse=True))
# print(marks)

# LIST =[12, 44, 20,1,2]
# LIST.reverse
# print(LIST)

# list=[2,1,3]
# list.insert(1,5)
# print(list)

# list=[2,1,3]
# list.remove(1)
# print(list)

# list=[2,1,3]
# list.pop(1)
# print(list)
                 #tuple
# tup=(2,1,3)
# print(tup[0])
# print(tup[2])
# print(type(1))

# tuple =(1,2,3,4,5)
# print(tuple)
# print(type(tuple))

# tuple =(1,2,3,4,5)
# print(tuple[1:3])
# print(tuple)

# tuple =(1,2,3,4,5)
# print(tuple.index(2))
# tuple =(1,2,3,4,5,2)
# print(tuple.count(2))

# movies=[]
# movies.append(input("Enter the first movies:"))
# movies.append(input("Enter the second movies:"))
# movies.append(input("Enter the third movies:"))
# print(movies)

                #dictonary& sets


# info={
#     "key":"values",
#     "subject":["python", "c", "java"],
#     "topis":("dict", "set"),
#     "age":35,
#     "adult":True
# }
# print(type(info))

# dict = {
#     "name":"vishal",
#     "key": "values",
#     "subject": ["python", "c", "java"],
#     "topics": ("dict", "set"),
#     "age": 35,
#     "adult": True
# }
# dict ["name"]="c++"
# dict["surname"]="yadav"
# print(dict)

# print(dict["key"])
# print(dict["subject"])
# print(dict["topics"])
# print(dict["age"])
# print(dict["adult"])

        #null dictionary
# nul={}
# nul["name"]="vishal"
# print(nul)


        # nested dictionary
# student={
#     "name":"vishal",
#     "subject":{
#         "phy":97,
#         "chem":87,
#         "math":98,
#     }
# }
# print(student)
# print(student["subject"])
# print(student["subject"] ["chem"])

# student={
#     "name":"vishal",
#     "subject":{
#         "phy":97,
#         "chem":87,
#         "math":98
#     }
# }
        # keys method
# print(student.keys())
# print(list(student.keys()))
# print(len(student.keys()))
        # method values
# print(student.values())        
        # iteams
# print(student.items())  
# print(list(student.items()))   
# pairs= list(student.items())  
# print(pairs[0]) 
        # get method
# print(student["name"])
# print(student.get("name767"))        
        # /update method
# print(student.update({"city":"delhi"}))
# new={"village":"mathiya","city":"delhi"}
# print(student.update(new))      
# print(student)     

# coll={1, 2,3,4,"helo","world","helo",4}
# print(coll)
# print(type(coll))
                # empty sets
# collection=set()
# print(type(collection))
# collection =set()
# collection.add(1)
# collection.add(2)
# collection.add(2)
# collection.remove(2)
# print(collection)

# collection =set()
# collection.add(1)
# collection.add(2)
# collection.add("apna")
# collection.add((1,2,3))
# collection.clear()
# print(len(collection))
# pop method
# collection ={"hello","apna","college","and","tumhara","college"}
# print(collection.pop())
# print(collection.pop())
# print(collection.pop())

# set1={1,2,3}
# set2={2,3,4}
# print(set1.union(set2))
# print(set1,set2)

# set1={1,2,3}
# set2={2,3,4}
# print(set1.intersection(set2))

# question.1
# dict={
#     "cat":"a small animal",
#     "table":["a piece of furniture","list of facts & figures"]
# }
# print(dict)

# question.2
# subject={
#     "python","java","c","c++","javascript",
#     "python","java","c++","python","java"
# }
# print(len(subject))
# question.3
# marks={}
# x=int(input("Enter the phy :"))
# marks.update({"phy":x})
# x=int(input("Enter the chem :"))
# marks.update({"chem":x})
# x=int(input("Enter the math :"))
# marks.update({"math":x})
# print(marks)

# question.4
# values={9,9.19 }
# print(values)

# values={
#     ("float",9.0),
#     ("int",9)
# }

num =[1,2,8,4,6,7,9,49]
idx =0
x =49
for i in num:
    if(i == 49):
        print("index no: ",idx)
        break
    idx +=1