# 📘 UNIT 1: Comprehensive Exam Notes — Programming in PHP (UGCA-1929)
**BCA Semester 5 | IKGPTU | External Exam: 60 Marks**  
> Specially prepared for **10-Mark Section B Questions** and **2-Mark Section A Definitions**.

---

# 📑 TABLE OF CONTENTS
1. [Core 10-Mark Question 1: PHP Introduction, Architecture, Client vs Server & Features](#-topic-1-php-architecture-working-mechanism--features-10-marks)
2. [Core 10-Mark Question 2: Variables, Data Types & Scope (Local, Global, Static)](#-topic-2-variables-data-types--variable-scope-10-marks)
3. [Core 10-Mark Question 3: Operators & Control Flow Structures](#-topic-3-operators--control-structures-in-php-10-marks)
4. [Section A Booster: 2-Mark Quick Definitions & FAQs](#-section-a-booster-2-mark-definitions--faqs)

---

# 🌟 TOPIC 1: PHP Architecture, Working Mechanism & Features [10 Marks]

### 1. Introduction to PHP
* **Definition:** **PHP** stands for **Hypertext Preprocessor** (originally *Personal Home Page*).
* It is an **open-source, server-side, interpreted scripting language** designed specifically for web development to create dynamic and data-driven web pages.
* PHP files have the extension `.php` and can contain standard HTML tags, CSS styles, JavaScript, and PHP scripts enclosed within standard tags: `<?php ... ?>`.

---

### 2. Client-Side Scripting vs Server-Side Scripting

| Comparison Parameter | Client-Side Scripting (e.g., JavaScript) | Server-Side Scripting (e.g., PHP) |
|---|---|---|
| **Execution Environment** | Runs locally on the client's Web Browser. | Runs remotely on the Web Server (Apache/Nginx). |
| **Source Code Security** | Code is completely visible via "View Page Source". | Code is completely hidden; only generated output is sent. |
| **Database Connectivity** | Cannot directly query backend databases. | Natively connects to MySQL, PostgreSQL, Oracle, etc. |
| **Primary Use Cases** | Form validation, UI animations, DOM updates. | Business logic, authentication, database CRUD, sessions. |
| **Server Resource Usage** | Relies on the client machine; zero server overhead. | Uses server CPU, memory, and database connections. |

---

### 3. Architecture & Working Flow of PHP

#### A. Architecture Diagram
```
  +------------------+
  |  Client Browser  |
  +------------------+
         |  ▲
    (1)  |  |  (5) HTTP Response
    HTTP |  |      (Plain HTML + CSS)
 Request |  |
         v  |
  +-----------------------------------------------------------+
  |                        WEB SERVER                         |
  |                    (e.g., Apache/IIS)                     |
  |                                                           |
  |    (2) Identifies .php file -> Routes to PHP Engine       |
  |                                                           |
  |          +--------------------------------------+         |
  |          |              PHP ENGINE              |         |
  |          |    - Zend Engine / Lexer & Parser    |         |
  |          |    - Executes Business Logic         |         |
  |          +--------------------------------------+         |
  |                             |                             |
  |                         (3) | Executes SQL Query          |
  |                             v                             |
  |                  +----------------------+                 |
  |                  |    MySQL Database    |                 |
  |                  +----------------------+                 |
  |                                                           |
  |    (4) Translates dynamic results into standard HTML      |
  +-----------------------------------------------------------+
```

#### B. Step-by-Step Processing Flow:
1. **HTTP Request:** The user types a URL (e.g., `http://localhost/test.php`) in their web browser and presses enter.
2. **Server Inspection:** The Apache Web Server intercepts the request, notes the `.php` extension, and forwards the file to the **PHP Engine (Zend Engine)**.
3. **Execution & Database Access:** The PHP engine compiles the script to opcode and executes it line-by-line. It reads cookies, manages sessions, and queries the database as instructed.
4. **HTML Generation:** The engine merges dynamic data into pure **HTML/CSS/JS**.
5. **HTTP Response:** The web server sends the clean HTML output back to the client browser. The browser renders the web page without seeing a single line of raw PHP code.

---

### 4. Embedding PHP in HTML (Syntax & Working Example)

PHP code can be embedded anywhere within an HTML file using standard PHP tags:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Dynamic PHP Page</title>
</head>
<body>
    <h1>Welcome to BCA Semester 5</h1>

    <?php
        // Defining variables
        $subjectName = "Programming in PHP";
        $subjectCode = "UGCA-1929";
        $examDate = "11-Nov-2026";

        // Generating dynamic output
        echo "<p><b>Subject:</b> " . $subjectName . " (" . $subjectCode . ")</p>";
        echo "<p><b>Scheduled Date:</b> " . $examDate . "</p>";
    ?>
</body>
</html>
```

---

### 5. Salient Features of PHP
1. **Open Source & Free:** Completely free to download, use, and update without recurring license fees.
2. **Platform Independence (Cross-Platform):** Runs flawlessly across Windows, Linux, Unix, and macOS environments.
3. **Robust Database Support:** Provides native extensions for MySQL (`mysqli`, `PDO`), PostgreSQL, SQLite, and Oracle.
4. **High Speed & Concurrency:** Executes as an Apache module inside memory, providing faster execution than CGI scripts.
5. **Session & Cookie Handling:** Includes robust built-in state management via `$_SESSION` and `$_COOKIE`.
6. **Case Sensitivity Conventions:**
   * **Variables:** Are strictly **case-sensitive** (`$value` ≠ `$Value`).
   * **Keywords and Functions:** Are **case-insensitive** (`echo`, `ECHO`, `Echo` behave identically).

---

### 6. Development Environment & Requirements (XAMPP / WAMP / LAMP)
To run PHP server-side scripts locally, a full web stack is required:

* **Hardware Requirements:**
  * Minimum 1 GHz Processor (x86/x64).
  * 1 GB RAM (2 GB+ recommended).
  * 500 MB free hard disk space for server stack.
* **Software Requirements (The Web Stack):**
  * **Operating System:** Windows, Linux, or macOS.
  * **Web Server:** Apache HTTP Server or Nginx.
  * **PHP Engine:** PHP 7.x / 8.x parser.
  * **Database:** MySQL / MariaDB.
* **All-in-One Local Packages:**
  * **WAMP:** Windows, Apache, MySQL, PHP.
  * **LAMP:** Linux, Apache, MySQL, PHP.
  * **XAMPP:** Cross-Platform (X), Apache, MariaDB/MySQL, PHP, Perl.
  * *Execution Path:* Files are placed in the web document root (e.g., `C:/xampp/htdocs/` or `/var/www/html/`) and accessed in the browser via `http://localhost/filename.php`.

---

# 🌟 TOPIC 2: Variables, Data Types & Variable Scope [10 Marks]

### 1. Variables in PHP
* A variable is a named memory location used to store data values during execution.
* In PHP, variables always start with a dollar symbol (`$`).
* **Rules for Naming Variables:**
  1. Must start with a `$` followed by a letter (`a-z`, `A-Z`) or underscore (`_`).
  2. Cannot start with a numeric digit (e.g., `$1name` is **invalid**).
  3. Can contain only alphanumeric characters and underscores (`$user_name`, `$roll10`).
  4. Variable names are **case-sensitive** (`$age` is different from `$Age`).
  5. PHP is **loosely typed**; variables do not need explicit data type declarations before assignment.

---

### 2. Data Types in PHP
PHP supports 8 basic data types categorized into 3 categories:

| Category | Data Type | Description | Example |
|---|---|---|---|
| **Scalar Types** | `Integer` | Whole numbers without decimals | `$count = 45;` |
| | `Float / Double` | Numbers containing decimal points | `$price = 99.75;` |
| | `String` | Sequence of characters inside quotes | `$msg = "Hello World";` |
| | `Boolean` | Stores either `TRUE` or `FALSE` | `$is_valid = true;` |
| **Compound Types** | `Array` | Holds multiple values in a single variable | `$colors = array("Red", "Blue");` |
| | `Object` | Instance of a user-defined class | `$car = new Car();` |
| **Special Types** | `NULL` | Variable explicitly assigned no value | `$result = NULL;` |
| | `Resource` | Special pointer holding external references | `$file = fopen("data.txt", "r");` |

---

### 3. Type Checking & Type Casting (Testing & Changing Types)

#### A. Displaying Type Information & Testing Data Types
PHP provides built-in functions to inspect and test variable types at runtime:
* `gettype($var)`: Returns the string representation of the variable type (e.g., `"integer"`, `"string"`).
* `var_dump($var)`: Dumps structured information about a variable, including its type and value.
* **Testing Functions (Boolean Return):**
  * `is_int($var)` / `is_integer($var)`: Returns `true` if variable is an integer.
  * `is_string($var)`: Returns `true` if variable is a string.
  * `is_float($var)`: Returns `true` if variable is a float/double.
  * `is_bool($var)`: Returns `true` if variable is boolean.
  * `is_array($var)`: Returns `true` if variable is an array.

```php
<?php
$val = 125;
echo gettype($val); // Output: integer

if (is_int($val)) {
    echo "$val is an Integer";
}
?>
```

#### B. Type Casting & `settype()` (Changing Types)
1. **Explicit Casting (C-Style Casting):** Converts the value temporarily using casting operators like `(int)`, `(float)`, `(string)`, `(bool)`, `(array)`.
```php
<?php
$price = "450.50";         // String
$intPrice = (int)$price;   // Converted to Integer 450
?>
```

2. **Using `settype()` Function:** Permanently modifies the original variable's type.
```php
<?php
$score = "95";
settype($score, "integer"); // Permanently changed from string to integer
echo gettype($score);        // Output: integer
?>
```

---

### 4. Dynamic Variables / Variable Variables (`$$var`)
* A **dynamic variable** (or variable variable) takes the *value* of one variable and treats that value as the *name* of a new variable.
* It uses two dollar signs: `$$`.

```php
<?php
$greeting = "welcome";
$$greeting = "Welcome to BCA Exam Preparation!";

// Now $welcome has been created dynamically!
echo $greeting;  // Output: welcome
echo $welcome;   // Output: Welcome to BCA Exam Preparation!
echo $$greeting; // Output: Welcome to BCA Exam Preparation!
?>
```

---

### 5. Variable Scope in PHP
Scope refers to the context within which a variable is accessible and valid. PHP has three primary variable scopes:

#### A. Local Scope
* A variable declared **inside a function** has local scope.
* It is created when the function starts and destroyed when the function exits.
* It cannot be accessed outside the function.

```php
<?php
function testLocal() {
    $localVar = 50; // Local Scope
    echo "Inside Function: " . $localVar . "<br>";
}
testLocal();
// echo $localVar; // Fatal Error: Undefined variable
?>
```

#### B. Global Scope
* A variable declared **outside all functions** has global scope.
* It can be accessed directly outside functions, but **NOT** automatically inside functions.
* To access a global variable inside a function, use the `global` keyword or the `$GLOBALS['varName']` superglobal array.

```php
<?php
$globalNum = 100; // Global Scope

function testGlobal() {
    global $globalNum; // Accessing global variable inside function
    echo "Inside Function: " . $globalNum . "<br>";
}
testGlobal();
echo "Outside Function: " . $globalNum;
?>
```

#### C. Static Scope
* Normally, local variables are destroyed when a function finishes execution.
* When a variable is defined with the `static` keyword, it **retains its value** across multiple successive function calls.

```php
<?php
function counter() {
    static $count = 0; // Static variable initialized only once
    $count++;
    echo "Count: " . $count . "<br>";
}

counter(); // Output: Count: 1
counter(); // Output: Count: 2
counter(); // Output: Count: 3
?>
```

---

### 4. Constants in PHP
* A constant is an identifier whose value cannot change during script execution.
* Constants do not use a `$` sign and are globally accessible across the entire script.
* **Defined using:**
  1. `define(name, value)`: Standard procedural definition.
  2. `const NAME = value`: Modern compile-time definition.

```php
<?php
define("SITE_TITLE", "BCA Exam Portal");
const PASS_MARKS = 40;

echo SITE_TITLE;  // Output: BCA Exam Portal
echo PASS_MARKS;   // Output: 40
?>
```

---

# 🌟 TOPIC 3: Operators & Control Structures in PHP [10 Marks]

### 1. Categories of Operators in PHP
1. **Arithmetic:** `+`, `-`, `*`, `/`, `%` (Modulus), `**` (Exponentiation)
2. **Assignment:** `=`, `+=`, `-=`, `*=`, `/=`, `%=`
3. **Comparison:** `==` (Value match), `===` (Value + Type match/Identical), `!=`, `<>`, `!==`, `>`, `<`, `>=`, `<=`
4. **Logical:** `&&` (And), `||` (Or), `!` (Not), `and`, `or`, `xor`
5. **Increment / Decrement:** `++$x` (Pre), `$x++` (Post), `--$x`, `$x--`
6. **String Concatenation:** `.` (Dot operator) and `.=` (Concatenate-assignment)

---

### 2. Conditional / Decision-Making Statements

#### A. If-Else Ladder
Used to evaluate multiple conditions in sequence.

```php
<?php
$marks = 78;

if ($marks >= 80) {
    echo "Grade: A+";
} elseif ($marks >= 60) {
    echo "Grade: A";
} elseif ($marks >= 40) {
    echo "Grade: B (Pass)";
} else {
    echo "Grade: F (Fail)";
}
?>
```

#### B. Switch-Case Statement
Alternative to long if-else ladders for testing an expression against multiple discrete values.

```php
<?php
$day = "Wed";

switch ($day) {
    case "Mon":
        echo "Start of work week.";
        break;
    case "Wed":
        echo "PHP University Exam Day!";
        break;
    case "Sun":
        echo "Holiday.";
        break;
    default:
        echo "Normal weekday.";
        break;
}
?>
```

---

### 3. Iteration / Looping Statements

#### A. `while` Loop (Entry-Controlled)
Executes a block of code as long as the test condition remains true.
```php
<?php
$i = 1;
while ($i <= 5) {
    echo "Step: $i <br>";
    $i++;
}
?>
```

#### B. `do-while` Loop (Exit-Controlled)
Guarantees at least one execution of the loop block before evaluating the condition.
```php
<?php
$i = 10;
do {
    echo "Value is: $i <br>";
    $i++;
} while ($i <= 5); // Condition fails, but prints once
?>
```

#### C. `for` Loop
Used when the number of iterations is known in advance.
```php
<?php
for ($num = 1; $num <= 5; $num++) {
    echo "Square of $num is: " . ($num * $num) . "<br>";
}
?>
```

---

# ⚡ SECTION A BOOSTER: 2-Mark Definitions & FAQs

### Q1. What is PHP and who created it?
**Ans:** PHP (Hypertext Preprocessor) is an open-source, server-side scripting language used to build dynamic web applications. It was created by **Rasmus Lerdorf** in 1994.

### Q2. What is the difference between `echo` and `print`?
**Ans:**
* `echo` has no return value, is slightly faster, and can take multiple comma-separated arguments.
* `print` returns a value of `1` (can be used inside expressions) and accepts only a single argument.

### Q3. What is the difference between `==` and `===` in PHP?
**Ans:**
* `==` (Equal): Checks only value equality after type coercion (`"10" == 10` evaluates to `true`).
* `===` (Identical): Checks both **value AND data type** without conversion (`"10" === 10` evaluates to `false`).

### Q4. What are PHP Superglobals?
**Ans:** Built-in predefined arrays that are globally available throughout a script regardless of scope.  
**Examples:** `$_GET`, `$_POST`, `$_SESSION`, `$_COOKIE`, `$_SERVER`, `$_FILES`, `$_REQUEST`, `$GLOBALS`.

### Q5. What is the output of `<?php $x = 5; echo ++$x + $x++; ?>`?
**Ans:**
* `++$x` pre-increments `$x` to `6` and returns `6`.
* `$x++` uses current value `6` for addition, then increments `$x` to `7`.
* Total Output: `6 + 6 = 12`.

