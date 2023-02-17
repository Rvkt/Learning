import os

dstn = input('Destination Path:\n')
os.chdir(dstn)


for i in range(1):
    # Documents Files
    with open(f'test{i}.doc', 'w'):
        pass
    with open(f'test{i}.txt', 'w'):
        pass
    with open(f'test{i}.pdf', 'w'):
        pass
    with open(f'test{i}.ppt', 'w'):
        pass

    # Image Files
    with open(f'test{i}.jpg', 'w'):
        pass
    with open(f'test{i}.png', 'w'):
        pass

    # Audio Files
    with open(f'test{i}.mp3', 'w'):
        pass
    with open(f'test{i}.wav', 'w'):
        pass

    # Video Files
    with open(f'test{i}.avi', 'w'):
        pass

    # Ebook File Extension
    with open(f'test{i}.epub', 'w'):
        pass

    # Archive Files
    with open(f'test{i}.rar', 'w'):
        pass
    with open(f'test{i}.zip', 'w'):
        pass
    with open(f'test{i}.7z', 'w'):
        pass
    with open(f'test{i}.iso', 'w'):
        pass

    # Fonts Files
    with open(f'test{i}.ttf', 'w'):
        pass
    with open(f'test{i}.otf', 'w'):
        pass

    # Installer Files
    with open(f'test{i}.exe', 'w'):
        pass
    with open(f'test{i}.apk', 'w'):
        pass

    # Web Files
    with open(f'test{i}.html', 'w'):
        pass

    # Illustrator Files
    with open(f'test{i}.svg', 'w'):
        pass
    with open(f'test{i}.ai', 'w'):
        pass

    # Photoshop Files
    with open(f'test{i}.psd', 'w'):
        pass


# SketchUP
    with open(f'test{i}.skp', 'w'):
        pass