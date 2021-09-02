def is_anagram(s,s1):
    if len(s)!= len(s1):
        return False
    else: 
        for i,j in zip(s,s1):
            if i!=j:
                return False
        return True

s1="LISTEN".lower()
s="SILENT".lower()
res: bool = is_anagram(s,s1)
print("Anagram") if res else print("Not anagram")



def is_anagram(ana,grama):
    n=0
    m=0
    anaSin=ana.replace(" ","").lower()
    gramaSin=grama.replace(" ","").lower()
    list(anaSin)
    list(gramaSin)
    
    for i in anaSin:
        n+=ord(i)
    for j in gramaSin:
        m+=ord(j)
    if ana == "" or grama == "" or ana==" " or grama==" ":
        print("No es anagrama")
    elif n == m:
        print("Es anagrama")
    else:
        print("No es anagrama")
while True:
    text1=input("Ingresa cadena 1: ")
    text2=input("Ingresa cadena 2: ")
    is_anagram(text1,text2)