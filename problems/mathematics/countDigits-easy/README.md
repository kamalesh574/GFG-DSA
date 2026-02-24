# 📌 Count Digits

## 🧠 Problem Statement

Given an integer `n`, return the total number of digits present in the number.

---

## 🧩 Examples

### Example 1

**Input:**
```
n = 12345
```

**Output:**
```
5
```

---

### Example 2

**Input:**
```
n = 7
```

**Output:**
```
1
```

---

### Example 3

**Input:**
```
n = 0
```

**Output:**
```
1
```

---

# 💡 Approach 1 — Iterative Method

## 🔹 Idea

Keep dividing the number by `10` until it becomes `0`.  
Each division removes one digit.

Example:

```
12345 → 1234 → 123 → 12 → 1 → 0
```

Each step counts as one digit.

---

## 🧪 Java Code (Iterative)

```java
class Solution {
    public int countDigits(int n) {
        
        // Base case
        if (n == 0)
            return 1;
        
        int count = 0;
        
        while (n != 0) {
            n = n / 10;
            count++;
        }
        
        return count;
    }
}
```

### ⏱ Complexity

- **Time:** O(log₁₀ n)  
- **Space:** O(1)

---

# 💡 Approach 2 — Recursive Method

## 🔹 Idea

Each recursive call removes one digit by dividing by `10`  
and adds `1` to the result

---

## 🧪 Java Code (Recursive)

```java
class Solution {
    public int countDigits(int n) {
        
        // Base case
        if (n / 10 == 0)
            return 1;
        
        // Recursive call
        return 1 + countDigits(n / 10);
    }
}
```

---

## 🔍 Recursion Flow Example

```
countDigits(3456)
= 1 + countDigits(345)
= 1 + (1 + countDigits(34))
= 1 + (1 + (1 + countDigits(3)))
= 1 + 1 + 1 + 1
= 4
```

### ⏱ Complexity

- **Time:** O(log₁₀ n)  
- **Space:** O(log₁₀ n) (due to recursion stack)

---

# 💡 Approach 3 — Logarithmic (Mathematical) Method

## 🔹 Formula

```
Number of digits = ⌊ log₁₀(n) ⌋ + 1
```

### Why this works:

- `log₁₀(n)` gives the highest power of 10 in `n`
- Taking `floor` gives digit position
- Adding `1` gives total number of digits

---

## ⚠️ Edge Case

If `n == 0`, return `1`.

---

## 🧪 Java Code (Logarithmic)

```java
class Solution {
    public int countDigits(int n) {
        
        if (n == 0)
            return 1;
        
        return (int) Math.floor(Math.log10(n) + 1);
    }
}
```

---

### ⏱ Complexity

- **Time:** O(1)  
- **Space:** O(1)

---

# 🆚 Approach Comparison

| Approach      | Time Complexity | Space Complexity | Notes |
|--------------|----------------|----------------|-------|
| Iterative    | O(log n)       | O(1)           | Simple and safe |
| Recursive    | O(log n)       | O(log n)       | Uses recursion stack |
| Logarithmic  | O(1)           | O(1)           | Most optimized mathematically |

---

# 🎯 Key Learnings

- Digit removal using division  
- Recursive problem breakdown  
- Using logarithmic math for optimization  
- Comparing algorithm efficiency  
- Handling edge cases properly  

---

## 🏷 Topic
Mathematics
