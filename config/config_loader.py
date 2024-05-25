import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import yaml


def load_config() -> dict:
    """
    config.yamlファイルを読み込み、設定を辞書として返します。

    Returns:
        dict: 設定が格納された辞書。
    """
    config_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 
        'config.yaml'
    )
    
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    
    return config
