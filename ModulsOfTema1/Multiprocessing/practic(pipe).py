import multiprocessing as mp
from PIL import Image
import datetime

def resize_image(image_paths, pipe: mp.Pipe, stop_event):
    for image_path in image_paths:
        image = Image.open(image_path).resize((700, 500))
        image.save(image_path)
        pipe.send(image_path)
    stop_event.set()

def change_color(pipe: mp.Pipe, stop_event):
    while not stop_event.is_set():
        image_path = pipe.recv()
        image = Image.open(image_path).convert('L')
        image.save(image_path)

if __name__ == '__main__':
    data = []
    conn1, conn2 = mp.Pipe()
    stop_event = mp.Event

    for image in range(2, 11):
        data.append(f'./images/{image}.jpg')

    resize_process = mp.Process(target=resize_image, args=(data, conn1, stop_event))
    change_process = mp.Process(target=change_color, args=(conn2, stop_event))
    start = datetime.datetime.now()
    resize_process.start()
    change_process.start()
    resize_process.join()
    change_process.join()
    end = datetime.datetime.now()
    print(end - start)