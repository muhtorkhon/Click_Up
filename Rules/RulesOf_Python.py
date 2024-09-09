# --->     reverse string

# gap = "Nigga"
# print(gap[::-1]) #=> aggiN

# --------------------------------------------------------------------------------- #

# --->  ==>count()<==  How many word or letter in string   <--- #

# gap = "Nigga Bitch Fuck asshole shit"
# print(gap.count('i')) # => 3

# --------------------------------------------------------------------------------- #

# --->  ==>capialize()<==  Only the first letter will become large and the rest will be small 

# gap = "niGGa"
# print(gap.capitalize()) # => Nigga

# ---------------------------------------------------------------------------------#

# --->  ==>find()<==  Returns the index at which the searched string is located  

# gap = "I have a big dick my nigga"
# print(gap.find('my')) # => Nigga 18

# --------------------------------------------------------------------------------- #

# --->  ==>replace()<==  Returns the index at which the searched string is located  

# replace(del, add, How many leter replece)
# gap = "Fuck of, up, around, you"
# x = "you"
# y = "Nigga"
# print(gap.replace(x, y)) # => Fuck of, up, around, Nigga
# print(gap.replace(a:= input("Enter del: "), b:= input("Enter add: "))) # => Etring at consule

# --------------------------------------------------------------------------------- #

# --->  ==>split()<== default qiymatida har doyim probel or enter bo'yicha chopadi va list qaytaradi 

# gap =  "Whore, Slut"
# a = gap.split()
# print(a) # => ['Whore,', 'Slut']
# print(*a) # => Whore, Slut

# --------------------------------------------------------------------------------- #

# --->  ==>join(), eval()<== join is iterablr and eval is string

# a = "+".join('12345')
# print(f"{a} = {eval(a)  }") # => 1+2+3+4+5 = 15

# --------------------------------------------------------------------------------- #

# ---> ==> eumerate() and isinstance(,int)

# for index, value in enumerate("Nigga"):
#   print(index, value)

# a = [1,4,False,'Nigga', 1] 
# sum = 0
# for i in a:
#   if isinstance(i,int):
#     sum += i
# print(sum)

# --------------------------------------------------------------------------------- #

# ---> ==> clean() List ichini tozalashga xzmat qladi

# gap =  ['something', True, 24, 45.7]
# gap.clear()
# print(gap)

# --------------------------------------------------------------------------------- #

# ---> ==> copy() gives copy 

# a = ['someone']
# b =  ['something', True, 24, 45.7]
# a = b.copy()
# print(b)
# print(a)

# --------------------------------------------------------------------------------- #

# ---> ==> append() yuborilgan matinni (list qlib) oxiridan qo'shadi (Iterablr)
# ---> ==> extend() yuborilgan matinni listga ajraib qo'shadi

# gap =  ['something', True, 24, 45.7]
# gap1 =  ["hi",34,True]
# gap.extend(gap1)
# gap.append(gap1)
# print(gap)

# --------------------------------------------------------------------------------- #

# ---> ==> insert() berilgan index bo'yicha qo'shadi ,2 ta parametrli (Iterable)

# gap =  ['something', True, 24, 45.7]
# gap.insert(1,'black')
# gap.insert(len(gap),"Black") # Ohiridan qo'shadi
# print(gap)

# --------------------------------------------------------------------------------- #

# ---> ==> remove() kiritirilgan matinni o'chiradi 
# ---> ==> pop() index bo'yicha ochiradi va qiymat betilmasa oxiridan o'chiradi 

# gap =  ['something', True, 24, 45.7]
# gap.remove(True)
# gap1 = gap.pop(0)
# print(gap)
# print(gap1)

# --------------------------------------------------------------------------------- #

# ---> ==> reverse() list ichini teskari kilip beradi

# gap =  [4, 7, 24, 45.7]
# gap.reverse()
# gap.sort( reverse = True) # Teskari sortlash
# print(gap)

# --------------------------------------------------------------------------------- #

# ---> ==> sorted()  (Iterable)

# gap = ['Hi', 'My', 'Nigga']
# a ="".join(sorted(gap)) # => HiMyNigga
# a ="".join(sorted(gap, reverse=True)) # => NiggaMyHi | Teskati 
# print(a)

# --------------------------------------------------------------------------------- #

# ---> ==> key  (Iterable)

# gap = ['23','567','865','999','2024','9']
# res = max(gap, key = len)
# res = max(gap, key = lambda x: len(x))
# res = max(gap, key = int)
# print(res)

# --------------------------------------------------------------------------------- #

# ---> ==> get(key) yuborilgan key_ning valuesi qaytariladi (dictionary)
# --->get()=> Mavjud bo'lmagan key bersaxam error bermaydi (non qaytaradi)

# dic = {'color':'Black', 'Brand':'Mustang','year': 1997}
# print(a := dic.get('color')) 

# --------------------------------------------------------------------------------- #

# ---> ==> popitem() default sifatida ohiridan o'chirad va qiymat berilmaydi (dictionary)
# popitem() => pop()dan farqi ham key ham valuesini ochiradi (sugirib oladi)

# dic = {'color':'Black', 'Brand':'Mustang','year': 1997}
# q = dic.popitem()
# print(q)

# --------------------------------------------------------------------------------- #

# ---> ==>  (dictionary)



