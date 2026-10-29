# Guess Paper 2026 — Linux Operating System
**UGCA-1935 | M.Code: 90318 | PTU BCA Semester 5**
**Time: 3 Hours | Max Marks: 60 | External Exam**

> **Instructions:** Section A is compulsory (10 × 2 = 20). Attempt any 4 from Section B (4 × 10 = 40).

---

# SECTION A — Short Answer Questions (10 × 2 = 20 Marks)
*All questions are compulsory. Each carries 2 marks.*

**Q1.** Define the Linux Kernel. What are its two main functions?

**Q2.** What is Open Source software? Name any two Open Source licenses.

**Q3.** List the three modes of the `vi` editor and how to switch between them.

**Q4.** What is a pipe (`|`) in Linux? Give one example using `ls` and `grep`.

**Q5.** Differentiate between a Hard Link and a Soft (Symbolic) Link.

**Q6.** What does `chmod 755 file.sh` mean? Explain the octal values.

**Q7.** What is a process in Linux? Define PID and PPID.

**Q8.** List all runlevels (0–6) and state what each runlevel represents.

**Q9.** What is the purpose of `/etc/passwd` file? List any four fields it contains.

**Q10.** What is RPM? Write the command to install and remove a package using RPM.

---

# SECTION B — Long Answer Questions (Attempt any 4 × 10 = 40 Marks)

---

## Q1. Linux Architecture [VERY HIGH PROBABILITY]

**(a)** Draw and explain the Linux Architecture with a neat diagram. Describe the role of each layer: Hardware, Kernel, Shell, and Applications. **(6 marks)**

**(b)** List and explain any four key features of Linux that make it popular over other operating systems. **(4 marks)**

### Model Answer Framework:

**Architecture Diagram:**
```
+--------------------------------------------------+
|          USER / APPLICATION LAYER                |
|  (gcc, vim, bash scripts, web browsers, etc.)    |
+--------------------------------------------------+
|              SHELL LAYER                         |
|  (bash, sh, csh, ksh — interprets user cmds)    |
+--------------------------------------------------+
|              KERNEL LAYER                        |
|  ┌────────────┬────────────┬────────────────┐    |
|  │ Process    │ Memory     │ Device/File    │    |
|  │ Management │ Management │ Management     │    |
|  └────────────┴────────────┴────────────────┘    |
+--------------------------------------------------+
|              HARDWARE LAYER                      |
|  (CPU, RAM, HDD, NIC, Keyboard, Monitor)         |
+--------------------------------------------------+
```

**Kernel Functions:**
- Process Management: scheduling, creating/terminating processes
- Memory Management: allocation, virtual memory, paging
- File System Management: reads/writes files on disk
- Device Management: drivers for hardware devices
- System Calls: interface between user programs and kernel

**Shell Functions:**
- Command interpreter — reads user input, passes to kernel
- Types: bash (Bourne Again Shell), sh, csh (C Shell), ksh (Korn Shell)
- Supports scripting, variables, loops, functions

**Key Features of Linux:**
1. **Multiuser** — multiple users can log in simultaneously
2. **Multitasking** — multiple processes run concurrently
3. **Open Source** — source code freely available (GNU GPL)
4. **Portability** — runs on x86, ARM, SPARC, MIPS
5. **Security** — file permissions, users/groups, SELinux
6. **Stability** — can run for years without reboot

---

## Q2. Shell Scripting — Variables, Loops & Functions [VERY HIGH PROBABILITY]

**(a)** Write a shell script to find the **factorial** of a given number using a `while` loop. **(4 marks)**

**(b)** Write a shell script to check whether a given number is a **palindrome**. **(3 marks)**

**(c)** Explain the types of shells available in Linux with one feature of each. **(3 marks)**

### Model Answer Framework:

**(a) Factorial using while loop:**
```bash
#!/bin/bash
echo "Enter a number:"
read n
fact=1
i=1
while [ $i -le $n ]
do
  fact=$((fact * i))
  i=$((i + 1))
done
echo "Factorial of $n = $fact"
```

**(b) Palindrome check:**
```bash
#!/bin/bash
echo "Enter a number:"
read num
rev=0
temp=$num
while [ $temp -gt 0 ]
do
  digit=$((temp % 10))
  rev=$((rev * 10 + digit))
  temp=$((temp / 10))
done
if [ $num -eq $rev ]
then
  echo "$num is a Palindrome"
else
  echo "$num is not a Palindrome"
fi
```

**(c) Shell Types:**
| Shell | Full Name | Feature |
|---|---|---|
| sh | Bourne Shell | Original UNIX shell, basic scripting |
| bash | Bourne Again Shell | Default in Linux, powerful scripting |
| csh | C Shell | C-like syntax, history mechanism |
| ksh | Korn Shell | Combines sh + csh features |
| zsh | Z Shell | Advanced auto-completion, plugins |

---

## Q3. File Permissions & Links [VERY HIGH PROBABILITY]

**(a)** Explain Linux file permissions in detail. How do you set permissions using both **symbolic** and **octal** notation with `chmod`? **(6 marks)**

**(b)** Differentiate between Hard Link and Soft Link. Give the command to create each. **(4 marks)**

### Model Answer Framework:

**(a) File Permissions:**

Every file has permissions for 3 categories:
```
Owner (u)   Group (g)   Others (o)
  rwx          rwx         rwx
```
- **r** = read (4), **w** = write (2), **x** = execute (1)

**Example:** `ls -l` output:
```
-rwxr-xr--  1 john staff 1024 Oct 29 file.sh
```
- `-` = regular file (d=directory, l=link)
- `rwx` = owner can read, write, execute
- `r-x` = group can read, execute
- `r--` = others can only read

**Octal Notation:**
| Octal | Binary | Permission |
|:---:|:---:|:---:|
| 7 | 111 | rwx |
| 6 | 110 | rw- |
| 5 | 101 | r-x |
| 4 | 100 | r-- |
| 0 | 000 | --- |

```bash
chmod 755 file.sh   # rwxr-xr-x
chmod 644 file.txt  # rw-r--r--
chmod 700 secret.sh # rwx------
```

**Symbolic Notation:**
```bash
chmod u+x file.sh       # add execute for owner
chmod g-w file.txt      # remove write from group
chmod o=r file.txt      # set others to read only
chmod a+r file.txt      # add read for all (a = all)
```

**chown — Change Ownership:**
```bash
chown john file.txt          # change owner
chown john:staff file.txt    # change owner and group
chgrp staff file.txt         # change group only
```

**(b) Hard Link vs Soft Link:**
| Feature | Hard Link | Soft Link (Symbolic) |
|---|---|---|
| Command | `ln file hardlink` | `ln -s file softlink` |
| Inode | Same inode as original | Different inode |
| Works across filesystems | ❌ No | ✅ Yes |
| If original deleted | Link still works | Link breaks (dangling) |
| Can link directories | ❌ No | ✅ Yes |
| File size | Same as original | Small (stores path) |

```bash
ln file.txt hardlink.txt       # hard link
ln -s file.txt softlink.txt    # soft/symbolic link
```

---

## Q4. User & Group Administration [VERY HIGH PROBABILITY]

**(a)** Explain the structure of `/etc/passwd` and `/etc/shadow` files with an example. **(4 marks)**

**(b)** Explain the commands to add, modify, and delete a user in Linux with proper syntax and options. **(4 marks)**

**(c)** Write commands to create a group, add a user to it, and set a group password. **(2 marks)**

### Model Answer Framework:

**(a) /etc/passwd Structure:**
```
username:password:UID:GID:GECOS:home_dir:shell
john:x:1001:1001:John Doe:/home/john:/bin/bash
```
- **username**: login name
- **x**: password stored in /etc/shadow
- **UID**: User ID (0=root, 1-999=system, 1000+=regular)
- **GID**: Primary Group ID
- **GECOS**: Full name / comments
- **home_dir**: home directory path
- **shell**: default login shell

**/etc/shadow Structure:**
```
username:encrypted_pass:lastchg:min:max:warn:inactive:expire
john:$6$xyz...:18000:0:99999:7:::
```
- Stores encrypted passwords (MD5/SHA-512)
- Readable only by root

**(b) User Management Commands:**
```bash
# Add user
useradd username              # basic add
useradd -m -s /bin/bash john  # with home dir and shell
useradd -u 1050 -g staff john # specify UID and group

# Set/change password
passwd john

# Modify user
usermod -s /bin/sh john       # change shell
usermod -aG sudo john         # add to supplementary group
usermod -l newname oldname    # rename user

# Delete user
userdel john                  # delete user (keep home)
userdel -r john               # delete user + home dir
```

**(c) Group Commands:**
```bash
groupadd developers           # create group
gpasswd -a john developers    # add user to group
gpasswd developers            # set group password
groupdel developers           # delete group
```

---

## Q5. Process Management [HIGH PROBABILITY]

**(a)** Explain process states in Linux. Describe the commands `ps`, `top`, `kill`, `nice`, and `renice` with syntax and examples. **(7 marks)**

**(b)** What are runlevels in Linux? List all 7 runlevels and their equivalent systemd targets. **(3 marks)**

### Model Answer Framework:

**(a) Process States:**
```
NEW → READY → RUNNING → TERMINATED
                ↓↑
             WAITING/BLOCKED
                ↓↑
             STOPPED (Ctrl+Z)
               ↓
            ZOMBIE (finished but parent not acknowledged)
```

**Process Commands:**

```bash
# ps — process snapshot
ps            # current user's processes
ps -a         # all processes in terminal
ps -aux       # all processes with details (user, CPU, MEM)
ps -ef        # full format with PPID

# top — real-time process monitor
top           # interactive; press q to quit
              # press k then PID to kill
              # press r to renice

# kill — send signal to process
kill PID           # send SIGTERM (15) — graceful stop
kill -9 PID        # send SIGKILL — force kill
kill -l            # list all signals
killall firefox    # kill by process name

# nice — start process with priority
nice -n 10 ./script.sh    # range: -20 (highest) to 19 (lowest)

# renice — change priority of running process
renice -n 5 -p 1234       # change PID 1234 to priority 5
```

**(b) Runlevels:**
| Runlevel | Description | systemd Target |
|:---:|---|---|
| 0 | Halt / Shutdown | poweroff.target |
| 1 | Single User Mode (maintenance) | rescue.target |
| 2 | Multi-user, No NFS | multi-user.target |
| 3 | Multi-user, Text Mode (CLI) | multi-user.target |
| 4 | Undefined / Custom | — |
| 5 | Multi-user, GUI (Graphical) | graphical.target |
| 6 | Reboot | reboot.target |

```bash
# systemd commands
systemctl get-default              # get current target
systemctl set-default graphical.target  # set default
systemctl isolate rescue.target    # switch runlevel now
init 3                             # old-style: switch to runlevel 3
```

---

## Q6. File System Hierarchy & Key File Commands [HIGH PROBABILITY]

**(a)** Explain the Linux File System Hierarchy Standard (FHS). Draw the directory tree and explain the purpose of each major directory. **(5 marks)**

**(b)** Explain `grep`, `find`, and `tar` commands with 2 examples each. **(5 marks)**

### Model Answer Framework:

**(a) FHS Directory Tree:**
```
/ (root)
├── /bin    — essential user binaries (ls, cp, mv, bash)
├── /sbin   — system binaries (fsck, ifconfig, reboot)
├── /etc    — configuration files (/etc/passwd, /etc/fstab)
├── /home   — home directories of users (/home/john)
├── /root   — root user's home directory
├── /var    — variable data (logs: /var/log, mail, spool)
├── /tmp    — temporary files (cleared on reboot)
├── /usr    — user programs (/usr/bin, /usr/lib, /usr/share)
├── /lib    — shared libraries needed by /bin and /sbin
├── /dev    — device files (disk: /dev/sda, terminal: /dev/tty)
├── /proc   — virtual filesystem: running process info
├── /sys    — virtual filesystem: hardware/kernel info
├── /mnt    — mount point for temporary mounts
├── /media  — mount point for removable media (USB, CD)
└── /boot   — bootloader files (vmlinuz, grub)
```

**(b) Key Commands:**

**grep — search text patterns:**
```bash
grep "error" log.txt              # find "error" in file
grep -i "ERROR" log.txt          # case-insensitive
grep -r "main" /home/john/       # recursive in directory
grep -n "root" /etc/passwd       # show line numbers
grep -v "bash" /etc/passwd       # lines NOT matching
```

**find — search files:**
```bash
find / -name "file.txt"           # find by name
find /home -user john             # find files owned by john
find /tmp -type f -mtime +7       # files older than 7 days
find . -name "*.sh" -perm 755     # .sh files with 755 perm
find / -size +100M                # files larger than 100MB
```

**tar — archive & compress:**
```bash
# Create archive
tar -cvf archive.tar /home/john/  # c=create, v=verbose, f=file
tar -czvf archive.tar.gz /home/   # z=gzip compress

# Extract archive
tar -xvf archive.tar              # x=extract
tar -xzvf archive.tar.gz          # extract gzip

# List contents
tar -tvf archive.tar              # t=list contents
```

---

*End of Guess Paper*

> **Note:** Questions 1 (Architecture), 2 (Shell Scripting), 3 (File Permissions), and 4 (User Admin) are MUST PREPARE. Attempt these 4 in Section B for maximum marks.
