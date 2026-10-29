# ⚡ LAST DAY REVISION — Programming in Java
### BCA Sem 5 | IKGPTU | UGCA-1932 | M.Code: 90315
> 🔥 Sirf yahi padho — exam mein yehi aata hai!

---

## 📖 PART 1 — TOP 15 DEFINITIONS (2 Marks Each)

> Format: Definition (1 line) + Key Point (2-3 lines) — **3-4 lines max**

---

**1. Java**
Java ek object-oriented, platform-independent programming language hai jo Sun Microsystems ne banai (1995). Java ka principle hai — **"Write Once, Run Anywhere (WORA)"**. Java code compile hoke **bytecode** banta hai jo JVM pe chalti hai. Isko interpreted + compiled dono kaha ja sakta hai.

---

**2. JVM (Java Virtual Machine)**
JVM ek virtual machine hai jo Java **bytecode (.class file)** ko execute karta hai. Yeh platform-specific hoti hai lekin bytecode platform-independent. JVM ke andar **ClassLoader, Bytecode Verifier, Interpreter, JIT Compiler** hote hain. Isi wajah se Java platform independent hai.

---

**3. Constructor**
Constructor ek special method hai jiska naam class ke naam se same hota hai aur koi return type nahi hoti (void bhi nahi). Jab bhi koi object create hota hai, constructor automatically call hota hai. Types: **Default, Parameterized, Copy Constructor**.

---

**4. Inheritance**
Inheritance ek OOP concept hai jisme ek class (child/subclass) dusri class (parent/superclass) ke properties aur methods inherit karti hai. Keyword: **`extends`**. Types: Single, Multilevel, Hierarchical. Java mein multiple inheritance (class se) supported nahi hai.

---

**5. Polymorphism**
Polymorphism matlab "ek kaam, alag tarike". Java mein 2 types: **Compile-time (Method Overloading)** aur **Runtime (Method Overriding)**. Overloading mein same method name, alag parameters. Overriding mein child class parent class ka method redefine karti hai.

---

**6. Abstract Class**
Abstract class woh class hai jisme kam se kam ek **abstract method** ho (body nahi). Keyword: **`abstract`**. Abstract class ka object directly nahi banta. Isko inherit karke child class mein sab abstract methods implement karne padte hain.

---

**7. Interface**
Interface ek contract hai jisme **sirf abstract methods aur constants** hote hain (Java 8 se default methods bhi). Keyword: **`interface`** aur **`implements`**. Ek class multiple interfaces implement kar sakti hai — isi se Java mein multiple inheritance achieve hoti hai.

---

**8. Exception**
Exception ek runtime error hai jo program execution rokti hai. Java mein exception handling ke liye **try, catch, finally, throw, throws** keywords use hote hain. Exceptions 2 types ki: **Checked** (compile time) aur **Unchecked** (runtime).

---

**9. Thread**
Thread ek lightweight process hai — program execution ki smallest unit. Java mein thread create karne ke 2 tarike: **`Thread` class extend** karo ya **`Runnable` interface implement** karo. Method: `start()` se thread start hoti hai, `run()` actual kaam karta hai.

---

**10. Multithreading**
Multithreading ek feature hai jisme ek saath multiple threads execute hoti hain. Isse CPU utilization improve hoti hai. Java mein `java.lang.Thread` class use hoti hai. Thread lifecycle: **New → Runnable → Running → Blocked → Dead**.

---

**11. Applet**
Applet ek Java program hai jo web browser mein run hoti hai. Yeh `java.applet.Applet` class ko extend karti hai. Application se alag — Applet ka `main()` method nahi hota. Lifecycle methods: **init(), start(), stop(), destroy(), paint()**.

---

**12. Package**
Package related classes aur interfaces ka collection hai — jaise ek folder. 2 types: **Built-in** (`java.lang`, `java.util`, `java.io`) aur **User-defined**. Keyword: `package` (define karne ke liye) aur `import` (use karne ke liye).

---

**13. String Class**
String ek **immutable** class hai `java.lang` package mein. Immutable matlab ek baar create hone ke baad change nahi hoti. Important methods: `length()`, `charAt()`, `substring()`, `indexOf()`, `equals()`, `toUpperCase()`, `trim()`.

---

**14. StringBuffer**
StringBuffer ek **mutable** class hai jisme string ko modify kiya ja sakta hai. Yeh **thread-safe** hai (synchronized). Important methods: `append()`, `insert()`, `delete()`, `reverse()`, `replace()`. String se faster for modifications.

---

**15. Synchronization**
Synchronization ek mechanism hai jo ensure karta hai ki ek time pe sirf **ek thread** shared resource access kare. Keyword: **`synchronized`**. Isse **race condition** aur **data inconsistency** rokti hai. Method ya block dono ko synchronized kiya ja sakta hai.

---

## 📊 PART 2 — TOP 5 "DIFFERENCE BETWEEN" TABLES

---

### 1️⃣ Java vs C++

| Feature | Java | C++ |
|---------|------|-----|
| Platform | Platform Independent (WORA) | Platform Dependent |
| Pointers | Nahi hote (no explicit pointers) | Hote hain |
| Memory Management | Automatic (Garbage Collector) | Manual (free/delete) |
| Multiple Inheritance | Interface se possible | Class se directly possible |
| Header Files | Nahi (`import` use hota hai) | Hote hain (`#include`) |
| Main Method | `public static void main(String[] args)` | `int main()` |

---

### 2️⃣ Abstract Class vs Interface

| Feature | Abstract Class | Interface |
|---------|---------------|-----------|
| Keyword | `abstract` | `interface` |
| Methods | Abstract + Concrete dono | Only abstract (Java 8 se default bhi) |
| Variables | Any type | Only `public static final` |
| Constructor | Ho sakta hai | Nahi hota |
| Multiple Inheritance | Nahi | Haan (multiple implement kar sakte hain) |
| `extends`/`implements` | `extends` | `implements` |
| Speed | Fast | Slow (extra indirection) |

---

### 3️⃣ String vs StringBuffer

| Feature | String | StringBuffer |
|---------|--------|-------------|
| Mutability | Immutable | Mutable |
| Thread Safety | Thread-safe (immutable) | Thread-safe (synchronized) |
| Performance | Slow (new object banta hai) | Fast (same object modify) |
| Storage | String Pool | Heap |
| Methods | `length()`, `substring()` etc. | `append()`, `reverse()` etc. |

---

### 4️⃣ throw vs throws

| Feature | throw | throws |
|---------|-------|--------|
| Purpose | Exception **manually throw** karne ke liye | Exception **declare** karne ke liye |
| Location | Method body ke andar | Method signature mein |
| Exception Type | Ek baar mein ek exception | Multiple exceptions |
| Checked Exception | Directly nahi throw kar sakte | Declare kar sakte hain |
| Example | `throw new ArithmeticException();` | `void method() throws IOException` |

---

### 5️⃣ Process vs Thread

| Feature | Process | Thread |
|---------|---------|--------|
| Definition | Program ka executing instance | Process ka smallest part |
| Memory | Alag memory space | Shared memory space |
| Communication | Mushkil (IPC needed) | Aasaan (shared memory) |
| Creation Time | Slow | Fast |
| Context Switch | Slow | Fast |
| Dependency | Independent | Process pe dependent |

---

## 💻 PART 3 — TOP 3 PROGRAMS (Complete + Working)

---

### Program 1: Exception Handling ⭐⭐⭐

```java
// Exception Handling — try, catch, finally, multiple exceptions
public class ExceptionDemo {
    public static void main(String[] args) {
        try {
            int a = 10, b = 0;
            int result = a / b;           // ArithmeticException
            System.out.println(result);
            
            int[] arr = new int[5];
            arr[10] = 100;               // ArrayIndexOutOfBoundsException
        }
        catch (ArithmeticException e) {
            System.out.println("Arithmetic Error: " + e.getMessage());
        }
        catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Array Error: " + e.getMessage());
        }
        finally {
            System.out.println("Finally block ALWAYS executes!");
        }
    }
}
```
**Output:**
```
Arithmetic Error: / by zero
Finally block ALWAYS executes!
```

**Key Points (Section A ke liye):**
- `try` — risky code yahan
- `catch` — exception handle karta hai
- `finally` — always execute hota hai (exception ho ya na ho)
- `throw` — manually exception throw karo
- `throws` — method signature mein declare karo

---

### Program 2: Thread Creation (DONO TARIKE) ⭐⭐⭐

```java
// METHOD 1: Thread class extend karke
class MyThread extends Thread {
    public void run() {
        for (int i = 1; i <= 3; i++) {
            System.out.println("Thread 1: " + i);
            try { Thread.sleep(500); } 
            catch (InterruptedException e) { }
        }
    }
}

// METHOD 2: Runnable interface implement karke
class MyRunnable implements Runnable {
    public void run() {
        for (int i = 1; i <= 3; i++) {
            System.out.println("Thread 2: " + i);
            try { Thread.sleep(500); } 
            catch (InterruptedException e) { }
        }
    }
}

public class ThreadDemo {
    public static void main(String[] args) {
        MyThread t1 = new MyThread();          // Method 1
        Thread t2 = new Thread(new MyRunnable()); // Method 2
        
        t1.start();   // start() call karo, run() directly mat karo!
        t2.start();
    }
}
```
**Output (order vary kar sakta hai — concurrent execution):**
```
Thread 1: 1
Thread 2: 1
Thread 1: 2
Thread 2: 2 ...
```

**Thread Lifecycle Diagram:**
```
NEW ──start()──► RUNNABLE ──CPU milte hi──► RUNNING
                    ▲                           │
                    │ notify()/               sleep()/
                    │ I/O complete            wait()/I/O
                    │                           │
                  BLOCKED ◄────────────────────┘
                    │
              run() ends
                    │
                   DEAD
```

---

### Program 3: String Operations ⭐⭐⭐

```java
// String class ke important methods
public class StringDemo {
    public static void main(String[] args) {
        String s = "Hello IKGPTU Java";
        
        System.out.println("Length: " + s.length());           // 17
        System.out.println("UpperCase: " + s.toUpperCase());   // HELLO IKGPTU JAVA
        System.out.println("LowerCase: " + s.toLowerCase());   // hello ikgptu java
        System.out.println("Substring: " + s.substring(6, 12)); // IKGPTU
        System.out.println("IndexOf: " + s.indexOf("Java"));   // 13
        System.out.println("Replace: " + s.replace("Java", "BCA")); // Hello IKGPTU BCA
        System.out.println("Equals: " + s.equals("Hello"));    // false
        System.out.println("Contains: " + s.contains("IKGPTU")); // true
        
        // StringBuffer — mutable
        StringBuffer sb = new StringBuffer("Hello");
        sb.append(" World");      // Hello World
        sb.insert(5, " Java");    // Hello Java World
        sb.delete(5, 10);         // Hello World
        sb.reverse();             // dlroW olleH
        System.out.println("StringBuffer: " + sb);
    }
}
```

---

## 📋 PART 4 — TOP 3 LONG ANSWER FRAMEWORKS (10 Marks)

---

### Framework 1: JVM Architecture (Q2 Type) ⭐⭐⭐

**Introduction (2 lines):** JVM bytecode execute karta hai, platform-specific.

**Diagram:**
```
Java Source (.java)
       │ javac (compiler)
       ▼
  Bytecode (.class)
       │
  ┌────▼────────────────────────────┐
  │           JVM                  │
  │  ┌──────────────────────────┐  │
  │  │    Class Loader          │  │ ← .class file load karta hai
  │  ├──────────────────────────┤  │
  │  │  Bytecode Verifier       │  │ ← Security check
  │  ├──────────────────────────┤  │
  │  │  Execution Engine        │  │
  │  │  ├─ Interpreter          │  │ ← Line by line execute
  │  │  └─ JIT Compiler         │  │ ← Fast (native code)
  │  ├──────────────────────────┤  │
  │  │  Garbage Collector       │  │ ← Unused memory free
  │  └──────────────────────────┘  │
  └─────────────────────────────────┘
```

**Key Components (4 lines each):**
- **ClassLoader:** .class files ko load karta hai (Bootstrap, Extension, Application)
- **Bytecode Verifier:** Security check — malicious code detect karta hai
- **Interpreter:** Bytecode ko line-by-line execute karta hai (slow)
- **JIT Compiler:** Frequently used bytecode ko native machine code mein convert karta hai (fast)
- **Garbage Collector:** Unused objects ki memory automatically free karta hai

**Java Features (4 points):** Simple, OOP, Platform-Independent, Secure, Robust, Multithreaded, Distributed, Dynamic

---

### Framework 2: Inheritance with Diagram (Q3 Type) ⭐⭐⭐

**Definition (2 lines):** Inheritance = parent class ka code child mein reuse. `extends` keyword.

**Types:**

```
1. SINGLE:          2. MULTILEVEL:       3. HIERARCHICAL:
   A                   A                    A
   │                   │                   / \
   B                   B                  B   C
                        │
                        C
```

**Code Pattern (yahi likhna hai):**
```java
// Single Inheritance
class Animal {
    void eat() { System.out.println("Animal eats"); }
}
class Dog extends Animal {
    void bark() { System.out.println("Dog barks"); }
}

// Multilevel Inheritance
class A { void methodA() { System.out.println("A"); } }
class B extends A { void methodB() { System.out.println("B"); } }
class C extends B { void methodC() { System.out.println("C"); } }

// Main
public class Main {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.eat();   // inherited from Animal
        d.bark();  // own method
        
        C obj = new C();
        obj.methodA(); obj.methodB(); obj.methodC();
    }
}
```

**super keyword:** `super.methodName()` — parent class method call karo. `super()` — parent constructor call.

**Important points:**
- Java mein **multiple inheritance** (class se) nahi — Diamond problem
- Interface se multiple inheritance possible hai
- `extends` keyword use hota hai

---

### Framework 3: Applet Lifecycle (Q7 Type) ⭐⭐⭐

**Definition:** Applet = browser mein run hone wala Java program. `Applet` class extend karta hai.

**Lifecycle Diagram:**
```
Browser loads Applet
        │
    init()          ← Ek baar: initialization (variables set karo)
        │
    start()         ← Har baar page aane pe: execution start
        │
    paint()         ← Display: Graphics draw karo
        │
    stop()          ← Page leave karne pe: execution pause
        │
    destroy()       ← Browser close: cleanup
```

**Complete Applet Program:**
```java
import java.applet.*;
import java.awt.*;

/*
<applet code="AppletDemo.class" width="300" height="200">
</applet>
*/

public class AppletDemo extends Applet {
    String message;
    
    public void init() {
        message = "Hello IKGPTU!";
        setBackground(Color.yellow);
    }
    
    public void start() {
        System.out.println("Applet Started");
    }
    
    public void paint(Graphics g) {
        g.setColor(Color.red);
        g.setFont(new Font("Arial", Font.BOLD, 20));
        g.drawString(message, 50, 100);
        g.drawRect(20, 20, 200, 150);    // Rectangle draw karo
    }
    
    public void stop() {
        System.out.println("Applet Stopped");
    }
    
    public void destroy() {
        System.out.println("Applet Destroyed");
    }
}
```

**Applet vs Application:**

| Feature | Applet | Application |
|---------|--------|-------------|
| Runs in | Browser | Command line / OS |
| main() | Nahi hota | Hota hai |
| Security | Restricted | Full access |
| Base class | `Applet` | Koi nahi |

---

## 🚀 EXAM DAY QUICK CHECKLIST

```
Section A (40 min):
□ Q1(b) — JVM/JRE/JDK difference ✍️
□ Q1(c) — Constructor definition ✍️
□ Q1(f) — throw vs throws table ✍️
□ Q1(g) — String vs StringBuffer table ✍️
□ Q1(h) — Thread definition + lifecycle states ✍️

Section B (100 min — choose 4):
□ Q5 — Exception Handling (EASIEST — always do this!)
□ Q6 — Multithreading (dono programs yaad hain)
□ Q3 — Inheritance (diagram + 3 types ka program)
□ Q7 — Applet lifecycle (diagram + program)

Last 20 min:
□ Diagrams check karo
□ Program semicolons check karo
□ Section A answers 3-4 lines mein hain?
```

---
> 🙏 **All the Best for your exam! You've got this! 💪**
> 
> *"Ek raat mein toh nahi padha ja sakta, lekin ek raat mein sahi cheezein padhi ja sakti hain!"*

