/*! switchable - v1.3.1 - 2013-10-25 2:54:13 PM
* Copyright (c) 2013 yiminghe; Licensed  */
KISSY.add("gallery/switchable/1.3.1/base",function(a,b,c,d){function e(c,e){var f=this;f._triggerInternalCls=a.guid(w),f._panelInternalCls=a.guid(x),e=e||{},"markupType"in e||(e.panelCls?e.markupType=1:e.panels&&(e.markupType=2));for(var g=f.constructor;g;)e=a.merge(g.Config,e),g=g.superclass?g.superclass.constructor:null;f.container=b.get(c),f.config=e,f.activeIndex=e.activeIndex;var h;f.activeIndex>-1||("number"==typeof e.switchTo?h=e.switchTo:f.activeIndex=0),f._init(),f._initPlugins(),f.fire(p),h!==d&&f.switchTo(h)}function f(a){if(a&&a.length){if(1==a.length)return a[0].parentNode;for(var c=a[0],d=0;!d&&c!=document.body;){c=c.parentNode,d=1;for(var e=1;e<a.length;e++)if(!b.contains(c,a[e])){d=0;break}}return c}return null}function g(a){var b={};return b.type=a.type,b.target=a.target,{originalEvent:b}}var h="display",i="block",j=a.makeArray,k="none",l=c.Target,m="forward",n="backward",o=".",p="init",q="beforeSwitch",r="switch",s="beforeRemove",t="add",u="remove",v="ks-switchable-",w=v+"trigger-internal",x=v+"panel-internal";return e.getDomEvent=g,e.addPlugin=function(a,b){b=b||e;for(var c=a.priority=a.priority||0,d=0,f=b.Plugins=b.Plugins||[];d<f.length&&!(f[d].priority<c);d++);f.splice(d,0,a)},e.Config={markupType:0,navCls:v+"nav",contentCls:v+"content",triggerCls:v+"trigger",panelCls:v+"panel",triggers:[],panels:[],hasTriggers:!0,triggerType:"mouse",delay:.1,activeIndex:-1,activeTriggerCls:"ks-active",switchTo:d,steps:1,viewSize:[]},a.augment(e,l,{_initPlugins:function(){for(var b=this,c=[],d=b.constructor;d;)d.Plugins&&c.push.apply(c,[].concat(d.Plugins).reverse()),d=d.superclass?d.superclass.constructor:null;c.reverse(),a.each(c,function(a){a.init&&a.init(b)})},_init:function(){var a=this,b=a.config;a._parseMarkup(),b.hasTriggers&&a._bindTriggers(),a._bindPanels()},_parseMarkup:function(){var a,c,d,e=this,g=e.container,h=e.config,i=[],k=[];switch(h.markupType){case 0:a=b.get(o+h.navCls,g),a&&(i=b.children(a)),c=b.get(o+h.contentCls,g),k=b.children(c);break;case 1:i=b.query(o+h.triggerCls,g),k=b.query(o+h.panelCls,g);break;case 2:i=h.triggers,k=h.panels,a=h.nav,c=h.content}d=k.length,e.length=Math.ceil(d/h.steps),e.nav=a||h.hasTriggers&&f(i),!h.hasTriggers||e.nav&&0!=i.length||(i=e._generateTriggersMarkup(e.length)),e.triggers=j(i),e.panels=j(k),e.content=c||f(k)},_generateTriggersMarkup:function(a){var c,d,e=this,f=e.config,g=e.nav||b.create("<ul>");for(g.className=f.navCls,d=0;a>d;d++)c=b.create("<li>"),d===e.activeIndex&&(c.className=f.activeTriggerCls),c.innerHTML=d+1,g.appendChild(c);return e.container.appendChild(g),e.nav=g,b.children(g)},_bindTriggers:function(){var b=this,d=b.config,e=b._triggerInternalCls,f=b.nav,g=b.triggers;a.each(g,function(a){b._initTrigger(a)}),c.delegate(f,"click","."+e,function(a){var c=a.currentTarget,d=b._getTriggerIndex(c);b._onFocusTrigger(d,a)}),"mouse"===d.triggerType&&(c.delegate(f,"mouseenter","."+e,function(a){var c=a.currentTarget,d=b._getTriggerIndex(c);b._onMouseEnterTrigger(d,a)}),c.delegate(f,"mouseleave","."+e,function(){b._onMouseLeaveTrigger()}))},_initTrigger:function(a){b.addClass(a,this._triggerInternalCls)},_bindPanels:function(){var b=this,c=b.panels;a.each(c,function(a){b._initPanel(a)})},_initPanel:function(a){b.addClass(a,this._panelInternalCls)},_onFocusTrigger:function(a,b){var c=this;c._triggerIsValid(a)&&(this._cancelSwitchTimer(),c.switchTo(a,d,g(b)))},_onMouseEnterTrigger:function(b,c){var e=this;if(e._triggerIsValid(b)){var f=g(c);e.switchTimer=a.later(function(){e.switchTo(b,d,f)},1e3*e.config.delay)}},_onMouseLeaveTrigger:function(){this._cancelSwitchTimer()},_triggerIsValid:function(a){return this.activeIndex!==a},_cancelSwitchTimer:function(){var a=this;a.switchTimer&&(a.switchTimer.cancel(),a.switchTimer=d)},_getTriggerIndex:function(b){var c=this;return a.indexOf(b,c.triggers)},_resetLength:function(){this.length=this._getLength()},_getLength:function(a){var b=this,c=b.config;return a===d&&(a=b.panels.length),Math.ceil(a/c.steps)},_afterAdd:function(a,b,c){var e=this;e._resetLength();var f=e._getLength(a+1)-1;1==e.config.steps&&e.activeIndex>=f&&(e.activeIndex+=1);var g=e.activeIndex;e.activeIndex=-1,e.switchTo(g),b?e.switchTo(f,d,d,c):c()},add:function(c){var d=c.callback||a.noop,e=this,f=e.nav,g=e.content,h=c.trigger,i=c.panel,j=c.active,k=e.panels.length,l=null!=c.index?c.index:k,m=e.triggers,n=e.panels,o=e.length,p=null,q=null;l=Math.max(0,Math.min(l,k));var r=n[l]||null;n.splice(l,0,i),g.insertBefore(i,r),1==e.config.steps?(q=m[l]||null,f.insertBefore(h,q),m.splice(l,0,h)):(p=e._getLength(),p!=o&&(b.append(h,f),m.push(h))),e._initPanel(i),e._initTrigger(h),e._afterAdd(l,j,d),e.fire(t,{index:l,trigger:h,panel:i})},remove:function(c){function e(){if(o&&(b.remove(o),k.splice(f,1)),n){b.remove(n);for(var a=0;a<m.length;a++)if(m[a]==n){h.triggers.splice(a,1);break}}h._resetLength(),h.fire(u,{index:f,trigger:n,panel:o})}var f,g=c.callback||a.noop,h=this,i=h.config.steps,j=h.length,k=h.panels;f="index"in c?c.index:c.panel;var l=h._getLength(k.length-1),m=h.triggers,n=null,o=null;if(k.length&&(f=a.isNumber(f)?Math.max(0,Math.min(f,k.length-1)):a.indexOf(f,k),n=1==i?m[f]:l!==j?m[j-1]:null,o=k[f],h.fire(s,{index:f,panel:o,trigger:n})!==!1)){if(0==l)return e(),g(),void 0;var p=h.activeIndex;if(i>1)return p==l?h.switchTo(p-1,d,d,function(){e(),g()}):(e(),h.activeIndex=-1,h.switchTo(p,d,d,function(){g()})),void 0;if(p==f){var q=p>0?p-1:p+1;h.switchTo(q,d,d,function(){e(),0==p&&(h.activeIndex=0),g()})}else p>f&&(p--,h.activeIndex=p),e(),g()}},switchTo:function(a,b,c,e){var f=this,g=f.config,h=f.activeIndex,i=f.triggers;return f._triggerIsValid(a)?f.fire(q,{fromIndex:h,toIndex:a})===!1?f:(f.fromIndex=h,g.hasTriggers&&f._switchTrigger(i[h]||null,i[a]),b===d&&(b=a>h?m:n),f.activeIndex=a,f._switchView(b,c,function(){e&&e.call(f)}),f):f},_switchTrigger:function(a,c){var d=this.config.activeTriggerCls;a&&b.removeClass(a,d),b.addClass(c,d)},_getFromToPanels:function(){var a,b,c=this,d=c.fromIndex,e=c.config.steps,f=c.panels,g=c.activeIndex;return a=d>-1?f.slice(d*e,(d+1)*e):null,b=f.slice(g*e,(g+1)*e),{fromPanels:a,toPanels:b}},_switchView:function(a,c,d){var e=this,f=e._getFromToPanels(),g=f.fromPanels,j=f.toPanels;g&&b.css(g,h,k),b.css(j,h,i),setTimeout(function(){e._fireOnSwitch(c)},0),d&&d.call(this)},_fireOnSwitch:function(b){var c=this;c.fire(r,a.merge(b,{fromIndex:c.fromIndex,currentIndex:this.activeIndex}))},prev:function(a){var b=this;b.switchTo((b.activeIndex-1+b.length)%b.length,n,a)},next:function(a){var b=this;b.switchTo((b.activeIndex+1)%b.length,m,a)},destroy:function(d){for(var e=this,f=e.constructor;f;)a.each(f.Plugins,function(a){a.destroy&&a.destroy(e)}),f=f.superclass?f.superclass.constructor:null;d?(c.remove(e.container),e.content&&c.remove(e.content),e.nav&&c.remove(e.nav)):b.remove(e.container),e.nav=null,e.content=null,e.container=null,e.triggers=[],e.panels=[],e.detach()}}),e},{requires:["dom","event"]}),KISSY.add("gallery/switchable/1.3.1/accordion/base",function(a,b,c){function d(a,b){var c=this;return c instanceof d?(d.superclass.constructor.apply(c,arguments),void 0):new d(a,b)}return a.extend(d,c,{_switchTrigger:function(a,c){var e=this,f=e.config;f.multiple?b.toggleClass(c,f.activeTriggerCls):d.superclass._switchTrigger.apply(e,arguments)},_triggerIsValid:function(a){return this.config.multiple||d.superclass._triggerIsValid.call(this,a)},_switchView:function(a,c,e){var f=this,g=f.config,h=f._getFromToPanels().toPanels;g.multiple?(b.toggle(h),this._fireOnSwitch(c),e&&e.call(this)):d.superclass._switchView.apply(f,arguments)}}),d.Config={markupType:1,triggerType:"click",multiple:!1},d},{requires:["dom","../base"]}),KISSY.add("gallery/switchable/1.3.1/carousel/base",function(a,b,c,d){function e(a,b){var c=this;return c instanceof e?(e.superclass.constructor.apply(c,arguments),void 0):new e(a,b)}var f="ks-switchable-",g=".",h="added",i="removed",j="prevBtn",k="nextBtn",l={originalEvent:{target:1}};return e.Config={circular:!0,prevBtnCls:f+"prev-btn",nextBtnCls:f+"next-btn",disableBtnCls:f+"disable-btn"},a.extend(e,d,{_init:function(){function d(a){b.removeClass([f[j],f[k]],n),0==a&&b.addClass(f[j],n),a==f.length-1&&b.addClass(f[k],n)}var f=this;e.superclass._init.call(f);var m=f.config,n=m.disableBtnCls;a.each(["prev","next"],function(a){var d=f[a+"Btn"]=b.get(g+m[a+"BtnCls"],f.container);c.on(d,"mousedown",function(b){b.preventDefault();var c=f.activeIndex;"prev"!=a||0==c&&!m.circular||f[a](l),"next"!=a||c==f.length-1&&!m.circular||f[a](l)})}),m.circular||(f.on(h+" "+i,function(){d(f.activeIndex)}),f.on("switch",function(a){d(a.currentIndex)})),c.delegate(f.content,"click",g+f._panelInternalCls,function(a){var b=a.currentTarget;f.fire("itemSelected",{item:b})})},destroy:function(a){var b=this;a&&(b.nextBtn&&c.remove(b.nextBtn),b.prevBtn&&c.remove(b.prevBtn)),e.superclass.destroy.apply(b,arguments)}}),e},{requires:["dom","event","../base"]}),KISSY.add("gallery/switchable/1.3.1/slide/base",function(a,b){function c(a,b){var d=this;return d instanceof c?(c.superclass.constructor.apply(d,arguments),void 0):new c(a,b)}return c.Config={autoplay:!0,circular:!0},a.extend(c,b),c},{requires:["../base"]}),KISSY.add("gallery/switchable/1.3.1/tabs/base",function(a,b){function c(a,b){var f=this;return f instanceof c?(c.superclass.constructor.call(f,a,b),f.on("beforeSwitch",d),f.on("switch",e),void 0):new c(a,b)}function d(a){this.panels[a.toIndex].style.visibility=""}function e(a){this.panels[a.fromIndex].style.visibility="hidden"}return a.extend(c,b),c.Config={},c},{requires:["../base"]}),KISSY.add("gallery/switchable/1.3.1/lazyload",function(a,b,c){function d(a,b){b=b||j;var c=a.getAttribute(b);c&&a.src!=c&&(a.src=c,a.removeAttribute(b))}function e(c,e,g){var h;"img-src"===e&&(e="img"),a.isArray(c)||(c=[b.get(c)]),a.each(c,function(c){switch(e){case"img":h="IMG"===c.nodeName?[c]:b.query("img",c),a.each(h,function(a){d(a,g||j+l)});break;default:b.query("textarea",c).each(function(a){b.hasClass(a,g||k+l)&&f(a,!0)})}})}function f(a,c){a.style.display="none",a.className="";var d=b.create("<div>");a.parentNode.insertBefore(d,a),b.html(d,a.value,c)}var g="beforeSwitch",h="img",i="textarea",j="data-ks-lazyload",k="ks-datalazyload",l="-custom",m={};return m[h]="lazyImgAttribute",m[i]="lazyTextareaClass",a.mix(c.Config,{lazyImgAttribute:"data-ks-lazyload-custom",lazyTextareaClass:"ks-datalazyload-custom",lazyDataType:i}),c.addPlugin({name:"lazyload",init:function(a){function c(b){var h=a._realStep||j.steps,i=b.toIndex*h,l=i+h;e(a.panels.slice(i,l),k,f),d()&&a.detach(g,c)}function d(){var c,d,e,g,j=k===h,l=j?"img":k===i?"textarea":"";if(l)for(c=b.query(l,a.container),d=0,g=c.length;g>d;d++)if(e=c[d],j?b.attr(e,f):b.hasClass(e,f))return!1;return!0}var f,j=a.config,k=j.lazyDataType;"img-src"===k?k=h:"area-data"===k&&(k=i),j.lazyDataType=k,f=j[m[k]],k&&f&&(a.on(g,c),c({toIndex:a.activeIndex}))}}),c},{requires:["dom","./base"]}),KISSY.add("gallery/switchable/1.3.1/effect",function(a,b,c,d,e,f){var g,h="display",i="block",j="none",k="opacity",l="z-index",m="position",n="relative",o="absolute",p="scrollx",q="scrolly",r="fade",s="left",t="top",u="float",v="px";return a.mix(e.Config,{effect:j,duration:.5,easing:"easeNone"}),e.Effects={none:function(a){var c=this,d=c._getFromToPanels(),e=d.fromPanels,f=d.toPanels;e&&b.css(e,h,j),b.css(f,h,i),a&&a()},fade:function(c){var e=this,g=e._getFromToPanels(),h=g.fromPanels,i=g.toPanels;h&&1!==h.length&&a.error("fade effect only supports steps == 1.");var j=e.config,m=h?h[0]:null,n=i[0];e.anim&&(e.anim.stop(),b.css(e.anim.fromEl,{zIndex:1,opacity:0}),b.css(e.anim.toEl,"zIndex",9)),b.css(n,k,1),m?(e.anim=new d(m,{opacity:0},j.duration,j.easing,function(){e.anim=f,b.css(n,l,9),b.css(m,l,1),c&&c()}).run(),e.anim.toEl=n,e.anim.fromEl=m):(b.css(n,l,9),c&&c())},scroll:function(a,c,e){var g=this,h=g.fromIndex,i=g.config,j=i.effect===p,k=g.viewSize[j?0:1]*g.activeIndex,l={};l[j?s:t]=-k+v,g.anim&&g.anim.stop(),e||h>-1?g.anim=new d(g.content,l,i.duration,i.easing,function(){g.anim=f,a&&a()}).run():(b.css(g.content,l),a&&a())}},g=e.Effects,g[p]=g[q]=g.scroll,e.addPlugin({priority:10,name:"effect",init:function(c){var d=c.config,e=d.effect,f=c.panels,g=c.content,k=d.steps,l=f[0],t=c.container,v=c.activeIndex;if(e!==j)switch(b.css(f,h,i),e){case p:case q:if(b.css(g,m,o),"static"==b.css(g.parentNode,m)&&b.css(g.parentNode,m,n),e===p&&(b.css(f,u,s),b.width(g,"999999px")),c.viewSize=[d.viewSize[0]||l&&b.outerWidth(l,!0)*k,d.viewSize[1]||l&&b.outerHeight(l,!0)*k],c.viewSize[0]||a.error("switchable must specify viewSize if there is no panels"),1==k&&l){var w=1,x=c.viewSize,y=l.parentNode.parentNode,z=[Math.min(b.width(t),b.width(y)),Math.min(b.height(t),b.height(y))];"scrollx"==e?w=Math.floor(z[0]/x[0]):"scrolly"==e&&(w=Math.floor(z[1]/x[1])),w>d.steps&&(c._realStep=w)}break;case r:var A,B=v*k,C=B+k-1;a.each(f,function(a,c){A=c>=B&&C>=c,b.css(a,{opacity:A?1:0,position:o,zIndex:A?9:1})})}}}),a.augment(e,{_switchView:function(b,c,d){var e=this,f=e.config,h=f.effect,i=a.isFunction(h)?h:g[h];i.call(e,function(){e._fireOnSwitch(c),d&&d.call(e)},b)}}),e},{requires:["dom","event","anim","./base"]}),KISSY.add("gallery/switchable/1.3.1/circular",function(a,b,c,d){function e(a){var d,e=this,f=e.fromIndex,g=e.config,h=e.length,j="scrollx"===g.scrollType,k=j?"left":"top",l=e.activeIndex,m=e.viewSize[j?0:1],n=e.panels,o={},p={},q=e._realStep,r=m*h;if(o[k]=-m*l,-1==f)return b.css(e.content,o),a&&a(),void 0;l+q>h?(p={position:"relative"},p[k]=r,d=l+q-h,b.css(n.slice(0,d),p),b.css(n.slice(d,q),i)):b.css(n.slice(0,q),i);var s=b.css(n[f],"position"),t=(f+h-l)%h,u=(l-f+h)%h;u>t&&"relative"==s?b.css(e.content,k,-(m*(h+f))):f==h-1&&0==l?b.css(e.content,k,m):b.css(e.content,k,-(m*f)),e.anim&&e.anim.stop(),e.anim=new c(e.content,o,g.duration,g.easing,function(){e.anim=0,a&&a()}).run()}function f(a,d){var e,f=this,i=f.fromIndex,j=f.config,k=f.length,l="scrollx"===j.scrollType,m=l?"left":"top",n=f.activeIndex,o=f.viewSize[l?0:1],p=-o*n,q=f.panels,r=f.config.steps,s={},t="backward"===d;e=t&&0===i&&n===k-1||!t&&i===k-1&&0===n,f.anim&&(f.anim.stop(),"relative"==q[i*r].style.position&&h.call(f,q,i,m,o,1)),e&&(p=g.call(f,q,n,m,o)),s[m]=p+"px",i>-1?f.anim=new c(f.content,s,j.duration,j.easing,function(){e&&h.call(f,q,n,m,o,1),f.anim=void 0,a&&a()}).run():(b.css(f.content,s),a&&a())}function g(a,c,d,e){var f,g=this,h=g.config,i=h.steps,j=g.length,k=c*i,l=(c+1)*i;return f=a.slice(k,l),b.css(f,"position","relative"),b.css(f,d,(c?-1:1)*e*j),c?e:-e*j}function h(a,c,d,e,f){var g,h=this,i=h.config,j=i.steps,k=h.length,l=c*j,m=(c+1)*j;g=a.slice(l,m),b.css(g,"position",""),b.css(g,d,""),f&&b.css(h.content,d,c?-e*(k-1):"")}var i={position:"",left:"",top:""};a.mix(d.Config,{circular:!1}),d.adjustPosition=g,d.resetPosition=h,d.addPlugin({name:"circular",priority:5,init:function(a){var b=a.config,c=b.effect;!b.circular||"scrollx"!==c&&"scrolly"!==c||(b.scrollType=c,b.effect=a._realStep?e:f)}})},{requires:["dom","anim","./base","./effect"]}),KISSY.add("gallery/switchable/1.3.1/aria",function(a,b,c,d){function e(){this.stop&&this.stop()}function f(){this.start&&this.start()}d.addPlugin({name:"aria",init:function(a){if(a.config.aria){var b=a.container;c.on(b,"focusin",e,a),c.on(b,"focusout",f,a)}}});var g=["a","input","button","object"],h="oriTabIndex";return{setTabIndex:function(c,d){c.tabIndex=d,a.each(b.query("*",c),function(c){var e=c.nodeName.toLowerCase();a.inArray(e,g)&&(b.hasAttr(c,h)||b.attr(c,h,c.tabIndex),c.tabIndex=-1!=d?b.attr(c,h):d)})}}},{requires:["dom","event","./base"]}),KISSY.add("gallery/switchable/1.3.1/carousel/aria",function(a,b,c,d,e,f){function g(b){var c=this,d=c.config.steps,e=b.currentIndex,f=c.activeIndex,g=c.panels,h=g[e*d],i=c.triggers,j=i[e],k=b.originalEvent&&!(!b.originalEvent.target&&!b.originalEvent.srcElement);(k||-1==f)&&(a.each(i,function(a){w(a,-1)}),a.each(g,function(a){w(a,-1)}),j&&w(j,0),w(h,0),k&&h.focus())}function h(c){var d=null;return a.each(this.triggers,function(a){return a==c||b.contains(a,c)?(d=a,!1):void 0}),d}function i(a){var c=b.next(a),d=this.triggers;c||(c=d[0]),w(a,-1),c&&(w(c,0),c.focus())}function j(a){var c=b.prev(a),d=this.triggers;c||(c=d[d.length-1]),w(a,-1),c&&(w(c,0),c.focus())}function k(b){var c,d=b.keyCode,e=this,f=b.target;switch(d){case t:case s:c=h.call(e,f),c&&(i.call(e,c),b.halt());break;case r:case q:c=h.call(e,f),c&&(j.call(e,c),b.halt());break;case v:case u:c=h.call(e,f),c&&(e.switchTo(a.indexOf(c,e.triggers),void 0,x),b.halt())}}function l(c){var d=null;return a.each(this.panels,function(a){return a==c||b.contains(a,c)?(d=a,!1):void 0}),d}function m(a){var c=this,d=b.next(a),e=c.panels;d||(d=e[0]),w(a,-1),w(d,0),o.call(c,d,y)&&d.focus()}function n(a){var c=b.prev(a),d=this,e=d.panels;c||(c=e[e.length-1]),w(a,-1),w(c,0),o.call(d,c,z)&&c.focus()}function o(b,c){var d=this,e=a.indexOf(b,d.panels),f=d.config.steps,g=Math.floor(e/f);return g==d.activeIndex?1:0==e%f||e%f==f-1?(d.switchTo(g,c,x),0):1}function p(a){var b,c=this,d=a.keyCode,e=a.target;switch(d){case t:case s:b=l.call(c,e),b&&(m.call(c,b),a.halt());break;case r:case q:b=l.call(c,e),b&&(n.call(c,b),a.halt());break;case v:case u:b=l.call(c,e),b&&(c.fire("itemSelected",{item:b}),a.halt())}}var q=37,r=38,s=39,t=40,u=32,v=13,w=d.setTabIndex,x={originalEvent:{target:1}},y="forward",z="backward";a.mix(e.Config,{aria:!1}),f.addPlugin({name:"aria",init:function(b){if(b.config.aria){var d=b.triggers,e=b.panels,f=b.content,h=b.activeIndex;f.id||(f.id=a.guid("ks-switchbale-content")),f.setAttribute("role","listbox");var i=0;a.each(d,function(a){w(a,h==i?"0":"-1"),a.setAttribute("role","button"),a.setAttribute("aria-controls",f.id),i++}),i=0,a.each(e,function(a){w(a,"-1"),a.setAttribute("role","option"),i++}),b.on("switch",g,b);var j=b.nav;j&&c.on(j,"keydown",k,b),c.on(f,"keydown",p,b);var l=b.prevBtn,m=b.nextBtn;l&&(w(l,0),l.setAttribute("role","button"),c.on(l,"keydown",function(a){(a.keyCode==v||a.keyCode==u)&&(b.prev(x),a.preventDefault())})),m&&(w(m,0),m.setAttribute("role","button"),c.on(m,"keydown",function(a){(a.keyCode==v||a.keyCode==u)&&(b.next(x),a.preventDefault())}))}}},e)},{requires:["dom","event","../aria","./base","../base"]}),KISSY.add("gallery/switchable/1.3.1/autoplay",function(a,b,c,d,e){var f=200,g=a.Env.host,h=function(a){var c=b.scrollTop(),d=b.viewportHeight(),e=b.offset(a),f=b.height(a);return e.top>c&&e.top+f<c+d};return a.mix(d.Config,{pauseOnScroll:!1,autoplay:!1,interval:5,pauseOnHover:!0}),d.addPlugin({name:"autoplay",init:function(b){function d(){i=a.later(function(){b.paused||b.next()},k,!0)}var i,j=b.config,k=1e3*j.interval;j.autoplay&&(j.pauseOnScroll&&(b.__scrollDetect=a.buffer(function(){b[h(b.container)?"start":"stop"]()},f),c.on(g,"scroll",b.__scrollDetect)),d(),b.stop=function(){i&&(i.cancel(),i=e),b.paused=!0},b.start=function(){i&&(i.cancel(),i=e),b.paused=!1,d()},j.pauseOnHover&&(c.on(b.container,"mouseenter",b.stop,b),c.on(b.container,"mouseleave",b.start,b)))},destroy:function(a){a.__scrollDetect&&(c.remove(g,"scroll",a.__scrollDetect),a.__scrollDetect.stop())}}),d},{requires:["dom","event","./base"]}),KISSY.add("gallery/switchable/1.3.1/tabs/aria",function(a,b,c,d,e,f){function g(c){var d=this.triggers,e=null;return a.each(d,function(a){(a==c||b.contains(a,c))&&(e=a)}),e}function h(a){switch(a.keyCode){case k:case l:!a.ctrlKey||a.altKey||a.shiftKey||a.halt();break;case r:a.ctrlKey&&!a.altKey&&a.halt()}}function i(a){var b=a.target,c=this,d=a.ctrlKey&&!a.shiftKey&&!a.altKey;switch(a.keyCode){case n:case o:g.call(c,b)&&(c.prev(t(a)),a.halt());break;case p:case q:g.call(c,b)&&(c.next(t(a)),a.halt());break;case l:d&&(a.halt(),c.next(t(a)));break;case k:d&&(a.halt(),c.prev(t(a)));break;case r:a.ctrlKey&&!a.altKey&&(a.halt(),a.shiftKey?c.prev(t(a)):c.next(t(a)))}}function j(a){var b=a.originalEvent&&!(!a.originalEvent.target&&!a.originalEvent.srcElement),c=this,d=a.fromIndex,e=a.currentIndex;if(d!=e){var f=c.triggers[d],g=c.triggers[e],h=c.panels[d],i=c.panels[e];if(f&&s(f,"-1"),s(g,"0"),b)try{g.focus()}catch(j){}h&&h.setAttribute("aria-hidden","true"),i.setAttribute("aria-hidden","false")}}var k=33,l=34,m="added",n=37,o=38,p=39,q=40,r=9;a.mix(f.Config,{aria:!0}),d.addPlugin({name:"aria",init:function(d){function e(b){b.setAttribute("role","tab"),s(b,"-1"),b.id||(b.id=a.guid("ks-switchable"))}function f(a,b){a.setAttribute("role","tabpanel"),a.setAttribute("aria-hidden","true"),a.setAttribute("aria-labelledby",b.id)}if(d.config.aria){var g=d.triggers,k=d.activeIndex,l=d.panels,n=d.container;d.nav&&b.attr(d.nav,"role","tablist");var o=0;a.each(g,e),d.on(m,function(a){var b;e(b=a.trigger),f(a.panel,b)}),o=0,a.each(l,function(a){var b=g[o];f(a,b),o++}),k>-1&&(s(g[k],"0"),l[k].setAttribute("aria-hidden","false")),d.on("switch",j,d),c.on(n,"keydown",i,d),c.on(n,"keypress",h,d)}}},f);var s=e.setTabIndex,t=d.getDomEvent},{requires:["dom","event","../base","../aria","./base"]}),KISSY.add("gallery/switchable/1.3.1/accordion/aria",function(a,b,c,d,e,f){function g(c){var d=this.triggers,e=null;return a.each(d,function(a){(a==c||b.contains(a,c))&&(e=a)}),e}function h(c){var d=this.panels,e=null;return a.each(d,function(a){(a==c||b.contains(a,c))&&(e=a)}),e}function i(b){var c=this,d=c.triggers,e=c.panels;return d[a.indexOf(b,e)]}function j(a){var b=this,c=g.call(b,a);return c||(c=i.call(b,h.call(b,a))),c}function k(a){switch(a.keyCode){case s:case t:!a.ctrlKey||a.altKey||a.shiftKey||a.halt();break;case A:a.ctrlKey&&!a.altKey&&a.halt()}}function l(a){var b,c=a.target,d=this,e=d.triggers,f=!a.ctrlKey&&!a.shiftKey&&!a.altKey,h=a.ctrlKey&&!a.shiftKey&&!a.altKey;switch(a.keyCode){case C:case B:(b=g.call(d,c))&&f&&(q.call(d,b),a.halt());break;case w:case x:(b=g.call(d,c))&&(n.call(d,b),a.halt());break;case y:case z:(b=g.call(d,c))&&(p.call(d,b),a.halt());break;case t:h&&(a.halt(),b=j.call(d,c),p.call(d,b));break;case s:h&&(a.halt(),b=j.call(d,c),n.call(d,b));break;case v:f&&(b=j.call(d,c),o.call(d,0),a.halt());break;case u:f&&(b=j.call(d,c),o.call(d,e.length-1),a.halt());break;case A:a.ctrlKey&&!a.altKey&&(a.halt(),b=j.call(d,c),a.shiftKey?n.call(d,b):p.call(d,b))}}function m(c,d){var e=this,f=e.triggers,g=f[c];if(a.each(f,function(a){a!==g&&(D(a,"-1"),b.removeClass(a,"ks-switchable-select"),a.setAttribute("aria-selected","false"))}),d)try{g.focus()}catch(h){}D(g,"0"),b.addClass(g,"ks-switchable-select"),g.setAttribute("aria-selected","true")}function n(b){var c=this,d=c.triggers,e=a.indexOf(b,d),f=0==e?d.length-1:e-1;m.call(c,f,!0)}function o(a){m.call(this,a,!0)}function p(b){var c=this,d=c.triggers,e=a.indexOf(b,d),f=e==d.length-1?0:e+1;m.call(c,f,!0)}function q(b){var c=this;c.switchTo(a.indexOf(b,c.triggers))}function r(b){var c=b.originalEvent&&!(!b.originalEvent.target&&!b.originalEvent.srcElement),d=this,e=d.config.multiple,f=b.currentIndex,g=d.panels,h=d.triggers,i=h[f],j=g[f];e||(a.each(g,function(a){a!==j&&a.setAttribute("aria-hidden","true")}),a.each(h,function(a){a!==i&&a.setAttribute("aria-hidden","true")}));var k=j.getAttribute("aria-hidden");j.setAttribute("aria-hidden","false"==k?"true":"false"),i.setAttribute("aria-expanded","false"==k?"false":"true"),m.call(d,f,c)}var s=33,t=34,u=35,v=36,w=37,x=38,y=39,z=40,A=9,B=32,C=13;a.mix(e.Config,{aria:!0}),f.addPlugin({name:"aria",init:function(d){if(d.config.aria){var e=d.container,f=d.activeIndex;b.attr(e,"aria-multiselectable",d.config.multiple?"true":"false"),d.nav&&b.attr(d.nav,"role","tablist");var g=d.triggers,h=d.panels,i=0;a.each(h,function(b){b.id||(b.id=a.guid("ks-accordion-tab-panel"))}),a.each(g,function(b){b.id||(b.id=a.guid("ks-accordion-tab"))}),a.each(g,function(a){a.setAttribute("role","tab"),a.setAttribute("aria-expanded",f==i?"true":"false"),a.setAttribute("aria-selected",f==i?"true":"false"),a.setAttribute("aria-controls",h[i].id),D(a,f==i?"0":"-1"),i++}),i=0,a.each(h,function(a){var b=g[i];a.setAttribute("role","tabpanel"),a.setAttribute("aria-hidden",f==i?"false":"true"),a.setAttribute("aria-labelledby",b.id),i++}),d.on("switch",r,d),c.on(e,"keydown",l,d),c.on(e,"keypress",k,d)}}},e);var D=d.setTabIndex},{requires:["dom","event","../aria","./base","../base"]}),KISSY.add("gallery/switchable/1.3.1/index",function(a,b,c,d,e,f){var g={Accordion:c,Carousel:d,Slide:e,Tabs:f};return a.mix(b,g),b},{requires:["./base","./accordion/base","./carousel/base","./slide/base","./tabs/base","./lazyload","./effect","./circular","./carousel/aria","./autoplay","./aria","./tabs/aria","./accordion/aria"]});