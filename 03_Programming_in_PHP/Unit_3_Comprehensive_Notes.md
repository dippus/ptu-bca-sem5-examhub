# 📘 UNIT 3: Comprehensive Exam Notes — Programming in PHP (UGCA-1929)
**BCA Semester 5 | IKGPTU | External Exam: 60 Marks**  
> Specially prepared for **10-Mark Section B Questions** and **2-Mark Section A Definitions** (High-Yield Focus).

---

# 📑 TABLE OF CONTENTS
1. [🔴 SECTION A: High-Yield 2-Mark Questions & Answers](#-section-a-high-yield-2-mark-questions-all-repeated-pyqs)
2. [🌟 TOPIC 1 (10 Marks): Form Handling in PHP (`$_GET` vs `$_POST` & `$_REQUEST`)](#-topic-1-form-handling--superglobal-arrays-10-marks)
3. [🌟 TOPIC 2 (10 Marks): State Management — Sessions vs Cookies Architecture](#-topic-2-state-management--sessions-vs-cookies-10-marks)
4. [🌟 TOPIC 3 (10 Marks): File Handling & File Uploading (`$_FILES`)](#-topic-3-file-handling--file-upload-in-php-10-marks)

---

# 🔴 SECTION A: High-Yield 2-Mark Questions (All Repeated PYQs)

### Q1. What is the difference between `$_GET` and `$_POST` superglobals? *(Nov 2025, 2024, 2023)*
**Answer:**

| Parameter | `$_GET` | `$_POST` |
|---|---|---|
| **Data Transmission** | Appends submitted form data directly to the URL (`?key=val`). | Sends submitted form data securely inside the HTTP request body. |
| **Visibility** | Completely visible in browser address bar (Unsafe for passwords). | Completely hidden from URL (Safe for credentials). |
| **Data Capacity** | Limited to ~2048 characters (URL length limit). | Virtually unlimited (configured in `php.ini` `post_max_size`). |
| **Bookmarkability** | Can be bookmarked and cached. | Cannot be bookmarked or cached. |
| **Ideal Use Case** | Search queries, filters, pagination. | User registration, login forms, sensitive transactions. |

---

### Q2. Differentiate between `include` and `require` statements. *(Nov 2024, 2023)*
**Answer:**

| Feature | `include` | `require` |
|---|---|---|
| **Error Level on Failure** | Throws a non-fatal **E_WARNING** if file is missing. | Throws a fatal **E_COMPILE_ERROR** if file is missing. |
| **Script Execution** | Execution **continues** despite missing file. | Execution **stops immediately (halts script)**. |
| **Best Used For** | Optional layout components (header, footer, sidebar). | Critical operational files (database connection, configuration). |

---

### Q3. Why must `session_start()` be called before any HTML tag? *(Nov 2025)*
**Answer:**
* `session_start()` initializes a session and sends a session identification cookie (`PHPSESSID`) to the browser via **HTTP response headers**.
* In HTTP protocols, headers must always be transmitted before any actual HTML body content.
* If any whitespace, echo, or HTML tag is sent before `session_start()`, PHP triggers a *"Headers already sent"* warning and fails to establish the session.

---

### Q4. What is a Cookie in PHP? How is it created and deleted?
**Answer:**
* A **Cookie** is a small text file (up to 4 KB) stored on the **client's computer** by the browser to track user preferences across requests.
* **Creation:** Using `setcookie(name, value, expire, path);`  
  * *Example:* `setcookie("user", "Rahul", time() + 3600, "/");` (Expires in 1 hour).
* **Deletion:** Set the expiration timestamp to a past time:  
  * *Example:* `setcookie("user", "", time() - 3600, "/");`

---

### Q5. List the common file access modes in PHP `fopen()`. *(Nov 2024)*
**Answer:**
* `"r"`: Read-only. File pointer at the beginning. (File must exist).
* `"w"`: Write-only. Erases file content (truncates to 0 length) or creates a new file.
* `"a"`: Append-only. Keeps existing content and writes at the end. Creates file if missing.
* `"r+"`: Read and Write. Pointer at the beginning.
* `"w+"`: Read and Write. Truncates file or creates new.

---

### Q6. What is the role of `enctype="multipart/form-data"` in HTML forms?
**Answer:**
* By default, forms encode data as `application/x-www-form-urlencoded`.
* When uploading binary files (images, PDFs) via `<input type="file">`, `enctype="multipart/form-data"` is strictly required. It tells the browser to split binary stream data into parts so the server's `$_FILES` array can parse it.

---

# 🌟 TOPIC 1: Form Handling & Superglobal Arrays [10 Marks]

> ❓ **Repeated Exam Question:**  
> **"Explain form handling in PHP. Differentiate between GET and POST methods. Write a complete PHP script to collect and validate user inputs (Name, Email, Course) and display the submitted information."** *(Nov 2025, Nov 2024)*

---

### 1. Introduction to Form Handling
* HTML forms collect data from users, and PHP processes this data on the server side.
* When a user clicks the "Submit" button, data is transferred to the script designated in the form's `action` attribute using the specified `method` (`GET` or `POST`).
* PHP automatically captures incoming form elements into associative **Superglobal Arrays**:
  * `$_GET`: Stores values submitted via `method="GET"`.
  * `$_POST`: Stores values submitted via `method="POST"`.
  * `$_REQUEST`: A combined superglobal containing contents of `$_GET`, `$_POST`, and `$_COOKIE`.

---

### 2. Request Handling Workflow (Diagram)

```
  +-----------------------------------------------------------+
  |                   CLIENT (WEB BROWSER)                    |
  |                                                           |
  |   <form action="process.php" method="POST">               |
  |     Name:  <input name="uname">                           |
  |     Email: <input name="uemail">                          |
  |     <input type="submit">                                 |
  +-----------------------------------------------------------+
                                |
                                | (HTTP POST with Form Data)
                                v
  +-----------------------------------------------------------+
  |                    APACHE WEB SERVER                      |
  |                                                           |
  |   Parses body -> Populates Superglobal Array:             |
  |   $_POST = [                                              |
  |      "uname"  => "Simran Kaur",                           |
  |      "uemail" => "simran@example.com"                     |
  |   ];                                                      |
  |                                                           |
  |   Zend Engine executes business validation logic.         |
  +-----------------------------------------------------------+
                                |
                                | (HTTP Response: Validated HTML)
                                v
  +-----------------------------------------------------------+
  |              Rendered Result on Client Screen             |
  +-----------------------------------------------------------+
```

---

### 3. Complete Working Demonstration Program

Save this script as `register.php`. It contains both the HTML Form and PHP Processing logic in one file:

```php
<!DOCTYPE html>
<html>
<head>
    <title>Student Registration Portal</title>
    <style>
        .form-box { border: 2px solid #4f46e5; padding: 20px; width: 350px; border-radius: 8px; }
        .result-box { margin-top: 20px; padding: 15px; background: #e0e7ff; border-radius: 8px; }
    </style>
</head>
<body>

<div class="form-box">
    <h2>BCA Student Registration</h2>
    <!-- Form submitting to itself using POST -->
    <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST">
        <label>Full Name:</label><br>
        <input type="text" name="student_name" required><br><br>

        <label>Email Address:</label><br>
        <input type="email" name="student_email" required><br><br>

        <label>Select Course:</label><br>
        <select name="student_course">
            <option value="BCA Sem-5">BCA Sem-5</option>
            <option value="B.Tech CSE">B.Tech CSE</option>
            <option value="MCA">MCA</option>
        </select><br><br>

        <input type="submit" name="btn_submit" value="Submit Application">
    </form>
</div>

<?php
// PHP Script to process form submission
if (isset($_POST['btn_submit'])) {
    // 1. Sanitizing and reading input
    $name   = htmlspecialchars($_POST['student_name']);
    $email  = htmlspecialchars($_POST['student_email']);
    $course = htmlspecialchars($_POST['student_course']);

    // 2. Validation
    if (!empty($name) && !empty($email)) {
        echo "<div class='result-box'>";
        echo "<h3>✅ Submission Successful!</h3>";
        echo "<p><b>Student Name:</b> " . $name . "</p>";
        echo "<p><b>Email ID:</b> " . $email . "</p>";
        echo "<p><b>Enrolled Course:</b> " . $course . "</p>";
        echo "</div>";
    } else {
        echo "<p style='color:red;'>Please fill all required fields.</p>";
    }
}
?>

</body>
</html>
```

---

# 🌟 TOPIC 2: State Management — Sessions vs Cookies [10 Marks]

> ❓ **Repeated Exam Question:**  
> **"What is State Management in Web Applications? Differentiate between Sessions and Cookies in PHP with a neat diagram. Write a PHP script to demonstrate session-based user login and logout."** *(Nov 2025, Nov 2024)*

---

### 1. The State Management Problem
* The **HTTP protocol is stateless** — every request from a client to a server is completely independent. The server does not naturally remember who the user is between page clicks.
* To maintain user state (like login authentication, shopping carts), PHP provides two mechanisms: **Cookies (Client-Side)** and **Sessions (Server-Side)**.

---

### 2. Comprehensive Comparison: Session vs Cookie

| Feature | Cookie | Session |
|---|---|---|
| **Storage Location** | Client's Web Browser / Local Hard Disk. | Secure Web Server Memory or Temporary Directory. |
| **Security** | Low (User can inspect, tamper, or disable cookies). | High (Data stored on server; client only holds a session ID). |
| **Storage Limit** | Max **4 KB** per cookie, ~20 cookies per domain. | Virtually unlimited (bounded only by server RAM / disk). |
| **Lifetime** | Persists until expiry timestamp or manual deletion. | Ends when user closes browser or calls `session_destroy()`. |
| **Access Method** | Accessible via `$_COOKIE['key']`. | Accessible via `$_SESSION['key']`. |

---

### 3. Architecture & Lifecycle Diagram

```
 CLIENT BROWSER                                      WEB SERVER
+---------------+                               +-------------------+
|               |  (1) First Login Request      |                   |
|               | ----------------------------> | Authenticates User|
|               |                               | Creates Session   |
|               |  (2) HTTP Header: Set-Cookie  | Stored on Server: |
|               |      PHPSESSID = xyz789       | [user => 'admin'] |
|               | <---------------------------- | Session ID: xyz789|
|               |                               +-------------------+
| Stores Cookie |                                         |
| [PHPSESSID]   |  (3) Subsequent Page Request            |
|               |      Header: Cookie PHPSESSID=xyz789   |
|               | ----------------------------> Matches Session ID!|
|               |                               Grants Page Access  |
|               |  (4) Protected Page Content   |                   |
|               | <---------------------------- |                   |
+---------------+                               +-------------------+
```

---

### 4. Complete Implementation: Login & Logout Flow

#### File 1: `login.php` (Starting Session)
```php
<?php
session_start(); // Step 1: Always first line!

// Dummy authentication check
if (isset($_POST['login_btn'])) {
    $user = $_POST['uname'];
    $pass = $_POST['upass'];

    if ($user == "admin" && $pass == "12345") {
        $_SESSION['authenticated_user'] = $user;
        $_SESSION['login_time'] = time();
        header("Location: dashboard.php"); // Redirect
        exit();
    } else {
        $error = "Invalid Username or Password!";
    }
}
?>
<!-- Login Form -->
<form method="POST">
    <h2>Portal Login</h2>
    <?php if(isset($error)) echo "<p style='color:red;'>$error</p>"; ?>
    User: <input type="text" name="uname" required><br><br>
    Pass: <input type="password" name="upass" required><br><br>
    <input type="submit" name="login_btn" value="Login">
</form>
```

#### File 2: `dashboard.php` (Accessing Session & Protected Page)
```php
<?php
session_start();

// Check if user is authenticated
if (!isset($_SESSION['authenticated_user'])) {
    header("Location: login.php"); // Redirect unauthorized user
    exit();
}
?>
<!DOCTYPE html>
<html>
<body>
    <h1>Welcome, <?php echo $_SESSION['authenticated_user']; ?>!</h1>
    <p>You have securely logged into the BCA Sem-5 Examination Portal.</p>
    <a href="logout.php">Click here to Logout</a>
</body>
</html>
```

#### File 3: `logout.php` (Destroying Session)
```php
<?php
session_start();
session_unset();    // Free all session variables
session_destroy();  // Destroy all data registered to a session

header("Location: login.php"); // Redirect back to login
exit();
?>
```

---

# 🌟 TOPIC 3: File Handling & File Upload in PHP [10 Marks]

> ❓ **Repeated Exam Question:**  
> **"Explain File Handling functions in PHP with examples: `fopen()`, `fread()`, `fwrite()`, `fclose()`. Also explain the complete procedure for handling file uploads using the `$_FILES` superglobal array."** *(Nov 2025, Nov 2023)*

---

### 1. Basic File Handling Operations

PHP provides procedural functions to interact with server files:

```php
<?php
$filename = "student_records.txt";

// 1. OPENING & WRITING TO A FILE
$fileHandler = fopen($filename, "w") or die("Unable to open file!");
$txt = "RollNo: 101, Name: Rohan, Marks: 92\n";
fwrite($fileHandler, $txt);
fclose($fileHandler); // Always close open handlers!

// 2. OPENING & READING ENTIRE FILE
$fileHandler = fopen($filename, "r") or die("File not found!");
$fileContent = fread($fileHandler, filesize($filename));
echo "<b>File Content:</b><br>" . nl2br($fileContent);
fclose($fileHandler);

// 3. READING LINE BY LINE USING feof() AND fgets()
$fileHandler = fopen($filename, "r");
while (!feof($fileHandler)) {
    $line = fgets($fileHandler);
    echo "Line: " . $line . "<br>";
}
fclose($fileHandler);
?>
```

---

### 2. File Uploading in PHP (`$_FILES` Superglobal)

When uploading files, PHP populates the 2D associative array `$_FILES['upload_field_name']`:
* `$_FILES['file']['name']`: Original client-side filename (e.g., `resume.pdf`).
* `$_FILES['file']['type']`: MIME type (e.g., `image/jpeg`, `application/pdf`).
* `$_FILES['file']['size']`: File size in bytes.
* `$_FILES['file']['tmp_name']`: Temporary file location on the web server.
* `$_FILES['file']['error']`: Error code (`0` means success).

---

### 3. Complete File Upload Script with Validations

```php
<!DOCTYPE html>
<html>
<head><title>File Upload System</title></head>
<body>

<!-- Crucial: enctype="multipart/form-data" -->
<form action="" method="POST" enctype="multipart/form-data">
    <h3>Select Image to Upload (Max 2 MB, JPG/PNG only):</h3>
    <input type="file" name="user_file" required><br><br>
    <input type="submit" name="upload_btn" value="Upload File">
</form>

<?php
if (isset($_POST['upload_btn'])) {
    $targetDir = "uploads/";
    
    // Create directory if missing
    if (!is_dir($targetDir)) { mkdir($targetDir, 0777, true); }

    $fileName = basename($_FILES["user_file"]["name"]);
    $targetFilePath = $targetDir . $fileName;
    $fileType = strtolower(pathinfo($targetFilePath, PATHINFO_EXTENSION));
    $fileSize = $_FILES["user_file"]["size"];

    // Validation 1: Allowed extensions
    $allowed = array("jpg", "jpeg", "png", "pdf");

    if (!in_array($fileType, $allowed)) {
        echo "<p style='color:red;'>❌ Error: Only JPG, PNG, and PDF files are allowed.</p>";
    } 
    // Validation 2: Size limit (2 MB = 2 * 1024 * 1024 bytes)
    elseif ($fileSize > 2097152) {
        echo "<p style='color:red;'>❌ Error: File size exceeds 2 MB limit.</p>";
    } 
    else {
        // Step: Move file from temporary directory to target directory
        if (move_uploaded_file($_FILES["user_file"]["tmp_name"], $targetFilePath)) {
            echo "<p style='color:green;'>✅ File <b>$fileName</b> uploaded successfully!</p>";
        } else {
            echo "<p style='color:red;'>❌ Error occurred while uploading file.</p>";
        }
    }
}
?>

</body>
</html>
```

