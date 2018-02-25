'把种子下载的电视剧都放到一个文件夹里
Dim a,b,c,res,source,target
res=""
source=""
target="T:\迅雷下载\[CYW][琅琊榜之风起长林][01-08集][国语中字][WEB-MP4-H265][3840X2160P][4K版本][无水印][每集约1G][转载标注出处][CYW]\"
Set objFSO=CreateObject("Scripting.FileSystemObject")
For i=38 to 50
	if i Mod 2 = 1 Then
		a=Right("0"&i,2)'集数不足两位的要补0
		b=Right("0"&(i+1),2)
	Else
		a=Right("0"&(i-1),2)
		b=Right("0"&i,2)
	End If
	c=Right("0"&i,2)
	source = "T:\迅雷下载\[CYW][琅琊榜之风起长林][" & a&"-" &b &"集][国语中字][WEB-MP4-H265][3840X2160P][4K版本][无水印][每集约1G][转载标注出处][CYW]\[CYW][琅琊榜之风起长林]EP" &c &".WEB-DL.MP4.3840X2160P.H265.国语中字.无水印.[菜牙电影网].mp4"
	objFSO.MoveFile source, target
next
MsgBox("OK")
