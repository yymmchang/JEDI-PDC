# PPDataIntegration


<a href="https://github.com/cislab-ntut/PPDataIntegration/blob/master/README(Chinese).md">[Chinese ver.]</a> <br>


Through the GBF technology to achieve MPSI (Multi-Party Private Set Intersection) dataset integration display webpage.  <br />
The goal is to integrate the intersection data of datasets.  <br />

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
**選擇檔案** button → Select multiple files to upload at once  <br />
**Upload**  button → Upload the file  <br />  
Upload file limit: txt  <br />

Here is an example to upload 4 txt files(Respectively name1.txt, name2.txt, name3.txt, namec.txt)  <br />
![image](https://user-images.githubusercontent.com/55148438/164232516-e12224c1-20ad-442c-b5f4-007200b4ad67.png)


## /upload
Uploaded files / View uploaded files <br />
There are multiple radio buttons below (the option is the uploaded file), you can select the file to be used as a query  <br />
-   #file1
-   #file2
-   #file3
-   #file4

![image](https://user-images.githubusercontent.com/55148438/164232802-9fb197c7-7bd2-4ee3-9422-f5647d4cb03c.png)
<br />
**#file**  button → View the file content (the option name is the same as the uploaded file name)  <br />
![image](https://user-images.githubusercontent.com/55148438/164390595-86fa2d8e-da4c-4cf5-955e-49c0eb6f149f.png)
<br />
**sumbit** button → Submit query option  <br />


## /validate
View integration results  <br />
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

