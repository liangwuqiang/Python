oojs.define({name:"winNotice",namespace:"rs.business",$winNotice:function(){this.notice()},sendByImage:function(url,win){var img=new Image();var key="cpro_log_"+Math.floor(Math.random()*2147483648).toString(36);win=win||window;win[key]=img;img.onload=img.onerror=img.onabort=function(){img.onload=img.onerror=img.onabort=null;win[key]=null;img=null};img.src=url},notice:function(){try{if(window.winUrlArr&&window.winUrlArr.length){var urls=window.winUrlArr;for(var i=0,count=urls.length;i<count;i++){for(var j=0,num=urls[i].length;j<num;j++){if(urls[i][j]){this.sendByImage(urls[i][j])}}}}return true}catch(e){}}});