from PIL import Image
from utils import get_batch_pics

def demo_get_batch_pics():
    img = Image.open("172.png")
    pics = get_batch_pics(img, 15, 15, 15)

def main():
    demo_get_batch_pics()

if __name__ == "__main__":
    main()