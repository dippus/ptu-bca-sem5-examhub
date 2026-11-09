# 📘 UNIT 2: Comprehensive Exam Notes — Programming in PHP (UGCA-1929)
**BCA Semester 5 | IKGPTU | External Exam: 60 Marks**  
> Specially prepared for **10-Mark Section B Questions** and **2-Mark Section A Definitions** (High-Yield Focus).

---

# 📑 TABLE OF CONTENTS
1. [🔴 SECTION A: High-Yield 2-Mark Questions & Answers](#-section-a-high-yield-2-mark-questions-all-repeated-pyqs)
2. [🌟 TOPIC 1 (10 Marks): PHP Arrays (Indexed, Associative, Multidimensional) & `foreach` Loop](#-topic-1-php-arrays--foreach-loop-10-marks--100-repeat)
3. [🌟 TOPIC 2 (10 Marks): User-Defined Functions (Pass by Value vs Reference & Default Args)](#-topic-2-user-defined-functions-in-php-10-marks)
4. [🌟 TOPIC 3 (10 Marks): High-Scoring University Programs (Palindrome & Sum of Evens)](#-topic-3-high-scoring-practical-programs-10-marks)

---

# 🔴 SECTION A: High-Yield 2-Mark Questions (All Repeated PYQs)

### Q1. What is the difference between `while()` and `do-while()` loops? *(Nov 2025)*
**Answer:**

| Parameter | `while()` Loop | `do-while()` Loop |
|---|---|---|
| **Type** | Entry-Controlled Loop. | Exit-Controlled Loop. |
| **Condition Check** | Condition is tested **before** entering the loop body. | Condition is tested **after** executing the loop body. |
| **Minimum Iterations** | Executes **0 times** if condition is initially false. | Guaranteed to execute **at least 1 time** even if condition is false. |

```php
// do-while executes at least once:
$x = 10;
do {
    echo $x; // Prints 10
} while ($x < 5);
```

---

### Q2. Mention two built-in string functions used for joining and splitting strings (`explode` vs `implode`). *(Nov 2024, Nov 2023)*
**Answer:**
1. **`explode(separator, string)`:** Splits a single string into an array based on a delimiter.
   * *Example:*
     ```php
     $str = "PHP,Java,Linux";
     $arr = explode(",", $str); // Returns array: ["PHP", "Java", "Linux"]
     ```
2. **`implode(separator, array)` / `join()`:** Joins elements of an array into a single combined string.
   * *Example:*
     ```php
     $colors = array("Red", "Green", "Blue");
     echo implode(" - ", $colors); // Output: Red - Green - Blue
     ```

---

### Q3. How do you traverse an associative array using `foreach()` loop? Write syntax and example. *(Nov 2024)*
**Answer:**
An associative array uses custom string keys. We traverse both keys and values using `foreach($array as $key => $value)`.

```php
<?php
$student = array("Name" => "Rahul", "Semester" => "5th", "City" => "Jalandhar");

foreach ($student as $key => $val) {
    echo "$key: $val <br>";
}
?>
```
* **Output:**
  ```text
  Name: Rahul
  Semester: 5th
  City: Jalandhar
  ```

---

### Q4. What is the purpose of Default Arguments in a PHP function? Give an example. *(Nov 2025)*
**Answer:**
* **Default Arguments** allow a function parameter to take a default fallback value if the caller does not pass an argument during the function invocation.
* Prevents "Missing argument" fatal errors and makes function calls flexible.

```php
<?php
function greetUser($name = "Guest") {
    echo "Hello, " . $name . "!<br>";
}

greetUser("Aman"); // Output: Hello, Aman!
greetUser();       // Output: Hello, Guest! (Default value used)
?>
```

---

### Q5. What is the difference between `strcmp()` and `strcasecmp()`?
**Answer:**
* **`strcmp($str1, $str2)`:** Performs a binary-safe, **case-sensitive** string comparison. Returns `0` if equal. (`strcmp("PHP", "php")` $\neq 0$).
* **`strcasecmp($str1, $str2)`:** Performs a binary-safe, **case-insensitive** string comparison. Returns `0` if equal. (`strcasecmp("PHP", "php")` evaluates to `0`).

---

### Q6. What is the Ternary Operator (`? :`) in PHP? Write its syntax.
**Answer:**
The ternary operator is a compact shorthand alternative to a basic `if-else` statement. It takes three operands:
* **Syntax:** `(condition) ? (value_if_true) : (value_if_false);`
* **Example:**
```php
<?php
$marks = 65;
$result = ($marks >= 40) ? "Pass" : "Fail";
echo $result; // Output: Pass
?>
```

---

### Q7. What are Variable Functions (Dynamic Functions) in PHP? *(Nov 2023)*
**Answer:**
* PHP supports variable functions: if a variable name has parentheses appended to it, PHP looks for a function whose name matches the string value stored inside that variable and executes it.
```php
<?php
function sayHello() {
    echo "Welcome to PHP!";
}

$funcName = "sayHello";
$funcName(); // Calls sayHello() -> Output: Welcome to PHP!
?>
```

---

# 🌟 TOPIC 1: PHP Arrays & `foreach` Loop [10 Marks — 100% REPEAT]

> ❓ **Repeated Exam Question:**  
> **"What is an Array in PHP? Explain Indexed, Associative, and Multidimensional arrays with suitable examples. Also explain how the `foreach` loop is used to traverse array elements."** *(Nov 2025, Nov 2024, Nov 2023)*

---

### 1. Introduction to Arrays in PHP
* **Definition:** An **Array** is a special compound variable that can store multiple values of different data types under a single variable name.
* In PHP, arrays are created using the `array()` constructor function or the short bracket syntax `[]`.
* Unlike traditional languages like C/Java, PHP arrays are dynamic, ordered maps that can hold heterogeneous data (integers, strings, floats, objects together).

---

### 2. Anatomy and Types of Arrays (3 Types)

```
                            PHP Arrays
       +------------------------+------------------------+
       |                        |                        |
[Indexed Array]        [Associative Array]     [Multidimensional Array]
- Numeric indices      - Named string keys     - Array inside an array
- Starts at index 0    - Key => Value pair     - Matrix / Grid format
```

#### A. Indexed Array (Numeric Index)
* Elements are indexed automatically with numeric numbers starting from index `0`.
```php
<?php
// Creating indexed array
$subjects = array("PHP", "Java", "Linux", "IoT");

// Accessing elements
echo $subjects[0]; // Output: PHP
echo $subjects[2]; // Output: Linux
?>
```

#### B. Associative Array (Named Keys)
* Uses user-defined strings as keys instead of sequential numbers. Uses the `=>` (fat arrow) operator to assign a value to a key.
```php
<?php
// Creating associative array
$studentMarks = array(
    "PHP"   => 85,
    "Java"  => 78,
    "Linux" => 90
);

// Accessing elements via named key
echo "Marks in PHP: " . $studentMarks["PHP"]; // Output: 85
?>
```

#### C. Multidimensional Array (Array of Arrays)
* An array containing one or more nested arrays. Used to represent tables, grids, and matrices.
```php
<?php
$students = array(
    array("Aman", 101, 88),
    array("Riya", 102, 92),
    array("Karan", 103, 75)
);

// Accessing: $array[row][column]
echo $students[0][0] . " scored " . $students[0][2] . " marks.";
// Output: Aman scored 88 marks.
?>
```

---

### 3. Traversal using `foreach` Loop

The `foreach` loop is designed specifically for traversing arrays without managing index counters or array boundaries manually.

#### Syntax 1: Value Only (For Indexed Arrays)
```php
foreach ($array as $value) {
    // Statement using $value
}
```

#### Syntax 2: Key and Value (For Associative Arrays)
```php
foreach ($array as $key => $value) {
    // Statement using both $key and $value
}
```

---

### 4. Complete Demonstration Program (Boxed Code)

```php
<?php
echo "<h3>1. Traversing Indexed Array:</h3>";
$colors = array("Crimson", "Emerald", "Sapphire");

foreach ($colors as $c) {
    echo "Color: " . $c . "<br>";
}

echo "<h3>2. Traversing Associative Array (Student Details):</h3>";
$student = array(
    "Roll No" => "BCA-501",
    "Name"    => "Vikram Singh",
    "Course"  => "BCA Semester 5",
    "Grade"   => "A+"
);

echo "<table border='1' cellpadding='5' cellspacing='0'>";
echo "<tr><th>Field</th><th>Value</th></tr>";

foreach ($student as $field => $val) {
    echo "<tr><td>$field</td><td>$val</td></tr>";
}
echo "</table>";
?>
```

#### Output Representation:
```text
1. Traversing Indexed Array:
Color: Crimson
Color: Emerald
Color: Sapphire

2. Traversing Associative Array:
+----------+----------------+
| Field    | Value          |
+----------+----------------+
| Roll No  | BCA-501        |
| Name     | Vikram Singh   |
| Course   | BCA Semester 5 |
| Grade    | A+             |
+----------+----------------+
```

---

# 🌟 TOPIC 2: User-Defined Functions in PHP [10 Marks]

> ❓ **Repeated Exam Question:**  
> **"What is a Function? Explain User-Defined Functions with syntax and return statements. Differentiate between Call by Value and Call by Reference with suitable demonstration code."**

---

### 1. Introduction & Syntax
* A **Function** is a self-contained, reusable block of statements that performs a specific task.
* Functions are not executed immediately upon page load; they are executed when called.
* **Basic Syntax:**
```php
function functionName($param1, $param2) {
    // Function body
    return $result; // Optional return statement
}
```

---

### 2. Pass by Value vs Pass by Reference (Comparison Table)

| Feature | Pass by Value (Default) | Pass by Reference (`&`) |
|---|---|---|
| **Mechanism** | A **copy** of the variable's value is passed to the function. | The **memory address / reference** of the variable is passed. |
| **Original Variable** | Original variable in the calling scope **remains unchanged**. | Changes made inside the function **directly modify the original variable**. |
| **Syntax** | Normal parameter syntax: `function modify($x)` | Uses ampersand (`&`) before parameter: `function modify(&$x)` |
| **Memory** | Uses extra memory to store variable copies. | Memory efficient because no copy is created. |

---

### 3. Demonstration Code: Value vs Reference

```php
<?php
// 1. Function using Pass by Value
function addTenValue($num) {
    $num = $num + 10;
    echo "Inside Function (Value): $num <br>";
}

// 2. Function using Pass by Reference (Notice the '&' sign)
function addTenRef(&$num) {
    $num = $num + 10;
    echo "Inside Function (Ref): $num <br>";
}

$original = 20;

echo "<b>--- Pass by Value Test ---</b><br>";
addTenValue($original);
echo "Original Variable after Value call: " . $original . "<br><br>"; // Still 20!

echo "<b>--- Pass by Reference Test ---</b><br>";
addTenRef($original);
echo "Original Variable after Ref call: " . $original . "<br>"; // Changed to 30!
?>
```

#### Output:
```text
--- Pass by Value Test ---
Inside Function (Value): 30
Original Variable after Value call: 20

--- Pass by Reference Test ---
Inside Function (Ref): 30
Original Variable after Ref call: 30
```

---

### 4. Default Arguments in Functions
If an argument is omitted during invocation, PHP assigns its predefined default value:
```php
<?php
function calculateDiscount($price, $discountPercent = 10) {
    $discount = ($price * $discountPercent) / 100;
    return $price - $discount;
}

echo "Final Price 1: " . calculateDiscount(1000, 20); // Uses 20% -> 800
echo "<br>";
echo "Final Price 2: " . calculateDiscount(1000);     // Uses default 10% -> 900
?>
```

---

# 🌟 TOPIC 3: High-Scoring Practical Programs [10 Marks]

*(In programs ko likhne par examiner seedha **10/10 marks** deta hai)*

### Program 1: Check if String or Number is a Palindrome *(Nov 2024)*
A Palindrome reads the same forwards and backwards (e.g., `"MADAM"`, `"121"`).

```php
<?php
function checkPalindrome($input) {
    // strrev() reverses a string in PHP
    $reversed = strrev($input);

    if ($input == $reversed) {
        return "<b>'$input'</b> is a Palindrome!";
    } else {
        return "<b>'$input'</b> is NOT a Palindrome.";
    }
}

// Test cases
echo checkPalindrome("madam") . "<br>"; // Palindrome
echo checkPalindrome("12321") . "<br>"; // Palindrome
echo checkPalindrome("college") . "<br>"; // Not Palindrome
?>
```

---

### Program 2: Sum of Only EVEN Numbers in an Array *(Nov 2023)*

```php
<?php
function sumEvenNumbers($numbers) {
    $evenSum = 0;

    foreach ($numbers as $val) {
        // Checking if divisible by 2
        if ($val % 2 == 0) {
            $evenSum += $val;
        }
    }
    return $evenSum;
}

// Array of integers
$data = array(12, 7, 18, 5, 20, 9, 4);

$result = sumEvenNumbers($data);
echo "Array Elements: " . implode(", ", $data) . "<br>";
echo "<b>Sum of Even Numbers (12 + 18 + 20 + 4): </b>" . $result;
?>
```

#### Output:
```text
Array Elements: 12, 7, 18, 5, 20, 9, 4
Sum of Even Numbers (12 + 18 + 20 + 4): 54
```

