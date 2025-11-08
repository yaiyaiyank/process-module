# processモジュール

自分のエコシステム用につくったプロセス用モジュール<br>
役立ちそう ∧ 機密情報なし なのでパブリックで公開

そのうちthreadやasyncに手を出すかもです。

# install
### 動作環境
* Python 3.13↑
### インストール方法 
uvなら
```bash
uv add git+https://github.com/yaiyaiyank/process-module
```
pipなら
```bash
pip install git+https://github.com/yaiyaiyank/process-module
```
### 備考
標準ライブラリのみで完結するので外部ライブラリ依存なし

# usage

```python
from process_module import execute_cmd
from pathlib import Path

# このファイルのカレントディレクトリのwebpを全てpngに変換してみた
image_folder = Path(__file__).parent
webp_files = image_folder.glob("*.webp")

for webp_file in webp_files:
    png_file = webp_file.with_suffix(".png")
    execute_cmd(f'ffmpeg -i "{webp_file}" "{png_file}"')
    # webpは削除
    webp_file.unlink()
```