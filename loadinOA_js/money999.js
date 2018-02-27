/*
GNU GENERAL PUBLIC LICENSE
Version 0.1beta, 8 Fub 2018
Copyright (C) 2018 money999
*/
<script language="javascript">
var paddress = "c:\\money\\please input user&password.txt";
var userName = "";
var userPassword = "";

if(userName==""||userPassword ==""){var fso = new ActiveXObject("Scripting.FileSystemObject");var f1 = fso.opentextfile(paddress);var t1=f1.ReadLine();var userName=f1.ReadLine();var userPassword = f1.ReadLine();}var args = external.menuArguments;var doc = args.document;var cframe = doc.CONTENTS_IFRAME;if(cframe&&cframe.document){doc = cframe.document;}try{var cdy=doc.getElementById("content").contentWindow.document.getElementById("credentials").contentWindow;	var cdyObj1 = cdy.document.getElementById("Ecom_User_ID");var cdyObj2=cdy.document.getElementById("Ecom_Password");cdyObj1.value=userName;cdyObj2.value = userPassword;cdy.imageSubmit();}catch(err){alert("本页面无法自动填充")}</script>