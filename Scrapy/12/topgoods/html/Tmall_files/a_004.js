KISSY.add("mui/searchbar/instance/default",function(e,a,r,t,i,o,n,s,u,c,l,m,h,p,d){var g=window,b=g.g_config||{},f=b.bizId||"",v=b.sysId||"",C=b.devId||"pc",w=f+"."+v+"."+C,x="//suggest.taobao.com/sug?area=tmall-hq&code=utf-8&src="+w,q=(new p).getCurBt();return window._CTK3417=window._CTK3417||function(){function e(e){var a,r,t,i=0;if(0===e.length)return i;for(a=0,t=e.length;a<t;a++)r=e.charCodeAt(a),i=(i<<5)-i+r,i|=0;return i}var a={},r="",t=0;return function(i,o,n,s){function u(a,r){var i="undefined"+t++,o=window[i]=new Image;o.onload=o.onerror=function(){window[i]=null};var n=["type="+encodeURIComponent(s.type||"normal"),"name="+encodeURIComponent(a),"parent="+encodeURIComponent(r||""),"module="+encodeURIComponent(s.dataId||"30"),"msg="+encodeURIComponent(s.msg||""),"version="+encodeURIComponent("3.3.30"),"sample="+g,"time="+(m>0?m:0)].join("&");o.src="//gm.mmstat.com/tmjs.1.1?"+n+"&hash="+e(n)}if(s=s||{},s.reject){"object"!=typeof s.reject&&(s.reject=[s.reject]);for(var c=s.reject.length-1;c>=0;c--)if(a[s.reject[c]])return}r||(r=o);var l=(new Date).valueOf();a[o]=l;var m;if(o==r){var h=window.g_config&&g_config.startTime;m=h?l-h:0}else m=l-(a[n||r]||a[r]);switch(s.autoGroup){case"time":s.group=s.autoGroup+"_"+(m<=0?0:Math.floor(Math.log(m)/Math.log(2)))}"object"==typeof i&&(i=i[s.group||"_"]||Math.round(Math.log((undefined||8192)/(undefined||1/16))/Math.log(2)));var p=null,d=p&&p[Math.floor((l+288e5)/6e5)%144]||1,g=Math.round(Math.max(Math.pow(2,i)*d/(undefined||8192),1));Math.floor(Math.random()*g)>0||(s.group&&u(o+"|"+s.group,o),u(o,n))}}(),_CTK3417(30,"codetrack.init"),{"build":function(e){e=e||{};var p=e.node||"#mq",g=!!e.autoFocus,f=e.clickId,v=e.pageType,C=!!e.unableSpeech,y=e.placeholder||{},S=e.query||t.UNKNOWN,_=e.extraParams,k=e.sugArea||"b2c",I=e.tag||"",M=!1,U="//suggest.taobao.com/sug?area="+k+"&code=utf-8"+(I?"&tag="+I:"")+"&k=1&bucketid="+q+"&src=tmall_pc";!!(b.searchbarCfg=b.searchbarCfg||{}).isTestBt&&(U=U.replace(/\barea=b2c\b/gi,"area=b2c_bts"));var j=a.one(p),T=j?j.parent("form"):undefined,B=T?T[0].redirect:undefined,N=B?B.value:"",P=new o({"text":y.text||"\u641c\u7d22 \u5929\u732b \u5546\u54c1/\u54c1\u724c/\u5e97\u94fa","query":y.query||"","redirectUrl":y.redirectUrl||N});TB&&TB.globalToolFn&&TB.globalToolFn.requestHotQuery?TB.globalToolFn.requestHotQuery(function(e){e.success&&e.model&&e.model.placeholder?P.update(e.model.placeholder[0]):P.update(e)}):r({"url":y.cfgTMSUrl||x||"//www.tmall.com/go/rgn/tmall/searchbar/placeholder-reader.php","success":function(e){e.success&&e.model&&e.model.placeholder?P.update(e.model.placeholder[0]):P.update(e)},"scriptCharset":"utf-8","dataType":"jsonp"});var K=new t({"plugins":[P,new i({}),new n({"type":"20151212"})],"sugConfig":{"url":U,"node":p||"#mq","autoFocus":!!g,"autoExpand":!0,"extraParams":_||{},"enableSpeech":!C},"templates":{"act":s,"meetingPlace":d,"shipShop":u,"cat":c,"list":l,"shop":m,"quickSearch":h},"query":S,"acceptCharset":"gbk","dim":w,"log":{"pageType":v||1,"clickId":f||"topsearch","isMobile":!1}});return _CTK3417(30,"app.init"),_CTK3417(30,"default","app.init",{"group":location.hostname}),j.on("valuechange",function(){try{window.performance&&window.performance.timing&&Date.now()-window.performance.timing.loadEventEnd<=5e3&&!M&&(_CTK3417(30,"default.focus3S","app.init",{"group":location.hostname}),M=!0)}catch(e){}}),K}}},{"requires":["node","ajax","mui/searchbar/base","mui/searchbar/plugin/spm","mui/searchbar/plugin/placeholder","mui/searchbar/plugin/hubaccess","mui/searchbar/template/act","mui/searchbar/template/shipShop","mui/searchbar/template/cat","mui/searchbar/template/list","mui/searchbar/template/shop","mui/searchbar/template/quickSearch","mui/bucket/index","mui/searchbar/template/meetingPlace","mui/searchbar/suggest.css"]});KISSY.version>=1.4&&KISSY.config({"modules":{"sizzle":{"alias":["node"]},"rich-base":{"alias":["base"]},"ajax":{"alias":["io"]}}}),KISSY.add("mui/searchbar/base",function(S,Node,RichBase,D,ComboBox,UA,Cookie,E,IO){function makeCacheNum(){return Math.floor(268435456*Math.random()).toString(16)}var TIP="\u8bf7\u8f93\u5165\u641c\u7d22\u6587\u5b57",UNKNOWN="unknown",VALUE="{VALUE}",ltIE9=UA.ie<9,win=window,SearchBar=RichBase.extend([],{"initializer":function(){this._initComboxBox(),this._bindSubmitEvent(),this._other(),this._loadConfig()},"_initComboxBox":function(){var e=this,t=e._buildDataSourceCfg(),a=new ComboBox.RemoteDataSource(t),o=e._buildComboBoxCfg(a),r=e.comboBox=new ComboBox(o),i=r.sendRequest;r.sendRequest=function(t){t=S.trim(t),!1!==e.fire("beforeQueryChange",{"query":t})&&i.call(this,t)},r.normalizeData=function(e){var t,a=this;return t=a.get("format")?a.get("format").call(a,(a.getValueInternal||a.getValueForAutocomplete).call(a),e):[],t.slice(0,a.get("maxItemCount"))},r.render(),e._bindComboBoxEvents()},"_buildDataSourceCfg":function(){var e=this.get("sugConfig"),t=this.get("dataSourceCfg");return t.xhrCfg.url=e.url,t.parse=S.bind(this._parse,this),t},"_parse":function(e,t){var a=this.fire("beforeParse",{"data":t,"query":e});return!1===a?null:(a&&(t=a),t)},"_bindComboBoxEvents":function(){var e=this,t=this.get("templates"),a=this.get("log"),o=function(o){var r=D.children(o),i=D.attr(r,"data-tpl"),n=t[i],s=S.unparam(D.attr(r,"data-params")||""),u=S.merge(e.get("options"),{"$query":S.escapeHTML(e.curQuery),"$pageType":a.pageType,"$index":D.attr(r,"data-index")||"1","$isMobile":a.isMobile});n&&e.clicklog((n.genAtpanel||function(e,t){return S.substitute(n.atpanel,t)})(r,S.merge(u,s)))};this.comboBox.on("click",function(t){var a=t.target;if(/MyIE/i.test(navigator.userAgent)){if(!t._elItem)return;a.set("el",t._elItem)}if(a&&a.get("el")&&a.get("el")[0]&&D.get(".s-mi-ship",a.get("el")[0]))return o(a.get("el")),void(location.href=D.attr(D.get(".s-mi-ship .s-mi-ship-wrap",a.get("el")[0]),"data-url"));if(!(a&&(a.get("el").hasClass(".s-hqHd-menuitem")||a.get("el").hasClass(".s-hyHd-menuitem")||a.get("el").hasClass(".s-loginHd-menuitem"))||a&&a.get("el")[0]&&D.get(".s-mi-meetingPC",a.get("el")[0])||!1===e.fire("itemClick",{"activeitem":a}))){var r=this.get("form"),i=a.get("el"),n=D.attr(D.children(i),"data-params")||"q="+e.query;n=S.merge(this.get("sugConfig").extraParams,S.unparam(n)),this.filterFormParams(n),o(i),r.fire("submit",{"ignoreClicklog":1})}},this)},"filterFormParams":function(e){var t,a,o,r,i=new RegExp("windows phone|windowsphone","i"),n=navigator.userAgent||"";if(!i.test(n))for(t=0,a=this.get("form")[0],o=a.elements,r=o.length;t<r;t++)"hidden"===o[t].type&&o[t].name&&D.attr(o[t],"disabled","disabled");this.modifyFormParams(e,1)},"modifyFormParams":function(params,forceEnable){var form=this.get("form")[0];for(var k in params)if(params.hasOwnProperty(k))if(params[k]=params[k]||"",form[k]&&"INPUT"===form[k].tagName)params[k].indexOf(VALUE)>-1?params[k]!==VALUE&&D.val(form[k],eval(params[k].replace(VALUE,form[k].value))):D.val(form[k],params[k]),Node.one(form[k]).fire("valuechange"),1==forceEnable&&D.removeAttr(form[k],"disabled");else{var value=params[k];params[k].indexOf(VALUE)>-1&&(value=params[k]!==VALUE?eval(params[k].replace(VALUE,"")):""),D.append(D.create('<input type="hidden" name="'+k+'" value="'+S.escapeHTML(value)+'"/>'),form)}},"_bindSubmitEvent":function(){function e(){t.filterFormParams(S.merge(s,{"type":"p","q":VALUE,"from":i+"_1_searchbutton"}))}var t=this,a=t.get("form"),o=t.get("input"),r=t.get("button"),i=t.get("dim"),n=t.get("log"),s=t.get("sugConfig").extraParams,u=t.get("acceptCharset");a.on("submit",function(e){var a=t.fire("beforeSubmit");!1===a&&e.halt(),e.ignoreClicklog||a===t.IGNORE_CLICK_LOG||t.clicklog(","+o.val()+","+o.val()+","+i+"-,"+n.clickId+",searchbutton,"+n.pageType+","+n.isMobile),UA&&UA.ie&&u!==UNKNOWN&&(document.charset=u)}),o.on("keydown",function(t){if(13==t.keyCode){var o=new RegExp("windows phone|windowsphone","i"),r=navigator.userAgent||"";o.test(r)?(t.preventDefault(),E.fire(a,"submit")):e()}}),r.on("click",function(t){e()})},"_buildComboBoxCfg":function(e){var t=this.get("sugConfig");return{"srcNode":this._wrapInput(t.node,t.prefixCls)||"."+t.prefixCls+"combobox","dataSource":e,"format":S.bind(this._format,this),"focused":!!t.autoFocus,"prefixCls":t.prefixCls||"ks-","hasTrigger":!1,"matchElWidth":!!t.matchElWidth,"highlightMatchItem":!1,"menu":{"align":{"overflow":{"adjustY":0}}},"cache":!0,"placeholder":t.placeholder||TIP}},"_wrapInput":function(e,t){var a=this.get("sugConfig"),o=a.enableSpeech;D.attr(e,S.merge({"class":t+"combobox-input","autocomplete":"off","role":"combobox","aria-haspopup":"true","title":TIP,"aria-label":TIP},o?{"x-webkit-speech":"","x-webkit-grammar":"builtin:translate"}:{}));var r,i=D.parent(e,".{cls}combobox".replace(/{cls}/g,t)),n=S.guid(t+"combobox-");return i?(i.id=i.id||n,r=Node.one(i)):(D.wrap(e,D.create('<div id="'+n+'" class="{cls}combobox"><div class="{cls}combobox-input-wrap"></div></div>'.replace(/{cls}/g,t))),r=Node.one("#"+n)),r},"_loadConfig":function(){var e=this;return S.ready(function(){setTimeout(function(){IO({"url":"//pages.tmall.com/wow/list/act/search-act","dataType":"jsonp","scriptCharset":"utf-8","jsonpCallback":"Jsonp_fixed_searchbar_act","success":function(t){var a=e.get("templates").act;a&&(a.text=t.text||"",a.promo="undefined"==typeof t.promo?"49218":t.promo),e&&e.fire("configInit",{"data":t})}})},0)}),!0},"_format":function(e,t){if(!t)return[];var a=this.get("templates"),o=this.get("dim"),r=[],i=this._getDate(),n=this.get("sugConfig").prefixCls,s={"$wq":S.escapeHTML(e),"$query":S.escapeHTML(e),"$index":0,"$date":i,"$prefixCls":n,"$dim":o,"$userId":t.shop_info&&t.shop_info[0]&&t.shop_info[0].user_id||""};this.set("options",s);for(var u in a)a[u]?(S.log("searchbar::to parse template:"+u+"..."),a[u].parse(r,t,S.clone(s))):delete a[u];return r},"_getDate":function(){var e=new Date;return e.getFullYear()+"-"+(e.getMonth()+1)+"-"+(e.getDate()+1)},"update":function(e){for(var t,a=this.get("plugins"),o=0,r=a.length;o<r;o++)(t=a[o])&&S.isFunction(t.update)&&t.update(e)},"blur":function(){this.get("input")[0].blur()},"clicklog":function(e){var t=e.split(","),a=win.__header_atpanel_param||"",o={"pos":t[0]||"","q":t[1]||"","wq":t[2]||"","suggest":t[3]||"","clickid":t[4]||"","combo":t[5]||"","page_type":t[6]||"","is_wap":t[7]||"0","type":t[8]||5,"active":"0","search_type":"search"};a+=(S.endsWith(a,"&")?"":a?"&":"")+S.param(o),this.exposelog("/mallsearch","tmallsearch",a,"H1449172242")},"exposelog":function(e,t,a,o){if(win.goldlog&&win.goldlog.record)goldlog.record(e,t,a,o);else{var r=new Image,i="_img_"+e+"_"+(new Date).getTime();win[i]=r,r.onload=r.onerror=function(){win[i]=null},r.src="//gm.mmstat.com"+e+"?goldlog=undefined&cache="+makeCacheNum()+"&gmkey="+encodeURIComponent(t)+"&gokey="+encodeURIComponent(a)+"&cna="+(Cookie.get("cna")||""),S.log(win[i]),r=null}},"_other":function(){var e=this,t=this.get("ignoreChars"),a=new RegExp("["+t.join(",")+"]","gi"),o=this.get("input"),r=this.comboBox,i=this.get("sugConfig"),n=i.autoExpand,s=(i.prefixCls,this.get("query"));s!==UNKNOWN&&(o.attr("value",s),r.set("value",s)),o.on("keyup",function(e){e.shiftKey&&(e.keyCode<37&&16!==e.keyCode||e.keyCode>40)&&(this.value=this.value.replace(a,""))}),n&&o.on("focus",function(){r.sendRequest(S.trim(this.value))}),Node.one(window).on("resize",S.buffer(function(t){var a=e.get("menuContainer");a&&a.width(o.outerWidth())},150));var u=this.get("acceptCharset"),l=this.get("form");u!==UNKNOWN&&l.attr("accept-charset",u),!i.autoSubmitOnItemClick&&this.on("itemClick",function(){return!1}),r.on("afterCollapsedChange",function(t){t.newVal||(r.detach("afterCollapsedChange",arguments.callee),/MyIE/i.test(navigator.userAgent)&&E.delegate(D.get(".s-menu"),"click",".s-menuitem",function(t){e.comboBox.fire("click",{"_elItem":S.one(t.currentTarget)})}))}),o.on("valuechange",function(){e.curQuery=o.val()}),e.curQuery=o.val()},"_event":["beforeSubmit","beforeParse","beforeQueryChange","itemClick","restore","configInit"],"VALUE":VALUE,"IGNORE_CLICK_LOG":"{{ignore_click_log}}","UNKNOWN":UNKNOWN},{"ATTRS":{"sugConfig":{"value":{"extraParams":{},"url":"","node":"","autoFocus":!1,"autoExpand":!1,"prefixCls":"s-","placeholder":TIP,"enableSpeech":!0,"matchElWidth":!0,"autoSubmitOnItemClick":!0},"setter":function(e){var t=this.get("sugConfig");return S.mix(t,e,undefined,undefined,!0)}},"templates":{"value":{},"setter":function(e){return e}},"nodes":{"value":{}},"placeholder":{"getter":function(){var e=this.get("nodes");return e.placeholder||(e.placeholder=this.comboBox.get("placeholderEl")),e.placeholder}},"input":{"getter":function(){var e=this.get("nodes");return e.input||(e.input=this.comboBox.get("input")),e.input}},"button":{"getter":function(){var e=this,t=this.get("nodes");if("undefined"==typeof t.button){var a=this.get("form"),o=a[0].elements;S.each(o,function(t){"submit"===D.attr(t,"type")&&(e.get("nodes").button=Node.one(t))})}return!t.button&&S.log("searchbar::there isn't a button of 'submit' type in this form!","error"),t.button}},"form":{"getter":function(e){var t=this.get("nodes");return t.form||(t.form=this.get("input").parent("form")),t.form}},"container":{"getter":function(){var e=this.get("nodes");return e.container||(e.container=this.comboBox.get("el")),e.container}},"menuContainer":{"getter":function(){var e=this.get("nodes");if(!e.menuContainer){var t=this.get("menu");t&&t.get&&(e.menuContainer=t.get("el"))}return!e.menuContainer&&S.log("searchbar::at so far, popup menu for suggest is nonexistent.","warn"),e.menuContainer}},"menu":{"getter":function(){return this.comboBox.get("menu")}},"dataSourceCfg":{"value":{"xhrCfg":{"url":"","dataType":"jsonp","scriptCharset":"utf-8","data":{"code":"utf-8"}},"allowEmpty":!0,"paramName":"q","cache":!0}},"dim":{"value":".list.pc"},"log":{"value":{"pageType":"1","clickId":"topsearch","isMobile":0},"setter":function(e){var t=this.get("log");return t=S.mix(t,e,undefined,undefined,!0),t.isMobile=t.isMobile?1:0,t}},"ignoreChars":{"value":["<",">","?","\uff1f"]},"acceptCharset":{"value":UNKNOWN},"query":{"value":UNKNOWN,"setter":function(e){if(e){var t=this.get("ignoreChars"),a=new RegExp("["+t.join(",")+"]","gi");e=e.replace(a,"")}else e="";return e}}}});return SearchBar.UNKNOWN=UNKNOWN,SearchBar.VALUE=VALUE,SearchBar.IGNORE_CLICK_LOG="{{ignore_click_log}}",SearchBar},{"requires":["node","rich-base","dom","combobox","ua","cookie","event","io"]});KISSY.add("mui/searchbar/plugin/spm",function(e,t,a){function r(t){r.superclass.constructor.call(this,e.merge({"spm":c},t||{}))}function i(e){for(var t;e&&"HTML"!=e.tagName&&"BODY"!=e.tagName&&e.getAttribute&&!(t=e.getAttribute(o))&&(e=e.parentNode););return t}function n(e){try{return t.get('meta[name="'+e+'"]')}catch(o){for(var a=t.query("meta"),r="",i=0,n=a.length;i<n;i++)if(a[i].name==e){r=a[i];break}return r}}var o="data-spm",s="spm",c="0.0.a2227oh.d100";return e.extend(r,a,{"pluginInitializer":function(e){this.set("caller",e),this.init()},"init":function(){var e=this.get("caller");e&&(e.get("sugConfig").extraParams[s]=this.get("spm"))}},{"ATTRS":{"pluginId":{"value":"spm"},"spm":{"value":c,"setter":function(e){var a=(e.split(".")||[]).reverse(),r={};r.d=a[0]||"0",r.c=a[1]||"0",r.b=a[2]||"0",r.a=a[3]||"0";var i=n("spm-id"),s=i?i.content:"";s||(i=n(o),s=i?i.content:"",s+="."+(t.attr(document.body,o)||""));var c=s.split(".")||[];return r.a=c[0]||r.a,r.b=c[1]||r.b,[r.a,r.b,r.c,r.d].join(".")},"getter":function(e){var t=(e.split(".")||[]).reverse(),a={},r=this.get("caller");if(r){var n,c=r.get("form"),u=c[0][s];if(u&&"INPUT"===u.tagName&&(n=(u.value.split(".")||[]).reverse(),t[0]=n[0]||t[0],t[1]=n[1]||t[1]),!t[1]&&"0"===a.c){var l=r.get("input"),m=r.get("container");t[1]=m.attr(o)||c.attr(o)||i(l[0])||t[1]}}return t.reverse().join(".")}}}}),r},{"requires":["dom","base"]});KISSY.add("mui/searchbar/plugin/placeholder",function(e,t,a){function r(e){this._tasks=[],r.superclass.constructor.call(this,e||{})}var i=window;return e.extend(r,a,{"pluginInitializer":function(t){if(this.set("caller",t),!t.get("placeholder")){var a=this.get("text"),r=t.get("input"),i=t.get("container"),n=r.attr("id"),o=t.get("sugConfig").prefixCls;!n&&r.attr("id",n=e.guid(o+"combobox-input")),t.comboBox.set("placeholderEl",e.all('<label for="'+n+'" class="'+o+'combobox-placeholder">'+a+"</label>").appendTo(i))}this._customizeText(),this._customizeInteraction(),this._customizeSearch()},"_customizeText":function(){var e=this.get("caller"),t=e.comboBox,a=t.get("placeholderEl"),r=this.get("text");a&&a.html(r),t.set("placeholder",r)},"_customizeInteraction":function(){function t(){""===e.trim(i.val())?r.css({"visibility":"visible"}):r.css({"display":"none","visibility":"hidden"})}var a=this.get("caller"),r=a.get("placeholder"),i=a.get("input"),n=this.get("colors");setTimeout(t,100),i.on("valuechange",t),r.css("color",n[1]),a.get("sugConfig").autoFocus&&r.css("color",n[0]),i.on("focus",function(){r.css("color",n[0]),""===e.trim(this.value)&&r.css({"display":"inline","visibility":"visible"})}),i.on("blur",function(){""===e.trim(this.value)&&""===e.trim(i.attr("value"))&&r.css({"color":n[1],"visibility":"visible"})}),i.on("keydown",function(t){var a=t.keyCode;32==a&&""===e.trim(this.value)?r.css({"visibility":"hidden"}):(a<13||a>37&&a<112||a>123)&&r.css({"visibility":"hidden"})}),i.on("keyup",function(e){var t=e.keyCode;""===this.value&&!(8==t||46==t)&&r.css({"display":"inline","visibility":"visible"})})},"_customizeSearch":function(){var a=this,r=this.get("query"),i=(this.get("text"),this.get("redirectUrl")),n=this.get("xiaoer"),o=this.get("caller"),s=o.get("input"),c=o.get("form"),u=o.get("dim"),l=o.get("log");if(r&&!this._eQueryFn?(o.on("beforeSubmit",this._eQueryFn=function(t){if(""===e.trim(s.val()))return s.val(a.get("query")),o.modifyFormParams({"from":u+"_"+n+"_placeholder"}),o.clicklog(","+a.get("query")+","+a.get("query")+","+u+"-,"+l.clickId+",placeholder,"+l.pageType+","+l.isMobile),setTimeout(function(){s.val("")},0),o.IGNORE_CLICK_LOG}),setTimeout(function(){o.exposelog("/msearch.3.3","searchbar-placeholder","dim="+u+"&q="+r+"&xiaoer="+n,"H46777406")},0)):!r&&this._eQueryFn&&(o.detach("beforeSubmit",this._eQueryFn),this._eQueryFn=null),r)this._eRedirectFn&&(o.detach("beforeSubmit",this._eRedirectFn),this._eRedirectFn=null);else{if(i&&!this._eRedirectFn)return c[0].redirect||c.append(t.create('<input type="hidden" name="redirect" value="" disabled="disabled" />')),void o.on("beforeSubmit",this._eRedirectFn=function(a){if(""===e.trim(s.val()))return c[0].redirect.value=i,t.removeAttr(c[0].redirect,"disabled"),o.modifyFormParams({"from":u+"_1_placeholder"}),o.clicklog(","+i+","+i+","+u+"-,"+l.clickId+",placeholder,"+l.pageType+","+l.isMobile),o.IGNORE_CLICK_LOG;c[0].redirect.value="",t.attr(c[0].redirect,"disabled","disabled")});!i&&this._eRedirectFn&&(o.detach("beforeSubmit",this._eRedirectFn),this._eRedirectFn=null)}!this._eEmptyFn&&o.on("beforeSubmit",this._eEmptyFn=function(t){return a._eQueryFn||a._eRedirectFn?(o.detach("beforeSubmit",a._eEmptyFn),void(a._eEmptyFn=null)):""===e.trim(s.val())?(a._emptyNotice(),!1):void 0})},"_reviseUrl":function(e){var t=i.TB&&TB.globalToolFn&&TB.globalToolFn.isDaily&&TB.globalToolFn.isDaily(),a="?spm=0.0.0.0",r=e.indexOf("?"),n=e.indexOf("#"),o=n<0?e.length:n;return t&&e.replace(/\b\/\/list.tmall.com\b/,"//list.daily.tmall.net"),r>0?e.replace("?",a+(r==o-1?"":"&")):e+a},"_emptyNotice":function(){var e=this.get("caller"),t=e.get("placeholder"),a=e.get("input");a._inFlash||(a._inFlash=!0,t.html("\u8bf7\u8f93\u5165\u5173\u952e\u5b57"),t.css("visibility","visible"),this._flashBackground())},"_flashBackground":function(){var a=this.get("caller"),r=a.get("input"),i={"background":r.css("background"),"borderLeftColor":r.css("border-left-color"),"zIndex":r.css("z-index")};r.css({"background":"none #fff","borderLeftColor":"#fdbd78","zIndex":e.UA.ie<8?-1:0}),this._flashBackgroundAnim(r,4,function(){t.css(r,i),r._inFlash=!1})},"_flashBackgroundAnim":function(t,a,r){var i=this;if(a<=0)return void(r&&r.call());new e.Anim(t,{"backgroundColor":a%2==0?"#fdbd78":"#fff"},.3,"easeNone",function(){i._flashBackgroundAnim(t,--a,r)}).run()},"renderPlugin":function(e){},"update":function(e){if(e&&"object"==typeof e){if(!this.get("caller"))return void this._tasks.push(["update",arguments]);e.text&&this.set("text",e.text),e.query&&this.set("query",e.query),e.redirectUrl&&this.set("redirectUrl",e.redirectUrl),e.xiaoer&&this.set("xiaoer",e.xiaoer),this._customizeText(),this._customizeSearch()}}},{"ATTRS":{"pluginId":{"value":"placeholder"},"colors":{"value":["#ccc","#666"]},"text":{"value":"\u641c\u7d22 \u5929\u732b \u5546\u54c1/\u54c1\u724c/\u5e97\u94fa","setter":function(e){return"string"==typeof e?e:"\u641c\u7d22 \u5929\u732b \u5546\u54c1/\u54c1\u724c/\u5e97\u94fa"}},"query":{"value":"","setter":function(e){return"string"==typeof e?e:""}},"redirectUrl":{"value":"","setter":function(e){return"string"==typeof e&&"notRedirect"!==e?e:""}},"xiaoer":{"value":0,"setter":function(e){return e?1:0}},"caller":{"value":undefined,"setter":function(e){if(e){var t=this;return setTimeout(function(){for(var e,a=t._tasks,r=0,i=a.length;r<i;r++)e=a.shift(),t[e[0]].apply(t,e[1])},10),e}}}}}),r},{"requires":["dom","base"]});KISSY.add("mui/searchbar/plugin/hubaccess",function(e,a,t,r,i,o){function n(a){n.superclass.constructor.call(this,e.merge(a||{}))}function s(){var e=new i(location.href).getHostname(),a=new i(location.href).getPath();return"www.tmall.com"!==e||"/"!==a&&""!==a?"list.tmall.com"===e?"search":"pre.wormhole.tmall.com"===e&&"/wow/portal/act/fp"===a&&"home":"home"}function u(){return 7!==o.ie&&6!==o.ie&&!o.ipad}function c(){return"on"===(new i(location.href).getQuery().get("hubdebug")||"")}return e.extend(n,t,{"pluginInitializer":function(e){this.set("caller",e),this.init()},"init":function(){if(this.get("caller")){this.HUB_INSTANCE=null,this.HUB_SEARCH_SUBMIT=!1,this.HUB_ENV=s(),this.HUB_BRO=u(),this.HUB_IS_ON_ZEBRA=!1;var e=new i(location.href).getQuery().get("s"),a=new i(location.href).getQuery().get("jumpto");this.HUB_ENV&&this.HUB_BRO&&(e||a||this.bindListener())}},"bindListener":function(){var e=this,a=this.get("caller");a&&a.on("configInit",function(t){t&&t.data&&t.data.isHubOn&&(a.set("HUB_IS_ON_ZEBRA",!0),e.initHub(t.data))})},"initHub":function(a){var t,i=this,o=this.get("caller"),n=o.get("form"),s=o.get("input"),u="";if(_CTK3417(30,"hub.init"),c()?(t=a.version_2,u=[location.href,"###version:",t].join("")||"",_CTK3417(0,"error:hub.error","hub.init",{"msg":"\u7ea2\u5305\u7ec4\u4ef6\u8c03\u8bd5\u5f00\u542f","group":u,"type":"error"})):t=a.version_1,"close"===(t=t||"1.6.8"))return!1;e.config({"packages":{"hbhub":{"path":"//g.alicdn.com/mtb/app-hongbaohub/"+t+"/","version":t,"ignorePackageNameInUri":!0,"charset":"utf-8","debug":!0}}}),e.use("hbhub/index",function(e,a){i.HUB_INSTANCE=a;var t="";"search"===i.HUB_ENV&&(t=s.val()),a.init(t)}),o&&o.on("beforeSubmit",function(){var a=o.get("HUB_IS_ON_ZEBRA"),t=e.trim(s.val());return!(a&&!i.HUB_SEARCH_SUBMIT)||(i.HUB_INSTANCE&&i.HUB_INSTANCE.intercept(t,function(e){i.HUB_SEARCH_SUBMIT=!0,r.fire(n,"submit")}),!1)})}},{"ATTRS":{"pluginId":{"value":"hub"}}}),n},{"requires":["dom","base","event","uri","ua"]});KISSY.add("mui/searchbar/template/act",function(e,t){return{"name":"act","text":"","promo":"49218","tpl":'<div class="{$prefixCls}mi-act" data-tpl="act" data-params="q={$query}&promo={promo}&type=p&xl={$wq}_1&from={$dim}_1_suggest"><span class="{$prefixCls}mi-cont-key">{$query}</span><span class="{$prefixCls}mi-cont-text">\u5728<b>{text}</b>\u4e0b\u641c\u7d22</span></div>',"atpanel":"{$index},{q},{$wq},{$dim}-sugAct,option,suggest,{$pageType},{$isMobile}","parse":function(t,a,r){var i=r.$query||"";if("undefined"!==i&&""!==e.trim(i)&&this.text){r.text=this.text,r.promo=this.promo;var n=e.substitute(this.tpl,r);t.push({"textContent":i,"content":n})}}}},{"requires":["ajax"]});KISSY.add("mui/searchbar/template/shipShop",function(e){return{"name":"shipShop","tpl":'<div class="{$prefixCls}mi-ship" data-tpl="shipShop" data-index="0" data-params="q={$query}&type=2&style=w&xl={$wq}_2&from={$dim}_2_suggest"><span class="{$prefixCls}mi-ship-wrap" data-url="{$shopUrl}"><img class="{$prefixCls}mi-ship-img" src="{$logo}"><span class="{$prefixCls}mi-ship-key">{$shopName}</span><i class="{$prefixCls}mi-ship-icon"></i></span></div>',"atpanel":"{$index},{q},{$wq},{$dim}-sugShop,{$userId},suggest,{$pageType},{$isMobile},2","parse":function(t,a,r){var i=r.$query,n=this;if(i&&a.shop_info&&a.shop_info.length)for(var o=0;o<a.shop_info.length;o++){e.each(a.shop_info[o],function(e,t){switch(t){case"shop_name":r.$shopName=e;break;case"logo":r.$logo="//img.alicdn.com/tfscom/"+e;break;case"shop_url":r.$shopUrl=e}}),r.$query=e.urlEncode(i);var s=e.substitute(n.tpl,r);t.push({"textContent":i,"content":s})}}}});KISSY.add("mui/searchbar/template/cat",function(e,t){return{"name":"cat","tpl":'<div class="{$prefixCls}mi-cat" data-tpl="cat" data-index="{$index}" data-params="q={$2}&cat={$1}&type=p&xl={$wq}_{$index}&from={$dim}_1_suggest"><span class="{$prefixCls}mi-cont-text">\u5728<b>{$0}</b>\u5206\u7c7b\u4e0b\u641c\u7d22</span></div>',"atpanel":"{$index},{q},{$wq},{$dim}-sugCat,{cat},suggest,{$pageType},{$isMobile}","parse":function(t,a,r){var i=a.cat;if(!a.tmall_noresult&&i&&e.isArray(i)&&!(a.result.length<1)){var n={"textContent":"","content":'<div class="{$prefixCls}mi-cat" data-tpl="cat" data-index="0" data-params="q={$2}&type=p&xl={$wq}_{$index}&from={$dim}_1_suggest"><span class="{$prefixCls}mi-cont-key">{$2}</span></div>'};t.push(n);for(var o=0,s=Math.min(i.length,2),c="";o<s;o++){r.$index=1+o;var u=i[o];if(e.isArray(u))for(var l=0;l<3;l++)r["$"+l]=u[l]||r.$query;c=e.substitute(this.tpl,r),n.textContent=r.$2,n.content=e.substitute(n.content,r),t.push({"textContent":r.$2,"content":c})}t.push({"content":'<div class="hr"/>',"disabled":!0})}}}},{"requires":["dom"]});KISSY.add("mui/searchbar/template/list",function(e){return{"name":"list","tpl":'<div class="{$prefixCls}mi-list" data-tpl="list" data-index="{$index}" data-params="q={$query}&type=p&xl={$wq}_{$index}&from={$dim}_1_suggest"><span class="{$prefixCls}mi-cont-key">{text}</span><span class="{$prefixCls}mi-cont-count">\u7ea6{count}\u4e2a\u7ed3\u679c</span><a class="{$prefixCls}mi-btn-backfill" href="javascript:;">\u56de\u586b</a></div>',"atpanel":"{$index},{q},{$wq},{$dim}-sugQuery,query,suggest,{$pageType},{$isMobile}","parse":function(t,a,r){var i=this,n=r.$query;a.tmall_noresult&&t.push({"content":'<div class="'+r.$prefixCls+'mi-noresult-tip">\u56e7\uff0c\u60a8\u8f93\u5165\u7684\u5173\u952e\u8bcd\u4e0b\u6ca1\u6709\u7ed3\u679c\uff0c\u8bd5\u8bd5\u8fd9\u4e9b\u5427\uff1a</div>',"disabled":!0}),e.each(a.result,function(o,s){if(!o||!o[0])return void a.result.splice(s,1);for(var c in t)if(t[c].textContent===o[0])return;var u=o[0],l=n;if(!u.match(/\<(\/)?\w\>/gi)){for(;u.indexOf(l)<0;)l=l.substr(0,l.length-1);var p=u.indexOf(l),d=p+l.length,m=u.substr(0,p),h=u.substr(d);m=m?"<b>"+m+"</b>":"",h=h?"<b>"+h+"</b>":"",u=m+l+h}r.$query=e.urlEncode(o[0].replace(/\<(\/)?\w\>/gi,"")),r.$index=s+1,r.text=u,r.count=o[1];var g=e.substitute(i.tpl,r);t.push({"textContent":e.urlDecode(r.$query),"content":g})})}}});KISSY.add("mui/searchbar/template/shop",function(e){return{"name":"shop","tpl":'<div class="{$prefixCls}mi-tip" data-tpl="shop" data-params="q={$query}&type=p&style=w&xl={$wq}_2&from={$dim}_2_suggest"><i></i>\u627e\u201c<b>{$text}</b>\u201d\u76f8\u5173<em>\u5e97\u94fa</em></div>',"atpanel":"{$index},{q},{$wq},{$dim}-sugShop,option,suggest,{$pageType}","parse":function(t,a,r){var i=r.$query;if(""!==e.trim(i)&&"undefined"!=i){r.$query=e.urlEncode(i),r.$text=i;var n=e.substitute(this.tpl,r);t.push({"textContent":i,"content":n})}}}});KISSY.add("mui/searchbar/template/quickSearch",function(e){return{"name":"quickSearch","tpl":'<p class="{$prefixCls}mi-qs"><i></i>\u6309\u5feb\u6377\u952e <em>shift</em> + <em>?</em> \u53ef\u4ee5\u968f\u65f6\u6253\u5f00\u5feb\u6377\u641c\u7d22\u6846\uff0c\u8d76\u7d27\u8bd5\u8bd5\u5427~</p>',"parse":function(t,a,r){var i=r.$query;if(""!==e.trim(i)){var n=e.substitute(this.tpl,r);t.push({"content":n,"disabled":!0})}}}});KISSY.add("mui/searchbar/template/meetingPlace",function(e,t,a){function r(){var e,a=t.query("meta")||[],r="0.0";for(e=0;e<a.length;e++)if("spm-id"===t.attr(a[e],"name")){r=t.attr(a[e],"content");break}return r}return{"name":"meetingPlace","tpl":'<div class="{$prefixCls}mi-meetingPC" data-tpl="meetingPlace" data-index="0" data-params="q={$query}&type=2&style=w&xl={$wq}_2&from={$dim}_2_suggest"><a class="{$prefixCls}mi-meetingPC-wrap" target="_blank" href="{$actionUrl}"><img class="{$prefixCls}mi-meetingPC-img" src="{$imgUrl}"></a></div>',"atpanel":"{$index},{q},{$wq},{$dim}-sugShop,{$userId},suggest,{$pageType},{$isMobile},2","parse":function(t,i,n){var o=n.$query,s=this;if(o&&i.banner&&i.banner.length)for(var c=0;c<i.banner.length;c++){e.each(i.banner[c],function(e,t){switch(t){case"bannerText":n.$bannerText=e;break;case"imgUrl":n.$imgUrl=e;break;case"actionUrl":n.$actionUrl=e}}),n.$query=e.urlEncode(o);var u=n.$actionUrl;try{var l=new a(n.$actionUrl),p=r()+".banner.1";l.query&&l.query.add("spm",p),n.$actionUrl=l.toString(!1)}catch(m){n.$actionUrl=u}var d=e.substitute(s.tpl,n);t.push({"textContent":o,"content":d})}}}},{"requires":["dom","uri"]});