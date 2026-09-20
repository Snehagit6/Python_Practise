#String reverse:M1
name = "Sneha"
l = list(name)
name_reverse=''
for i in range(len(l)):
    name_reverse+=l.pop()
print(name_reverse)

string="I Work At HCL"
l=string.split()
for i in range(len(l)):

    if len(l[i])>1 and l[i].isupper()==False:
            rev=''
            for k in l[i]:

                l[i]=k+rev.title()

print(l)

nl=[string.split()[i][::-1].title()if len(string.split()[i])>1 and l[i].isupper()==False else string.split()[i] for i in range(len(string.split()))]
print(' '.join(nl))


#String reverse:M2
sty="flower"
sty_rev=''
for s in range(len(sty)-1,-1,-1):
    sty_rev=sty_rev+sty[s]
print(sty_rev)

str1='A$B$C$D'
str2='$'.join([i for i in (''.join(str1.split('$'))[::-1])])
print(str2)
str1='A$BC$D'
# $EF$G'
str2=(''.join(str1.split('$'))[::-1])
print(str2)
index=[i for i in range(len(str1)) if str1[i]=='$']
print(index)
str3=str2[0:index[0]]+'$'+str2[index[0]:index[1]-1]+'$'+str2[index[1]-1:]
     # +'$'+str2[index[2]-2:index[3]-3]+'$'+str2[index[3]-3:]
print("Rearranged string : ",str3)

#String reverse using recursion:M3
name="Tridha"
rev_name=""
def funcrev(name):
    if len(name)<=1:
        return name
    else :

        return name[-1]+funcrev(name[:-1])
print(funcrev(name))

#String reverse:M4
print("Compre reverse:",''.join([name[len(name)-i] for i in range(1,len(name)+1)]))

#String reverse:M6
print("Reverse Slicing:",name[::-1])

#String reverse:M7
rev=""
for i in name:
    rev=i+rev
print("Iter rev:",rev)

