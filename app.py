import json
from pathlib import Path
import streamlit as st


class Shop:
    """
    Malik Mobile Accessories Shop

    Handles:
    - Product management
    - Inventory
    - Orders
    - Order cancellation
    - JSON database
    """

    DATABASE = Path("data.json")


    def __init__(self):
        self.data_file = "data.json"
        self.data = self.load_data()


    # ========================================================
    # DATABASE
    # ========================================================
    def load_data(self):
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)

            if isinstance(data, list):
                data = {
                    "products": data,
                    "customers": [],
                    "orders": []
                }

            data.setdefault("products", [])
            data.setdefault("customers", [])
            data.setdefault("orders", [])

            return data

        except FileNotFoundError:
            return {
                "products": [],
                "customers": [],
                "orders": []
            }

        except json.JSONDecodeError:
            return {
                "products": [],
                "customers": [],
                "orders": []
            }


    

    def save_data(self):
        """Save current data to JSON file."""

        try:
            with self.DATABASE.open(
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    self.data,
                    file,
                    indent=4
                )

            return True

        except OSError as error:
            st.error(
                f"Unable to save database: {error}"
            )

            return False

    # ========================================================
    # PRODUCT MANAGEMENT
    # ========================================================

    def add_product( self,product_name,quantity,price):
        """
        Add a new product.

        If product already exists,
        its quantity is increased.
        """

        product_name = product_name.strip()

        if not product_name:
            return False, "Product name cannot be empty."

        if quantity <= 0:
            return False, "Quantity must be greater than 0."

        if price <= 0:
            return False, "Price must be greater than 0."

        # Check existing product
        for product in self.data["products"]:

            if (
                product["Product_Name"].lower()
                == product_name.lower()
            ):

                product["Quantity"] += quantity
                product["Price"] = price

                self.save_data()

                return (
                    True,
                    f"{product_name} stock updated successfully."
                )

        # Add new product
        new_product = {
            "Product_Name": product_name,
            "Quantity": quantity,
            "Price": price
        }

        self.data["products"].append(
            new_product
        )

        self.save_data()

        return (
            True,
            f"{product_name} added successfully."
        )

    def edit_product(
        self,
        current_product_name,
        new_product_name,
        quantity,
        price
    ):
        """Edit an existing product."""

        current_product_name = current_product_name.strip()
        new_product_name = new_product_name.strip()

        if not current_product_name:
            return False, "Please select a product to edit."

        if not new_product_name:
            return False, "Product name cannot be empty."

        if quantity < 0:
            return False, "Quantity cannot be negative."

        if price <= 0:
            return False, "Price must be greater than 0."

        for product in self.data["products"]:

            if (
                product["Product_Name"].lower()
                == current_product_name.lower()
            ):

                if (
                    new_product_name.lower()
                    != current_product_name.lower()
                ):
                    for other_product in self.data["products"]:

                        if (
                            other_product is not product
                            and other_product["Product_Name"].lower()
                            == new_product_name.lower()
                        ):
                            return (
                                False,
                                "A product with this name already exists."
                            )

                product["Product_Name"] = new_product_name
                product["Quantity"] = quantity
                product["Price"] = price

                for order in self.data["orders"]:
                    if (
                        order["Product_Name"].lower()
                        == current_product_name.lower()
                    ):
                        order["Product_Name"] = new_product_name

                self.save_data()

                return (
                    True,
                    f"{current_product_name} updated successfully."
                )

        return False, "Product not found."

    # ========================================================
    # GET PRODUCTS
    # ========================================================

    def get_products(self):
        """Return all products."""

        return self.data["products"]

    # ========================================================
    # PLACE ORDER
    # ========================================================

    def add_order(
        self,
        product_name,
        quantity
    ):
        """Place an order."""

        if quantity <= 0:
            return False, "Quantity must be greater than 0."

        for product in self.data["products"]:

            if (
                product["Product_Name"].lower()
                == product_name.lower()
            ):

                # Check stock
                if quantity > product["Quantity"]:
                    return (
                        False,
                        "Not enough stock available."
                    )

                # Calculate total
                total = quantity * product["Price"]

                # Reduce stock
                product["Quantity"] -= quantity

                # Create order
                order = {
                    "Product_Name": product["Product_Name"],
                    "Quantity": quantity,
                    "Price": product["Price"],
                    "Total": total
                }

                self.data["orders"].append(order)

                self.save_data()

                return True, total

        return False, "Product not found."

    # ========================================================
    # GET ORDERS
    # ========================================================

    def get_orders(self):
        """Return order history."""

        return self.data["orders"]

    # ========================================================
    # CANCEL ORDER
    # ========================================================

    def cancel_order(self, order_index):
        """
        Cancel an order.

        The ordered quantity is returned
        to inventory.
        """

        orders = self.data["orders"]

        if (
            order_index < 0
            or order_index >= len(orders)
        ):
            return False, "Invalid order."

        order = orders[order_index]

        # Find product
        for product in self.data["products"]:

            if (
                product["Product_Name"].lower()
                == order["Product_Name"].lower()
            ):

                # Return quantity to stock
                product["Quantity"] += order["Quantity"]

                # Remove order
                orders.pop(order_index)

                self.save_data()

                return (
                    True,
                    "Order cancelled successfully."
                )

        return (
            False,
            "Product associated with this order was not found."
        )

    # ========================================================
    # STATISTICS
    # ========================================================

    def total_products(self):
        return len(self.data["products"])

    def total_stock(self):
        return sum(
            product["Quantity"]
            for product in self.data["products"]
        )

    def total_orders(self):
        return len(self.data["orders"])

    def total_sales(self):
        return sum(
            order["Total"]
            for order in self.data["orders"]
        )


# ============================================================
# STREAMLIT CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Mobile Accessories Shop",
    page_icon="🛒",
    layout="wide"
)


# ============================================================
# CREATE SHOP OBJECT
# ============================================================

shop = Shop()


# ============================================================
# HEADER
# ============================================================

st.title("🛒 Malik Mobile Accessories Shop")
st.write(
    "Inventory and Order Management System"
)


# ============================================================
# DASHBOARD METRICS
# ============================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📦 Products",
        shop.total_products()
    )

with col2:
    st.metric(
        "📊 Total Stock",
        shop.total_stock()
    )

with col3:
    st.metric(
        "🛍️ Orders",
        shop.total_orders()
    )

with col4:
    st.metric(
        "💰 Total Sales",
        f"Rs. {shop.total_sales():,}"
    )


st.divider()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📋 Shop Menu")

choice = st.sidebar.radio(
    "Select Operation",
    [
        "🏠 Dashboard",
        "➕ Add Product",
        "✏️ Edit Product",
        "📦 See Products",
        "🛒 Add Order",
        "❌ Cancel Order",
        "📜 Order History"
    ]
)


# ============================================================
# DASHBOARD
# ============================================================

if choice == "🏠 Dashboard":

    st.header("🏠 Dashboard")

    products = shop.get_products()

    if not products:

        st.info(
            "Your shop currently has no products."
        )

    else:

        st.subheader("Inventory Overview")

        for product in products:

            quantity = product["Quantity"]

            if quantity == 0:
                status = "🔴 Out of Stock"

            elif quantity <= 5:
                status = "🟠 Low Stock"

            else:
                status = "🟢 In Stock"

            st.write(
                f"**{product['Product_Name']}**  "
                f"| Stock: {quantity}  "
                f"| Price: Rs. {product['Price']:,}  "
                f"| {status}"
            )


# ============================================================
# ADD PRODUCT
# ============================================================

elif choice == "➕ Add Product":

    st.header("➕ Add Product")

    with st.form("product_form"):

        product_name = st.text_input(
            "Product Name",
            placeholder="Example: USB Type-C Cable"
        )

        quantity = st.number_input(
            "Quantity",
            min_value=1,
            value=1,
            step=1
        )

        price = st.number_input(
            "Price (Rs.)",
            min_value=1,
            value=100,
            step=10
        )

        submit = st.form_submit_button(
            "Add Product",
            type="primary"
        )

    if submit:

        success, message = shop.add_product(
            product_name,
            quantity,
            price
        )

        if success:

            st.success(
                f"✅ {message}"
            )

            st.rerun()

        else:

            st.error(
                f"❌ {message}"
            )


# ============================================================
# EDIT PRODUCT
# ============================================================

elif choice == "✏️ Edit Product":

    st.header("✏️ Edit Product")

    products = shop.get_products()

    if not products:

        st.info(
            "There are no products to edit yet."
        )

    else:

        product_names = [
            product["Product_Name"]
            for product in products
        ]

        selected_product_name = st.selectbox(
            "Select Product to Edit",
            product_names
        )

        selected_product = next(
            product
            for product in products
            if product["Product_Name"]
            == selected_product_name
        )

        with st.form("edit_product_form"):

            new_product_name = st.text_input(
                "Product Name",
                value=selected_product["Product_Name"]
            )

            new_quantity = st.number_input(
                "Quantity",
                min_value=0,
                value=int(selected_product["Quantity"]),
                step=1
            )

            new_price = st.number_input(
                "Price (Rs.)",
                min_value=1,
                value=int(selected_product["Price"]),
                step=10
            )

            submit = st.form_submit_button(
                "Update Product",
                type="primary"
            )

        if submit:

            success, message = shop.edit_product(
                selected_product_name,
                new_product_name,
                new_quantity,
                new_price
            )

            if success:

                st.success(
                    f"✅ {message}"
                )

                st.rerun()

            else:

                st.error(
                    f"❌ {message}"
                )


# ============================================================
# SEE PRODUCTS
# ============================================================

elif choice == "📦 See Products":

    st.header("📦 Shop Products")

    products = shop.get_products()

    if not products:

        st.info(
            "Shop product list is empty."
        )

    else:

        product_table = []

        for index, product in enumerate(
            products,
            start=1
        ):

            quantity = product["Quantity"]

            if quantity == 0:
                status = "🔴 Out of Stock"

            elif quantity <= 5:
                status = "🟠 Low Stock"

            else:
                status = "🟢 In Stock"

            product_table.append(
                {
                    "#": index,
                    "Product Name": product["Product_Name"],
                    "Quantity": quantity,
                    "Price": f"Rs. {product['Price']:,}",
                    "Status": status
                }
            )

        st.dataframe(
            product_table,
            use_container_width=True,
            hide_index=True
        )


# ============================================================
# ADD ORDER
# ============================================================

elif choice == "🛒 Add Order":

    st.header("🛒 Add Order")

    products = shop.get_products()

    # Only products with stock
    available_products = [
        product
        for product in products
        if product["Quantity"] > 0
    ]

    if not available_products:

        st.warning(
            "No products are currently available."
        )

    else:

        product_names = [
            product["Product_Name"]
            for product in available_products
        ]

        selected_product = st.selectbox(
            "Select Product",
            product_names
        )

        # Find selected product
        selected = next(
            product
            for product in available_products
            if product["Product_Name"]
            == selected_product
        )

        st.info(
            f"Available Quantity: "
            f"**{selected['Quantity']}**\n\n"
            f"Price: "
            f"**Rs. {selected['Price']:,}**"
        )

        quantity = st.number_input(
            "Order Quantity",
            min_value=1,
            max_value=selected["Quantity"],
            value=1,
            step=1
        )

        total = (
            quantity
            * selected["Price"]
        )

        st.subheader(
            f"Total: Rs. {total:,}"
        )

        if st.button(
            "✅ Complete Order",
            type="primary"
        ):

            success, result = shop.add_order(
                selected_product,
                quantity
            )

            if success:

                st.success(
                    f"Order completed successfully! "
                    f"Total = Rs. {result:,}"
                )

                st.rerun()

            else:

                st.error(
                    f"❌ {result}"
                )


# ============================================================
# CANCEL ORDER
# ============================================================

elif choice == "❌ Cancel Order":

    st.header("❌ Cancel Order")

    orders = shop.get_orders()

    if not orders:

        st.info(
            "No previous orders found."
        )

    else:

        order_options = []

        for index, order in enumerate(
            orders,
            start=1
        ):

            order_options.append(
                f"{index}. "
                f"{order['Product_Name']} | "
                f"Quantity: {order['Quantity']} | "
                f"Total: Rs. {order['Total']:,}"
            )

        selected_order = st.selectbox(
            "Select Order",
            order_options
        )

        order_index = order_options.index(
            selected_order
        )

        st.warning(
            "Cancelling this order will return "
            "the quantity to your inventory."
        )

        if st.button(
            "❌ Cancel Selected Order",
            type="primary"
        ):

            success, message = shop.cancel_order(
                order_index
            )

            if success:

                st.success(
                    f"✅ {message}"
                )

                st.rerun()

            else:

                st.error(
                    f"❌ {message}"
                )


# ============================================================
# ORDER HISTORY
# ============================================================

elif choice == "📜 Order History":

    st.header("📜 Order History")

    orders = shop.get_orders()

    if not orders:

        st.info(
            "No orders have been placed yet."
        )

    else:

        order_table = []

        for index, order in enumerate(
            orders,
            start=1
        ):

            order_table.append(
                {
                    "#": index,
                    "Product": order["Product_Name"],
                    "Quantity": order["Quantity"],
                    "Price": f"Rs. {order['Price']:,}",
                    "Total": f"Rs. {order['Total']:,}"
                }
            )

        st.dataframe(
            order_table,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        st.metric(
            "💰 Total Sales",
            f"Rs. {shop.total_sales():,}"
        )


# ============================================================
# SIDEBAR FOOTER
# ============================================================

st.sidebar.divider()

st.sidebar.caption(
    "Mobile Accessories Shop"
)

st.sidebar.caption(
    "Powered by Python + Streamlit 🐍"
)
