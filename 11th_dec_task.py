
emp_records = [
('_id','Name','Age','Marks'),
(1,'Steven',23,(95,90,60,65,77,80)),
(2,'Nick',24,  (95,93,60,65,60,81)),
(3,'Peter',23, (77,90,34,76,77,80)),
(4,'Dan',23,   (95,58,60,65,66,89)),
(5,'Tim',25,   (23,55,56,43,56,45)),
(6,'Dave',24,   (0,35,55,76,77,80)),
(7,'John',27, (92,'Ab',60,65,77,80)),
(8,'Jacob',27, (98,89,60,65,77,80)),
(9,'Chris',25, (97,98,96,99,97,89))
]

# separate pass and fail students
pass_students = []
fail_students = []

for _id,name,age,marks in emp_records[1:]:
    fail = False
    for m in marks:
        if str(m)=="Ab" or str(m)=="0" or (str(m).isdigit() and int(m)<35):
            fail = True
            break
    if fail:
        fail_students.append(name)
    else:
        total = sum(int(m) for m in marks if str(m).isdigit())
        pass_students.append((name,total,marks))
print("Pass students:",pass_students)
print("Fail students:",fail_students)

# 1. Topper
topper = max(pass_students,key=lambda x:x[1])[0]
print("Topper:",topper)

# 2. Last grade student
last_grade = min(pass_students,key=lambda x:x[1])[0]
print("Last grade:",last_grade)

# 3. Failures
print("Failures:",fail_students)

# 4. Totals of pass students
print("Totals:",[[name,total] for name,total,_ in pass_students])

# 5a. AI subject (second mark)
ai_marks = [(name,marks[1]) for name, total,marks in pass_students]
top_ai = max(ai_marks,key=lambda x:x[1])[0]
low_ai = min(ai_marks,key=lambda x:x[1])[0]
print("AI Top:",top_ai)
print("AI Least:",low_ai)

#5b. Subjects with most toppers
subjects = ["ML","AI","Python","Cloud","DB","Prompt"]
top_subjects = []
for i,sub in enumerate(subjects):
    best = max(pass_students,key=lambda x:x[2][i])[2][i]
    winners = [name for name,total,marks in pass_students if marks[i]==best]
    if winners:
        top_subjects.append(sub)
print("Subjects with most toppers:",top_subjects)

# 5c. Subjects with most failures
fail_subjects = []
for i,sub in enumerate(subjects):
    count = 0
    for _id,name,age,marks in emp_records[1:]:
        m = marks[i]
        if str(m)=="Ab" or str(m)=="0" or (str(m).isdigit() and int(m)<35):
            count+=1
    fail_subjects.append((sub,count))
most_fail = max(fail_subjects,key=lambda x:x[1])[0]
print("Subject with most failures:",most_fail)  
