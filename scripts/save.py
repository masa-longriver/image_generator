from io import BytesIO
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PIL import Image as PILImage
import requests


def save_image(url: str, save_path: str) -> None:
    """
    指定されたURLから画像をダウンロードし、指定されたパスに保存します。

    Args:
        url (str): ダウンロードする画像のURL。
        save_path (str): 画像を保存するパス。

    Returns:
        None
    """
    response = requests.get(url)
    img = PILImage.open(BytesIO(response.content))
    img.save(save_path, format='PNG')