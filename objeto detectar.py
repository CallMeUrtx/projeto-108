import cv2

# Carrega o vídeo
cap = cv2.VideoCapture('video.mp4')

# Inicializa o objeto rastreado com as coordenadas do primeiro frame
ret, frame = cap.read()
bbox = cv2.selectROI(frame, False)
tracker = cv2.TrackerCSRT_create()
tracker.init(frame, bbox)

# Loop para processar cada frame do vídeo
while True:
    # Lê o próximo frame
    ret, frame = cap.read()

    # Sai do loop se o vídeo terminar
    if not ret:
        break

    # Rastreia o objeto no frame atual
    success, bbox = tracker.update(frame)

    # Desenha o retângulo ao redor do objeto rastreado
    if success:
        x, y, w, h = [int(i) for i in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostra o frame do vídeo com o objeto rastreado
    cv2.imshow('Object Tracking', frame)

    # Pressione a tecla 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera os recursos e fecha as janelas
cap.release()
cv2.destroyAllWindows()

