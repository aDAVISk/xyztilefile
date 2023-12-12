
# ref: https://qiita.com/studio_haneya/items/9aad8f9ede11e58b41a8

from setuptools import setup, find_packages

setup(
    name='xyztilefile',  # パッケージ名（pip listで表示される）
    version="0.0.1",  # バージョン
    description="manage files in xyz tile format",  # 説明
    author='aDAVISk',  # 作者名
    license='MIT',  # ライセンス
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src')
)
