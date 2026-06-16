# 1
import numpy as np

# Testing your agent without real data
# Simulating user behavior
# Initializing AI model weights
# Shuffling datasets

'''2 — np.random.rand()
Random floats between 0 and 1'''
# 1D array
print(np.random.rand(5))
# [0.37 0.95 0.73 0.59 0.15]

# 2D array
print(np.random.rand(3, 4))
# 3 rows 4 columns of random floats

'''3 — np.random.randint()
Random whole numbers between a range'''



# randint(low, high, size)
print(np.random.randint(0, 100, 5))
# [23 67 45 89 12]

# 2D array of random marks
print(np.random.randint(0, 100, (3, 4)))
# 3 students 4 subjects

'''4 — np.random.randn()
Random numbers from normal distribution

What is Normal Distribution?
It is a pattern where most values cluster around the middle and fewer values appear at the extremes.

Real Life Example
Heights of 1000 people:
Very short    → few people
Short         → some people
Average       → MOST people  ← middle
Tall          → some people
Very tall     → few people
This natural pattern is called normal distribution.

The Bell Curve
        ████
      ████████
    ████████████
  ████████████████
████████████████████
-3  -2  -1   0   1   2   3

Center is always 0
Most values fall between -1 and 1
Very few values beyond -3 or 3'''
print(np.random.randn(5))
# [-0.5  1.2  0.3 -1.1  0.8]
# Numbers centered around 0

'''5 — np.random.seed()
Makes random numbers repeatable'''
# Without seed — different every time
print(np.random.rand(3))  # [0.37 0.95 0.73]
print(np.random.rand(3))  # [0.12 0.44 0.68]

# With seed — same every time
np.random.seed(42)
print(np.random.rand(3))  # always [0.37 0.95 0.73]
np.random.seed(42)
print(np.random.rand(3))  # always [0.37 0.95 0.73]

'''6 — np.random.choice()
Pick random items from an array'''
arr = np.array([10, 20, 30, 40, 50])

# Pick 3 random items
print(np.random.choice(arr, 3))
# [30 10 50]

# Pick without repetition
print(np.random.choice(arr, 3, replace=False))
# [20 40 10]

'''7 — np.random.shuffle()
Randomly shuffle an array'''

arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print(arr)
# [3 1 5 2 4]
print("="*50)
# tasks

# np.random.seed(42)

# 1. Create 10 random student marks between 0-100
print(np.random.randint(0,100,10))
# 2. Create 3x4 random marks array
print(np.random.randint(0,100,(3,4)))
print("="*50)
# 3. Simulate 50 API response times between 100-600ms
# 4. Find average, max, min of response times
response_time=np.random.randint(100,600,50)

print(response_time)
print("mean",response_time.mean())
print("max",response_time.max())
print("min",response_time.min())


# 5. Find how many responses were above 400ms
print("response>400 ms",np.where(response_time>400)[0]+1)
# 6. Shuffle the student marks array
marks=np.random.randint(0,100,10)
print("======")
print(marks)
# print(np.random.shuffle(marks))
print(marks)
# 7. Pick 5 random marks from student array
print("======")

marks = np.random.randint(0, 100, 10)
print("Original:", marks)

# Pick 5 without repetition
picked = np.random.choice(marks, 5, replace=False)
print("Picked  :", picked)





print("*"*90)
# task set 1

# import numpy as np
# np.random.seed(42)

# 1. Generate 20 random temperatures between -10 and 45
temp=np.random.randint(-10,45,20)
print(temp)
# 2. Find average temperature
print(temp.mean())
# 3. How many days were above 30 degrees
greater_30=np.where(temp>30)[0]+1
print(">30",greater_30)
# 4. How many days were below 0 degrees
below_0=np.where(temp<0)[0]+1
print("0>",below_0)

# task set 2
np.random.seed(42)

# Create sales data for 4 shops over 7 days
# Random sales between 500 and 5000
sales=np.random.randint(500,5000,[4,7])
print("sales data \n",sales)

# 1. Which shop had highest total sales
best_shope=np.sum(sales,axis=1)
print("best shope")
print(best_shope)
print(np.argmax(best_shope)+1)
# 2. Which day had lowest total sales across all shops
day_with_low_sale=np.sum(sales,axis=0)
print("day_with_low_sale\n",day_with_low_sale)
print(np.argmin(sales)+1)
# 3. Average daily sales per shop
average_sales=np.mean(sales,axis=1)
print("average_sales\n",average_sales)


# 4. Days where any shop sold more than 4000
# Both shop and day
rows, col = np.where(sales >= 4000)

print("Shop numbers:", rows + 1)
print("Day numbers :", col + 1)
# sales_moreThan_4000=np.where(sales>=4000)[0]+1
# print("sales_moreThan_4000\n",sales_moreThan_4000)


'''sales = np.array([
    [1360, 4272, 3592,  966, 4926, 3944, 3671],  # Shop 1
    [3419,  630, 2185, 1269, 2891, 2933, 1684],  # Shop 2
    [3885, 4617, 3404,  974, 1582, 3058, 2547],  # Shop 3
    [3247, 1475, 2306,  689, 3234, 3505, 2399]   # Shop 4
])

np.where(sales >= 4000)
Returns TWO arrays inside a tuple:
(array([0, 0, 2]),   ← row positions
array([1, 4, 1]))   ← col positions

rows, cols = np.where(sales >= 4000)

rows gets first array  → [0, 0, 2]
cols gets second array → [1, 4, 1]

rows[0]=0, cols[0]=1 → Shop 1, Day 2 → value 4272 
rows[1]=0, cols[1]=4 → Shop 1, Day 5 → value 4926 
rows[2]=2, cols[2]=1 → Shop 3, Day 2 → value 4617  

print("Shop numbers:", rows + 1)
[1 1 3] ← Shop 1, Shop 1, Shop 3

print("Day numbers :", cols + 1)
[2 5 2] ← Day 2, Day 5, Day 2

visually

           Day1  Day2  Day3  Day4  Day5  Day6  Day7
Shop 1:   [1360  4272  3592   966  4926  3944  3671]
                  ↑                 ↑
              rows=0,cols=1    rows=0,cols=4

Shop 2:   [3419   630  2185  1269  2891  2933  1684]
          (nothing above 4000)

Shop 3:   [3885  4617  3404   974  1582  3058  2547]
                  ↑
              rows=2,cols=1

Shop 4:   [3247  1475  2306   689  3234  3505  2399]
          (nothing above 4000)
          
          
'''
# tasks set 3
np.random.seed(42)

# 1. Generate 100 response times
'''where mean is 200 and std is 40 ms 
formula=mean+std*np.....'''
response_times = 200 + 40 * np.random.randn(100)
print("Response times:\n", response_times)

# 2. Clip between 50 and 500ms
response_times = np.clip(response_times, 50, 500)

# 3. Average response time
print("Average  :", response_times.mean())

# 4. 90th percentile
p90 = np.percentile(response_times, 90)
print("P90      :", p90)

# 5. How many above 90th percentile
above_p90 = np.where(response_times > p90)[0].shape[0]
print("Above p90:", above_p90)

# 6. Fastest and slowest
print("Fastest  :", np.min(response_times))
print("Slowest  :", np.max(response_times))

# task set 4

np.random.seed(42)

questions = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Simulate exam question selection
print("choice\n",np.random.choice(questions,3))
# 1. Shuffle all questions
np.random.shuffle(questions)
print("shuffled\n",questions)
# 2. Pick 5 random questions for exam
print("choice\n",np.random.choice(questions,5))
# 3. Pick 3 questions without repetition
print("choice\n",np.random.choice(questions,3,replace=False))
# 4. Pick 3 questions with repetition allowed

print("choice\n",np.random.choice(questions,3,replace=True))


# task set 5
# 5 agents running for 7 days
# Each agent processes random requests (50-200)
# Each request has random success rate (0 to 1)
# 1. Create requests array (5 agents x 7 days)
# 2. Create success rate array (5 agents x 7 days)
requests=np.random.randint(50,200,[5,7])
print("req\n",requests)
success=np.random.rand(5,7)
print("success:\n",success)
# 3. Find most active agent (highest total requests)
total_requests=np.sum(requests,axis=1)
print("total:",total_requests)
print("highest total requests=\n",np.argmax(total_requests)+1)
# 4. Find most reliable agent (highest avg success rate)
reliable=np.mean(success,axis=1)
print("avg:",reliable)
print("reliable agent:",np.argmax(reliable)+1)


# 5. Find worst performing day (lowest avg success rate)
worst_performing_day=np.mean(success,axis=0)
print("worst performing day avg:",worst_performing_day)
print("worst day:",np.argmin(worst_performing_day)+1)
# 6. Find agents with average success rate above 0.7
avg_success_rate=np.mean(success,axis=1)
print("avg success rate:",avg_success_rate)
print("above 0.7 agents:",np.where(avg_success_rate>0.7)[0]+1)
# 7. Shuffle agents order randomly
np.random.shuffle(requests)
print(requests)