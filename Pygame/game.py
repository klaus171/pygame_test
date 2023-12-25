import pygame
import random
import operator
import time

pygame.init()

# 색깔 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("1분 대결: 사칙연산 게임")

# 폰트 설정 (D2Coding 폰트 사용)
font_path = "D2Coding.ttc"
font = pygame.font.Font(font_path, 36)

# 연산자와 해당 연산자의 함수 매핑
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(list(operators.keys()))
    result = operators[operator](num1, num2)
    question = f"{num1} {operator} {num2}"
    return question, result

def main():
    score = 0
    start_time = time.time()
    end_time = start_time + 60  # 1분 설정
    running = True

    while time.time() < end_time:
        question, answer = generate_question()
        user_answer = ''

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        try:
                            user_answer = float(user_answer)
                        except ValueError:
                            pass

                        if user_answer == answer:
                            score += 1
                        break
                    elif event.key == pygame.K_BACKSPACE:
                        user_answer = user_answer[:-1]
                    else:
                        user_answer += event.unicode

            screen.fill(BLACK)
            text_question = font.render("문제: " + question + " =", True, WHITE)
            text_input = font.render("답: " + str(user_answer), True, WHITE)  # 문자열로 변환하여 출력
            screen.blit(text_question, (50, 50))
            screen.blit(text_input, (50, 100))
            pygame.display.flip()

    # 1분이 끝나면 점수 표시
    screen.fill(BLACK)
    text_score = font.render(f"최종 점수: {score}", True, WHITE)
    screen.blit(text_score, (screen_width // 2 - 100, screen_height // 2))
    pygame.display.flip()

    # 2초 후에 창 닫힘
    pygame.time.wait(2000)
    pygame.quit()

if __name__ == "__main__":
    main()
