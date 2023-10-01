import tkinter as tk
from tkinter import messagebox

class ZshoesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zshoes - Trendy Shoes Marketplace")

        # Brief text about the purpose of the app
        intro_label = tk.Label(root, text="Welcome to Zshoes - Your Trendy Shoes Marketplace!")
        intro_label.pack(pady=10)

        # Frame to hold the list of shoes
        shoes_frame = tk.Frame(root)
        shoes_frame.pack(padx=10, pady=10, side=tk.LEFT)

        # Adding some sample shoes
        trending_shoes = [("Nike Air Max", "$120", "Comfortable and stylish."),
                          ("Adidas Superstar", "$90", "Classic design for everyday wear."),
                          ("Puma RS-X", "$100", "Futuristic and trendy.")]

        # Create a LabelFrame for each shoe
        for shoe in trending_shoes:
            shoe_frame = tk.LabelFrame(shoes_frame, text=f"{shoe[0]} - {shoe[1]}")
            shoe_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

            # Display shoe details
            details_label = tk.Label(shoe_frame, text=f"Description: {shoe[2]}")
            details_label.pack(pady=5)

            # Button to view details
            details_button = tk.Button(shoe_frame, text="View Details", command=lambda s=shoe: self.show_details(s))
            details_button.pack(pady=5)

    def show_details(self, selected_shoe):
        details_window = tk.Toplevel(self.root)
        details_window.title(f"Details of {selected_shoe[0]}")

        # Displaying details of the selected shoe
        details_label = tk.Label(details_window, text=f"Description: {selected_shoe[2]}")
        details_label.pack(pady=10)

        price_label = tk.Label(details_window, text=f"Price: {selected_shoe[1]}")
        price_label.pack(pady=5)

        # Button to close the details window
        close_button = tk.Button(details_window, text="Close", command=details_window.destroy)
        close_button.pack(pady=10)

def main():
    root = tk.Tk()
    app = ZshoesApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
