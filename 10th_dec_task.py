# cleaning data
import re
emp_records = """ [(1, 'Nick $$#  Jr.', 23, '45000.0$'),
(2, 'Nick Jr.', 63, '245000.0&**&'),
(3, 'Nick Sr.', 53, 145000.0),
(4, 'Dan  ^^', 23, '45000.0'),
(5, 'Steve', 23, 46000.0), 
(6, 'Steve Jr.', 24, '***146000.0'), 
(7, '&&^^Steve    Sr.', 65, 446000.0)] """


up_emp_records = eval(emp_records)


cleaned_recs = [
    (
        emp_id,
        ' '.join(re.sub(r'[^a-zA-Z0-9 .]', '', name).split()),    
        age,
        float(re.sub(r'[^0-9.]', '', str(salary)))               
    )
    for emp_id, name, age, salary in up_emp_records
]

print(cleaned_recs)



# 1. Sum of salaries of all the employees

total_sal = 0

for *other, salary in cleaned_recs:
        total_sal += salary
print(f'Total salary of employees: {total_sal}')



# 2. Names of employees whose age < 25

for *other, age in cleaned_recs:
        if age < 25:
                print(*other, age)




# 3.update the net takeaway after deducting the tax in a new column and print the new data.

updated_emp_rec = []
for emp_id, name, age, salary in cleaned_recs:  

    if salary <= 500000:
        tax_rate = 0.05
    elif salary < 1000000:
        tax_rate = 0.10
    else:
        tax_rate = 0.15
    
    salary_after_tax_deduction = salary * (1 - tax_rate)
    updated_emp_rec.append((emp_id, name, age, salary, salary_after_tax_deduction))

print(updated_emp_rec)


#updating age of employee based on the id if even plus or plus five
for emp_id, name, age, salary in cleaned_recs:
      if emp_id % 2 == 0:
            print(emp_id, name, age+10, salary)
      else:
            print(emp_id, name, age+5, salary)

# we need to convert our list of tuples into tuple of lists.

tuple_of_lists =  tuple(map(list,zip(*cleaned_recs)))
print(tuple_of_lists)

