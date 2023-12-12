
# ref: https://qiita.com/studio_haneya/items/9aad8f9ede11e58b41a8
# ref: https://qiita.com/shonansurvivors/items/0fbcbfde129f2d26301c

from setuptools import setup, find_packages

# long_description(後述)に、GitHub用のREADME.mdを指定
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='xyztilefile',  # パッケージ名（pip listで表示される）
    version="0.0.1",  # バージョン
    description="manage files in xyz tile format",  # 説明
    author='aDAVISk',  # 作者名
    license='MIT',  # ライセンス
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='xyztilefile xyz-tile xyztile',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)
