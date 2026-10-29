# 📝 GUESS PAPER 2026 — Programming in PHP (UGCA-1929)
**M.Code: 90312 | BCA Semester 5 | IKGPTU**
**Time: 3 Hours | Max Marks: 60**
> Note: Section A is compulsory. Attempt any FOUR questions from Section B.

---

# ✅ SECTION A — Short Answer Questions (10 × 2 = 20 Marks)
*All questions are compulsory*

---

**Q1. What is PHP? List any two features of PHP.**

**Answer:**
- PHP (Hypertext Preprocessor) is a server-side, open-source scripting language used for web development.
- Features:
  1. **Platform Independent** – runs on Windows, Linux, macOS
  2. **Database Support** – connects easily with MySQL, Oracle
  3. **Open Source** – free to use
  4. **Embedded in HTML** – PHP code written inside HTML using `<?php ... ?>`

---

**Q2. Differentiate between client-side and server-side scripting.**

**Answer:**
| Client-Side | Server-Side |
|-------------|------------|
| Runs on browser | Runs on web server |
| Example: JavaScript | Example: PHP, ASP |
| No server needed | Requires a server |
| Less secure | More secure |

---

**Q3. What are variables in PHP? What are the rules for naming variables?**

**Answer:**
- Variable: A named memory location to store data. Declared using `$` sign.
- Example: `$name = "BCA";`
- Rules:
  1. Starts with `$` followed by a letter or underscore
  2. Case-sensitive (`$Name` ≠ `$name`)
  3. Cannot start with a digit
  4. No spaces or special characters except `_`

---

**Q4. What is variable scope in PHP? Explain local and global scope.**

**Answer:**
- **Scope** = where a variable can be accessed.
- **Local scope**: Variable declared inside a function; accessible only within that function.
- **Global scope**: Variable declared outside functions; NOT auto-accessible inside functions.
- Use `global $var;` inside function to access global variable.
- **Static**: Retains value between function calls. `static $count = 0;`

---

**Q5. What is an associative array? Give an example.**

**Answer:**
- Associative array uses **named keys** (strings) instead of numeric indexes.
```php
<?php
  $student = array("name"=>"Rahul", "age"=>21, "city"=>"Amritsar");
  echo $student["name"]; // Output: Rahul
?>
```

---

**Q6. What is the difference between `$_GET` and `$_POST`?**

**Answer:**
| $_GET | $_POST |
|-------|--------|
| Data sent via URL | Data sent via HTTP body |
| Visible in URL (less secure) | Not visible in URL (more secure) |
| Limited data (255 chars) | No size limit |
| Used for search/read | Used for login/forms |
| Bookmarkable | Not bookmarkable |

---

**Q7. What is a session in PHP? How to start a session?**

**Answer:**
- **Session**: A way to store user data on the SERVER across multiple pages.
- Session data is stored on server; a session ID is stored in cookie on client.
- Start session: `session_start();` (must be first line before HTML)
- Store data: `$_SESSION["username"] = "admin";`
- Destroy: `session_destroy();`

---

**Q8. What is `fopen()` in PHP? List its file modes.**

**Answer:**
- `fopen(filename, mode)` – opens a file and returns a file pointer.
- Common Modes:
  - `"r"` – Read only (file must exist)
  - `"w"` – Write (creates/truncates file)
  - `"a"` – Append (creates if not exists)
  - `"r+"` – Read + Write
  - `"w+"` – Read + Write (truncates)

---

**Q9. What is `mysqli_connect()`? Write its syntax.**

**Answer:**
- Used to establish a connection between PHP and MySQL database.
- **Syntax:**
```php
$conn = mysqli_connect("hostname", "username", "password", "database");
```
- **Example:**
```php
$conn = mysqli_connect("localhost", "root", "", "student_db");
if(!$conn) { die("Connection failed: " . mysqli_connect_error()); }
```

---

**Q10. What is `mysqli_fetch_assoc()`? How is it different from `mysqli_fetch_array()`?**

**Answer:**
| mysqli_fetch_assoc() | mysqli_fetch_array() |
|----------------------|----------------------|
| Returns associative array only | Returns both associative + numeric array |
| Access by column name: `$row["name"]` | Access by name OR index: `$row[0]` or `$row["name"]` |
| Less memory usage | More memory usage |
| Preferred for clarity | More flexible |

---

# ✅ SECTION B — Long Answer Questions (Attempt any 4 × 10 = 40 Marks)

---

## Q1. Explain PHP Arrays in detail with examples. Also explain the `foreach` loop. [10 Marks]

**Types of Arrays in PHP:**

### 1️⃣ Indexed Array
- Numeric index starting from 0.
```php
<?php
  $fruits = array("Apple", "Banana", "Mango");
  echo $fruits[0]; // Apple
  echo $fruits[2]; // Mango

  // Using for loop
  for($i = 0; $i < count($fruits); $i++) {
      echo $fruits[$i] . "<br>";
  }
?>
```

### 2️⃣ Associative Array
- Uses string keys.
```php
<?php
  $student = array("name"=>"Rahul", "age"=>21, "marks"=>85);
  echo "Name: " . $student["name"] . "<br>";
  echo "Age: " . $student["age"] . "<br>";
?>
```

### 3️⃣ Multidimensional Array
- Array containing arrays.
```php
<?php
  $students = array(
    array("Rahul", 21, 85),
    array("Priya", 20, 90),
    array("Amit", 22, 78)
  );
  // Access: $students[row][column]
  echo $students[0][0]; // Rahul
  echo $students[1][2]; // 90
?>
```

### foreach Loop
- Specially designed to iterate over arrays.
- **Syntax:** `foreach($array as $value)` or `foreach($array as $key => $value)`
```php
<?php
  // With indexed array
  $colors = array("Red", "Green", "Blue");
  foreach($colors as $color) {
      echo $color . "<br>";
  }

  // With associative array
  $person = array("name"=>"Priya", "city"=>"Delhi", "age"=>20);
  foreach($person as $key => $value) {
      echo "$key : $value <br>";
  }
?>
```

**Useful Array Functions:**
| Function | Purpose |
|----------|---------|
| `count($arr)` | Number of elements |
| `sort($arr)` | Sort ascending |
| `rsort($arr)` | Sort descending |
| `array_push($arr, val)` | Add element at end |
| `array_pop($arr)` | Remove last element |
| `array_merge($a, $b)` | Merge two arrays |
| `in_array(val, $arr)` | Search in array |
| `array_keys($arr)` | Get all keys |
| `array_values($arr)` | Get all values |

---

## Q2. Explain User-Defined Functions in PHP with Pass by Value, Pass by Reference, and Default Parameters. [10 Marks]

**Function**: A reusable block of code. Defined with `function` keyword.

**Syntax:**
```php
function functionName($param1, $param2) {
    // code
    return $value;
}
```

### 1️⃣ Pass by Value
- Copy of variable is passed. Original NOT affected.
```php
<?php
  function addTen($num) {
      $num = $num + 10;
      echo "Inside: $num <br>"; // 20
  }
  $x = 10;
  addTen($x);
  echo "Outside: $x <br>"; // 10 (unchanged)
?>
```

### 2️⃣ Pass by Reference
- Using `&` operator. Original variable IS modified.
```php
<?php
  function addTen(&$num) {
      $num = $num + 10;
  }
  $x = 10;
  addTen($x);
  echo "Outside: $x"; // 20 (changed!)
?>
```

### 3️⃣ Default Parameters
- Default value used if no argument is passed.
```php
<?php
  function greet($name = "Student") {
      echo "Hello, $name! <br>";
  }
  greet("Rahul"); // Hello, Rahul!
  greet();        // Hello, Student!
?>
```

### 4️⃣ Return Values
```php
<?php
  function multiply($a, $b) {
      return $a * $b;
  }
  $result = multiply(5, 4);
  echo "Result: $result"; // 20
?>
```

### 5️⃣ Variable Functions
- Store function name in variable, then call it.
```php
<?php
  function sayHello() { echo "Hello!"; }
  $func = "sayHello";
  $func(); // Output: Hello!
?>
```

**String Functions:**
| Function | Purpose | Example |
|----------|---------|---------|
| `strlen($s)` | Length | `strlen("PHP")` → 3 |
| `strtoupper($s)` | Uppercase | `strtoupper("php")` → PHP |
| `strtolower($s)` | Lowercase | |
| `strrev($s)` | Reverse | `strrev("PHP")` → PHQ |
| `str_replace(f,r,$s)` | Replace | |
| `substr($s, start, len)` | Substring | |
| `strpos($s, find)` | Find position | |
| `trim($s)` | Remove whitespace | |
| `explode(del, $s)` | Split to array | |
| `implode(del, $arr)` | Join array | |

---

## Q3. Explain Form Handling in PHP using $_GET and $_POST with a complete example. Also explain other superglobals. [10 Marks]

### HTML Form (form.html)
```html
<html>
<body>
<form action="process.php" method="POST">
  Name: <input type="text" name="uname"><br>
  Email: <input type="text" name="email"><br>
  <input type="submit" value="Submit">
</form>
</body>
</html>
```

### Process File (process.php)
```php
<?php
  // Collect data
  $name  = $_POST["uname"];
  $email = $_POST["email"];

  // Validation
  if(empty($name)) {
      echo "Name is required!";
  } elseif(!filter_var($email, FILTER_VALIDATE_EMAIL)) {
      echo "Invalid email!";
  } else {
      echo "Welcome, $name! <br>";
      echo "Your email: $email";
  }
?>
```

### Using $_GET (Search Example)
```php
<!-- search.html -->
<form action="search.php" method="GET">
  Search: <input type="text" name="query">
  <input type="submit" value="Go">
</form>

<!-- search.php -->
<?php
  $q = $_GET["query"];
  echo "You searched for: $q";
  // URL becomes: search.php?query=PHP
?>
```

### PHP Superglobals Table
| Superglobal | Purpose |
|------------|---------|
| `$_GET` | Data from URL/form (GET method) |
| `$_POST` | Data from form (POST method) |
| `$_REQUEST` | Combines GET + POST + COOKIE |
| `$_SESSION` | Server-side user session data |
| `$_COOKIE` | Cookie data from browser |
| `$_FILES` | Uploaded file data |
| `$_SERVER` | Server & request info |
| `$_ENV` | Environment variables |
| `$GLOBALS` | All global variables |

### $_SERVER Examples
```php
<?php
  echo $_SERVER["SERVER_NAME"];   // localhost
  echo $_SERVER["PHP_SELF"];      // current script name
  echo $_SERVER["REQUEST_METHOD"]; // GET or POST
  echo $_SERVER["REMOTE_ADDR"];   // client IP
?>
```

---

## Q4. Explain Session and Cookie management in PHP with complete programs. [10 Marks]

### 🍪 COOKIES
- Small data stored on **CLIENT (browser)**.
- Set with `setcookie()`, read with `$_COOKIE`.

**Setting a Cookie:**
```php
<?php
  // setcookie(name, value, expiry, path)
  setcookie("username", "Rahul", time() + (86400 * 30), "/");
  // 86400 = 1 day | 86400*30 = 30 days
  echo "Cookie set!";
?>
```

**Reading a Cookie:**
```php
<?php
  if(isset($_COOKIE["username"])) {
      echo "Welcome back, " . $_COOKIE["username"];
  } else {
      echo "Cookie not found.";
  }
?>
```

**Deleting a Cookie:**
```php
<?php
  setcookie("username", "", time() - 3600, "/");
  // Set expiry in the past to delete
?>
```

---

### 🔐 SESSIONS
- Data stored on **SERVER**.
- More secure than cookies.

**Login with Session (login.php):**
```php
<?php
  session_start();
  $user = $_POST["username"];
  $pass = $_POST["password"];

  if($user == "admin" && $pass == "1234") {
      $_SESSION["user"] = $user;
      $_SESSION["logged_in"] = true;
      header("Location: dashboard.php");
  } else {
      echo "Invalid credentials!";
  }
?>
```

**Checking Session (dashboard.php):**
```php
<?php
  session_start();
  if(!isset($_SESSION["logged_in"])) {
      header("Location: login.php");
      exit();
  }
  echo "Welcome, " . $_SESSION["user"];
?>
```

**Logout (logout.php):**
```php
<?php
  session_start();
  session_unset();    // Remove all session variables
  session_destroy();  // Destroy session
  header("Location: login.php");
?>
```

**Session vs Cookie:**
| Session | Cookie |
|---------|--------|
| Stored on SERVER | Stored on CLIENT (browser) |
| More secure | Less secure |
| Lost when browser closes (default) | Persists for set duration |
| No size limit issue | Max 4KB |
| `$_SESSION["key"]` | `$_COOKIE["key"]` |
| `session_start()` required | `setcookie()` required |

---

## Q5. Explain File Handling in PHP. Write programs for reading, writing, and file upload. [10 Marks]

### File Handling Functions
| Function | Purpose |
|----------|---------|
| `fopen(file, mode)` | Open file |
| `fclose($fp)` | Close file |
| `fread($fp, size)` | Read from file |
| `fwrite($fp, string)` | Write to file |
| `fgets($fp)` | Read one line |
| `feof($fp)` | Check end of file |
| `file_exists(file)` | Check if file exists |
| `file_get_contents(file)` | Read entire file as string |
| `file_put_contents(file, data)` | Write string to file |
| `unlink(file)` | Delete file |

### Program 1: Write to a File
```php
<?php
  $file = fopen("data.txt", "w"); // open for write
  if($file) {
      fwrite($file, "Hello, PHP File Handling!\n");
      fwrite($file, "This is line 2.\n");
      fclose($file);
      echo "File written successfully!";
  } else {
      echo "Error opening file!";
  }
?>
```

### Program 2: Read from a File
```php
<?php
  $file = fopen("data.txt", "r");
  if($file) {
      while(!feof($file)) {
          $line = fgets($file);
          echo $line . "<br>";
      }
      fclose($file);
  } else {
      echo "File not found!";
  }

  // OR simpler:
  if(file_exists("data.txt")) {
      echo file_get_contents("data.txt");
  }
?>
```

### Program 3: File Upload
**upload_form.html:**
```html
<form action="upload.php" method="POST" enctype="multipart/form-data">
  Select File: <input type="file" name="myfile"><br>
  <input type="submit" value="Upload">
</form>
```

**upload.php:**
```php
<?php
  if(isset($_FILES["myfile"])) {
      $filename  = $_FILES["myfile"]["name"];
      $tmpname   = $_FILES["myfile"]["tmp_name"];
      $filesize  = $_FILES["myfile"]["size"];
      $filetype  = $_FILES["myfile"]["type"];
      $error     = $_FILES["myfile"]["error"];

      // Validate
      $allowed = array("jpg","jpeg","png","gif","pdf");
      $ext = pathinfo($filename, PATHINFO_EXTENSION);

      if(in_array(strtolower($ext), $allowed)) {
          $dest = "uploads/" . $filename;
          if(move_uploaded_file($tmpname, $dest)) {
              echo "File uploaded successfully!<br>";
              echo "Name: $filename | Size: $filesize bytes";
          } else {
              echo "Upload failed!";
          }
      } else {
          echo "File type not allowed!";
      }
  }
?>
```

**$_FILES Array Keys:**
| Key | Description |
|-----|-------------|
| `["name"]` | Original filename |
| `["tmp_name"]` | Temp path on server |
| `["size"]` | File size in bytes |
| `["type"]` | MIME type |
| `["error"]` | Error code (0 = success) |

---

## Q6. Explain PHP with MySQL. Write a complete program to connect to MySQL and perform CRUD operations. [10 Marks]

### Step 1: Connect to Database
```php
<?php
  $conn = mysqli_connect("localhost", "root", "", "college_db");
  if(!$conn) {
      die("Connection Failed: " . mysqli_connect_error());
  }
  echo "Connected successfully!";
?>
```

### Step 2: CREATE (Insert Data)
```php
<?php
  $conn = mysqli_connect("localhost", "root", "", "college_db");
  $sql = "INSERT INTO students (name, age, marks) VALUES ('Rahul', 21, 85)";
  if(mysqli_query($conn, $sql)) {
      echo "Record inserted!";
  } else {
      echo "Error: " . mysqli_error($conn);
  }
  mysqli_close($conn);
?>
```

### Step 3: READ (Fetch & Display in HTML Table)
```php
<?php
  $conn = mysqli_connect("localhost", "root", "", "college_db");
  $sql = "SELECT * FROM students";
  $result = mysqli_query($conn, $sql);
?>
<html>
<body>
<table border="1">
  <tr>
    <th>ID</th><th>Name</th><th>Age</th><th>Marks</th>
  </tr>
  <?php
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
        echo "<tr><td colspan='4'>No records found</td></tr>";
    }
  ?>
</table>
</body>
</html>
<?php mysqli_close($conn); ?>
```

### Step 4: UPDATE
```php
<?php
  $conn = mysqli_connect("localhost", "root", "", "college_db");
  $sql = "UPDATE students SET marks=90 WHERE name='Rahul'";
  if(mysqli_query($conn, $sql)) {
      echo "Record updated! Rows: " . mysqli_affected_rows($conn);
  } else {
      echo "Error: " . mysqli_error($conn);
  }
  mysqli_close($conn);
?>
```

### Step 5: DELETE
```php
<?php
  $conn = mysqli_connect("localhost", "root", "", "college_db");
  $sql = "DELETE FROM students WHERE id=1";
  if(mysqli_query($conn, $sql)) {
      echo "Record deleted!";
  } else {
      echo "Error: " . mysqli_error($conn);
  }
  mysqli_close($conn);
?>
```

### Key MySQL Functions Table
| Function | Purpose |
|----------|---------|
| `mysqli_connect()` | Connect to DB |
| `mysqli_query($conn, $sql)` | Run SQL query |
| `mysqli_fetch_assoc($result)` | Fetch as associative array |
| `mysqli_fetch_array($result)` | Fetch as both assoc + numeric |
| `mysqli_num_rows($result)` | Count rows returned |
| `mysqli_affected_rows($conn)` | Count rows affected (INSERT/UPDATE/DELETE) |
| `mysqli_error($conn)` | Get last error |
| `mysqli_close($conn)` | Close connection |
