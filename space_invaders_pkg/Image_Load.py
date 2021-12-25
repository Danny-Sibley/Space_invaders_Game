import pygame

pygame.init()

class Image_Load():
    def __init__(self):
        self.image = None 
    
    def image_display(self, image):
        self.image = image 
        return pygame.image.load(image)