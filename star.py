import pygame
import time

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기

screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀(제목) 설정
pygame.display.set_caption("바운스볼") #게임 이름

# FPS 초당 프레임 변수 설정
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("D:/바운스볼/background.png")

ball = pygame.image.load("D:/바운스볼/ball.png")
ball_size = ball.get_rect().size # 캐릭터의 사이즈 가져오기
R = ball_size[0] # 캐릭터의 가로 크기
pos_x = (screen_width / 2) - (R / 2) # 화면 가로에 중간지점에 캐릭터의 가로 위치
pos_y = screen_height - R # 화면 세로 크기 가장 아래에 캐릭터의 세로 위치

star = pygame.image.load("D:/바운스볼/star.png")
star_size = star.get_rect().size # 캐릭터의 사이즈 가져오기
sR = star_size[0] # 캐릭터의 가로 크기
star_pos_x = 400 # 화면 가로에 중간지점에 적 캐릭터의 가로 위치
star_pos_y = 400 # 화면 세로 크기 중간지점에 적 캐릭터의 세로 위치

ground = screen_height - R
g = 0
to_y = 0

font1 = pygame.font.SysFont("arial", 30)
img1 = font1.render('YOU WIN!', True, (255,0,0))

running = True
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수 설정

    for event in pygame.event.get(): # running 중 키보드나,마우스 입력값(이벤트)을 체크해주는것
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는지
            running = False # 게임이 진행중이 아님

    # x좌표 이동
    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        pos_x -= 3

    if key_event[pygame.K_RIGHT]:
        pos_x += 3

    # 점프
    if pos_y < ground:
        g += 0.1
    else:
        g = 0
    to_y = 5
    pos_y -= to_y - g

    # X 경계값 설정
    if pos_x < 0:
        pos_x = 0
    elif pos_x > screen_width - R:
        pos_x = screen_width - R


    # 충돌 처리를 위한 rect 정보 업데이트 (실제 좌표를 알아야 충돌처리가 됨)
    ball_rect = ball.get_rect()
    ball_rect.left = pos_x
    ball_rect.top = pos_y

    star_rect = star.get_rect()
    star_rect.left = star_pos_x
    star_rect.top = star_pos_y


    screen.blit(background, (0, 0)) # 배경 그리기(background 가 표시되는 위치)

    # 충돌 체크
    if ball_rect.colliderect(star_rect):
        screen.blit(img1, (240,240))
        pygame.display.update()
        time.sleep(2)
        break
    else:
        screen.blit(star, (star_pos_x, star_pos_y)) # 별 그리기
        
    screen.blit(ball, (pos_x, pos_y)) # 캐릭터 그리기



    pygame.display.update() # 게임화면을 지속적으로 그리기(for 문도는동안 계속)
    
# pygame 종료
pygame.quit()
