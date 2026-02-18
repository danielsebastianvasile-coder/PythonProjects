import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageEnhance, ImageDraw, ImageFilter
import cv2
import numpy as np

# Look aplicatie
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class ModernEditor(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Config Fereastra principala
        self.title("Editor Imagini PRO")
        self.geometry("1100x750")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # VARIABILE
        self.original_image = None
        self.display_image = None
        self.tk_image = None
        self.first_loaded_image = None

        # Istoric
        self.history = []
        self.history_pos = -1

        # Crop vars
        self.cropping = False
        self.start_x = self.start_y = 0

        # Eraser vars
        self.eraser_on = False
        self.eraser_size = 20
        self.mask_image = None
        self.mask_draw = None

        self.img_scale = 1
        self.img_x_offset = 0
        self.img_y_offset = 0

        # SLIDERE
        self.adjust_values = {
            "Luminozitate": 0,
            "Contrast": 0,
            "Saturație": 0,
            "Tonuri luminoase": 0,
            "Tonuri întunecate": 0,
            "Claritate": 0,
            "Vinietă": 0
        }

        self.slider_widgets = {}
        self._job = None

        self.setup_ui()

    def setup_ui(self):
        # 1. SIDEBAR
        self.sidebar = ctk.CTkFrame(self, width=300, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(3, weight=1)

        lbl_title = ctk.CTkLabel(self.sidebar, text="PRO EDITOR", font=("Roboto Medium", 24))
        lbl_title.grid(row=0, column=0, padx=20, pady=(20, 10))

        #Frame Butoane Import/Save
        btn_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        btn_frame.grid(row=1, column=0, padx=10, pady=5)

        ctk.CTkButton(btn_frame, text="Importă", width=100, command=self.load_image, fg_color="#2da44e",
                      hover_color="#2c974b").pack(side="left", padx=5)
        ctk.CTkButton(btn_frame, text="Salvează", width=100, command=self.save_image, fg_color="#0969da",
                      hover_color="#005cc5").pack(side="left", padx=5)

        #Frame Butoane Istoric & RESET
        ur_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        ur_frame.grid(row=2, column=0, padx=10, pady=5)

        # Undo
        ctk.CTkButton(ur_frame, text="⟲", width=60, command=self.undo, fg_color="#444").pack(side="left", padx=3)
        # Reset
        ctk.CTkButton(ur_frame, text="RESET", width=80, command=self.reset_image, fg_color="#c0392b",
                      hover_color="#e74c3c").pack(side="left", padx=3)
        # Redo
        ctk.CTkButton(ur_frame, text="⟳", width=60, command=self.redo, fg_color="#444").pack(side="left", padx=3)

        self.tabs = ctk.CTkTabview(self.sidebar, width=280)
        self.tabs.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        self.tab_adj = self.tabs.add("Ajustări")
        self.tab_filters = self.tabs.add("Filtre")
        self.tab_tools = self.tabs.add("Unelte")

        self.setup_sliders()
        self.setup_filters()
        self.setup_tools()

        self.btn_compare = ctk.CTkButton(self.sidebar, text="Apasă lung pt. Original", fg_color="#888")
        self.btn_compare.grid(row=4, column=0, padx=20, pady=20, sticky="ew")
        self.btn_compare.bind("<ButtonPress-1>", self.start_compare)
        self.btn_compare.bind("<ButtonRelease-1>", self.stop_compare)

        # 2. CANVAS
        self.canvas_frame = ctk.CTkFrame(self, fg_color="#1a1a1a")
        self.canvas_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.canvas = tk.Canvas(self.canvas_frame, bg="#1a1a1a", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True, padx=2, pady=2)

        self.canvas.bind("<ButtonPress-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        self.canvas.bind("<Configure>", self.resize_event)

    def setup_sliders(self):
        scroll = ctk.CTkScrollableFrame(self.tab_adj, label_text="Parametri")
        scroll.pack(fill="both", expand=True)

        for name in self.adjust_values:
            lbl = ctk.CTkLabel(scroll, text=name, font=("Arial", 11))
            lbl.pack(anchor="w", pady=(5, 0))

            slider = ctk.CTkSlider(scroll, from_=-100, to=100, command=lambda v, n=name: self.on_slider_change(n, v))
            slider.set(0)
            slider.pack(fill="x", pady=(0, 10))

            self.slider_widgets[name] = slider
            slider.bind("<ButtonRelease-1>", lambda event: self.add_to_history())

    def setup_filters(self):
        scroll = ctk.CTkScrollableFrame(self.tab_filters)
        scroll.pack(fill="both", expand=True)

        filters = {
            "Original": self.reset_image,
            "Intens": lambda: self.apply_filter_preset(1.05, 1.1, 1.4),
            "Dramatic": lambda: self.apply_filter_preset(0.95, 1.4, 0.8),
            "Mono": lambda: self.apply_filter_preset(1.0, 1.0, 0.0),
            "Noir": lambda: self.apply_filter_preset(0.85, 1.5, 0.0)
        }

        for name, func in filters.items():
            ctk.CTkButton(scroll, text=name, command=func, fg_color="transparent", border_width=1,
                          border_color="#555").pack(pady=3, fill="x")

    def setup_tools(self):
        ctk.CTkLabel(self.tab_tools, text="Transformare", font=("Arial", 13, "bold")).pack(pady=10)
        ctk.CTkButton(self.tab_tools, text="✂ Crop Selection", command=self.start_crop).pack(pady=5, fill="x")

        frm_rot = ctk.CTkFrame(self.tab_tools, fg_color="transparent")
        frm_rot.pack(pady=5)
        ctk.CTkButton(frm_rot, text="⟳ 90°", width=80, command=lambda: self.rotate_image(90)).pack(side="left", padx=2)
        ctk.CTkButton(frm_rot, text="Flip H", width=80, command=lambda: self.flip_image("h")).pack(side="left", padx=2)

        ctk.CTkLabel(self.tab_tools, text="Magic Eraser (AI)", font=("Arial", 13, "bold"), text_color="#ff5555").pack(
            pady=(20, 5))

        self.switch_eraser = ctk.CTkSwitch(self.tab_tools, text="Activează Eraser", command=self.toggle_eraser)
        self.switch_eraser.pack(pady=5)

        ctk.CTkLabel(self.tab_tools, text="Mărime Pensulă").pack(pady=(5, 0))
        self.slider_brush = ctk.CTkSlider(self.tab_tools, from_=5, to=100, command=self.change_eraser_size)
        self.slider_brush.set(20)
        self.slider_brush.pack(pady=5)

    def on_slider_change(self, name, val):
        self.adjust_values[name] = int(val)
        if self._job:
            self.after_cancel(self._job)
        self._job = self.after(50, self.apply_all_adjustments)

    def resize_event(self, event):
        if self.display_image:
            self.show_image()

    def load_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.jfif *.webp *.bmp")])
        if path:
            self.original_image = Image.open(path).convert("RGB")
            self.display_image = self.original_image.copy()
            self.first_loaded_image = self.original_image.copy()

            self.history = []
            self.history_pos = -1

            for k in self.adjust_values:
                self.adjust_values[k] = 0
                if k in self.slider_widgets:
                    self.slider_widgets[k].set(0)

            self.add_to_history()
            self.show_image()

    def save_image(self):
        if self.display_image:
            path = filedialog.asksaveasfilename(defaultextension=".png")
            if path:
                self.display_image.save(path)
                messagebox.showinfo("Saved", "Imagine salvată cu succes!")

    def add_to_history(self):
        if not self.display_image: return
        if self.history_pos < len(self.history) - 1:
            self.history = self.history[:self.history_pos + 1]

        state = {
            "display": self.display_image.copy(),
            "original": self.original_image.copy(),
            "values": self.adjust_values.copy()
        }
        self.history.append(state)
        self.history_pos += 1

        if len(self.history) > 20:
            self.history.pop(0)
            self.history_pos -= 1

    def undo(self):
        if self.history_pos > 0:
            self.history_pos -= 1
            self.restore_state()

    def redo(self):
        if self.history_pos < len(self.history) - 1:
            self.history_pos += 1
            self.restore_state()

    def restore_state(self):
        state = self.history[self.history_pos]
        self.display_image = state["display"].copy()
        self.original_image = state["original"].copy()
        self.adjust_values = state["values"].copy()

        for name, val in self.adjust_values.items():
            if name in self.slider_widgets:
                self.slider_widgets[name].set(val)

        self.show_image()

    def show_image(self):
        if not self.display_image: return
        cw = self.canvas.winfo_width()
        ch = self.canvas.winfo_height()
        if cw < 10: cw = 700
        if ch < 10: ch = 600

        iw, ih = self.display_image.size
        ratio = min(cw / iw, ch / ih)
        nw, nh = int(iw * ratio), int(ih * ratio)

        resized = self.display_image.resize((nw, nh), Image.Resampling.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(resized)

        self.canvas.delete("all")
        self.canvas.create_image(cw // 2, ch // 2, anchor="center", image=self.tk_image)
        self.img_scale = ratio
        self.img_x_offset = (cw - nw) // 2
        self.img_y_offset = (ch - nh) // 2

    def apply_filter_preset(self, b, c, s):
        if not self.original_image: return
        img = self.display_image.copy()
        img = ImageEnhance.Brightness(img).enhance(b)
        img = ImageEnhance.Contrast(img).enhance(c)
        img = ImageEnhance.Color(img).enhance(s)

        self.display_image = img
        self.original_image = img.copy()

        for k in self.adjust_values:
            self.adjust_values[k] = 0
            if k in self.slider_widgets:
                self.slider_widgets[k].set(0)

        self.add_to_history()
        self.show_image()

    def apply_all_adjustments(self):
        if not self.original_image: return

        img = self.original_image.copy()
        vals = self.adjust_values

        shadows = vals["Tonuri întunecate"]
        highlights = vals["Tonuri luminoase"]

        if shadows != 0 or highlights != 0:
            lut = []
            for i in range(256):
                x = i / 255.0
                if shadows != 0:
                    factor = shadows / 100.0
                    x = x + (factor * 0.5) * (1 - x) * (1 - x)

                if highlights != 0:
                    factor = highlights / 100.0
                    x = x + (factor * 0.5) * x * x
                lut.append(min(255, max(0, int(x * 255))))

            if img.mode == 'RGB':
                img = img.point(lut * 3)
            else:
                img = img.point(lut)

        b_factor = 1 + vals["Luminozitate"] / 100
        if b_factor != 1: img = ImageEnhance.Brightness(img).enhance(max(0.0, b_factor))

        c_factor = 1 + vals["Contrast"] / 100
        if c_factor != 1: img = ImageEnhance.Contrast(img).enhance(max(0.0, c_factor))

        s_factor = 1 + vals["Saturație"] / 100
        if s_factor != 1: img = ImageEnhance.Color(img).enhance(max(0.0, s_factor))

        sh_factor = 1 + vals["Claritate"] / 100
        if sh_factor != 1: img = ImageEnhance.Sharpness(img).enhance(max(0.0, sh_factor))

        if vals["Vinietă"] != 0:
            w, h = img.size
            vignette_color = 0 if vals["Vinietă"] < 0 else 255
            intensity = abs(vals["Vinietă"]) / 100.0

            mask = Image.new("L", (w, h), 0)
            d = ImageDraw.Draw(mask)

            scale_x = 1.1 - (intensity * 0.4)
            scale_y = 1.1 - (intensity * 0.4)
            oval_w = w * scale_x
            oval_h = h * scale_y
            x0, y0 = (w - oval_w) / 2, (h - oval_h) / 2
            d.ellipse((x0, y0, x0 + oval_w, y0 + oval_h), fill=255)

            mask = mask.filter(ImageFilter.GaussianBlur(radius=max(w, h) // 5))
            solid_layer = Image.new("RGB", (w, h), (vignette_color, vignette_color, vignette_color))
            img = Image.composite(img, solid_layer, mask)

        self.display_image = img
        self.show_image()

    def reset_image(self):
        if self.first_loaded_image:
            self.display_image = self.first_loaded_image.copy()
            self.original_image = self.first_loaded_image.copy()
            for k in self.adjust_values:
                self.adjust_values[k] = 0
                if k in self.slider_widgets: self.slider_widgets[k].set(0)
            self.add_to_history()
            self.show_image()

    #TOOLS
    def start_compare(self, event):
        if self.first_loaded_image:
            self.temp_display = self.display_image
            self.display_image = self.first_loaded_image
            self.show_image()

    def stop_compare(self, event):
        if hasattr(self, 'temp_display'):
            self.display_image = self.temp_display
            self.show_image()

    def rotate_image(self, angle):
        if not self.display_image: return
        self.display_image = self.display_image.rotate(angle, expand=True)
        self.original_image = self.display_image.copy()
        self.add_to_history()
        self.show_image()

    def flip_image(self, mode):
        if not self.display_image: return
        method = Image.FLIP_TOP_BOTTOM if mode == "v" else Image.FLIP_LEFT_RIGHT
        self.display_image = self.display_image.transpose(method)
        self.original_image = self.display_image.copy()
        self.add_to_history()
        self.show_image()

    def start_crop(self):
        self.cropping = True
        self.switch_eraser.deselect()
        self.eraser_on = False
        messagebox.showinfo("Crop", "Trage cu mouse-ul pe imagine pentru a decupa.")

    def toggle_eraser(self):
        self.eraser_on = bool(self.switch_eraser.get())
        if self.eraser_on: self.cropping = False

    def change_eraser_size(self, val):
        self.eraser_size = int(val)

    def get_real_coords(self, x, y):
        if self.img_scale == 0: return 0, 0
        rx = int((x - self.img_x_offset) / self.img_scale)
        ry = int((y - self.img_y_offset) / self.img_scale)
        return rx, ry

    def on_click(self, event):
        self.start_x, self.start_y = event.x, event.y
        if self.eraser_on and self.display_image:
            self.mask_image = Image.new("L", self.display_image.size, 0)
            self.mask_draw = ImageDraw.Draw(self.mask_image)
            self.paint_mask(event.x, event.y)

    def on_drag(self, event):
        if self.cropping:
            self.canvas.delete("crop_rect")
            self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline="#00FF00", width=2,
                                         tag="crop_rect")
        elif self.eraser_on:
            self.paint_mask(event.x, event.y)

    def paint_mask(self, x, y):
        r = self.eraser_size * self.img_scale
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="#ff5555", outline="", tag="eraser_trail")

        if self.mask_draw:
            rx, ry = self.get_real_coords(x, y)
            self.mask_draw.ellipse(
                (rx - self.eraser_size, ry - self.eraser_size, rx + self.eraser_size, ry + self.eraser_size), fill=255)

    def on_release(self, event):
        if self.cropping and self.display_image:
            self.canvas.delete("crop_rect")
            x1, y1 = self.get_real_coords(self.start_x, self.start_y)
            x2, y2 = self.get_real_coords(event.x, event.y)
            left, right = min(x1, x2), max(x1, x2)
            top, bottom = min(y1, y2), max(y1, y2)

            if right - left > 10 and bottom - top > 10:
                self.display_image = self.display_image.crop((left, top, right, bottom))
                self.original_image = self.display_image.copy()
                self.add_to_history()
                self.show_image()
            self.cropping = False

        elif self.eraser_on and self.display_image:
            self.apply_magic_eraser()
            self.canvas.delete("eraser_trail")
            self.mask_image = None

    def apply_magic_eraser(self):
        if not self.mask_image: return
        img_np = np.array(self.display_image)
        mask_np = np.array(self.mask_image)
        if len(img_np.shape) == 2:
            img_cv = cv2.cvtColor(img_np, cv2.COLOR_GRAY2BGR)
        else:
            img_cv = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
        res = cv2.inpaint(img_cv, mask_np, 3, cv2.INPAINT_TELEA)
        self.display_image = Image.fromarray(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
        self.original_image = self.display_image.copy()
        self.add_to_history()
        self.show_image()


if __name__ == "__main__":
    app = ModernEditor()
    app.mainloop()