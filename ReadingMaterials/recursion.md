## Recursion

Date: 15th November 2024 (Friday)

### **What is Recursion?**

Recursion is when a function (a block of code that does something) calls itself to solve a smaller piece of a problem.

Think of it like this:
- Imagine you’re climbing down a ladder with a bag of chocolates. Each time you step down, you eat one chocolate. When the bag is empty, you stop.

Recursion works the same way:
1. It keeps doing the same task (eating chocolates).
2. Stops when it reaches a condition (no chocolates left).

---

### **Important Parts of Recursion**
1. **Base Case**: The stopping point. Like when the bag is empty, stop eating chocolates.
2. **Recursive Case**: The repeated task. Like eating one chocolate and then checking the bag again.

---

### **How to Write a Recursive Function?**
A recursive function has two parts:
1. **Base Case**: What happens when we stop? (e.g., the bag is empty, return something simple).
2. **Recursive Call**: Solve a smaller piece of the problem.

---

### **Examples**

#### **1. Super Easy Example: Factorial**
**What is it?**  
Factorial of a number means multiplying all numbers from 1 to that number.  
For example:
- \( 4! = 4 \times 3 \times 2 \times 1 = 24 \)

**Python Code**
```python
def factorial(n):
    if n == 1:  # Base case: if the number is 1, stop
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call
```

**How it works?**
1. \( factorial(4) = 4 \times factorial(3) \)
2. \( factorial(3) = 3 \times factorial(2) \)
3. \( factorial(2) = 2 \times factorial(1) \)
4. \( factorial(1) = 1 \) (Stop here!)

---

#### **2. Easy Example: Sum of Numbers**
**What is it?**  
Add all numbers from 1 to \( n \).  
For example:
- \( sum(4) = 4 + 3 + 2 + 1 = 10 \)

**Python Code**
```python
def sum_numbers(n):
    if n == 0:  # Base case: if the number is 0, stop
        return 0
    else:
        return n + sum_numbers(n - 1)  # Recursive call
```

**How it works?**
1. \( sum(4) = 4 + sum(3) \)
2. \( sum(3) = 3 + sum(2) \)
3. \( sum(2) = 2 + sum(1) \)
4. \( sum(1) = 1 + sum(0) \)
5. \( sum(0) = 0 \) (Stop here!)

---

#### **3. Medium Example: Fibonacci Series**
**What is it?**  
Each number in the series is the sum of the two numbers before it.  
For example:
- \( 0, 1, 1, 2, 3, 5, 8, ... \)

**Python Code**
```python
def fibonacci(n):
    if n == 0:  # Base case 1
        return 0
    if n == 1:  # Base case 2
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive call
```

**How it works?**
1. \( fibonacci(4) = fibonacci(3) + fibonacci(2) \)
2. \( fibonacci(3) = fibonacci(2) + fibonacci(1) \)
3. \( fibonacci(2) = fibonacci(1) + fibonacci(0) \)

---

### **Try It Yourself**

#### **Problem Statement**
Write a recursive function to calculate the power of a number \( x^n \).  
For example:
- \( power(2, 3) = 2 \times 2 \times 2 = 8 \)
- \( power(5, 0) = 1 \)

**Hints for Writing the Code**
1. Base Case: If \( n = 0 \), return 1.
2. Recursive Case: Multiply \( x \) by \( power(x, n-1) \).

---

**Pro Tip for Beginners**  
If you get stuck:
1. Write down the steps on paper.
2. Follow the numbers going smaller until you hit the base case.

