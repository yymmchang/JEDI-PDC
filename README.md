# JEDI-PDC


<a href="https://github.com/cislab-ntut/PPDataIntegration/blob/master/README(Chinese).md">[Chinese ver.]</a> <br>

This repository is a simple PoC to demonstrate the effectiveness of the work, a.k.a JEDI-PDC.

Through the GBF technology to achieve PDC (Private Data Cleaning).  <br />
The goal is to find the misclassified data in datasets.  <br />

 <br />
Open the folder through the vscode compiler  <br />
Compile main.py  <br />

<br />

Download related packages at terminal:   <br />
`pip install flask`   <br />
`pip install phe `  <br />

 
Connection URL: 127.0.0.1:5000

## /
Upload files / Select the file to upload  <br />
**選擇檔案** button → Select exactly two files to upload at once  <br />
**Upload**  button → Upload the file  <br />  
Upload file limit: txt  <br />

Here is an example to upload 2 txt files(Respectively nameC.txt, nameS.txt)  <br />
![image](https://github.com/yymmchang/JEDI-PDC/blob/master/1753081742986.jpg)


## /upload
Uploaded files / View uploaded files <br />
There are two radio buttons below (the option is the uploaded file), you can select the file to be used as a client  <br />
-   #file1
-   #file2


![image](https://github.com/yymmchang/JEDI-PDC/blob/master/1753081843713.jpg)
<br />
**Run JEDI-PDC** button → Submit data cleaning option  <br />


## /validate
View cleaning results  <br />
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
