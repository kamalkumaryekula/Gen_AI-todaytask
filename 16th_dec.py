
s1 = set()
s2 = set()
for i in range(1,101):
    if i%2 == 0:
        s1.add(i)
    else:
        s2.add(i)
print(s1)
print(s2)



s1 = []
s2 = []

s3 = set()
for i in range(1,101):
    if i%2 == 0:
        s1.append(i)
    else:
        s2.append(i)

tuple_odd = tuple(s2)
tuple_even = tuple(s1)

s3.add(tuple_odd)
s3.add(tuple_even)
print(s3)



s =\
['steven_A@gmail.com',
 'nick_A@gmail.com',
 'peter_C@gmail.com',
 'dan_B@gmail.com',
 'tim_A@gmail.com',
 'dave_C@gmail.com',
 'john_B@gmail.com',
 'jacob_A@gmail.com',
 'chris_D@gmail.com']
a = set()
b = set()
c = set()
d = set()
for i in s:
    if "A" in i:
        a.add(i)
    elif "B" in i:
        b.add(i)
    elif "C" in i:
        c.add(i)
    elif "D" in i:
        d.add(i)
print(a)
print(b)
print(c)
print(d)


#strip special characters make a set.
_names = ["Mike#","Nick#","Sean#","Sean$"]
names = set()
for i in _names:
    names.add(i.strip("#$"))
print(names)


#no.of sections in a set.
s1 =set()
for m in s:
    n = m.split("@")
    s1.add(n[0][-1])
print(s1)



#
primes = set()
odds = set()
inter = set()
for i in range(1, 100):
    if i%2 != 0:
        odds.add(i)
    if i >1:
        for j in range(2,int(i**0.5)+1):
            if i%j ==0:
                break
        else:
               primes.add(i)

inter = primes & odds
print(inter)



email = \
['steven_A@gmail.com',
 'nick_A@outlook.com',
 'peter_C@gmail.com',
 'dan_B@outlook.com',
 'tim_A@gmail.com',
 'dave_C@rediff.com',
 'john_B@rediff.com',
 'jacob_A@gmail.com',
 'chris_D@yahoo.com']
#find unique mail services
type = set()
for i in email:
    n = i.split("@")
    m = n[1].split(".")
    type.add(m[0])
print(type)

#type ofusers in each service and their count.
services = {e.split("@")[1].split(".")[0] for e in email}
print(services)
users = []
ser_users = set()
for service in services:
    for e in email:
        if service in e:
            users.append(e.split("_")[0].capitalize())
    ser_users.add((service, tuple(users),len(users)))
    users =[]
print(ser_users)