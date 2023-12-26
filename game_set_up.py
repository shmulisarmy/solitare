import pygame


pygame.init()
width, height = 800, 800
window = pygame.display.set_mode((width, height))
font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)




class Card:
    size = (20, 100)
    color = (255, 255, 255)
    text_color = (0, 0, 0)

    def __init__(self):
        pass

    def display(self, card_list_location, card_list_index):
        self.x = card_list_location
        self.y = card_list_index*10

        card_rect = pygame.Rect(self.x, self.y *Card.size)

        pygame.draw.rect(window, (Card.color), card_rect)

        text_surface = font.render(self.text, True, Card.text_color)
        window.blit(text_surface, self.x + Card.size[0]//2, self.y + Card.size[0]//2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    window.fill("black")

    pygame.display.update()