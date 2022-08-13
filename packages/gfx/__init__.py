
def draw_text_center(tft, text, font, color, screen_width=240, screen_height=240, scale=1.0):
    word_len = tft.draw_len(font, text, scale)
    col = 0 if word_len > screen_width else (screen_width//2 - word_len//2)
    row = int((screen_height + font.HEIGHT) / 2)
    tft.draw(font, text, col, row, color, scale)