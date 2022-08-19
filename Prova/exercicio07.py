import cv2

print("Efeitos")
print("1 - Preto e branco")
print("2 - HSV")
print("3 - RGB")

efeito = int(input("\nDigite o efeito que você quer: "))

if(efeito == 1):
    cap = cv2.VideoCapture('./DocsProva/flor.mp4')
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    output = cv2.VideoWriter("novo_video.mp4", fourcc, 30.0, (1280,720))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LUV)
            frame=cv2.resize(frame,(1280,720))
            output.write(frame)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    output.release()
    cv2.destroyAllWindows()
elif(efeito == 2):
    cap = cv2.VideoCapture('./DocsProva/flor.mp4')
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    output = cv2.VideoWriter("novo_video.mp4", fourcc, 30.0, (1280,720))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            frame=cv2.resize(frame,(1280,720))
            output.write(frame)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    output.release()
    cv2.destroyAllWindows()
elif(efeito == 3):
    cap = cv2.VideoCapture('./DocsProva/flor.mp4')
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    output = cv2.VideoWriter("novo_video.mp4", fourcc, 30.0, (1280,720))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame=cv2.resize(frame,(1280,720))
            output.write(frame)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    output.release()
    cv2.destroyAllWindows()
else:
    print("Efeito nvalido")