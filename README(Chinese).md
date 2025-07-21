# JEDI-PDC

透過GBF技術達成PDC(隱私資料清理)的資料集整合展示網頁  <br />
目標為找出資料集合中分類錯誤的資料項  <br />

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
**選擇檔案** 按鈕 → 選擇2個檔案一次上傳  <br />
**Upload**  按鈕 → 上傳檔案  <br />  
上傳檔案限制: txt  <br />

此處範例上傳2個txt檔案(分別為nameC.txt, nameS.txt)  <br />
![image](https://github.com/yymmchang/JEDI-PDC/blob/master/1753081742986.jpg)


## /upload
下方有兩個單選框(選項為上傳之檔案)，可選取欲作為Client之檔案  <br />
-   #file1
-   #file2
![image](https://github.com/yymmchang/JEDI-PDC/blob/master/1753081843713.jpg)
<br />
**Run JEDI-PDC** 按鈕 → 提交資料清理選項  <br />


## /validate
查看清理結果  <br />
EX:
<table>
    <tr>
        <td>Queena</td>
        <td>nameC</td>
        <td>nameS</td>
    </tr>
    <tr>
        <td>Kelvin</td>
        <td>nameC</td>
        <td>nameS</td>
    </tr>
    <tr>
        <td>Ian</td>
        <td>nameC</td>
        <td>nameS</td>
    </tr>
    <tr>
        <td>Mike</td>
        <td>nameC</td>
        <td>nameS</td>
    </tr>
    <tr>
        <td>Kenny</td>
        <td>nameC</td>
        <td>nameS</td>
    </tr>
</table>

![image](https://github.com/yymmchang/JEDI-PDC/blob/master/1753081685196.jpg)
