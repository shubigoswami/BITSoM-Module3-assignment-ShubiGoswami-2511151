import requests
from datetime import datetime

BASE_URL = "https://dummyjson.com/products"
LOG_FILE = "error_log.txt"


# ----------------
# LOGGER
# ------------------
def log_error(function_name, error_type, message):
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] ERROR in {function_name}: {error_type} — {message}\n")


# ---------------
# TASK 1 — FILE I/O
# ------------
def file_operations():
    try:
        with open("python_notes.txt", "w", encoding="utf-8") as file:
            file.write("Topic 1: Variables store data.\n")
            file.write("Topic 2: Lists are ordered and mutable.\n")
            file.write("Topic 3: Dictionaries store key-value pairs.\n")
            file.write("Topic 4: Loops automate tasks.\n")
            file.write("Topic 5: Exception handling prevents crashes.\n")

        with open("python_notes.txt", "a", encoding="utf-8") as file:
            file.write("Topic 6: Functions reuse code.\n")
            file.write("Topic 7: APIs connect systems.\n")

        print("File written and appended.")

    except Exception as e:
        log_error("file_operations", "Error", str(e))


# -------------
# TASK 2 — API FETCH
# ---------------
def fetch_products():
    try:
        response = requests.get(f"{BASE_URL}?limit=20", timeout=5)

        if response.status_code == 200:
            products = response.json().get("products", [])

            print("\n--- Products ---")
            for p in products:
                print(f"{p['id']} | {p['title']} | ${p['price']} | {p['rating']}")

            return products
        else:
            log_error("fetch_products", "HTTPError", str(response.status_code))

    except requests.exceptions.ConnectionError:
        log_error("fetch_products", "ConnectionError", "No internet")
    except requests.exceptions.Timeout:
        log_error("fetch_products", "Timeout", "Slow response")

    return []


# --------------
# TASK 3 — SAFE DIVIDE
# ---------------
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid types"


# -------------
# TASK 3 — PRODUCT LOOKUP LOOP
# ---------------
def product_lookup_loop():
    while True:
        user_input = input("\nEnter product ID (1–100) or 'quit': ")

        if user_input.lower() == "quit":
            break

        if not user_input.isdigit():
            print("Enter a valid number")
            continue

        pid = int(user_input)

        if not (1 <= pid <= 100):
            print("Out of range")
            continue

        try:
            response = requests.get(f"{BASE_URL}/{pid}", timeout=5)

            if response.status_code == 200:
                p = response.json()
                print(f"{p['title']} - ${p['price']}")
            elif response.status_code == 404:
                print("Product not found")
                log_error("lookup_product", "HTTPError", "404 Not Found")

        except requests.exceptions.ConnectionError:
            print("No internet")
        except requests.exceptions.Timeout:
            print("Timeout")


# ------------
# TASK 4 — LOGGING TEST
# ----------
def trigger_errors():
    # Connection error
    try:
        requests.get("https://fake-url-xyz.com", timeout=5)
    except requests.exceptions.ConnectionError:
        log_error("fetch_products", "ConnectionError", "No connection")

    # HTTP 404
    try:
        response = requests.get(f"{BASE_URL}/999", timeout=5)
        if response.status_code == 404:
            log_error("lookup_product", "HTTPError", "404 Not Found")
    except Exception as e:
        log_error("lookup_product", "Error", str(e))


def display_logs():
    print("\n--- LOG FILE ---")
    try:
        with open(LOG_FILE, "r") as f:
            print(f.read())
    except:
        print("No logs yet")


# -----------------
# MAIN ( ONE ENTRY POINT)
# ------------------
if __name__ == "__main__":
    file_operations()

    products = fetch_products()

    print("\nSafe Divide Tests:")
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    print(safe_divide("ten", 2))

    trigger_errors()
    display_logs()

    # Uncomment if needed
    # product_lookup_loop()