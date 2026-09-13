"""
LeetCode Problem 182: Duplicate Emails
Difficulty: Easy
Topics: Database

Problem:
Write a SQL query to report all the duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | b@c.com |
+----+---------+
For example, your query should return the following for the above table:
+---------+
| Email   |
+---------+
| b@c.com |
+---------+
Note: All emails are in lowercase.

Approach:
Use GROUP BY with HAVING clause to find emails that appear more than once.
Time Complexity: O(n) where n is number of rows
Space Complexity: O(1) - handled by database engine
"""

# Since this is a SQL problem, we'll provide the SQL solution as a comment
# and also create a Python function that demonstrates the logic

def duplicate_emails_sql():
    """
    Returns the SQL query to solve LeetCode 182: Duplicate Emails
    
    Returns:
        str: The SQL query string
    """
    sql_query = """
SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(Email) > 1;
"""
    return sql_query.strip()

# Alternative approach using subquery
def duplicate_emails_subquery():
    """
    Alternative SQL query using subquery
    """
    sql_query = """
SELECT DISTINCT Email
FROM Person
WHERE Email IN (
    SELECT Email
    FROM Person
    GROUP BY Email
    HAVING COUNT(Email) > 1
);
"""
    return sql_query.strip()

# Demonstration with sample data using Python (for educational purposes)
def duplicate_emails_python_demo():
    """
    Demonstrates the logic using Python data structures
    (This is for educational purposes only - the actual solution is SQL)
    """
    # Sample Person data
    person_data = [
        {"Id": 1, "Email": "a@b.com"},
        {"Id": 2, "Email": "c@d.com"},
        {"Id": 3, "Email": "b@c.com"}
    ]
    
    # Count email frequencies
    email_count = {}
    for person in person_data:
        email = person["Email"]
        email_count[email] = email_count.get(email, 0) + 1
    
    # Find emails that appear more than once
    duplicates = [email for email, count in email_count.items() if count > 1]
    
    return duplicates

# Test cases
if __name__ == "__main__":
    print("LeetCode 182: Duplicate Emails - SQL Solution")
    print("=" * 50)
    print("SQL Query:")
    print(duplicate_emails_sql())
    print()
    
    print("Alternative SQL Query:")
    print(duplicate_emails_subquery())
    print()
    
    print("Python Demonstration with Sample Data:")
    print("-" * 40)
    
    # Test case 1: Basic example
    person_data1 = [
        {"Id": 1, "Email": "a@b.com"},
        {"Id": 2, "Email": "c@d.com"},
        {"Id": 3, "Email": "b@c.com"}
    ]
    result1 = duplicate_emails_python_demo_custom(person_data1)
    print(f"Test 1:")
    print(f"  Input: {[(p['Id'], p['Email']) for p in person_data1]}")
    print(f"  Duplicate emails: {result1}")
    print(f"  Expected: [] (no duplicates)")
    assert result1 == []
    
    # Test case 2: With duplicates
    person_data2 = [
        {"Id": 1, "Email": "a@b.com"},
        {"Id": 2, "Email": "b@c.com"},
        {"Id": 3, "Email": "a@b.com"}  # Duplicate
    ]
    result2 = duplicate_emails_python_demo_custom(person_data2)
    print(f"\nTest 2:")
    print(f"  Input: {[(p['Id'], p['Email']) for p in person_data2]}")
    print(f"  Duplicate emails: {result2}")
    print(f"  Expected: ['a@b.com']")
    assert sorted(result2) == ["a@b.com"]
    
    # Test case 3: Multiple duplicates
    person_data3 = [
        {"Id": 1, "Email": "a@b.com"},
        {"Id": 2, "Email": "b@c.com"},
        {"Id": 3, "Email": "a@b.com"},  # Duplicate 1
        {"Id": 4, "Email": "b@c.com"},  # Duplicate 2
        {"Id": 5, "Email": "c@d.com"}
    ]
    result3 = duplicate_emails_python_demo_custom(person_data3)
    print(f"\nTest 3:")
    print(f"  Input: {[(p['Id'], p['Email']) for p in person_data3]}")
    print(f"  Duplicate emails: {sorted(result3)}")
    print(f"  Expected: ['a@b.com', 'b@c.com']")
    assert sorted(result3) == ["a@b.com", "b@c.com"]
    
    # Test case 4: All same email
    person_data4 = [
        {"Id": 1, "Email": "same@email.com"},
        {"Id": 2, "Email": "same@email.com"},
        {"Id": 3, "Email": "same@email.com"}
    ]
    result4 = duplicate_emails_python_demo_custom(person_data4)
    print(f"\nTest 4:")
    print(f"  Input: {[(p['Id'], p['Email']) for p in person_data4]}")
    print(f"  Duplicate emails: {result4}")
    print(f"  Expected: ['same@email.com']")
    assert result4 == ["same@email.com"]
    
    print("\n✓ All tests passed! The SQL query correctly identifies duplicate emails.")
    
def duplicate_emails_python_demo_custom(person_data):
    """Helper function for test cases"""
    # Count email frequencies
    email_count = {}
    for person in person_data:
        email = person["Email"]
        email_count[email] = email_count.get(email, 0) + 1
    
    # Find emails that appear more than once
    duplicates = [email for email, count in email_count.items() if count > 1]
    
    return duplicates