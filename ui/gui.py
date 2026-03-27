import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

from tkinterdnd2 import DND_FILES, TkinterDnD

from core.stego_engine import hide_data, extract_data
from analysis.detector import analyze_image
from analysis.heatmap import generate_heatmap

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(TkinterDnD.Tk):

    def __init__(self):
        super().__init__()

        self.title("🔐 StegoVault Ultimate")
        self.geometry("1200x720")

        self.image_path = None
        self.files = []
        self.output_path = None

        self.original_img = None
        self.stego_img = None

        self.build()

    # ---------------- UI ---------------- #

    def build(self):

        self.grid_columnconfigure(1, weight=1)

        # LEFT PANEL
        left = ctk.CTkFrame(self, width=300)
        left.grid(row=0, column=0, sticky="ns", padx=10, pady=10)

        # RIGHT PANEL
        right = ctk.CTkFrame(self)
        right.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # TITLE
        ctk.CTkLabel(left, text="StegoVault Ultimate", font=("Arial", 22, "bold")).pack(pady=10)

        # SELECT IMAGE
        ctk.CTkButton(left, text="📂 Select Image", command=self.select_image).pack(pady=5)

        # DRAG DROP
        self.drop_label = ctk.CTkLabel(left, text="Drag & Drop Image Here", height=50)
        self.drop_label.pack(fill="x", pady=5)

        self.drop_label.drop_target_register(DND_FILES)
        self.drop_label.dnd_bind("<<Drop>>", self.drop_image)

        # ADD FILE
        ctk.CTkButton(left, text="📄 Add File", command=self.add_file).pack(pady=5)

        # TEXT INPUT
        self.text_input = ctk.CTkTextbox(left, height=100)
        self.text_input.pack(pady=5)
        self.text_input.insert("0.0", "Enter secret text here...")

        # PASSWORD
        self.password = ctk.CTkEntry(left, placeholder_text="Password", show="*")
        self.password.pack(pady=5)
        self.password.bind("<KeyRelease>", self.password_strength)

        self.strength_label = ctk.CTkLabel(left, text="Strength: ")
        self.strength_label.pack()

        # ACTION BUTTONS
        ctk.CTkButton(left, text="🔐 Hide Data", command=self.hide).pack(pady=5)
        ctk.CTkButton(left, text="🔓 Extract Data", command=self.extract).pack(pady=5)

        ctk.CTkButton(left, text="🔍 Analyze", command=self.analyze).pack(pady=5)
        ctk.CTkButton(left, text="🔥 Heatmap", command=self.heatmap).pack(pady=5)

        ctk.CTkButton(left, text="🔄 Reset", command=self.reset).pack(pady=5)
        ctk.CTkButton(left, text="❌ Exit", command=self.destroy).pack(pady=5)

        # STATUS
        self.status = ctk.CTkLabel(left, text="Ready", text_color="lightgreen")
        self.status.pack(pady=10)

        # RIGHT PANEL (IMAGES)
        ctk.CTkLabel(right, text="Image Comparison", font=("Arial", 18)).pack(pady=10)

        frame = ctk.CTkFrame(right)
        frame.pack(expand=True, fill="both")

        self.original_panel = ctk.CTkLabel(frame, text="Original Image")
        self.original_panel.pack(side="left", padx=10)

        self.stego_panel = ctk.CTkLabel(frame, text="Stego Image")
        self.stego_panel.pack(side="right", padx=10)

    # ---------------- FUNCTIONS ---------------- #

    def select_image(self):
        path = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp")])
        if path:
            self.image_path = path
            self.show_original(path)
            self.status.configure(text="Image selected ✅")
            messagebox.showinfo("Selected", os.path.basename(path))

    def drop_image(self, event):
        path = event.data.strip("{}")
        if os.path.isfile(path):
            self.image_path = path
            self.show_original(path)
            self.status.configure(text="Image loaded via Drag & Drop ✅")

    def show_original(self, path):
        img = Image.open(path)
        img.thumbnail((400, 400))
        self.original_img = ImageTk.PhotoImage(img)
        self.original_panel.configure(image=self.original_img, text="")

    def show_stego(self, path):
        img = Image.open(path)
        img.thumbnail((400, 400))
        self.stego_img = ImageTk.PhotoImage(img)
        self.stego_panel.configure(image=self.stego_img, text="")

    def add_file(self):
        path = filedialog.askopenfilename()
        if path:
            with open(path, "rb") as f:
                self.files.append((os.path.basename(path), f.read()))
            messagebox.showinfo("Added", os.path.basename(path))

    def password_strength(self, event=None):
        pwd = self.password.get()
        if len(pwd) < 4:
            s = "Weak"
        elif len(pwd) < 8:
            s = "Medium"
        else:
            s = "Strong"
        self.strength_label.configure(text=f"Strength: {s}")

    def hide(self):
        if not self.image_path:
            messagebox.showerror("Error", "Select image first!")
            return

        password = self.password.get()
        if not password:
            messagebox.showerror("Error", "Enter password!")
            return

        out = filedialog.asksaveasfilename(defaultextension=".png")
        if not out:
            return

        try:
            payload_files = list(self.files)

            # Add text as file
            text = self.text_input.get("1.0", "end").strip()
            if text:
                payload_files.append(("message.txt", text.encode()))

            if not payload_files:
                messagebox.showerror("Error", "No data to hide")
                return

            hide_data(self.image_path, payload_files, password, out)

            self.output_path = out
            self.show_stego(out)

            self.status.configure(text="Hidden successfully 🎉")
            messagebox.showinfo("Success", "Data hidden successfully!")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def extract(self):
        if not self.image_path:
            messagebox.showerror("Error", "Select image first!")
            return

        password = self.password.get()
        if not password:
            messagebox.showerror("Error", "Enter password!")
            return

        files = extract_data(self.image_path, password)

        if not files:
            messagebox.showerror("Error", "Wrong password or corrupted image!")
            return

        folder = filedialog.askdirectory()
        if not folder:
            return

        for name, data in files:
            with open(os.path.join(folder, name), "wb") as f:
                f.write(data)

        self.status.configure(text="Extraction complete 🎉")
        messagebox.showinfo("Success", "Files extracted successfully!")

    def analyze(self):
        if not self.image_path:
            messagebox.showerror("Error", "Select image first!")
            return

        result = analyze_image(self.image_path)
        messagebox.showinfo("Analysis Result", result)

    def heatmap(self):
        if not self.image_path or not self.output_path:
            messagebox.showerror("Error", "Need original & stego image!")
            return

        try:
            path = generate_heatmap(self.image_path, self.output_path)

            img = Image.open(path)
            img.thumbnail((400, 400))
            img = ImageTk.PhotoImage(img)

            self.stego_panel.configure(image=img)
            self.stego_panel.image = img

            messagebox.showinfo("Success", "Heatmap generated!")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def reset(self):
        self.image_path = None
        self.files.clear()
        self.output_path = None

        self.text_input.delete("1.0", "end")
        self.password.delete(0, "end")

        self.original_panel.configure(image="", text="Original Image")
        self.stego_panel.configure(image="", text="Stego Image")

        self.status.configure(text="Reset complete")
        messagebox.showinfo("Reset", "All fields cleared")