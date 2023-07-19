import requests

def download_image(url=''):
    try:
        response = requests.get (url=url)
        with open('req_img.jpg', 'wb') as file:
            file.write(response.content)

        return 'Изображение сохранено'
    except Exception as _ex:
        return 'Изображение не сохранено'

def download_video(url=''):
    try:
        response = requests.get (url=url)
        with open('req_video.mp4', 'wb') as file:
            file.write(response.content)

        return 'Видео сохранено'
    except Exception as _ex:
        return 'Видео не сохранено'

def main():
    print(download_video(url='https://youtu.be/A6c9Cn9V_Nw')) #Тут ссылку на видео
    print(download_image(url='')) #Тут вставляем ссылку на картинку


if __name__ == '__main__':
    main()
