## Magic numbers
def calculate_discount(price):
    return price * 0.1  # 0.1 represents a 10% discount

DISCOUNT_RATE = 0.1

def calculate_discount(price):
    return price * DISCOUNT_RATE

## Long Functions 
## Before
def process_order(order):
    validate_order(order)
    calculate_totals(order)
    apply_discounts(order)
    update_inventory(order)
    send_confirmation_email(order)
    log_order(order)

## After 
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

## Duplicate code
## Before
def calculate_area_rectangle(length, width):
    return length * width

def calculate_area_square(side):
    return side * side

## After 
def calculate_area_rectangle(length, width):
    return length * width

def calculate_area_square(side):
    return calculate_area_rectangle(side, side)

## Large Classes
## Before
class OrderManager:
    def create_order(self):
        pass
    def process_payment(self):
        pass
    def update_inventory(self):
        pass
    def send_email(self):
        pass

## After 
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

## Deeply Nested 
## Before
if user.is_authenticated():
    if user.has_permission('edit'):
        if document.is_editable():
            edit_document(document)


## After
if not user.is_authenticated():
    return
if not user.has_permission('edit'):
    return
if not document.is_editable():
    return
edit_document(document)


