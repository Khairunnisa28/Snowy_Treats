import tkinter as tk
from tkinter import messagebox, simpledialog, PhotoImage

# Program E-Commerce Snowy Treats

# Daftar menu es krim
menu = {
    "Vanilla": 15000,
    "Chocolate": 15000,
    "Strawberry": 15000,
    "Choco Chip": 20000,
    "Strawberry Cheesecake": 25000,
    "Peanut Butter 'n Chocolate": 25000
}

# Keranjang belanja
cart = {}

# Pilihan ukuran
sizes = {
    "Small": 5000,
    "Medium": 10000,
    "Large": 15000,
    "Cone": 0
}

def add_to_cart(flavor, size, quantity):
    if flavor in menu and size in sizes:
        price = menu[flavor] + sizes[size]
        if flavor in cart:
            cart[flavor]['quantity'] += quantity
        else:
            cart[flavor] = {'size': size, 'quantity': quantity, 'price': price}
        messagebox.showinfo("Info", f"{quantity} {size} {flavor} berhasil ditambahkan ke keranjang.")
        reset_button_colors()
    else:
        messagebox.showerror("Error", "Rasa atau ukuran tidak tersedia.")

def view_cart():
    if not cart:
        cart_text.set("Keranjang belanja kosong.")
    else:
        items = [f"{flavor} ({info['size']}) x{info['quantity']}: Rp {int(info['price'] * info['quantity'])}" for flavor, info in cart.items()]
        cart_text.set("\n".join(items))

def calculate_total():
    total = sum(info['price'] * info['quantity'] for info in cart.values())
    return total

def checkout():
    if not cart:
        messagebox.showerror("Error", "Keranjang belanja kosong. Tidak bisa checkout.")
    else:
        total = calculate_total()

        # Tampilkan informasi produk yang dibeli
        checkout_details = "Produk yang Dibeli:\n"
        for flavor, info in cart.items():
            checkout_details += f"{flavor} ({info['size']}) x{info['quantity']} = Rp {int(info['price'] * info['quantity'])}\n"

        checkout_details += f"\nTotal: Rp {int(total)}"

        # Input uang dari customer
        customer_money = simpledialog.askfloat("Pembayaran", f"Total belanja: Rp {int(total)}\nMasukkan uang yang diberikan: ", parent=root)

        if customer_money is not None:
            if customer_money < total:
                messagebox.showerror("Error", "Uang yang diberikan tidak cukup.")
            else:
                change = customer_money - total
                checkout_details += f"\nUang yang diberikan: Rp {int(customer_money)}\nKembalian: Rp {int(change)}"
                messagebox.showinfo("Checkout", checkout_details)
                cart.clear()  # Kosongkan keranjang setelah checkout
                cart_text.set("Keranjang belanja kosong.")
                quantity_entry.delete(0, tk.END)  # Reset input jumlah menjadi 0

# Fungsi untuk mereset warna tombol
def reset_button_colors():
    # Reset warna tombol rasa
    for button in [vanilla_button, chocolate_button, strawberry_button, choco_chip_button, strawberry_cheesecake_button, peanut_butter_button]:
        button.config(bg="SystemButtonFace")
    
    # Reset warna tombol ukuran
    for button in [cone_button, small_button, medium_button, large_button]:
        button.config(bg="SystemButtonFace")

# GUI Setup
root = tk.Tk()
root.title("Snowy Treats")

# Images for menu items
vanilla_img = PhotoImage(file="vanilla.png").subsample(4, 4)
chocolate_img = PhotoImage(file="chocolate.png").subsample(4, 4)
strawberry_img = PhotoImage(file="strawberry.png").subsample(4, 4)
choco_chip_img = PhotoImage(file="choco_chip.png").subsample(4, 4)
strawberry_cheesecake_img = PhotoImage(file="strawberry_cheesecake.png").subsample(4, 4)
peanut_butter_img = PhotoImage(file="peanut_butter.png").subsample(4, 4)
product_img = PhotoImage(file="product.png")

# Menu Label
menu_label = tk.Label(root, text="--- Menu Snowy Treats ---", font=("Arial", 14))
menu_label.pack()

# Product Image
product_image_label = tk.Label(root, image=product_img)
product_image_label.pack(pady=10)

# Title for Ice Cream Variants
variant_title_label = tk.Label(root, text="Pilih Varian Ice Cream", font=("Arial", 10))
variant_title_label.pack(pady=5)

# Menu Buttons
menu_frame = tk.Frame(root)
menu_frame.pack()

def select_flavor(flavor, button):
    reset_button_colors()
    selected_flavor.set(flavor)
    button.config(bg="lightblue")

selected_flavor = tk.StringVar()
selected_size = tk.StringVar(value="Small")

vanilla_button = tk.Button(menu_frame, image=vanilla_img, text="Vanilla\n Rp 15000", compound="top", width=100, height=100, command=lambda: select_flavor("Vanilla", vanilla_button))
vanilla_button.grid(row=0, column=0, padx=10, pady=10)

chocolate_button = tk.Button(menu_frame, image=chocolate_img, text="Chocolate\n RP 15000", compound="top", width=100, height=100, command=lambda: select_flavor("Chocolate", chocolate_button))
chocolate_button.grid(row=0, column=1, padx=10, pady=10)

strawberry_button = tk.Button(menu_frame, image=strawberry_img, text="Strawberry\n Rp 15000", compound="top", width=100, height=100, command=lambda: select_flavor("Strawberry", strawberry_button))
strawberry_button.grid(row=0, column=2, padx=10, pady=10)

choco_chip_button = tk.Button(menu_frame, image=choco_chip_img, text="Choco Chip\n Rp 20000", compound="top", width=100, height=100, command=lambda: select_flavor("Choco Chip", choco_chip_button))
choco_chip_button.grid(row=1, column=0, padx=10, pady=10)

strawberry_cheesecake_button = tk.Button(menu_frame, image=strawberry_cheesecake_img, text="Strawberry Cheese\n Rp 25000", compound="top", width=100, height=100, command=lambda: select_flavor("Strawberry Cheesecake", strawberry_cheesecake_button))
strawberry_cheesecake_button.grid(row=1, column=1, padx=10, pady=10)

peanut_butter_button = tk.Button(menu_frame, image=peanut_butter_img, text="Peanut n Chocolate\n Rp 25000", compound="top", width=100, height=100, command=lambda: select_flavor("Peanut Butter 'n Chocolate", peanut_butter_button))
peanut_butter_button.grid(row=1, column=2, padx=10, pady=10)

# Size Selection
size_label = tk.Label(root, text="Pilih Ukuran:")
size_label.pack()

size_frame = tk.Frame(root)
size_frame.pack(pady=10)

def select_size(size, button):
    reset_button_colors()
    selected_size.set(size)
    button.config(bg="lightgreen")

cone_button = tk.Button(size_frame, text="Cone\nRp 0", compound="top", width=10, height=3, command=lambda: select_size("Cone", cone_button))
cone_button.pack(side="left", padx=10)

small_button = tk.Button(size_frame, text="Cup Small\nRp 5000", width=10, height=3, command=lambda: select_size("Small", small_button))
small_button.pack(side="left", padx=10)

medium_button = tk.Button(size_frame, text="Cup Medium\nRp 10.000", width=10, height=3, command=lambda: select_size("Medium", medium_button))
medium_button.pack(side="left", padx=10)

large_button = tk.Button(size_frame, text="Cup Large\nRp 15.000", width=10, height=3, command=lambda: select_size("Large", large_button))
large_button.pack(side="left", padx=10)

# Quantity Input
quantity_label = tk.Label(root, text="Jumlah:")
quantity_label.pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

add_button = tk.Button(root, text="Tambah ke Keranjang", command=lambda: add_to_cart(selected_flavor.get(), selected_size.get(), int(quantity_entry.get())))
add_button.pack()

# Cart Section
cart_label = tk.Label(root, text="--- Keranjang Belanja ---", font=("Arial", 14))
cart_label.pack()

cart_text = tk.StringVar()
cart_text.set("Keranjang belanja kosong.")
cart_display = tk.Label(root, textvariable=cart_text, justify=tk.LEFT)
cart_display.pack()

view_cart_button = tk.Button(root, text="Lihat Keranjang", command=view_cart)
view_cart_button.pack()

# Checkout Button
checkout_button = tk.Button(root, text="Checkout", command=checkout)
checkout_button.pack()

# Run the Application
try:
    root.mainloop()
except Exception as e:
    print(f"Error: {e}")
