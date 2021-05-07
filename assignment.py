Question 1. [20 pts]

Write a function howManyMonths(start, rate, spending, target) where:

start - the starting balance in your bank account (float)

rate - the monthly interest rate (float) - like 0.001 for 0.1%

spending - the monthly amount that is spent each month (float)

target - the target savings that you’d like to achieve

The function returns how many months it takes to save the target savings amount. The function should return a -1 if the balance goes below 0 because the spending is too high. The function should also return -1 if the target is not reached after 100 months.

Each month you earn the monthly rate of interest, but you also spend the spending amount.

So, next_month_balance = start_balance * (1 + rate) - spending

1
def howManyMonths(start, rate, spending, target):
2
    # write your code here
3
​
4
# any test cases you'd like to have
5
​
6
​
ActiveCode (cosc_1306_cw6_f20_q1_ss)

Question in Context
Not yet graded
The following program uses a for loop to print all of the words in the list ‘words’ that start with “c”, and adds 1 to c_counter. Change the program so that it uses a while loop to complete the same task.

1
words = ["aardvark","cookies","asterisk","cowabunga","gryphon","angular","cringe"]
2
i = 0
3
c_counter = 0
4
for word in words:
5
    if word[0] == "c":
6
        print(word)
7
        c_counter = c_counter + 1
8
​
Activity: 1 ActiveCode (cne_330_for_to_while)

Question in Context
Not yet graded
Construct a program that will output all the even numbers from 0 to 99 using a for loop. Drag and drop the code blocks from the left column into the write column.

Hint: At least one line is incorrect. all lines provided.

Parsons (cne_330_for_parsons)

Question in Context
Not yet graded
Construct the code that will result in all IP addresses being printed.

Parsons (cne330_ip_address_for_loop)

Question in Context
Not yet graded
Write a function, `find_max_octet` that takes in a list of IP octets, and returns the largest octet.

