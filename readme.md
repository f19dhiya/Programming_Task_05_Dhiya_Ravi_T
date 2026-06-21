## About This Task

This task is about understanding how data is stored, processed, searched and analyzed using Lists in Python (and Arrays in C). These are basic but important concepts because almost every real software tool — including cybersecurity tools — works by storing data in some kind of list/array and then looping through it to search, count, or calculate things.

Below are the five Python programs I wrote for this task, along with what each one does and a sample run.

---

## 1. marks_analyzer.py – Student Marks Analyzer

**What it does:**
Takes marks of 5 students as input, stores them in a list, and then finds the highest, lowest, and average marks using Python's built-in `max()`, `min()`, and `sum()` functions.

**Sample Output:**
```
=== Student Marks Analyzer ===
Enter marks for Student 1: 78
Enter marks for Student 2: 85
Enter marks for Student 3: 92
Enter marks for Student 4: 67
Enter marks for Student 5: 88

--- Results ---
Highest Marks: 92
Lowest Marks: 67
Average Marks: 82.00
```

---

## 2. employee_search.py – Employee Record Search

**What it does:**
Stores a fixed list of employee names (John, Alice, David, Sophia, Michael) and lets the user search for a name. It loops through the list comparing each name to the search term and tells the user whether the record was found.

**Sample Output:**
```
=== Employee Record Search ===
Employee Records: ['John', 'Alice', 'David', 'Sophia', 'Michael']

Enter the name to search: Sophia
Record Found
```

If you search for a name that isn't in the list, it prints `Record Not Found` instead.

---

## 3. statistics_tool.py – Number Statistics Tool

**What it does:**
Takes 10 numbers from the user and stores them in a list. It then calculates the largest number, smallest number, sum, average, and counts how many numbers are even vs odd.

**Sample Output:**
```
=== Number Statistics Tool ===
(after entering 10 numbers)

--- Results ---
Largest Number: 90
Smallest Number: 10
Sum: 450
Average: 45.00
Even Numbers: 6
Odd Numbers: 4
```

---

## 4. log_analyzer.py – Cyber Security Log Analyzer

**What it does:**
Stores a list of login attempt results (Success/Failed) and counts how many were successful and how many failed, using the list's `.count()` method.

**Sample Output:**
```
=== Cyber Security Log Analyzer ===
Login Attempts: ['Success', 'Failed', 'Failed', 'Success', 'Failed', 'Success']

--- Results ---
Total Login Attempts: 6
Successful Logins: 3
Failed Logins: 3
```

**Why monitoring failed logins matters:**
A lot of failed login attempts in a row usually means someone is trying to guess a password (a brute-force attack), and it could also mean an account is being targeted by an attacker. By keeping track of failed logins, a security system can spot this pattern early, send an alert, or lock the account before the attacker actually gets in. This is one of the most basic but most important things real-world security monitoring tools do.

---

## 5. blacklist_checker.py – Blacklisted IP Checker

**What it does:**
Stores a list of IP addresses considered "blacklisted" and checks whether a user-entered IP exists in that list. This is a simplified version of what firewalls and intrusion detection systems do when checking incoming traffic against known malicious IPs.

**Sample Output:**
```
=== Blacklisted IP Checker ===
Blacklisted IPs: ['192.168.1.10', '10.0.0.5', '172.16.1.100', '192.168.0.50']

Enter an IP Address to check: 10.0.0.5
IP Found in Blacklist
```

---

## Contact_manager.py – Contact Management System

**What it does:**
A small menu-driven program that lets the user Add, View, Search, and Delete contacts. Contacts are stored as a list of dictionaries (name + phone number), and each menu option just loops through the list to find or change a record.

**Sample Output:**
```
=== Contact Management System ===
1. Add Contact
2. View Contacts
3. Search Contact
4. Delete Contact
5. Exit
Choose an option (1-5): 1
Enter contact name: Rahul
Enter phone number: 9876543210
Contact 'Rahul' added successfully.
```

---

## How to Run

Each file can be run on its own using:
```
python marks_analyzer.py
python employee_search.py
python statistics_tool.py
python log_analyzer.py
python blacklist_checker.py
python contact_manager.py
```

---

## What I Learned

Doing this task helped me understand how lists are used not just to store data, but to actually process it — searching through records, counting occurrences, and calculating stats like average/min/max. I also got a better idea of how something simple like a list of "Success/Failed" logins or blacklisted IPs connects to real cybersecurity concepts like brute-force detection and basic firewall/IDS logic.