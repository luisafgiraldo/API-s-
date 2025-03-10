import utils as u
import os
import time

URL_BASE = "https://api.staging.landing.ai/v1/tools"
IMAGES_PATH_BASE = os.path.join("VA", "Images")
API_KEY = "eTdiN3pjM2dpbWlhbnIwMzJlcDdvOiNpbnRlcm5hbDpPQXN5YW5qRHpxOUJhQzduOFFnODlzRlAyck9UZDBUeQ=="

start_time = time.time()

def Owlv2():

    import Owlv2

    IMAGE_DIR = u.union_path(IMAGES_PATH_BASE, "OWLv2 Image")
    IMAGE_PATH = u.first_file_finder(IMAGE_DIR)
    URL = f"{URL_BASE}/owlv2"
    PROMPTS = "Detect animals"

    Owlv2 = Owlv2.create(URL, IMAGE_PATH, PROMPTS)


Owlv2()


def Countgd():

    import Countgd

    IMAGE_DIR = u.union_path(IMAGES_PATH_BASE, "Countgd Counting")
    IMAGE_PATH = u.first_file_finder(IMAGE_DIR)
    URL = f"{URL_BASE}/countgd"
    PROMPTS = "Dogs"

    Countgd = Countgd.create(URL, IMAGE_PATH, PROMPTS)


Countgd()


def Florencev2_Roberta():

    import Florencev2

    IMAGE_DIR = u.union_path(IMAGES_PATH_BASE, "Florence-2 Roberta Vqa")
    IMAGE_PATH = u.first_file_finder(IMAGE_DIR)
    URL = f"{URL_BASE}/florence2"
    TASK = "<CAPTION>"

    Florencev2 = Florencev2.create(URL, IMAGE_PATH, TASK)


Florencev2_Roberta()


def Florencev2_OCR():

    import Florencev2

    IMAGE_DIR = u.union_path(IMAGES_PATH_BASE, "Florence2 OCR")
    IMAGE_PATH = u.first_file_finder(IMAGE_DIR)
    URL = f"{URL_BASE}/florence2"
    TASK = "<OCR>"

    Florencev2 = Florencev2.create(URL, IMAGE_PATH, TASK)


Florencev2_OCR()


def Florencev2QA():

    import Florencev2QA

    IMAGE_DIR = u.union_path(IMAGES_PATH_BASE, "IXC25 Image VQA")
    IMAGE_PATH = u.first_file_finder(IMAGE_DIR)
    URL = f"{URL_BASE}/florence2-qa"
    QUESTION = "What color is the car?"

    Florencev2QA = Florencev2QA.create(URL, IMAGE_PATH, QUESTION)


Florencev2QA()


def Depth_Anything_V2():

    import Depth_Anything_V2
    import numpy as np

    IMAGE_DIR = u.union_path(IMAGES_PATH_BASE, "Depth Anything V2")
    IMAGE_PATH = u.first_file_finder(IMAGE_DIR)
    URL = f"{URL_BASE}/depth-anything-v2"

    Depth_Anything_V2 = Depth_Anything_V2.create(URL, IMAGE_PATH)
    print(Depth_Anything_V2)


Depth_Anything_V2()


def Text_To_Od():

    import Text_To_Od

    IMAGE_DIR = u.union_path(IMAGES_PATH_BASE, "OWLv2 Video")
    VIDEO_PATH = u.first_file_finder(IMAGE_DIR)
    URL = f"{URL_BASE}/text-to-object-detection"
    # PROMPTS = "Detect elephants, giraffes, zebras, and other animals in the wildlife video, providing object labels, confidence scores, and bounding box coordinates"
    PROMPTS = "elephants"
    Text_To_Od = Text_To_Od.create(URL, VIDEO_PATH, PROMPTS, API_KEY)
    print(Text_To_Od)


#Text_To_Od()


def nsfw_classification():

    import nsfw_classification

    IMAGE_DIR = u.union_path(IMAGES_PATH_BASE, "ViT NSFW Classification")
    IMAGE_PATH = u.first_file_finder(IMAGE_DIR)
    URL = f"{URL_BASE}/nsfw-classification"

    nsfw_classification = nsfw_classification.create(URL, IMAGE_PATH)


nsfw_classification()


def Wsi_Embedding():

    import Wsi_Embedding

    IMAGE_DIR = u.union_path(IMAGES_PATH_BASE, "Tool Wsi Embedding")
    IMAGE_PATH = u.first_file_finder(IMAGE_DIR)
    URL = f"{URL_BASE}/wsi-embedding"

    Wsi_Embedding = Wsi_Embedding.create(URL, IMAGE_PATH)


Wsi_Embedding()


def qr_reader():

    import qr_reader

    IMAGE_DIR = u.union_path(IMAGES_PATH_BASE, "Tool Qr Reader")
    IMAGE_PATH = u.first_file_finder(IMAGE_DIR)
    URL = f"{URL_BASE}/qr-reader"

    qr_reader = qr_reader.create(URL, IMAGE_PATH)


qr_reader()


def loca():

    import loca

    IMAGE_DIR = u.union_path(IMAGES_PATH_BASE, "Loca Zero Shot Counting")
    IMAGE_PATH = u.first_file_finder(IMAGE_DIR)
    URL = f"{URL_BASE}/loca"

    loca = loca.create(URL, IMAGE_PATH)


loca()


def Pose_Detection():

    import Pose_Detection

    IMAGE_DIR = u.union_path(IMAGES_PATH_BASE, "Pose Detection")
    IMAGE_PATH = u.first_file_finder(IMAGE_DIR)
    URL = f"{URL_BASE}/pose-detector"

    Pose_Detection = Pose_Detection.create(URL, IMAGE_PATH)


Pose_Detection()


def Barcode_Reader():

    import Barcode_Reader

    IMAGE_DIR = u.union_path(IMAGES_PATH_BASE, "Barcode Reader")
    IMAGE_PATH = u.first_file_finder(IMAGE_DIR)
    URL = f"{URL_BASE}/barcode-reader"

    Barcode_Reader = Barcode_Reader.create(URL, IMAGE_PATH)


Barcode_Reader()

end_time = time.time()
total_time_minutes = (end_time - start_time) / 60
print(f"Total execution time: {total_time_minutes:.2f} minutes")