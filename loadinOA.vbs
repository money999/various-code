'为什么vb解析这么慢，因为开着“地球”客户端~~~
Dim username,password,IE  
username = "xxxxx"  
password = "xxxxx"
Set IE =CreateObject("InternetExplorer.Application")  
ie.FullScreen=0            
IE.Visible = True          
IE.Navigate "http://bids.fj.sgcc.com.cn:8080/nidp/idff/sso?RequestID=idpZa3qILUrd3rM07yA5ZDEl7r37E&MajorVersion=1&MinorVersion=2&IssueInstant=2018-01-04T02%3A06%3A24Z&ProviderID=http%3A%2F%2Fportal3.fj.sgcc.com.cn%3A80%2Fnesp%2Fidff%2Fmetadata&RelayState=MA%3D%3D&consent=urn%3Aliberty%3Aconsent%3Aunavailable&ForceAuthn=false&IsPassive=false&NameIDPolicy=onetime&ProtocolProfile=http%3A%2F%2Fprojectliberty.org%2Fprofiles%2Fbrws-art&target=http%3A%2F%2Fnewportal.fj.sgcc.com.cn%2Fportal%2Fportal_um%2Flogin.jsp&AuthnContextStatementRef=name%2Fpassword%2Furi"   
Do while IE.ReadyState<> 4 or IE.busy   
wscript.sleep 500                  
loop
IE.document.getElementById("content").contentWindow.document.getElementById("credentials").contentWindow.document.getelementByid("Ecom_User_ID").value=username   
IE.document.getElementById("content").contentWindow.document.getElementById("credentials").contentWindow.document.getelementByid("Ecom_Password").value=password
IE.document.getElementById("content").contentWindow.document.getElementById("credentials").contentWindow.imageSubmit()
