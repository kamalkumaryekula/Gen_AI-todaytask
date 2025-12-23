# create a dictionary if number is even add "even" else add "odd".
d1 = {}
for i in range(1,100):
    if i%2==0:
        d1[i] = "even"
    else:
        d1[i] = "odd"
    print(d1)

# create a dictionary where key is n and and value is n+1.
d = {}
for i in range(1,100):
    d[i] =i+1
    print(d)

print(d1.keys())
print(d1.values())
d1[71] = "not even"
print(d1)

l = [1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6]
d2 = {}
for i in l:
    if i in d2:
        d2[i] += 1
    else:
        d2[i] = 1
print(d2)


d3 = {"even": [], "odd": []}

for i in range(1,101):
    if i%2 == 0:
        d3["even"].append(i)
    else:
        d3["odd" ].append(i)
print(d3)



emails = \
['steven_A@gmail.com',
 'nick_A@outlook.com',
 'peter_C@gmail.com',
 'dan_B@outlook.com',
 'tim_A@zoho.com',
 'dave_C@rediff.com',
 'john_B@rediff.com',
 'jacob_A@gmail.com',
 'chris_D@yahoo.com']
d = {}
for email in emails:
    name ,section= email.split("@")[0].split("_")
    if section not in d:
        d[section] =[name]
    else:
        d[section].append(name)
print(d)

#
d_count= {}
for email in emails:
    ser,_ = email.split("@")[1].split(".")
    if ser not in d_count:
        if section not in d:
            d[section] =[name]
    else:
        d[section].append(name)
print(d_count)


nums = [2,7,11,15]
target = 9
    


class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}  
        for i, num in enumerate(nums):
            needed = target - num
            if needed in num_map:
                return [num_map[needed], i]  
            num_map[num] = i  
print(Solution().two_sum(nums, target))




student_records =\
[('_id', 'Name', 'Age', 'Marks', 'Email'), 
(1, 'Steven', 23, (95, 90, 60, 65, 77, 80), 'steven_A@gmail.com'), 
(2, 'Nick', 24, (95, 93, 60, 65, 60, 81), 'nick_A@gmail.com'), 
(3, 'Peter', 23, (77, 90, 34, 76, 77, 80), 'peter_C@gmail.com'), 
(4, 'Dan', 23, (95, 58, 60, 65, 66, 89), 'dan_B@gmail.com'), 
(5, 'Tim', 25, (23, 55, 56, 43, 56, 45), 'tim_A@gmail.com'), 
(6, 'Dave', 24, (0, 35, 55, 76, 77, 80), 'dave_C@gmail.com'), 
(7, 'John', 27, (92, 'Ab', 60, 65, 77, 80), 'john_B@gmail.com'), 
(8, 'Jacob', 27, (98, 89, 60, 65, 77, 80), 'jacob_A@gmail.com'), 
(9, 'Chris', 25, (97, 98, 96, 99, 97, 89), 'chris_B@gmail.com')] 

faculty_records =\
[('faculty_name', 'subject'), 
('Dr.Alex', 'AMI'), 
('Prof.Matt', 'AGI'), 
('Prof.Kevin', 'Prompt Engineering'), 
('Dr.Anthony', 'DeepLearning'), 
('Dr.Evans', 'Python'), 
('Ms.Robbie', 'Database')] 



marks = [rec[3] for rec in student_records[1:]]
sw_marks = list(zip(*marks))

subjects = [sub for fac, sub in faculty_records[1:]]
fac_dict = dict([[sub, fac] for fac, sub in faculty_records])

sw_marks_dict = {}

for _ind, marks_list in enumerate(sw_marks):
    sw_marks_dict[subjects[_ind]] = marks_list
sw_marks_dict
fin_sw_marks_dict = {}

for sub in sw_marks_dict:
    new_marks = [mar for mar in sw_marks_dict[sub] if mar != 'Ab' and int(mar) > 85]
    fin_sw_marks_dict[sub] = new_marks

_max = max(fin_sw_marks_dict.items(), key=lambda x: len(x[1]))[0]
w=[i for i in fin_sw_marks_dict if fin_sw_marks_dict[i]==fin_sw_marks_dict[_max]]

print(w)
