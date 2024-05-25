import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


def generate_from_text_by_dall_e_3(prompt: str,
                                   size: str = "1024x1024",
                                   style: str = "vivid") -> str:
    """
    DALL-E 3を使用してテキストから画像を生成します。

    Args:
        prompt (str): 画像生成のためのテキストプロンプト。
        size (str, optional): 生成される画像のサイズ。デフォルトは "1024x1024"。
        style (str, optional): 画像のスタイル。デフォルトは "vivid"。

    Returns:
        str: 生成された画像のURL。
    """
    model = "dall-e-3"
    client = OpenAI()
    response = client.images.generate(
        model=model,
        prompt=prompt,
        n=1,
        size=size,
        style=style,
        quality="hd"
    )

    return response.data[0].url