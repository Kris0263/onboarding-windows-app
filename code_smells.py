# ============================
# 📌 Code Smells and Refactoring Examples
# ============================

# 1. Magic Numbers
# ----------------

# Before: Using a hardcoded discount rate
def calculate_discount_before(price):
    return price * 0.1  # 0.1 represents a 10% discount

# After: Using a named constant for the discount rate
DISCOUNT_RATE = 0.1

def calculate_discount(price):
    return price * DISCOUNT_RATE

# 2. Long Functions
# -----------------

# Before: A function handling multiple responsibilities
def process_order_before(order):
    validate_order(order)
    calculate_totals(order)
    apply_discounts(order)
    update_inventory(order)
    send_confirmation_email(order)
    log_order(order)

# After: Breaking the function into smaller, focused functions
def process_order(order):
    validate_order(order)
    calculate_order(order)
    finalize_order(order)

def calculate_order(order):
    calculate_totals(order)
    apply_discounts(order)

def finalize_order(order):
    update_inventory(order)
    send_confirmation_email(order)
    log_order(order)

# 3. Duplicate Code
# -----------------

# Before: Separate functions with similar logic
def calculate_area_rectangle(length, width):
    return length * width

def calculate_area_square_before(side):
    return side * side

# After: Reusing existing functions to eliminate duplication
def calculate_area_square(side):
    return calculate_area_rectangle(side, side)

# 4. Large Classes (God Objects)
# ------------------------------

# Before: A class handling multiple responsibilities
class OrderManagerBefore:
    def create_order(self):
        pass
    def process_payment(self):
        pass
    def update_inventory(self):
        pass
    def send_email(self):
        pass

# After: Dividing responsibilities among specialized classes
class OrderManager:
    def create_order(self):
        pass

class PaymentProcessor:
    def process_payment(self):
        pass

class InventoryManager:
    def update_inventory(self):
        pass

class EmailService:
    def send_email(self):
        pass

# 5. Deeply Nested Conditionals
# -----------------------------

# Before: Multiple nested if statements
def edit_document_if_allowed_before(user, document):
    if user.is_authenticated():
        if user.has_permission('edit'):
            if document.is_editable():
                edit_document(document)

# After: Flattening conditionals for better readability
def edit_document_if_allowed(user, document):
    if not user.is_authenticated():
        return
    if not user.has_permission('edit'):
        return
    if not document.is_editable():
        return
    edit_document(document)


# ----------------------

# Before: Non-descriptive function name
def calc():
    pass

# After: Descriptive and consistent function name
def calculate_total():
    pass

