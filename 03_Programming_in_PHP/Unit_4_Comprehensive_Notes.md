# 📘 UNIT 4: Comprehensive Exam Notes — Programming in PHP (UGCA-1929)
**BCA Semester 5 | IKGPTU | External Exam: 60 Marks**  
> Specially prepared for **10-Mark Section B Questions** and **2-Mark Section A Definitions** (High-Yield Focus).

---

# 📑 TABLE OF CONTENTS
1. [🔴 SECTION A: High-Yield 2-Mark Questions & Answers](#-section-a-high-yield-2-mark-questions-all-repeated-pyqs)
2. [🌟 TOPIC 1 (10 Marks): Connecting PHP with MySQL & Displaying Records in HTML Table](#-topic-1-mysql-connectivity--display-in-html-table-10-marks--100-repeat)
3. [🌟 TOPIC 2 (10 Marks): Full CRUD Operations in PHP & MySQL (Insert, Update, Delete)](#-topic-2-full-crud-operations-in-php--mysql-10-marks)
4. [🌟 TOPIC 3 (10 Marks): Fetching Functions, Security & mysqli vs PDO](#-topic-3-fetching-functions-security--mysqli-vs-pdo-10-marks)

---

# 🔴 SECTION A: High-Yield 2-Mark Questions (All Repeated PYQs)

### Q1. What is `mysqli_connect()`? Write its syntax and parameters. *(Nov 2025, 2024, 2023)*
**Answer:**
* `mysqli_connect()` is a built-in PHP function used to establish an active connection between the PHP script and a MySQL database server.
* **Syntax:**
  ```php
  $conn = mysqli_connect(hostname, username, password, database_name, [port]);
  ```
* **Example:**
  ```php
  $conn = mysqli_connect("localhost", "root", "", "university_db");
  if (!$conn) {
      die("Connection Failed: " . mysqli_connect_error());
  }
  ```

---

### Q2. What is the difference between `mysqli_fetch_assoc()` and `mysqli_fetch_array()`? *(Nov 2025, 2024)*
**Answer:**

| Feature | `mysqli_fetch_assoc()` | `mysqli_fetch_array()` |
|---|---|---|
| **Return Array Type** | Returns an **Associative array only** (column names as keys). | Returns **both Associative and Numeric** indexed arrays (dual format). |
| **Element Access** | Accessed only by column name: `$row['name']`. | Accessed by name or index: `$row['name']` OR `$row[1]`. |
| **Memory Consumption** | Uses significantly less RAM (lightweight & clean). | Consumes approximately double memory per row fetched. |
| **Recommended Usage** | Industry standard for readable, self-documenting code. | Used only when column ordering index is strictly needed. |

---

### Q3. What is the purpose of `mysqli_error()` and `die()` functions?
**Answer:**
* **`mysqli_error($conn)`:** Returns a descriptive string containing the exact MySQL error message produced by the most recent database operation.
* **`die("message")` / `exit()`:** Prints the passed error message to the screen and **immediately halts** further PHP script execution, preventing corrupt operations.

---

### Q4. What does `mysqli_query()` return for `SELECT` vs `INSERT` queries?
**Answer:**
* For **`SELECT`** queries: Returns a `mysqli_result` object containing the fetched dataset on success, or `false` on failure.
* For **`INSERT`, `UPDATE`, `DELETE`** queries: Returns a boolean `true` on success, or `false` on failure.

---

### Q5. How do you find the total number of rows returned by a query?
**Answer:**
Using the built-in function **`mysqli_num_rows($result)`**.
```php
$result = mysqli_query($conn, "SELECT * FROM students");
$totalStudents = mysqli_num_rows($result);
echo "Total Records Found: " . $totalStudents;
```

---

# 🌟 TOPIC 1: MySQL Connectivity & Display in HTML Table [10 Marks — 100% REPEAT]

> ❓ **Repeated Exam Question:**  
> **"Explain the complete procedure for connecting PHP with a MySQL database. Write a PHP script with proper error handling to retrieve all records from a `students` table (`roll_no`, `name`, `course`, `marks`) and display them inside an aesthetically formatted HTML table."** *(Nov 2025, Nov 2024, Nov 2023)*

---

### 1. Database Connectivity Architecture (Boxed Diagram)

```
  +------------------+                    +-------------------------+
  |    PHP Script    |                    |      MySQL Database     |
  | (Apache Server)  |                    |       (Port 3306)       |
  +------------------+                    +-------------------------+
           |                                           |
           |  1. mysqli_connect(host, user, pass, db)  |
           | ----------------------------------------> |
           |  Connection Resource Link ($conn)         |
           | <---------------------------------------- |
           |                                           |
           |  2. mysqli_query($conn, "SELECT * ...")   |
           | ----------------------------------------> |
           |  Result Set Object ($result)              |
           | <---------------------------------------- |
           |                                           |
           |  3. while($row = mysqli_fetch_assoc())    |
           |  Iterates through each database record    |
           |                                           |
           |  4. Dynamically generates <tr><td>        |
           v                                           v
  +-----------------------------------------------------------------+
  |        HTML Web Page Rendered to Client with Data Table         |
  +-----------------------------------------------------------------+
```

---

### 2. Four-Step Database Procedure
1. **Establish Connection:** Call `mysqli_connect()` with server credentials.
2. **Execute SQL Query:** Send query string to MySQL server using `mysqli_query()`.
3. **Fetch & Traverse Records:** Use a `while` loop with `mysqli_fetch_assoc($result)` to retrieve records row-by-row.
4. **Close Connection:** Always release database resources using `mysqli_close($conn)`.

---

### 3. Complete Working Script (Exam-Ready Code)

```php
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>BCA Student Records Portal</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 30px; }
        table { width: 80%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #cbd5e1; padding: 12px; text-align: left; }
        th { background-color: #4f46e5; color: white; }
        tr:nth-child(even) { background-color: #f8fafc; }
        tr:hover { background-color: #e2e8f0; }
        .badge { padding: 4px 8px; border-radius: 4px; font-weight: bold; }
        .pass { background: #d1fae5; color: #065f46; }
        .fail { background: #fee2e2; color: #991b1b; }
    </style>
</head>
<body>

<h2>🎓 University Student Directory (BCA Sem 5)</h2>

<?php
// Step 1: Database Configuration & Connection
$host = "localhost";
$user = "root";
$pass = "";
$db   = "university_db";

$conn = mysqli_connect($host, $user, $pass, $db);

// Checking connection with detailed error reporting
if (!$conn) {
    die("<p style='color:red;'><b>Database Connection Failed:</b> " . mysqli_connect_error() . "</p>");
}

// Step 2: Prepare and Execute SELECT Query
$sql = "SELECT roll_no, name, course, marks FROM students ORDER BY roll_no ASC";
$result = mysqli_query($conn, $sql);

// Step 3: Check if records exist and generate HTML Table
if (mysqli_num_rows($result) > 0) {
    echo "<table>";
    echo "<thead>
            <tr>
                <th>Roll No</th>
                <th>Student Name</th>
                <th>Course</th>
                <th>Marks</th>
                <th>Status</th>
            </tr>
          </thead>";
    echo "<tbody>";

    // Loop through each row of the dataset
    while ($row = mysqli_fetch_assoc($result)) {
        $statusBadge = ($row['marks'] >= 40) 
            ? "<span class='badge pass'>PASS</span>" 
            : "<span class='badge fail'>FAIL</span>";

        echo "<tr>";
        echo "<td>" . $row['roll_no'] . "</td>";
        echo "<td><b>" . htmlspecialchars($row['name']) . "</b></td>";
        echo "<td>" . $row['course'] . "</td>";
        echo "<td>" . $row['marks'] . " / 100</td>";
        echo "<td>" . $statusBadge . "</td>";
        echo "</tr>";
    }

    echo "</tbody>";
    echo "</table>";
    echo "<p><i>Total Records Displayed: " . mysqli_num_rows($result) . "</i></p>";
} else {
    echo "<p>No student records found in the database.</p>";
}

// Step 4: Free result set and close connection
mysqli_free_result($result);
mysqli_close($conn);
?>

</body>
</html>
```

---

# 🌟 TOPIC 2: Full CRUD Operations in PHP & MySQL [10 Marks]

> ❓ **Repeated Exam Question:**  
> **"What does CRUD stand for? Write complete PHP scripts to perform INSERT and UPDATE operations in a MySQL database using form inputs."** *(Nov 2025, Nov 2024)*

CRUD stands for:
* **C** — **Create** (`INSERT INTO table_name ...`)
* **R** — **Read** (`SELECT * FROM table_name ...`)
* **U** — **Update** (`UPDATE table_name SET col = val WHERE condition`)
* **D** — **Delete** (`DELETE FROM table_name WHERE condition`)

---

### Part 1: INSERT Operation Script (`insert.php`)

```php
<!DOCTYPE html>
<html>
<body>
<h3>Add New Student Record</h3>

<form method="POST">
    Roll No: <input type="number" name="roll_no" required><br><br>
    Name:    <input type="text" name="name" required><br><br>
    Course:  <input type="text" name="course" required><br><br>
    Marks:   <input type="number" name="marks" required><br><br>
    <input type="submit" name="submit_btn" value="Save Record">
</form>

<?php
if (isset($_POST['submit_btn'])) {
    $conn = mysqli_connect("localhost", "root", "", "university_db");
    if (!$conn) { die("DB Connection Error: " . mysqli_connect_error()); }

    $roll   = (int)$_POST['roll_no'];
    $name   = mysqli_real_escape_string($conn, $_POST['name']);
    $course = mysqli_real_escape_string($conn, $_POST['course']);
    $marks  = (int)$_POST['marks'];

    $sql = "INSERT INTO students (roll_no, name, course, marks) 
            VALUES ($roll, '$name', '$course', $marks)";

    if (mysqli_query($conn, $sql)) {
        echo "<p style='color:green;'>✅ Record inserted successfully!</p>";
    } else {
        echo "<p style='color:red;'>❌ Insertion Error: " . mysqli_error($conn) . "</p>";
    }

    mysqli_close($conn);
}
?>
</body>
</html>
```

---

### Part 2: UPDATE Operation Script (`update.php`)

```php
<?php
$conn = mysqli_connect("localhost", "root", "", "university_db");
if (!$conn) { die("Connection Failed: " . mysqli_connect_error()); }

if (isset($_POST['update_btn'])) {
    $roll     = (int)$_POST['roll_no'];
    $newMarks = (int)$_POST['new_marks'];

    $sql = "UPDATE students SET marks = $newMarks WHERE roll_no = $roll";

    if (mysqli_query($conn, $sql)) {
        if (mysqli_affected_rows($conn) > 0) {
            echo "<p style='color:green;'>✅ Marks updated successfully!</p>";
        } else {
            echo "<p style='color:orange;'>⚠️ No record matched Roll No: $roll.</p>";
        }
    } else {
        echo "<p style='color:red;'>❌ Update Failed: " . mysqli_error($conn) . "</p>";
    }
}
?>

<form method="POST">
    <h3>Update Student Marks</h3>
    Enter Roll No to Update: <input type="number" name="roll_no" required><br><br>
    Enter New Marks:         <input type="number" name="new_marks" required><br><br>
    <input type="submit" name="update_btn" value="Update Marks">
</form>
```

---

### Part 3: DELETE Operation Script (`delete.php`)

```php
<?php
$conn = mysqli_connect("localhost", "root", "", "university_db");

if (isset($_GET['roll_no'])) {
    $roll = (int)$_GET['roll_no'];

    $sql = "DELETE FROM students WHERE roll_no = $roll";

    if (mysqli_query($conn, $sql)) {
        echo "<p style='color:green;'>✅ Student record deleted successfully.</p>";
    } else {
        echo "<p style='color:red;'>❌ Delete Error: " . mysqli_error($conn) . "</p>";
    }
}
mysqli_close($conn);
?>
```

---

# 🌟 TOPIC 3: Fetching Functions, Security & mysqli vs PDO [10 Marks]

### 1. Comparison: MySQLi vs PDO (PHP Data Objects)

| Feature | MySQLi Extension | PDO (PHP Data Objects) |
|---|---|---|
| **Database Support** | Works **only** with MySQL / MariaDB databases. | Works with **12 different database drivers** (MySQL, Oracle, PostgreSQL, MS SQL). |
| **Programming Paradigm**| Supports both Procedural and Object-Oriented APIs. | Strictly Object-Oriented API. |
| **Prepared Statements** | Supported (using `mysqli_stmt_bind_param()`). | Supported with named parameters (`:name`). |
| **Performance** | Marginally faster specifically with MySQL. | Slightly slower abstraction layer, but portable. |

---

### 2. SQL Injection & Prepared Statements Prevention

* **SQL Injection:** A critical security vulnerability where malicious SQL query segments are injected into application input fields (e.g., `' OR '1'='1`).
* **Prevention via Prepared Statements:** Separates SQL command logic from user-supplied parameters, completely neutralizing injection risks.

```php
<?php
$conn = mysqli_connect("localhost", "root", "", "university_db");

// 1. Prepare template with '?' placeholders
$stmt = mysqli_prepare($conn, "SELECT * FROM students WHERE roll_no = ? AND course = ?");

// 2. Bind parameters ('i' = integer, 's' = string)
$roll = 101;
$course = "BCA Sem-5";
mysqli_stmt_bind_param($stmt, "is", $roll, $course);

// 3. Execute securely
mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);

while ($row = mysqli_fetch_assoc($result)) {
    echo "Student: " . $row['name'];
}

mysqli_stmt_close($stmt);
mysqli_close($conn);
?>
```

