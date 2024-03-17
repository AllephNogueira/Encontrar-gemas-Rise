import pyautogui
import time
import cv2
import numpy as np

# Loop infinito
while True:
    # Captura uma imagem da tela
    screenshot = pyautogui.screenshot()

    # Converte a imagem capturada para um array numpy
    screenshot_np = np.array(screenshot)

    # Converte a imagem para o formato RGB
    screenshot_rgb = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2RGB)

    # Realiza a detecção da imagem na tela
    template = cv2.imread('gemas.png', cv2.IMREAD_COLOR)
    result = cv2.matchTemplate(screenshot_rgb, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Se a imagem for encontrada
    if max_val > 0.7:
        # Obtém as coordenadas e tamanho da imagem encontrada
        height, width, _ = template.shape
        left, top = max_loc
        right = left + width
        bottom = top + height

        # Desenha um retângulo vermelho ao redor da imagem encontrada
        cv2.rectangle(screenshot_rgb, (left, top), (right, bottom), (0, 0, 255), 2)

        # Mostra a imagem com o retângulo desenhado
        cv2.imshow('Detecção de Imagem', screenshot_rgb)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print('Encontramos um deposito de Gemas!')

    else:
        print("Depósito não localizado nessa região!.")

    # Aguarda 2 segundos antes da próxima execução
    time.sleep(2)
