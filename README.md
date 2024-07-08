<br />
<div align="center">
  <h3 align="center">Wappalyzer Crawler</h3>

  <p align="center">
    Wappalyzer 插件資料自動蒐集工具
  </p>
</div>

## 關於專案

這是一支用於自動蒐集 Chrome 瀏覽器上 Wappalyzer 插件所提供的網頁技術棧資料的小工具，透過結合 PyAutoGUI 和 Selenium，以類似 RPA 的方式對給定的 URL 清單內所有的網站站點自動進行訪問並匯出 Wappalyzer 提供的相關技術棧資料。

## 使用說明

若想要執行該小工具，使用步驟如下，

1. 安裝專案所需的 python 相依套件

    ```python
    pip install -r requirements.txt
    ```

2. 使用者於 website_url_list.txt 輸入要蒐集資料的網站 URL，一行一個站點
3. 在**專案根目錄**執行 main.py 即可進行自動蒐集，蒐集過程中需將鍵鼠交給程式操作，切勿自行移動

    ```python
    python main.py
    ```

4. 蒐集的技術棧資料將會存於 export 資料夾內
