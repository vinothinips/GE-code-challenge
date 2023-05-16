import math
import tkinter as tk
from PIL import ImageTk, Image
import numpy as np

class WatchAnimation:
    def __init__(self, master):
        self.master = master
        self.canvas_width = 600
        self.canvas_height = 600
        self.scale = 1.0
        self.rotation_angle = 0.0
        self.rotation_center = (self.canvas_width/2, self.canvas_height/2)

        self.canvas = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        # Load watch image
        try:
            self.watch_image = Image.open("watch_image.png")
            self.watch_image_tk = ImageTk.PhotoImage(self.watch_image)
        except FileNotFoundError:
            print("Watch image file not found.")
            self.master.destroy()
            return

        # Create watch display
        self.watch_display = self.canvas.create_image(
            self.canvas_width/2, self.canvas_height/2,
            image=self.watch_image_tk
        )

        self.animate()

    def animate(self):
        # Apply transformations to the watch display
        self.canvas.delete(self.watch_display)

        # Rotate around an arbitrary point (rotation_center)
        rotation_matrix = self.get_rotation_matrix(self.rotation_angle, self.rotation_center)
        rotated_image = self.apply_transformation(self.watch_image, rotation_matrix)

        # Scale up and down
        scaled_image = self.scale_image(rotated_image, self.scale)
        self.watch_image_tk = ImageTk.PhotoImage(scaled_image)

        # Update watch display
        self.watch_display = self.canvas.create_image(
            self.canvas_width/2, self.canvas_height/2,
            image=self.watch_image_tk
        )

        # Update animation parameters
        self.rotation_angle += 1.0
        self.scale = 1.0 + math.sin(math.radians(self.rotation_angle)) * 0.1

        self.master.after(50, self.animate)

    def get_rotation_matrix(self, angle, center):
        # Calculate rotation matrix
        theta = math.radians(angle)
        x, y = center
        rotation_matrix = np.array([
            [math.cos(theta), -math.sin(theta), (1 - math.cos(theta))*x + math.sin(theta)*y],
            [math.sin(theta), math.cos(theta), (1 - math.cos(theta))*y - math.sin(theta)*x],
            [0, 0, 1]
        ])
        return rotation_matrix

    def apply_transformation(self, image, matrix):
        # Apply transformation matrix to image
        transformed_image = image.transform(
            (self.canvas_width, self.canvas_height),
            Image.AFFINE,
            data=tuple(matrix.flatten()[:6]),
            resample=Image.BICUBIC
        )
        return transformed_image

    def scale_image(self, image, scale):
        # Scale image
        width = int(image.width * scale)
        height = int(image.height * scale)
        scaled_image = image.resize((width, height), Image.ANTIALIAS)
        return scaled_image


root = tk.Tk()
watch_animation = WatchAnimation(root)
root.mainloop()
