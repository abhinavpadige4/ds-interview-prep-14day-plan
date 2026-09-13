"""
LeetCode Problem 175: Combine Two Tables
Difficulty: Easy
Topics: Database

Problem:
Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| personId    | int     |
| firstName   | varchar |
| lastName    | varchar |
+-------------+---------+
personId is the primary key column for this table.

Table: Address
+-------------+---------+
| Column Name | Type    |
+ 
+-------------+---------+
| addressId   | int     |
| personId    | int     |
| city        | varchar |
| state       | varchar |
+-------------+---------+
addressId is the primary key column for this table.

Write a SQL query to report the first name, last name, city, and state of each person in the Person table. 
If the address of a personId is not present in the Address table, report null instead.

Return the result table in any order.

Example:
Input: 
Person table:
+----------+----------+-----------+
| personId | firstName| lastName  |
+----------+----------+-----------+
| 1        | Wang     | Allen     |
| 2        | Alice    | Bob       |
+----------+----------+-----------+
Address table:
+-----------+----------+-------+--------+
| addressId | personId | city  | state  |
+-----------+----------+-------+--------+
| 1         | 2        | New York | New York |
| 2         | 3        | Leetcode | None     |
+-----------+----------+-------+--------+
Output: 
+----------+----------+-----------+----------+
| firstName| lastName | city      | state    |
+----------+----------+-----------+----------+
| Wang     | Allen    | null      | null     |
| Alice    | Bob      | New York  | New York |
+----------+----------+-----------+----------+

Approach:
Use LEFT JOIN to combine Person table with Address table on personId.
This ensures all records from Person table are included, with matching 
address information where available, and NULL values where not present.
"""

# Since this is a SQL problem, we'll provide the SQL solution as a comment
# and also create a Python function that demonstrates the logic

def combine_tables_sql():
    """
    Returns the SQL query to solve LeetCode 175: Combine Two Tables
    
    Returns:
        str: The SQL query string
    """
    sql_query = """
SELECT 
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a ON p.personId = a.personId;
"""
    return sql_query.strip()

# Alternative: Using LEFT JOIN explicitly
def combine_tables_explicit_left_join():
    """
    Alternative SQL query using explicit LEFT JOIN keyword
    """
    sql_query = """
SELECT 
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a 
    ON p.personId = a.personId;
"""
    return sql_query.strip()

# Demonstration with sample data using Python (for educational purposes)
def combine_tables_python_demo():
    """
    Demonstrates the logic using Python data structures
    (This is for educational purposes only - the actual solution is SQL)
    """
    # Sample Person data
    person_data = [
        {"personId": 1, "firstName": "Wang", "lastName": "Allen"},
        {"personId": 2, "firstName": "Alice", "lastName": "Bob"}
    ]
    
    # Sample Address data
    address_data = [
        {"addressId": 1, "personId": 2, "city": "New York", "state": "New York"},
        {"addressId": 2, "personId": 3, "city": "Leetcode", "state": None}
    ]
    
    # Create a dictionary for quick address lookup by personId
    address_dict = {addr["personId"]: addr for addr in address_data}
    
    # Perform LEFT JOIN equivalent
    result = []
    for person in person_data:
        person_id = person["personId"]
        address_info = address_dict.get(person_id, {"city": None, "state": None})
        
        result.append({
            "firstName": person["firstName"],
            "lastName": person["lastName"],
            "city": address_info["city"],
            "state": address_info["state"]
        })
    
    return result

# Test cases
if __name__ == "__main__":
    print("LeetCode 175: Combine Two Tables - SQL Solution")
    print("=" * 50)
    print("SQL Query:")
    print(combine_tables_sql())
    print()
    
    print("Alternative SQL Query:")
    print(combine_tables_explicit_left_join())
    print()
    
    print("Python Demonstration with Sample Data:")
    print("-" * 40)
    result = combine_tables_python_demo()
    
    print("Input Person table:")
    print("+----------+----------+-----------+")
    print("| personId | firstName| lastName  |")
    print("+----------+----------+-----------+")
    for person in [{"personId": 1, "firstName": "Wang", "lastName": "Allen"},
                   {"personId": 2, "firstName": "Alice", "lastName": "Bob"}]:
        print(f"| {person['personId']:^8} | {person['firstName']:^8} | {person['lastName']:^9} |")
    print("+----------+----------+-----------+")
    print()
    
    print("Input Address table:")
    print("+-----------+----------+-------+--------+")
    print("| addressId | personId | city  | state  |")
    print("+-----------+----------+-------+--------+")
    for addr in [{"addressId": 1, "personId": 2, "city": "New York", "state": "New York"},
                 {"addressId": 2, "personId": 3, "city": "Leetcode", "state": None}]:
        city = addr["city"] if addr["city"] is not None else "null"
        state = addr["state"] if addr["state"] is not None else "null"
        print(f"| {addr['addressId']:^9} | {addr['personId']:^8} | {city:^5} | {state:^6} |")
    print("+-----------+----------+-------+--------+")
    print()
    
    print("Output Result:")
    print("+----------+----------+-----------+----------+")
    print("| firstName| lastName | city      | state    |")
    print("+----------+----------+-----------+----------+")
    for row in result:
        first_name = row["firstName"]
        last_name = row["lastName"]
        city = row["city"] if row["city"] is not None else "null"
        state = row["state"] if row["state"] is not None else "null"
        print(f"| {first_name:^8} | {last_name:^8} | {city:^9} | {state:^8} |")
    print("+----------+----------+-----------+----------+")
    print()
    
    # Verify expected results
    expected_first_names = ["Wang", "Alice"]
    expected_last_names = ["Allen", "Bob"]
    expected_cities = [None, "New York"]
    expected_states = [None, "New York"]
    
    assert len(result) == 2
    assert result[0]["firstName"] == "Wang"
    assert result[0]["lastName"] == "Allen"
    assert result[0]["city"] is None
    assert result[0]["state"] is None
    assert result[1]["firstName"] == "Alice"
    assert result[1]["lastName"] == "Bob"
    assert result[1]["city"] == "New York"
    assert result[1]["state"] == "New York"
    
    print("✓ All tests passed! The SQL query correctly implements LEFT JOIN logic.")