import sys, pygame
from pygame import mixer
pygame.init()

size = width, height = 1500, 800
speed = [2, 2]
black = 0, 0, 0

#画面の作成
screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
#画像は画像を表示指定するパイソンファイルと同じフォルダの中にないといけない
ballrect = ball.get_rect()
#ballを動かす準備

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)#ballをspeed分だけ移動
    
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        mixer.music.load("ボヨン.mp3")#音読み込み
        mixer.music.play(1)#音出力
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        mixer.music.load("ボヨン.mp3")
        mixer.music.play(1)

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
