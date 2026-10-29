# Last Day Revision — Linux OS (UGCA-1935)
**BCA Sem 5 | PTU | Read this the night before the exam**

---

## 🔑 TOP 15 DEFINITIONS

**1. Linux**
Free, open-source, Unix-like OS. Created by Linus Torvalds in 1991. Based on GNU/Linux. Kernel is monolithic. Multiuser, multitasking, portable.

**2. Kernel**
Core of OS. Manages CPU, memory, devices, file systems. Types: Monolithic (Linux), Microkernel (MINIX), Hybrid (Windows). Acts as bridge between hardware and software.

**3. Shell**
Command interpreter. Takes user commands → passes to kernel → returns output. Types: bash, sh, csh, ksh, zsh. Also a scripting language.

**4. Open Source**
Software whose source code is freely available, modifiable, and redistributable. Licenses: GPL, LGPL, MIT, Apache. Examples: Linux, Apache, Python.

**5. Process**
A running instance of a program. Has PID (Process ID), PPID (Parent PID). States: Running, Ready, Waiting, Stopped, Zombie. Managed by kernel scheduler.

**6. File Permissions**
3 entities: User(u), Group(g), Others(o). 3 permissions: read(r=4), write(w=2), execute(x=1). Set using `chmod`. Example: 755 = rwxr-xr-x.

**7. Hard Link**
Another name (directory entry) for same file. Same inode. Survives original file deletion. Cannot span filesystems. Created with `ln`.

**8. Soft Link (Symbolic Link)**
Pointer/shortcut to original file path. Different inode. Breaks if original deleted. Can span filesystems. Created with `ln -s`.

**9. Inode**
Data structure storing file metadata: size, permissions, owner, timestamps, disk block locations. Each file has unique inode number. NOT the filename.

**10. RPM (Red Hat Package Manager)**
Package format (.rpm) used in Red Hat, CentOS, Fedora. Commands: `rpm -ivh` (install), `rpm -e` (erase), `rpm -q` (query). Database in /var/lib/rpm.

**11. /etc/passwd**
Stores user account info. 7 fields: username:password:UID:GID:GECOS:home:shell. Password field shows 'x' meaning actual hash is in /etc/shadow.

**12. Runlevel**
Defines system operating state. 0=halt, 1=single-user, 3=multi-user CLI, 5=GUI, 6=reboot. Changed with `init N`. Replaced by systemd targets.

**13. Pipe (|)**
Connects STDOUT of one command to STDIN of next. Example: `ls -l | grep ".sh"`. Enables command chaining without temp files.

**14. I/O Redirection**
`>` redirect STDOUT to file (overwrite). `>>` append. `<` redirect file to STDIN. `2>` redirect STDERR. `2>&1` merge STDERR into STDOUT.

**15. grep**
Global Regular Expression Print. Searches for pattern in file(s). Key flags: `-i` (case-insensitive), `-r` (recursive), `-n` (line numbers), `-v` (invert match), `-c` (count).

---

## ⚡ IMPORTANT COMMANDS (One-liner each)

| Command | What it does |
|---|---|
| `chmod 755 file` | Set file permissions (rwxr-xr-x) using octal |
| `chmod u+x file` | Add execute permission for owner (symbolic) |
| `chown user:group file` | Change owner and group of file |
| `grep -i "word" file` | Search for word (case-insensitive) in file |
| `find / -name "file.txt"` | Find file by name from root directory |
| `tar -czvf out.tar.gz dir/` | Create compressed gzip archive of directory |
| `tar -xzvf out.tar.gz` | Extract compressed gzip archive |
| `ps -aux` | Show all running processes with CPU/MEM usage |
| `kill -9 PID` | Force kill a process by its PID |
| `top` | Real-time interactive process monitor |
| `useradd -m john` | Create user john with home directory |
| `passwd john` | Set or change password for user john |
| `ls -la` | List all files including hidden, with details |
| `cp -r src/ dest/` | Copy directory recursively |
| `mv file newname` | Move or rename file |
| `ln -s original link` | Create symbolic (soft) link |
| `ln original link` | Create hard link |
| `nice -n 10 cmd` | Run command with lower priority (10) |
| `renice -n 5 -p PID` | Change priority of running process |
| `rpm -ivh pkg.rpm` | Install RPM package with progress |
| `rpm -e packagename` | Uninstall RPM package |

---

## 📊 TOP 5 DIFFERENCE TABLES

### 1. Linux vs Windows
| Feature | Linux | Windows |
|---|---|---|
| Cost | Free / Open Source | Paid / Proprietary |
| Source Code | Available (GPL) | Closed source |
| Security | More secure | More vulnerable |
| File System | ext4, xfs, btrfs | NTFS, FAT32 |
| CLI | Powerful (bash) | Limited (cmd/PowerShell) |
| Stability | High (servers run years) | Needs reboots |
| Usage | Servers, dev, embedded | Desktop, gaming |

### 2. Hard Link vs Soft Link
| Feature | Hard Link | Soft Link |
|---|---|---|
| Inode | Same as original | Different (new) |
| If original deleted | Still works | Breaks (dangling) |
| Cross filesystem | ❌ No | ✅ Yes |
| Link directories | ❌ No | ✅ Yes |
| Command | `ln file link` | `ln -s file link` |
| Size | Same as original | Small (path size) |

### 3. Absolute vs Relative Path
| Feature | Absolute Path | Relative Path |
|---|---|---|
| Starts from | Root `/` | Current directory |
| Example | `/home/john/file.txt` | `./file.txt` or `../dir/` |
| Consistency | Same everywhere | Changes with location |
| Length | Longer | Shorter |
| Usage | Scripts, configs | Quick navigation |

### 4. RPM vs dpkg
| Feature | RPM | dpkg |
|---|---|---|
| Full form | Red Hat Package Manager | Debian Package |
| File extension | `.rpm` | `.deb` |
| Used in | RHEL, CentOS, Fedora | Debian, Ubuntu |
| Install | `rpm -ivh pkg.rpm` | `dpkg -i pkg.deb` |
| Remove | `rpm -e pkg` | `dpkg -r pkg` |
| Query | `rpm -q pkg` | `dpkg -l pkg` |
| High-level tool | yum / dnf | apt / apt-get |

### 5. Shell vs Kernel
| Feature | Shell | Kernel |
|---|---|---|
| What it is | Command interpreter | Core of OS |
| Layer | User space | Kernel space |
| Interacts with | User & Kernel | Hardware |
| Examples | bash, sh, csh, ksh | Linux kernel |
| Function | Parses and runs commands | Manages resources |
| Access | Direct user interaction | Via system calls |

---

## 💻 2 SHELL SCRIPTS THAT ALWAYS COME

### Script 1: Factorial using while loop
```bash
#!/bin/bash
echo "Enter number:"
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

### Script 2: Palindrome Check
```bash
#!/bin/bash
echo "Enter number:"
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
  echo "$num is NOT a Palindrome"
fi
```

### BONUS: Fibonacci using while loop
```bash
#!/bin/bash
echo "Enter count:"
read n
a=0
b=1
i=1
echo "Fibonacci series:"
while [ $i -le $n ]
do
  echo -n "$a "
  temp=$((a + b))
  a=$b
  b=$temp
  i=$((i + 1))
done
echo ""
```

---

## 📝 TOP 3 LONG ANSWER FRAMEWORKS

### Framework 1: Linux Architecture (10 marks)
**Intro (1 line):** Linux is an open-source, monolithic kernel OS developed by Linus Torvalds in 1991.

**Draw this diagram:**
```
┌────────────────────────────────┐
│   Applications / User Programs │  ← gcc, vim, Firefox
├────────────────────────────────┤
│         SHELL LAYER            │  ← bash, sh, csh, ksh
├────────────────────────────────┤
│         KERNEL LAYER           │
│  ┌─────────┬──────┬─────────┐  │
│  │ Process │ Mem  │ File Sys│  │  ← Core services
│  │  Mgmt   │ Mgmt │  Mgmt  │  │
│  └─────────┴──────┴─────────┘  │
│  ┌─────────────────────────┐   │
│  │   Device Drivers        │   │  ← NIC, disk, USB
│  └─────────────────────────┘   │
├────────────────────────────────┤
│        HARDWARE LAYER          │  ← CPU, RAM, HDD, NIC
└────────────────────────────────┘
```

**Explain each layer:** Hardware → Kernel (4 functions) → Shell (types) → Applications
**Features:** Multiuser, Multitasking, Open Source, Portable, Secure, Stable
**Conclude:** Linux powers 96% of world's servers.

---

### Framework 2: File Permissions (10 marks)
**Intro:** Linux uses discretionary access control — every file has owner, group, others.

**Permission string breakdown:**
```
- r w x | r - x | r - -
  owner   group   others
  (7)     (5)     (4)    → 754
```

**Cover these points:**
1. Three entities: user(u), group(g), others(o)
2. Three permissions: r(4), w(2), x(1) and their meanings
3. `ls -l` output interpretation (draw example)
4. Octal notation table (0-7) with binary
5. `chmod` examples: octal (`chmod 755`) and symbolic (`chmod u+x`)
6. `chown user:group file` — change ownership
7. `chgrp group file` — change group
8. Special permissions (mention): setuid, setgid, sticky bit
9. Hard link vs soft link (if asked together)

---

### Framework 3: User Administration (10 marks)
**Intro:** Linux is multiuser OS. Each user has UID, GID, home dir, shell.

**Cover these points:**
1. /etc/passwd — 7 fields (draw example line)
2. /etc/shadow — encrypted passwords, readable only by root
3. useradd with options (-m -s -u -g)
4. passwd command
5. usermod (modify: shell, group, name)
6. userdel / userdel -r
7. groupadd / groupdel / gpasswd
8. /etc/group file — format: groupname:x:GID:members

**Key commands to list:**
```bash
useradd -m -s /bin/bash john    # create with home+shell
passwd john                      # set password
usermod -aG sudo john            # add to group
userdel -r john                  # delete user + home
groupadd developers              # create group
gpasswd -a john developers       # add to group
cat /etc/passwd                  # view users
cat /etc/shadow                  # view encrypted passwords
id john                          # view UID, GID of user
who / w                          # who is logged in
```

---

## 🎯 EXAM DAY STRATEGY

```
Section A (20 marks):
- Attempt ALL 10 — no choice
- 2 marks = 3-4 lines max
- Don't waste time writing paragraphs

Section B (40 marks — attempt 4):
1. Shell Scripting (write both scripts) ← easiest 10
2. Linux Architecture (draw diagram)   ← diagram = marks
3. File Permissions (octal table)      ← formulas = marks
4. User Administration (commands)      ← list commands
→ Skip whichever unit you're weakest in

Time allocation:
- Section A: 40 minutes (4 min each)
- Section B Q1: 20 min
- Section B Q2: 20 min
- Section B Q3: 20 min
- Section B Q4: 20 min
- Review: 0 min (use all time writing)
```

> **Last tip:** In every long answer — draw a diagram or table. Examiners give marks for structure, not just content. A diagram in architecture/FHS/permissions answers can earn 2-3 extra marks.
