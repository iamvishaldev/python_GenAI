"""
========================================
🐍 PYTHON CORE NOTES (REVISION FILE)
Author: Vishal
========================================
"""

# ========================================
# 🧠 1. VARIABLES = REFERENCES
# ========================================

x = 10
print("x1:", id(x))

x = 11
print("x2:", id(x))  # New object created


# ========================================
# 🟡 2. SAME OBJECT REFERENCE
# ========================================

x = 12
y = x

print("x:", x, "y:", y)
print("Same ID:", id(x), id(y))  # Same memory


# ========================================
# 🔴 3. MUTABLE OBJECTS
# ========================================

x = [1, 2, 3]
y = x

y.append(4)

print("Mutable:", x)  # Both updated


# ========================================
# 🔵 4. IMMUTABLE OBJECTS
# ========================================

x = 10
y = x

y = y + 5

print("x:", x)  # 10
print("y:", y)  # 15
print("Different ID:", id(x), id(y))


# ========================================
# 🚀 5. LEGB RULE
# ========================================

# L → Local
# E → Enclosing
# G → Global
# B → Built-in


# ========================================
# 🟢 6. LOCAL SCOPE
# ========================================

def test():
    x = 10
    print("Local:", x)

test()


# ========================================
# 🟡 7. ENCLOSING SCOPE
# ========================================

def outer():
    x = "chai"

    def inner():
        x = "coffee"  # New local
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()


# ========================================
# 🔴 8. GLOBAL SCOPE
# ========================================

counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()

print("Global:", counter)


# ========================================
# 🔥 9. NONLOCAL (IMPORTANT)
# ========================================

def update_order():
    chai_type = "Elaichi"

    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"

    print("Before:", chai_type)
    kitchen()
    print("After:", chai_type)

update_order()


# ========================================
# ❌ 10. WITHOUT NONLOCAL (BUG CASE)
# ========================================

def update_order_bug():
    chai_type = "Elaichi"

    def kitchen():
        chai_type = "Kesar"  # New local (bug)

    kitchen()
    print("Bug Output:", chai_type)

update_order_bug()


# ========================================
# 💡 FINAL NOTES
# ========================================

"""
✔ Variables = references
✔ Mutable → same object change
✔ Immutable → new object
✔ nonlocal → modify enclosing scope
✔ global → modify global variable
"""