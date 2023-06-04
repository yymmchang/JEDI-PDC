# PPDataIntegration

透過GBF技術達成MPSI(多方私有集合交集)的資料集整合展示網頁  <br />
目標為整合資料集合中交集的資料項  <br />

 <br />
透過vscode編譯器打開資料夾 <br />
執行main.py   <br />
<br />

在termial處下載相關套件:   <br />
pip install flask   <br />
pip install phe   <br />

 <br />
連線網址: 127.0.0.1:5000 <br />

## /
Upload files 選擇檔案上傳  <br />
**選擇檔案** 按鈕 → 可以選擇多個檔案一次上傳  <br />
**Upload**  按鈕 → 上傳檔案  <br />  
上傳檔案限制: txt  <br />

此處範例上傳4個txt檔案(分別為name1.txt, name2.txt, name3.txt, namec.txt)  <br />
![image](https://user-images.githubusercontent.com/55148438/164232516-e12224c1-20ad-442c-b5f4-007200b4ad67.png)


## /upload
Uploaded files 可檢視上傳之檔案 <br />
下方有多個單選框(選項為上傳之檔案)，可選取欲作為query之檔案  <br />
-   #file1
-   #file2
-   #file3
-   #file4

![image](https://user-images.githubusercontent.com/55148438/164232802-9fb197c7-7bd2-4ee3-9422-f5647d4cb03c.png)
<br />
**#file**  按鈕 → 可以查看file內容 (選項名稱同上傳之檔案名)  <br />
![image](https://user-images.githubusercontent.com/55148438/164390595-86fa2d8e-da4c-4cf5-955e-49c0eb6f149f.png)
<br />
**sumbit** 按鈕 → 提交query選項  <br />


## /validate
查看整合結果  <br />
EX:
<table>
    <tr>
        <td>Alice</td>
        <td>14</td>
        <td>15</td>
        <td>16</td>
    </tr>
    <tr>
        <td>Bob</td>
        <td>20</td>
        <td>21</td>
        <td>22</td>
    </tr>
    <tr>
        <td>Charlie</td>
        <td>34</td>
        <td>35</td>
        <td>36</td>
    </tr>
</table>

![image](https://user-images.githubusercontent.com/55148438/164233338-05b55960-a5b3-42d5-b57d-362c334df2e1.png)
