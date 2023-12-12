from setuptools import setup, find_packages

setup(
    name='xyztilefile',  # パッケージ名（pip listで表示される）
    version="0.0.1",  # バージョン
    description="manage files in xyz tile format",  # 説明
    author='aDAVISk',  # 作者名
    packages=find_packages(),  # 使うモジュール一覧を指定する
    license='MIT'  # ライセンス
)
