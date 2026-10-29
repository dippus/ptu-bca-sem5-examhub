# ⚡ LAST DAY REVISION — Programming in PHP (UGCA-1929)
**BCA Sem 5 | IKGPTU | 60 Marks External**
> 🔥 Read this once. Attempt everything. Pass guaranteed.

---

## 📌 TOP 15 DEFINITIONS (3-4 lines each)

**1. PHP**
- Server-side scripting language. Open-source. Embedded in HTML using `<?php ?>`.
- Runs on web server (Apache/Nginx). Output sent to browser as plain HTML.
- Used to build dynamic websites, handle forms, manage databases.

**2. Variable**
- Named memory location. Declared with `$`. E.g., `$name = "Rahul";`
- Case-sensitive. Starts with `$` + letter/underscore. No spaces allowed.
- PHP is loosely typed — no need to declare data type.

**3. Variable Scope**
- **Local**: Inside function only. **Global**: Outside functions.
- Use `global $var;` inside function to access global variable.
- **Static**: `static $x = 0;` — retains value between function calls.

**4. Constant**
- Value that cannot change once defined.
- Defined with `define("PI", 3.14);` or `const PI = 3.14;`
- No `$` sign. Accessible anywhere (global scope automatically).

**5. Array**
- Variable that stores multiple values. Three types: Indexed, Associative, Multidimensional.
- Indexed: `$arr = array(10,20,30);` | Assoc: `$arr = array("key"=>"val");`
- Access: `$arr[0]` or `$arr["key"]`

**6. foreach Loop**
- Designed specifically for arrays. Iterates over each element.
- Syntax: `foreach($arr as $val)` or `foreach($arr as $key => $val)`
- No need to track index manually.

**7. User-Defined Function**
- Block of reusable code. Defined with `function` keyword.
- Can accept parameters and return values using `return`.
- Types: Pass by value (copy), Pass by reference (`&$param`), Default parameters.

**8. $_GET**
- Superglobal. Collects form data sent via URL (GET method).
- Data visible in URL. Max ~255 characters. Less secure.
- Access: `$_GET["fieldname"]`

**9. $_POST**
- Superglobal. Collects form data sent in HTTP body (POST method).
- Data NOT visible in URL. More secure. No size limit.
- Access: `$_POST["fieldname"]`

**10. Session**
- Stores user data on the SERVER across multiple pages.
- Identified by a session ID (stored in browser cookie).
- `session_start()` must be first line. Stored in `$_SESSION["key"]`.

**11. Cookie**
- Small data file stored on CLIENT (browser).
- Set using `setcookie(name, value, expiry)`. Read via `$_COOKIE["name"]`.
- Max size: 4KB. Can persist after browser closes.

**12. $_FILES**
- Superglobal for file uploads. Used with `enctype="multipart/form-data"` in form.
- Contains: `name`, `tmp_name`, `size`, `type`, `error`.
- Use `move_uploaded_file($tmp, $dest)` to save file.

**13. fopen()**
- Opens a file and returns a file pointer.
- Modes: `r` (read), `w` (write), `a` (append), `r+` (read+write).
- Always close with `fclose($fp)` after use.

**14. mysqli_connect()**
- Connects PHP to MySQL database.
- Syntax: `mysqli_connect("host", "user", "pass", "dbname")`
- Returns connection object or FALSE on failure.

**15. mysqli_fetch_assoc()**
- Fetches one row from query result as associative array.
- Returns column names as keys: `$row["column_name"]`
- Returns NULL when no more rows. Used in `while` loop.

---

## 📊 TOP 5 DIFFERENCE TABLES

### 1. $_GET vs $_POST
| $_GET | $_POST |
|-------|--------|
| Data in URL | Data in HTTP body |
| Visible (less secure) | Hidden (more secure) |
| ~255 char limit | No size limit |
| Bookmarkable | Not bookmarkable |
| For search/read | For login/submit |
| `method="GET"` | `method="POST"` |

### 2. include vs require
| include | require |
|---------|---------|
| Warning if file not found | Fatal error if file not found |
| Script continues | Script stops |
| Use for optional files | Use for essential files |
| `include "file.php"` | `require "file.php"` |
| `include_once` prevents re-include | `require_once` same |

### 3. Session vs Cookie
| Session | Cookie |
|---------|--------|
| Stored on SERVER | Stored on CLIENT |
| More secure | Less secure |
| `$_SESSION["key"]` | `$_COOKIE["key"]` |
| `session_start()` needed | `setcookie()` needed |
| Lost when browser closes | Can persist (set expiry) |
| No size limit | Max 4KB |

### 4. mysqli_fetch_assoc vs mysqli_fetch_array
| mysqli_fetch_assoc | mysqli_fetch_array |
|--------------------|--------------------|
| Assoc array only | Both assoc + numeric |
| `$row["name"]` | `$row["name"]` OR `$row[0]` |
| Less memory | More memory |
| Cleaner code | More flexible |
| Recommended | When index needed |

### 5. Client-side vs Server-side Scripting
| Client-Side | Server-Side |
|-------------|------------|
| Runs on browser | Runs on web server |
| JavaScript, VBScript | PHP, ASP, JSP |
| No server needed | Server required |
| Source code visible | Source code hidden |
| Fast (no round trip) | Slower (network call) |
| Cannot access DB directly | Can access database |

---

## 💻 TOP 3 COMPLETE PROGRAMS

### 🔴 Program 1: MySQL Connection + Fetch Data in HTML Table
```php
<?php
  // Step 1: Connect
  $conn = mysqli_connect("localhost", "root", "", "college_db");
  if(!$conn) {
      die("Connection Failed: " . mysqli_connect_error());
  }

  // Step 2: Run Query
  $sql = "SELECT * FROM students";
  $result = mysqli_query($conn, $sql);
?>
<!DOCTYPE html>
<html>
<body>
<h2>Student Records</h2>
<table border="1" cellpadding="8">
  <tr>
    <th>ID</th>
    <th>Name</th>
    <th>Age</th>
    <th>Marks</th>
  </tr>
  <?php
    // Step 3: Fetch and display
    if(mysqli_num_rows($result) > 0) {
        while($row = mysqli_fetch_assoc($result)) {
            echo "<tr>";
            echo "<td>" . $row["id"]    . "</td>";
            echo "<td>" . $row["name"]  . "</td>";
            echo "<td>" . $row["age"]   . "</td>";
            echo "<td>" . $row["marks"] . "</td>";
            echo "</tr>";
        }
    } else {
        echo "<tr><td colspan='4'>No records found.</td></tr>";
    }
    // Step 4: Close
    mysqli_close($conn);
  ?>
</table>
</body>
</html>
```

---

### 🔴 Program 2: Form Handling with Validation
**form.html**
```html
<!DOCTYPE html>
<html>
<body>
<form action="process.php" method="POST">
  Name:  <input type="text" name="uname"><br><br>
  Email: <input type="email" name="email"><br><br>
  Age:   <input type="number" name="age"><br><br>
  <input type="submit" value="Submit">
</form>
</body>
</html>
```

**process.php**
```php
<?php
  $name  = $_POST["uname"];
  $email = $_POST["email"];
  $age   = $_POST["age"];
  $error = "";

  // Validation
  if(empty($name)) {
      $error .= "Name is required.<br>";
  }
  if(empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
      $error .= "Valid email is required.<br>";
  }
  if(empty($age) || !is_numeric($age) || $age < 1) {
      $error .= "Valid age is required.<br>";
  }

  if($error != "") {
      echo "<b>Errors:</b><br>" . $error;
  } else {
      echo "Name: $name <br>";
      echo "Email: $email <br>";
      echo "Age: $age <br>";
      echo "Form submitted successfully!";
  }
?>
```

---

### 🔴 Program 3: File Upload
**upload_form.html**
```html
<!DOCTYPE html>
<html>
<body>
<h2>Upload a File</h2>
<form action="upload.php" method="POST" enctype="multipart/form-data">
  Select File: <input type="file" name="myfile"><br><br>
  <input type="submit" value="Upload File">
</form>
</body>
</html>
```

**upload.php**
```php
<?php
  if(isset($_FILES["myfile"])) {
      $filename  = $_FILES["myfile"]["name"];
      $tmpname   = $_FILES["myfile"]["tmp_name"];
      $filesize  = $_FILES["myfile"]["size"];
      $filetype  = $_FILES["myfile"]["type"];
      $error_code = $_FILES["myfile"]["error"];

      // Allowed extensions
      $allowed_ext = array("jpg", "jpeg", "png", "gif", "pdf", "txt");
      $ext = strtolower(pathinfo($filename, PATHINFO_EXTENSION));

      if($error_code !== 0) {
          echo "Upload error! Code: $error_code";
      } elseif(!in_array($ext, $allowed_ext)) {
          echo "File type '$ext' not allowed!";
      } elseif($filesize > 5000000) { // 5MB limit
          echo "File too large! Max 5MB.";
      } else {
          $upload_dir = "uploads/";
          $dest = $upload_dir . basename($filename);
          if(move_uploaded_file($tmpname, $dest)) {
              echo "✅ File uploaded successfully!<br>";
              echo "Name: $filename<br>";
              echo "Size: " . round($filesize/1024, 2) . " KB<br>";
              echo "Type: $filetype";
          } else {
              echo "❌ Failed to move file. Check uploads/ folder permissions.";
          }
      }
  } else {
      echo "No file selected!";
  }
?>
```

---

## 📋 TOP 3 LONG ANSWER FRAMEWORKS

### 🔷 Framework 1: PHP with MySQL Full CRUD (Write this for Q6)
**Structure to write in exam:**
1. **Introduction** (2 lines): PHP connects to MySQL using `mysqli_` functions.
2. **Connection code** — `mysqli_connect()`
3. **CREATE** — `INSERT INTO` with `mysqli_query()`
4. **READ** — `SELECT *` + `mysqli_fetch_assoc()` in while loop + HTML table display
5. **UPDATE** — `UPDATE SET WHERE` + `mysqli_query()`
6. **DELETE** — `DELETE FROM WHERE` + `mysqli_query()`
7. **Close** — `mysqli_close($conn)`

**Key functions to mention:**
- `mysqli_connect()`, `mysqli_query()`, `mysqli_fetch_assoc()`, `mysqli_num_rows()`, `mysqli_affected_rows()`, `mysqli_error()`, `mysqli_close()`

---

### 🔷 Framework 2: Session Management (Write this for Q4 part)
**Structure:**
1. **What is session** — server-side storage, identified by session ID
2. **Starting session** — `session_start()` must be FIRST line
3. **Storing data** — `$_SESSION["key"] = "value";`
4. **Reading data** — `echo $_SESSION["key"];`
5. **Checking session** — `isset($_SESSION["key"])`
6. **Destroying session** — `session_unset()` then `session_destroy()`
7. **Complete login example** (login.php + dashboard.php + logout.php)
8. **Session vs Cookie table**

---

### 🔷 Framework 3: Array Functions with Examples (Write this for Q1)
**Mention these with one-line examples:**

```php
<?php
  $a = array(5, 3, 8, 1, 9, 2);

  echo count($a);          // 6
  sort($a);                // ascending: 1,2,3,5,8,9
  rsort($a);               // descending: 9,8,5,3,2,1
  array_push($a, 10);      // add 10 at end
  array_pop($a);           // remove last element
  echo array_sum($a);      // sum of all elements
  echo in_array(8, $a);    // 1 (true) if 8 exists
  print_r(array_reverse($a)); // reverse array

  $b = array(1, 2, 3);
  $c = array(4, 5, 6);
  $merged = array_merge($b, $c); // [1,2,3,4,5,6]

  // Associative array functions
  $student = array("name"=>"Rahul", "age"=>21);
  print_r(array_keys($student));   // ["name","age"]
  print_r(array_values($student)); // ["Rahul", 21]
?>
```

---

## ⚡ QUICK CHEAT SHEET

```
PHP Tags:     <?php  ?>
Echo:         echo "Hello";  OR  print "Hello";
Comment:      // single line   /* multi line */
Concatenate:  "Hello" . " World"

DATA TYPES:   Integer, Float, String, Boolean, Array, Object, NULL

OPERATORS:
  Arithmetic: + - * / % **
  Comparison: == === != < > <= >=
  Logical:    && || ! and or
  String:     .  (dot = concatenate)

CONTROL:
  if / elseif / else
  switch / case / break / default
  while / do-while / for / foreach

FUNCTIONS:
  isset($var)   → check if variable set
  empty($var)   → check if empty
  is_numeric()  → check if number
  intval()      → convert to integer
  date("d-m-Y") → current date
  time()        → current timestamp
```

---

## 🎯 LAST MINUTE TIPS

- ✅ **Section A**: Write at least 3-4 lines per answer. Include one example/syntax.
- ✅ **Section B**: Always write code for every question. Examiners love code.
- ✅ **Start with Q6** (MySQL) — highest PYQ frequency, write the full SELECT table program.
- ✅ **Attempt 5 questions** from Section B even if you're unsure — partial marks count.
- ✅ **Write difference tables** — easy marks, clear presentation.
- ✅ **Always show output** as comment in code: `// Output: Hello`
- ✅ Use proper **headings** in long answers — Introduction, Syntax, Program, Output.
