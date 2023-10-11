import tkinter as tk
from tkinter import PhotoImage, messagebox, simpledialog

# Constants
BG_COLOR = "#F9DEC9"

class PurchaseWindow(tk.Toplevel):
    """Popup window for completing a purchase."""
    def __init__(self, master, shoe_name):
        super().__init__(master)
        self.title(f"Purchase {shoe_name}")
        self.configure(bg=BG_COLOR)

        # Labels and Entry widgets for user information
        name_label = tk.Label(self, text="Name:", bg=BG_COLOR)
        name_label.pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)

        address_label = tk.Label(self, text="Address:", bg=BG_COLOR)
        address_label.pack(pady=5)
        self.address_entry = tk.Entry(self)
        self.address_entry.pack(pady=5)

        card_label = tk.Label(self, text="Card Number:", bg=BG_COLOR)
        card_label.pack(pady=5)
        self.card_entry = tk.Entry(self)
        self.card_entry.pack(pady=5)

        # Button to complete the purchase
        purchase_button = tk.Button(self, text="Purchase", command=self.complete_purchase)
        purchase_button.pack(pady=10)

        # Button to exit the purchase window
        exit_button = tk.Button(self, text="Exit", command=self.destroy)
        exit_button.pack(pady=10)

    def complete_purchase(self):
        """Callback function for the 'Purchase' button."""
        # Retrieve user information
        name = self.name_entry.get()
        address = self.address_entry.get()
        card_number = self.card_entry.get()

        # Perform additional actions (e.g., send purchase information to a server, etc.)
        
        messagebox.showinfo("Purchase Complete", f"Thank you, {name}! Your purchase is complete.\n"
                                                  f"Item will be shipped to {address}.\n"
                                                  f"Card ending in {card_number[-4:]} was charged.")
        self.destroy()

class DetailsWindow(tk.Toplevel):
    """Popup window for displaying details of a selected shoe."""
    def __init__(self, master, selected_shoe):
        super().__init__(master)
        self.title(f"Details of {selected_shoe[0]}")
        self.configure(bg=BG_COLOR)

        # Displaying details of the selected shoe
        details_label = tk.Label(self, text=f"Description: {selected_shoe[2]}", bg=BG_COLOR)
        details_label.pack(pady=10)

        price_label = tk.Label(self, text=f"Price: {selected_shoe[1]}", bg=BG_COLOR)
        price_label.pack(pady=5)

        # Photo for the shoe
        image_path = f"{selected_shoe[0].lower().replace(' ', '_').replace('-', '_')}.png"
        try:
            shoe_image = PhotoImage(file=image_path)
           
            shoe_image = shoe_image.subsample(2, 2)
        except tk.TclError as e:
            print(f"Error loading image '{image_path}': {e}")
            shoe_image = None

        if shoe_image:
            shoe_label = tk.Label(self, image=shoe_image, bg=BG_COLOR)
            shoe_label.photo = shoe_image  # To prevent the image from being garbage collected
            shoe_label.pack(pady=10)
        else:
            print("Image not loaded successfully.")

        # Button to purchase
        purchase_button = tk.Button(self, text="Purchase", command=lambda: self.on_purchase_button(selected_shoe))
        purchase_button.pack(pady=5)

        # Button to exit
        exit_button = tk.Button(self, text="Exit", command=self.on_exit_button)
        exit_button.pack(pady=5)

    def on_purchase_button(self, shoe):
        """Callback function for the 'Purchase' button."""
        # Additional actions to perform when the "Purchase" button is clicked
        PurchaseWindow(self.master, shoe[0])

    def on_exit_button(self):
        """Callback function for the 'Exit' button."""
        self.destroy()

class ShoeFrame(tk.LabelFrame):
    """Frame for displaying details of a shoe."""
    def __init__(self, master, shoe):
        super().__init__(master, text=f"{shoe[0]} - {shoe[1]}", bg=BG_COLOR)
        self.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Display shoe details
        details_label = tk.Label(self, text=f"Description: {shoe[2]}", bg=BG_COLOR)
        details_label.pack(pady=5)

        # Button to see details
        see_details_button = tk.Button(self, text="See Details", command=lambda: self.on_see_details_button(shoe))
        see_details_button.pack(pady=5)

        # Photo for the shoe
        image_path = f"{shoe[0].lower().replace(' ', '_').replace('-', '_')}.png"
        try:
            shoe_image = PhotoImage(file=image_path)
           
            shoe_image = shoe_image.subsample(2, 2)
        except tk.TclError as e:
            print(f"Error loading image '{image_path}': {e}")
            shoe_image = None

        if shoe_image:
            shoe_label = tk.Label(self, image=shoe_image, bg=BG_COLOR)
            shoe_label.photo = shoe_image  
            shoe_label.pack(pady=10)
        else:
            print("Image not loaded successfully.")

    def on_see_details_button(self, shoe):
        """Callback function for the 'See Details' button."""
        # Additional actions to perform when the "See Details" button is clicked
        DetailsWindow(self.master, shoe)

class ShoeApp:
    """Main application class for the shoe marketplace."""
    def __init__(self, root):
        self.root = root
        self.root.title("Zshoes - Trendy Shoes Marketplace")
        self.root.configure(bg=BG_COLOR)

        # Brief text about the purpose of the app
        intro_label = tk.Label(root, text="Welcome to Zshoes - Your Ultimate Destination for Trendy and Trusted Shoe Shopping!",
                               bg=BG_COLOR, font=("Helvetica", 16, "bold"))
        intro_label.pack(pady=10)

        # Brief resume about Zshoes
        resume_text = ("Zshoes stands out as a premier online marketplace, offering a curated selection of the latest and "
                       "most stylish footwear for the discerning consumer. As one of the most important and trustworthy "
                       "places to buy shoes in today's market, Zshoes has earned its reputation through a commitment to "
                       "quality, trendsetting designs, and a seamless shopping experience.")

        resume_label = tk.Label(root, text=resume_text, bg=BG_COLOR, wraplength=600)
        resume_label.pack(pady=10)

        # Frame to hold the list of shoes
        shoes_frame = tk.Frame(root, bg=BG_COLOR)
        shoes_frame.pack(padx=10, pady=10)

        # Adding some sample shoes
        trending_shoes = [("Nike Air Max", "$120", "Comfortable and stylish."),
                          ("Adidas Superstar", "$90", "Classic design for everyday wear."),
                          ("Puma RS-X", "$100", "Futuristic and trendy.")]

        # Create a ShoeFrame for each shoe
        for shoe in trending_shoes:
            ShoeFrame(shoes_frame, shoe).pack(side=tk.LEFT, padx=10)  # Pack each ShoeFrame side by side

        # Button to exit the application
        exit_button = tk.Button(root, text="Exit", command=self.on_exit_button)
        exit_button.pack(pady=10)

    def on_exit_button(self):
        """Callback function for the 'Exit' button."""
        # Additional actions to perform when the "Exit" button is clicked
        if messagebox.askokcancel("Exit", "Do you really want to exit?"):
            self.root.destroy()

def main():
    root = tk.Tk()
    app = ShoeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
