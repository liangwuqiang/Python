.. _news:

Release notes
=============

Scrapy 1.4.0 (2017-05-18)
-------------------------

Scrapy 1.4 does not bring that many breathtaking new features
### Scrapy 1.4并不带来许多惊人的新功能
but quite a few handy improvements nonetheless.
### 但不少方便改进。

Scrapy now supports anonymous FTP sessions with customizable user and
### Scrapy现在支持匿名FTP会话和可定制的用户
password via the new :setting:`FTP_USER` and :setting:`FTP_PASSWORD` settings.
### 通过新密码:设置:“FTP_USER”和:设置:“FTP_PASSWORD”设置。
And if you're using Twisted version 17.1.0 or above, FTP is now available
### 如果你使用扭曲版本17.1.0或以上,FTP现在是可用的
with Python 3.

There's a new :meth:`response.follow <scrapy.http.TextResponse.follow>` method
### 有一个新:甲:“反应。按照< scrapy.http.TextResponse。遵循>的方法
for creating requests; **it is now a recommended way to create Requests
### 创建请求;* *现在推荐的方式来创建请求
in Scrapy spiders**. This method makes it easier to write correct
### 在Scrapy蜘蛛* *。这种方法更容易写正确
spiders; ``response.follow`` has several advantages over creating
### 蜘蛛;“响应。遵循“创造有几个优点
``scrapy.Request`` objects directly:

* it handles relative URLs;
### *它处理相对url;
* it works properly with non-ascii URLs on non-UTF8 pages;
### *它正常工作与非ascii url non-UTF8页;
* in addition to absolute and relative URLs it supports Selectors;
### *除了绝对和相对url它支持选择器;
  for ``<a>`` elements it can also extract their href values.
### 为“< >”的元素也可以提取它们的href值。

For example, instead of this::
### 例如,而不是这样的::

    for href in response.css('li.page a::attr(href)').extract():
        url = response.urljoin(href)
        yield scrapy.Request(url, self.parse, encoding=response.encoding)

One can now write this::
### 一个现在可以写这个:

    for a in response.css('li.page a'):
### 在response.css(李。一个“页):
        yield response.follow(a, self.parse)

Link extractors are also improved. They work similarly to what a regular
### 链接萃取器也得到改善。他们的工作原理与普通
modern browser would do: leading and trailing whitespace are removed
### 现代浏览器会做:前导和尾随空白中
from attributes (think ``href="   http://example.com"``) when building
### 从属性(想想“href = " http://example.com " ')在构建
``Link`` objects. This whitespace-stripping also happens for ``action``
### “链接”对象。这个whitespace-stripping也是“行动”
attributes with ``FormRequest``.

**Please also note that link extractors do not canonicalize URLs by default
### * *请注意,默认url链接提取器不规范化
anymore.** This was puzzling users every now and then, and it's not what
### 了。* *这是令人困惑的用户时不时的,这并不是什么
browsers do in fact, so we removed that extra transformation on extractred
### 浏览器做事实上,所以我们在extractred删除额外的转换
links.

For those of you wanting more control on the ``Referer:`` header that Scrapy
### 如果你想要更多的控制在“推荐人:“Scrapy头
sends when following links, you can set your own ``Referrer Policy``.
### 
Prior to Scrapy 1.4, the default ``RefererMiddleware`` would simply and
### Scrapy 1.4之前,默认“RefererMiddleware ' '只会和
blindly set it to the URL of the response that generated the HTTP request
### 盲目地将它设置为响应生成HTTP请求的URL
(which could leak information on your URL seeds).
### (可能泄漏你的URL信息种子)。
By default, Scrapy now behaves much like your regular browser does.
### 默认情况下,Scrapy现在的行为就像普通的浏览器。
And this policy is fully customizable with W3C standard values
### 这个政策是完全可定制的W3C标准的价值观
(or with something really custom of your own if you wish).
### (或与一些真正定制自己的如果你愿意)。
See :setting:`REFERRER_POLICY` for details.

To make Scrapy spiders easier to debug, Scrapy logs more stats by default
### Scrapy蜘蛛更容易调试,Scrapy默认日志更多的统计数据
in 1.4: memory usage stats, detailed retry stats, detailed HTTP error code
### 1.4:内存使用统计数据,详细的重试统计数据,详细的HTTP错误代码
stats. A similar change is that HTTP cache path is also visible in logs now.
### 统计数据。类似的变化是HTTP缓存路径也可见的日志了。

Last but not least, Scrapy now has the option to make JSON and XML items
### 最后但并非最不重要,现在Scrapy JSON和XML项目的选项
more human-readable, with newlines between items and even custom indenting
### 更可读,换行项目之间,甚至自定义缩进
offset, using the new :setting:`FEED_EXPORT_INDENT` setting.
### 偏移量,使用新的设置:“FEED_EXPORT_INDENT”设置。

Enjoy! (Or read on for the rest of changes in this release.)
### 享受吧!(或阅读的这个版本的变化。)

Deprecations and Backwards Incompatible Changes
### 不支持和向后不兼容的更改
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Default to ``canonicalize=False`` in :class:`scrapy.linkextractors.LinkExtractor`
### ——默认“规范化= False”:类:“scrapy.linkextractors.LinkExtractor”
  (:issue:`2537`, fixes :issue:`1941` and :issue:`1982`):
### (问题:“2537”,修复:问题:“1941”和:问题:' 1982 '):
  **warning, this is technically backwards-incompatible**
### * *的警告,这是技术上向后不兼容的* *
- Enable memusage extension by default (:issue:`2539`, fixes :issue:`2187`);
### 默认启用memusage扩展(问题:“2539”,修复:问题:' 2187 ');
  **this is technically backwards-incompatible** so please check if you have
### * *这是技术上和* *请检查如果你有
  any non-default ``MEMUSAGE_***`` options set.
### 任何非默认“MEMUSAGE_ * * * ' '选项集。
- ``EDITOR`` environment variable now takes precedence over ``EDITOR``
### ”-“编辑器”的环境变量现在优先于“编辑”“
  option defined in settings.py (:issue:`1829`); Scrapy default settings
### 备选defined in settings。问题:'(:py 1829’);Scrapy default settings
  no longer depend on environment variables. **This is technically a backwards
### 不再依赖于环境变量。* *这在技术上是一个倒退
  incompatible change**.
- ``Spider.make_requests_from_url`` is deprecated
  (:issue:`1728`, fixes :issue:`1495`).

New Features
~~~~~~~~~~~~

- Accept proxy credentials in :reqmeta:`proxy` request meta key (:issue:`2526`)
### -接受代理凭证:reqmeta:“代理”请求meta关键(问题:‘2526’)
- Support `brotli`_-compressed content; requires optional `brotlipy`_
### ——支持“brotli”_-compressed内容;需要可选brotlipy _
  (:issue:`2535`)
- New :ref:`response.follow <response-follow-example>` shortcut
### -新:裁判:“反应。按照< response-follow-example >的捷径
  for creating requests (:issue:`1940`)
- Added ``flags`` argument and attribute to :class:`Request <scrapy.http.Request>`
### ——添加“国旗”“参数和属性:类:“请求< scrapy.http.Request >”
  objects (:issue:`2047`)
- Support Anonymous FTP (:issue:`2342`)
### 支持匿名FTP(:问题:‘2342’)
- Added ``retry/count``, ``retry/max_reached`` and ``retry/reason_count/<reason>``
### -添加“重试/数' ',' '重试/ max_reached ' '和' '重试/ reason_count / <原因> ' '
  stats to :class:`RetryMiddleware <scrapy.downloadermiddlewares.retry.RetryMiddleware>`
  (:issue:`2543`)
- Added ``httperror/response_ignored_count`` and ``httperror/response_ignored_status_count/<status>``
### -添加“httperror / response_ignored_count‘和‘httperror / response_ignored_status_count / <地位> ' '
  stats to :class:`HttpErrorMiddleware <scrapy.spidermiddlewares.httperror.HttpErrorMiddleware>`
  (:issue:`2566`)
- Customizable :setting:`Referrer policy <REFERRER_POLICY>` in
### -可定制:设置:“引用< REFERRER_POLICY >政策”
  :class:`RefererMiddleware <scrapy.spidermiddlewares.referer.RefererMiddleware>`
  (:issue:`2306`)
- New ``data:`` URI download handler (:issue:`2334`, fixes :issue:`2156`)
### ——新的“数据:“URI下载处理程序(问题:“2334”,修复:问题:' 2156 ')
- Log cache directory when HTTP Cache is used (:issue:`2611`, fixes :issue:`2604`)
### 使用HTTP缓存日志缓存目录(问题:“2611”,修复:问题:' 2604 ')
- Warn users when project contains duplicate spider names (fixes :issue:`2181`)
### ——警告用户当项目包含重复的蜘蛛名称(修复:问题:' 2181 ')
- :class:`CaselessDict` now accepts ``Mapping`` instances and not only dicts (:issue:`2646`)
### -:类:“CaselessDict”现在接受“不仅映射的实例和字典(问题:‘2646’)
- :ref:`Media downloads <topics-media-pipeline>`, with :class:`FilesPipelines`
### -:裁判:“媒体下载< topics-media-pipeline >”,:类:“FilesPipelines”
  or :class:`ImagesPipelines`, can now optionally handle HTTP redirects
### 或:类:“ImagesPipelines”,现在可以选择处理HTTP重定向
  using the new :setting:`MEDIA_ALLOW_REDIRECTS` setting (:issue:`2616`, fixes :issue:`2004`)
### 使用新的设置:“MEDIA_ALLOW_REDIRECTS”设置(问题:“2616”,修复:问题:' 2004 ')
- Accept non-complete responses from websites using a new
### ——接受网站使用一种新的非完整的回应
  :setting:`DOWNLOAD_FAIL_ON_DATALOSS` setting (:issue:`2590`, fixes :issue:`2586`)
### :设置:“DOWNLOAD_FAIL_ON_DATALOSS”设置(问题:“2590”,修复:问题:' 2586 ')
- Optional pretty-printing of JSON and XML items via
### -可选的精细打印的JSON和XML项目通过
  :setting:`FEED_EXPORT_INDENT` setting (:issue:`2456`, fixes :issue:`1327`)
### :设置:“FEED_EXPORT_INDENT”设置(问题:“2456”,修复:问题:' 1327 ')
- Allow dropping fields in ``FormRequest.from_response`` formdata when
### ——在“FormRequest允许删除字段。from_response“formdata时
  ``None`` value is passed (:issue:`667`)
### ' '没有' '的值是通过(问题:‘667’)
- Per-request retry times with the new :reqmeta:`max_retry_times` meta key
### ——每请求重试时间与新:reqmeta:max_retry_times meta关键
  (:issue:`2642`)
- ``python -m scrapy`` as a more explicit alternative to ``scrapy`` command
### ——“python - m scrapy‘作为一个更明确的选择“scrapy“命令
  (:issue:`2740`)

.. _brotli: https://github.com/google/brotli
.. _brotlipy: https://github.com/python-hyper/brotlipy/

Bug fixes
~~~~~~~~~

- LinkExtractor now strips leading and trailing whitespaces from attributes
### ——LinkExtractor现在删除属性的前导和尾随空白
  (:issue:`2547`, fixes :issue:`1614`)
- Properly handle whitespaces in action attribute in :class:`FormRequest`
### -妥善处理空白在动作属性:类:“FormRequest”
  (:issue:`2548`)
- Buffer CONNECT response bytes from proxy until all HTTP headers are received
### ——字节缓冲连接响应来自代理收到,直到所有HTTP头
  (:issue:`2495`, fixes :issue:`2491`)
- FTP downloader now works on Python 3, provided you use Twisted>=17.1
### FTP下载器现在支持Python 3,如果你使用扭曲> = 17.1
  (:issue:`2599`)
- Use body to choose response type after decompressing content (:issue:`2393`,
### ——用身体来选择响应类型减压后内容(问题:“2393”,
  fixes :issue:`2145`)
- Always decompress ``Content-Encoding: gzip`` at :class:`HttpCompressionMiddleware
### Content-Encoding ! ! ! ! ! decompress一向- gzip:! ! ! ! ! ! HttpCompressionMiddleware:班:
  <scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware>` stage (:issue:`2391`)
- Respect custom log level in ``Spider.custom_settings`` (:issue:`2581`,
### 在“蜘蛛——尊重自定义日志级别。custom_settings ' '(:问题:“2581”,
  fixes :issue:`1612`)
- 'make htmlview' fix for macOS (:issue:`2661`)
### ——“让htmlview”解决macOS(问题:‘2661’)
- Remove "commands" from the command list  (:issue:`2695`)
### 从命令列表中删除“命令”(问题:' 2695 ')
- Fix duplicate Content-Length header for POST requests with empty body (:issue:`2677`)
### ——解决重复的内容长度为POST请求头用空的身体(问题:‘2677’)
- Properly cancel large downloads, i.e. above :setting:`DOWNLOAD_MAXSIZE` (:issue:`1616`)
### ——正确地取消大下载,即上图:设置:“DOWNLOAD_MAXSIZE”(问题:‘1616’)
- ImagesPipeline: fixed processing of transparent PNG images with palette
### - ImagesPipeline:固定加工透明PNG图像的调色板
  (:issue:`2675`)

Cleanups & Refactoring
~~~~~~~~~~~~~~~~~~~~~~

- Tests: remove temp files and folders (:issue:`2570`),
### ——测试:删除临时文件和文件夹(问题:‘2570’),
  fixed ProjectUtilsTest on OS X (:issue:`2569`),
### ProjectUtilsTest骨头固定结果有:X(2569 ! ! ! !):
  use portable pypy for Linux on Travis CI (:issue:`2710`)
### 使用便携式pypy Linux在特拉维斯CI(:问题:‘2710’)
- Separate building request from ``_requests_to_follow`` in CrawlSpider (:issue:`2562`)
### ——单独的从“构建请求_requests_to_follow ' '在CrawlSpider(问题:‘2562’)
- Remove “Python 3 progress” badge (:issue:`2567`)
### 删除“Python 3进展”徽章(:问题:‘2567’)
- Add a couple more lines to ``.gitignore`` (:issue:`2557`)
### ——“加多几行。gitignore ' '(:问题:‘2557’)
- Remove bumpversion prerelease configuration (:issue:`2159`)
### ——删除bumpversion预映配置(:问题:‘2159’)
- Add codecov.yml file (:issue:`2750`)
### ——添加codecov。yml文件(问题:‘2750’)
- Set context factory implementation based on Twisted version (:issue:`2577`,
### ——设置上下文工厂实现基于扭曲的版本(问题:“2577”,
  fixes :issue:`2560`)
- Add omitted ``self`` arguments in default project middleware template (:issue:`2595`)
### ”——添加省略了“自我”的参数默认项目中间件模板(问题:‘2595’)
- Remove redundant ``slot.add_request()`` call in ExecutionEngine (:issue:`2617`)
### ——删除冗余“slot.add_request()“叫ExecutionEngine(问题:' 2617 ')
- Catch more specific ``os.error`` exception in :class:`FSFilesStore` (:issue:`2644`)
### ——捕捉到更具体的“操作系统。错误的异常:类:“FSFilesStore”(问题:‘2644’)
- Change "localhost" test server certificate (:issue:`2720`)
### -改变“localhost”测试服务器证书(:问题:‘2720’)
- Remove unused ``MEMUSAGE_REPORT`` setting (:issue:`2576`)
### ——删除未使用的“MEMUSAGE_REPORT“设置(问题:‘2576’)

Documentation
~~~~~~~~~~~~~

- Binary mode is required for exporters (:issue:`2564`, fixes :issue:`2553`)
### 出口商需要二进制模式(问题:“2564”,修复:问题:' 2553 ')
- Mention issue with :meth:`FormRequest.from_response
### -提问题:甲:“FormRequest.from_response
  <scrapy.http.FormRequest.from_response>` due to bug in lxml (:issue:`2572`)
### 
- Use single quotes uniformly in templates (:issue:`2596`)
### 使用单引号统一模板(:问题:‘2596’)
- Document :reqmeta:`ftp_user` and :reqmeta:`ftp_password` meta keys (:issue:`2587`)
### ——文档:reqmeta:“ftp_user”和:reqmeta:“ftp_password”元键(问题:‘2587’)
- Removed section on deprecated ``contrib/`` (:issue:`2636`)
### -删除部分弃用“contrib / ' '(:问题:‘2636’)
- Recommend Anaconda when installing Scrapy on Windows
### 当在Windows上安装Scrapy——推荐蟒蛇
  (:issue:`2477`, fixes :issue:`2475`)
- FAQ: rewrite note on Python 3 support on Windows (:issue:`2690`)
### -常见问题:重写注意Python 3支持Windows(问题:‘2690’)
- Rearrange selector sections (:issue:`2705`)
### 重新排列选择部分(:问题:‘2705’)
- Remove ``__nonzero__`` from :class:`SelectorList` docs (:issue:`2683`)
### ——删除“__nonzero__‘:类:“SelectorList”文档(问题:‘2683’)
- Mention how to disable request filtering in documentation of
### ——提到如何禁用请求过滤的文档
  :setting:`DUPEFILTER_CLASS` setting (:issue:`2714`)
- Add sphinx_rtd_theme to docs setup readme (:issue:`2668`)
### ——添加sphinx_rtd_theme readme文档设置(问题:‘2668’)
- Open file in text mode in JSON item writer example (:issue:`2729`)
### ——打开的文件在JSON文本模式项作家的例子(问题:‘2729’)
- Clarify ``allowed_domains`` example (:issue:`2670`)
### ——澄清“allowed_domains ' '(例子:问题:' 2670 ')


Scrapy 1.3.3 (2017-03-10)
-------------------------

Bug fixes
~~~~~~~~~

- Make ``SpiderLoader`` raise ``ImportError`` again by default for missing
### ——让“SpiderLoader“提高“ImportError再次“默认情况下失踪
  dependencies and wrong :setting:`SPIDER_MODULES`.
  These exceptions were silenced as warnings since 1.3.0.
### 这些异常沉默,警告1.3.0自版本。
  A new setting is introduced to toggle between warning or exception if needed ;
### 介绍了一个新的设置之间切换警告或异常如果需要;
  see :setting:`SPIDER_LOADER_WARN_ONLY` for details.


Scrapy 1.3.2 (2017-02-13)
-------------------------

Bug fixes
~~~~~~~~~

- Preserve request class when converting to/from dicts (utils.reqser) (:issue:`2510`).
### ——保存请求类转换时/从字典(utils.reqser)(问题:‘2510’)。
- Use consistent selectors for author field in tutorial (:issue:`2551`).
### ——在教程中使用一致的为作者字段选择器(问题:‘2551’)。
- Fix TLS compatibility in Twisted 17+ (:issue:`2558`)
### ——修复TLS兼容性扭曲17 +(:问题:‘2558’)

Scrapy 1.3.1 (2017-02-08)
-------------------------

New features
~~~~~~~~~~~~

- Support ``'True'`` and ``'False'`` string values for boolean settings (:issue:`2519`);
### ——支持”“真“”和“”假的“布尔设置字符串值(问题:' 2519 ');
  you can now do something like ``scrapy crawl myspider -s REDIRECT_ENABLED=False``.
### 你现在可以做一些类似“scrapy爬myspider - s REDIRECT_ENABLED = False’”。
- Support kwargs with ``response.xpath()`` to use :ref:`XPath variables <topics-selectors-xpath-variables>`
### -支持与“response.xpath kwargs()“使用:裁判:“< topics-selectors-xpath-variables > XPath变量”
  and ad-hoc namespaces declarations ;
### 和特别的名称空间声明;
  this requires at least Parsel v1.1 (:issue:`2457`).
### 这至少需要Parsel v1.1(问题:‘2457’)。
- Add support for Python 3.6 (:issue:`2485`).
### ——添加对Python 3.6的支持(问题:‘2485’)。
- Run tests on PyPy (warning: some tests still fail, so PyPy is not supported yet).
### PyPy上运行测试(警告:一些测试仍然失败,所以PyPy不支持)。

Bug fixes
~~~~~~~~~

- Enforce ``DNS_TIMEOUT`` setting (:issue:`2496`).
### ——执行“DNS_TIMEOUT“设置(问题:‘2496’)。
- Fix :command:`view` command ; it was a regression in v1.3.0 (:issue:`2503`).
### -修复:命令:“视图”命令;这是一个回归在v1.3.0(问题:‘2503’)。
- Fix tests regarding ``*_EXPIRES settings`` with Files/Images pipelines (:issue:`2460`).
### -解决关于“测试* _EXPIRES设置“文件/图像管道(问题:‘2460’)。
- Fix name of generated pipeline class when using basic project template (:issue:`2466`).
### ——修复管道生成类的名称在使用基本的项目模板(问题:‘2466’)。
- Fix compatiblity with Twisted 17+ (:issue:`2496`, :issue:`2528`).
### ——解决相容性与扭曲的17 +(:问题:“2496”,:问题:' 2528 ')。
- Fix ``scrapy.Item`` inheritance on Python 3.6 (:issue:`2511`).
### ——解决“scrapy。在Python 3.6项“继承(问题:‘2511’)。
- Enforce numeric values for components order in ``SPIDER_MIDDLEWARES``,
### ——执行组件的数值顺序“SPIDER_MIDDLEWARES ' ',
  ``DOWNLOADER_MIDDLEWARES``, ``EXTENIONS`` and ``SPIDER_CONTRACTS`` (:issue:`2420`).
### “DOWNLOADER_MIDDLEWARES‘’、‘EXTENIONS ' '和' ' SPIDER_CONTRACTS ' '(:问题:‘2420’)。

Documentation
~~~~~~~~~~~~~

- Reword Code of Coduct section and upgrade to Contributor Covenant v1.4
### 重述代码贡献者约v1.4 Coduct部分和升级
  (:issue:`2469`).
- Clarify that passing spider arguments converts them to spider attributes
### ——明确传递蜘蛛参数将它们转换成蜘蛛属性
  (:issue:`2483`).
- Document ``formid`` argument on ``FormRequest.from_response()`` (:issue:`2497`).
### ”——文档“formid”的论点“FormRequest.from_response()' '(:问题:‘2497’)。
- Add .rst extension to README files (:issue:`2507`).
### ——添加。rst扩展README文件(问题:‘2507’)。
- Mention LevelDB cache storage backend (:issue:`2525`).
### ——提到并且缓存存储后端(问题:‘2525’)。
- Use ``yield`` in sample callback code (:issue:`2533`).
### ——使用“产量”“样品回调代码(问题:‘2533’)。
- Add note about HTML entities decoding with ``.re()/.re_first()`` (:issue:`1704`).
### 
- Typos (:issue:`2512`, :issue:`2534`, :issue:`2531`).
### 拼写错误(问题:“2512”,:问题:“2534”,:问题:' 2531 ')。

Cleanups
~~~~~~~~

- Remove reduntant check in ``MetaRefreshMiddleware`` (:issue:`2542`).
### ——删除reduntant检查“MetaRefreshMiddleware ' '(:问题:‘2542’)。
- Faster checks in ``LinkExtractor`` for allow/deny patterns (:issue:`2538`).
### ——在“快检查LinkExtractor“允许/拒绝模式(问题:‘2538’)。
- Remove dead code supporting old Twisted versions (:issue:`2544`).
### ——删除死代码支持旧的扭曲版本(问题:‘2544’)。


Scrapy 1.3.0 (2016-12-21)
-------------------------

This release comes rather soon after 1.2.2 for one main reason:
### 这个版本是1.2.2,而不久之后的一个主要原因:
it was found out that releases since 0.18 up to 1.2.2 (included) use
### 这是发现版本从0.18到1.2.2(包括)使用
some backported code from Twisted (``scrapy.xlib.tx.*``),
### 从扭曲的一些补丁代码(“scrapy.xlib.tx。* ' '),
even if newer Twisted modules are available.
### 即使新的扭曲的模块是可用的。
Scrapy now uses ``twisted.web.client`` and ``twisted.internet.endpoints`` directly.
### Scrapy现在使用“twisted.web。客户' '和' ' twisted.internet.endpoints直接“。
(See also cleanups below.)

As it is a major change, we wanted to get the bug fix out quickly
### 因为它是一个主要的变化,我们想摆脱错误修复的影响
while not breaking any projects using the 1.2 series.
### 虽然没有违反任何项目使用1.2系列。

New Features
~~~~~~~~~~~~

- ``MailSender`` now accepts single strings as values for ``to`` and ``cc``
### ”——“MailSender”“现在接受单一字符串值' ' ' '和' ' cc ' '
  arguments (:issue:`2272`)
- ``scrapy fetch url``, ``scrapy shell url`` and ``fetch(url)`` inside
### ——“scrapy获取url ' ',' ' scrapy壳url ' '和' ' fetch(url)“内部
  scrapy shell now follow HTTP redirections by default (:issue:`2290`);
### 默认scrapy壳牌现在遵循HTTP重定向(问题:' 2290 ');
  See :command:`fetch` and :command:`shell` for details.
### 看:命令:“获取”和:命令:“壳”的细节。
- ``HttpErrorMiddleware`` now logs errors with ``INFO`` level instead of ``DEBUG``;
### ”——“HttpErrorMiddleware”“现在日志错误' '信息' '水平而不是“调试”;
  this is technically **backwards incompatible** so please check your log parsers.
### 这在技术上是* *向后不兼容的* *请检查你的日志的解析器。
- By default, logger names now use a long-form path, e.g. ``[scrapy.extensions.logstats]``,
### ——默认情况下,日志的名字现在使用一个长篇的路径,例如“[scrapy.extensions.logstats]' ',
  instead of the shorter "top-level" variant of prior releases (e.g. ``[scrapy]``);
### 而不是短之前版本的变体(如“顶级”。“[scrapy]' ');
  this is **backwards incompatible** if you have log parsers expecting the short
### 这是* *向后不兼容的* *如果你有日志解析器等短
  logger name part. You can switch back to short logger names using :setting:`LOG_SHORT_NAMES`
### 记录器名称部分。你可以切换回短记录器名称使用:设置:“LOG_SHORT_NAMES”
  set to ``True``.

Dependencies & Cleanups
~~~~~~~~~~~~~~~~~~~~~~~

- Scrapy now requires Twisted >= 13.1 which is the case for many Linux
### - Scrapy现在要求扭曲> = 13.1是许多Linux
  distributions already.
- As a consequence, we got rid of ``scrapy.xlib.tx.*`` modules, which
### ——因此,我们摆脱了“scrapy.xlib.tx。*“模块
  copied some of Twisted code for users stuck with an "old" Twisted version
### 复制一些扭曲的代码为用户坚持一个“老”扭曲的版本
- ``ChunkedTransferMiddleware`` is deprecated and removed from the default
### ——“ChunkedTransferMiddleware“弃用和清除的默认值
  downloader middlewares.


Scrapy 1.2.3 (2017-03-03)
-------------------------

- Packaging fix: disallow unsupported Twisted versions in setup.py
### -包装修复:不允许不受支持的扭曲版本在setup . py


Scrapy 1.2.2 (2016-12-06)
-------------------------

Bug fixes
~~~~~~~~~

- Fix a cryptic traceback when a pipeline fails on ``open_spider()`` (:issue:`2011`)
### ——当管道失败修复一个神秘回溯“open_spider()' '(:问题:‘2011’)
- Fix embedded IPython shell variables (fixing :issue:`396` that re-appeared
### ——解决嵌入式IPython shell变量(修复:问题:396年的陆战队员
  in 1.2.0, fixed in :issue:`2418`)
### 在1.2.0,固定在:问题:' 2418 ')
- A couple of patches when dealing with robots.txt:
### -两个补丁在处理robots . txt:

  - handle (non-standard) relative sitemap URLs (:issue:`2390`)
### -处理(非标)相对站点url(:问题:‘2390’)
  - handle non-ASCII URLs and User-Agents in Python 2 (:issue:`2373`)
### ——处理非ascii url和用户代理在Python 2(:问题:‘2373’)

Documentation
~~~~~~~~~~~~~

- Document ``"download_latency"`` key in ``Request``'s ``meta`` dict (:issue:`2033`)
### ——文档”“download_latency”“关键在“请求”年代‘元’‘dict(问题:‘2033’)
- Remove page on (deprecated & unsupported) Ubuntu packages from ToC (:issue:`2335`)
### ——删除页面(弃用和不支持的)从ToC Ubuntu包(问题:‘2335’)
- A few fixed typos (:issue:`2346`, :issue:`2369`, :issue:`2369`, :issue:`2380`)
### 几个固定的拼写错误(:问题:“2346”,:问题:“2369”,:问题:“2369”,:问题:' 2380 ')
  and clarifications (:issue:`2354`, :issue:`2325`, :issue:`2414`)
### 和说明(问题:“2354”,:问题:“2325”,:问题:' 2414 ')

Other changes
~~~~~~~~~~~~~

- Advertize `conda-forge`_ as Scrapy's official conda channel (:issue:`2387`)
### ——通知“conda-forge”_ Scrapy官方conda通道(问题:‘2387’)
- More helpful error messages when trying to use ``.css()`` or ``.xpath()``
### ——更有用的错误信息时,使用“。css()“”或“”.xpath()' '
  on non-Text Responses (:issue:`2264`)
- ``startproject`` command now generates a sample ``middlewares.py`` file (:issue:`2335`)
### ——“startproject ' '现在命令生成一个样本的中间件)。py”文件(:问题:‘2335’)
- Add more dependencies' version info in ``scrapy version`` verbose output (:issue:`2404`)
### ——添加更多的依赖项的版本信息”“scrapy版本”的详细输出(问题:‘2404’)
- Remove all ``*.pyc`` files from source distribution (:issue:`2386`)
### ——删除所有' ' *。佩克“文件从源分布(:问题:‘2386’)

.. _conda-forge: https://anaconda.org/conda-forge/scrapy


Scrapy 1.2.1 (2016-10-21)
-------------------------

Bug fixes
~~~~~~~~~

- Include OpenSSL's more permissive default ciphers when establishing
### ——包括OpenSSL的更宽松的默认密码时建立
  TLS/SSL connections (:issue:`2314`).
- Fix "Location" HTTP header decoding on non-ASCII URL redirects (:issue:`2321`).
### ——解决“位置”HTTP头解码在非ascii URL重定向(问题:‘2321’)。

Documentation
~~~~~~~~~~~~~

- Fix JsonWriterPipeline example (:issue:`2302`).
### ——修复JsonWriterPipeline(例子:问题:' 2302 ')。
- Various notes: :issue:`2330` on spider names,
### -各种指出::问题:‘2330’在蜘蛛的名字,
  :issue:`2329` on middleware methods processing order,
### :问题:‘2329’中间件方法处理订单,
  :issue:`2327` on getting multi-valued HTTP headers as lists.
### :问题:‘2327’在HTTP头部多值列表。

Other changes
~~~~~~~~~~~~~

- Removed ``www.`` from ``start_urls`` in built-in spider templates (:issue:`2299`).
### -删除“www。' '从' ' start_urls”内置蜘蛛模板(问题:‘2299’)。


Scrapy 1.2.0 (2016-10-03)
-------------------------

New Features
~~~~~~~~~~~~

- New :setting:`FEED_EXPORT_ENCODING` setting to customize the encoding
### -新:设置:“FEED_EXPORT_ENCODING”设置自定义编码
  used when writing items to a file.
### 编写项目文件时使用。
  This can be used to turn off ``\uXXXX`` escapes in JSON output.
### 这可以用于关闭‘\ uXXXX“逃在JSON输出。
  This is also useful for those wanting something else than UTF-8
### 这对于那些想别的东西也有用比utf - 8
  for XML or CSV output (:issue:`2034`).
### 对于XML或CSV输出(问题:‘2034’)。
- ``startproject`` command now supports an optional destination directory
### ”——“startproject”'命令现在支持一个可选的目标目录
  to override the default one based on the project name (:issue:`2005`).
### 覆盖默认的一个基于项目名称(问题:‘2005’)。
- New :setting:`SCHEDULER_DEBUG` setting to log requests serialization
### -新:设置:“SCHEDULER_DEBUG”设置日志请求序列化
  failures (:issue:`1610`).
- JSON encoder now supports serialization of ``set`` instances (:issue:`2058`).
### - JSON编码器现在支持序列化的“设置”“实例(问题:‘2058’)。
- Interpret ``application/json-amazonui-streaming`` as ``TextResponse`` (:issue:`1503`).
### ——解读“应用程序/ json-amazonui-streaming ' ',' ' TextResponse ' '(:问题:‘1503’)。
- ``scrapy`` is imported by default when using shell tools (:command:`shell`,
### ——“scrapy“导入默认情况下在使用shell工具(命令:“壳”,
  :ref:`inspect_response <topics-shell-inspect-response>`) (:issue:`2248`).

Bug fixes
~~~~~~~~~

- DefaultRequestHeaders middleware now runs before UserAgent middleware
### -现在DefaultRequestHeaders中间件运行之前UserAgent中间件
  (:issue:`2088`). **Warning: this is technically backwards incompatible**,
### (问题:‘2088’)。* *警告:这是技术上向后不兼容的* *,
  though we consider this a bug fix.
### 尽管我们认为这错误修复。
- HTTP cache extension and plugins that use the ``.scrapy`` data directory now
### —HTTP缓存扩展和插件,使用' '。现在scrapy“数据目录
  work outside projects (:issue:`1581`).  **Warning: this is technically
### 工作以外的项目(问题:‘1581’)。* *警告:这是技术
  backwards incompatible**, though we consider this a bug fix.
### 向后不兼容的* *,虽然我们认为这个bug修复。
- ``Selector`` does not allow passing both ``response`` and ``text`` anymore
### ——“选择器”“不允许通过“响应”和“文本”了
  (:issue:`2153`).
- Fixed logging of wrong callback name with ``scrapy parse`` (:issue:`2169`).
### ——固定记录错误的回调的名字“scrapy解析“(问题:‘2169’)。
- Fix for an odd gzip decompression bug (:issue:`1606`).
### ——修复一个奇怪的gzip压缩错误(问题:‘1606’)。
- Fix for selected callbacks when using ``CrawlSpider`` with :command:`scrapy parse <parse>`
### ——修复选择回调在使用“CrawlSpider‘:命令:“scrapy解析<解析>”
  (:issue:`2225`).
- Fix for invalid JSON and XML files when spider yields no items (:issue:`872`).
### ——修复无效的JSON和XML文件当蜘蛛收益率没有物品(问题:‘872’)。
- Implement ``flush()`` fpr ``StreamLogger`` avoiding a warning in logs (:issue:`2125`).
### ——实现“冲洗()“玻璃钢”“StreamLogger“避免警告日志(问题:‘2125’)。

Refactoring
~~~~~~~~~~~

- ``canonicalize_url`` has been moved to `w3lib.url`_ (:issue:`2168`).
### ——“canonicalize_url“搬到”w3lib。url的_(:问题:‘2168’)。

.. _w3lib.url: https://w3lib.readthedocs.io/en/latest/w3lib.html#w3lib.url.canonicalize_url

Tests & Requirements
~~~~~~~~~~~~~~~~~~~~

Scrapy's new requirements baseline is Debian 8 "Jessie". It was previously
### Scrapy的新需求基线是Debian 8“杰西”。这是以前
Ubuntu 12.04 Precise.
What this means in practice is that we run continuous integration tests
### 在实践中这意味着什么是我们运行持续集成测试
with these (main) packages versions at a minimum:
### 与这些(主要)至少包版本:
Twisted 14.0, pyOpenSSL 0.14, lxml 3.4.
### 扭曲的14.0、0.14 pyOpenSSL lxml 3.4。

Scrapy may very well work with older versions of these packages
### Scrapy很可能使用旧版本的这些包
(the code base still has switches for older Twisted versions for example)
### (旧的扭曲版本的代码库仍有开关)
but it is not guaranteed (because it's not tested anymore).
### 但它并不能保证(因为它不是测试了)。

Documentation
~~~~~~~~~~~~~

- Grammar fixes: :issue:`2128`, :issue:`1566`.
### ——语法修复::问题:‘2128’,:问题:“1566”。
- Download stats badge removed from README (:issue:`2160`).
### ——下载统计徽章从README(问题:‘2160’)。
- New scrapy :ref:`architecture diagram <topics-architecture>` (:issue:`2165`).
### ——新scrapy:裁判:“架构图< topics-architecture >”(问题:‘2165’)。
- Updated ``Response`` parameters documentation (:issue:`2197`).
### ——更新”的反应“参数文档(问题:‘2197’)。
- Reworded misleading :setting:`RANDOMIZE_DOWNLOAD_DELAY` description (:issue:`2190`).
### -改误导:设置:“RANDOMIZE_DOWNLOAD_DELAY”描述(问题:‘2190’)。
- Add StackOverflow as a support channel (:issue:`2257`).
### ——添加StackOverflow作为支持频道(问题:‘2257’)。


Scrapy 1.1.4 (2017-03-03)
-------------------------

- Packaging fix: disallow unsupported Twisted versions in setup.py
### -包装修复:不允许不受支持的扭曲版本在setup . py


Scrapy 1.1.3 (2016-09-22)
-------------------------

Bug fixes
~~~~~~~~~

- Class attributes for subclasses of ``ImagesPipeline`` and ``FilesPipeline``
### ——类属性的子类“ImagesPipeline ' '和' ' FilesPipeline ' '
  work as they did before 1.1.1 (:issue:`2243`, fixes :issue:`2198`)
### 像以前一样工作1.1.1(问题:“2243”,修复:问题:' 2198 ')

Documentation
~~~~~~~~~~~~~

- :ref:`Overview <intro-overview>` and :ref:`tutorial <intro-tutorial>`
### - ref:! ! ! ! intro-overview >和< Overview:ref:intro-tutorial > < ! ! ! !辅导
  rewritten to use http://toscrape.com websites
### 重写使用http://toscrape.com网站
  (:issue:`2236`, :issue:`2249`, :issue:`2252`).


Scrapy 1.1.2 (2016-08-18)
-------------------------

Bug fixes
~~~~~~~~~

- Introduce a missing :setting:`IMAGES_STORE_S3_ACL` setting to override
### ——引入缺失:设置:“IMAGES_STORE_S3_ACL”设置覆盖
  the default ACL policy in ``ImagesPipeline`` when uploading images to S3
### 默认ACL策略在“ImagesPipeline“当将图片上传到S3
  (note that default ACL policy is "private" -- instead of "public-read" --
### (注意,默认ACL的政策是“私人”——而不是“公有可读”
  since Scrapy 1.1.0)
- :setting:`IMAGES_EXPIRES` default value set back to 90
### -:设置:“IMAGES_EXPIRES”默认值设置回90
  (the regression was introduced in 1.1.1)
### (1.1.1)介绍了回归


Scrapy 1.1.1 (2016-07-13)
-------------------------

Bug fixes
~~~~~~~~~

- Add "Host" header in CONNECT requests to HTTPS proxies (:issue:`2069`)
### ——添加“主机”头连接HTTPS请求代理(问题:‘2069’)
- Use response ``body`` when choosing response class
### ——使用响应“身体”“在选择响应类
  (:issue:`2001`, fixes :issue:`2000`)
- Do not fail on canonicalizing URLs with wrong netlocs
### ——不失败与错误的netlocs规范化的url
  (:issue:`2038`, fixes :issue:`2010`)
- a few fixes for ``HttpCompressionMiddleware`` (and ``SitemapSpider``):
### ——几个修复“HttpCompressionMiddleware“(和“SitemapSpider '):

  - Do not decode HEAD responses (:issue:`2008`, fixes :issue:`1899`)
### ——不解码头反应(问题:“2008”,修复:问题:' 1899 ')
  - Handle charset parameter in gzip Content-Type header
### ——gzip的content - type头处理字符集参数
    (:issue:`2050`, fixes :issue:`2049`)
  - Do not decompress gzip octet-stream responses
### ——不减压gzip八进制反应
    (:issue:`2065`, fixes :issue:`2063`)

- Catch (and ignore with a warning) exception when verifying certificate
### ——抓住时(而忽略警告)异常验证证书
  against IP-address hosts (:issue:`2094`, fixes :issue:`2092`)
### 对ip地址的主机(问题:‘2094’,修复:问题:' 2092 ')
- Make ``FilesPipeline`` and ``ImagesPipeline`` backward compatible again
### ”——让“FilesPipeline“”和“”ImagesPipeline“向后兼容的
  regarding the use of legacy class attributes for customization
### 关于遗产的使用定制的类属性
  (:issue:`1989`, fixes :issue:`1985`)


New features
~~~~~~~~~~~~

- Enable genspider command outside project folder (:issue:`2052`)
### ——允许genspider命令外的项目文件夹(:问题:‘2052’)
- Retry HTTPS CONNECT ``TunnelError`` by default (:issue:`1974`)
### ——重试HTTPS连接“TunnelError默认' '(:问题:‘1974’)


Documentation
~~~~~~~~~~~~~

- ``FEED_TEMPDIR`` setting at lexicographical position (:commit:`9b3c72c`)
### ——“FEED_TEMPDIR“设置在辞典编纂的位置(承诺:“9 b3c72c”)
- Use idiomatic ``.extract_first()`` in overview (:issue:`1994`)
### ——使用惯用“.extract_first()“在概述(:问题:‘1994’)
- Update years in copyright notice (:commit:`c2c8036`)
### 更新年版权声明(承诺:“c2c8036”)
- Add information and example on errbacks (:issue:`1995`)
### ——添加信息和例子errback(问题:' 1995 ')
- Use "url" variable in downloader middleware example (:issue:`2015`)
### ——下载中间件示例中使用“url”变量(问题:‘2015’)
- Grammar fixes (:issue:`2054`, :issue:`2120`)
### ——语法修复(问题:‘2054’,:问题:' 2120 ')
- New FAQ entry on using BeautifulSoup in spider callbacks (:issue:`2048`)
### ——新的FAQ条目使用BeautifulSoup蜘蛛回调(问题:‘2048’)
- Add notes about scrapy not working on Windows with Python 3 (:issue:`2060`)
### ——添加笔记scrapy不工作在Windows与Python 3(问题:‘2060’)
- Encourage complete titles in pull requests (:issue:`2026`)
### ——鼓励完成冠军拉请求(:问题:‘2026’)

Tests
~~~~~

- Upgrade py.test requirement on Travis CI and Pin pytest-cov to 2.2.1 (:issue:`2095`)
### py -升级。测试要求在特拉维斯CI和销pytest-cov 2.2.1(问题:‘2095’)


Scrapy 1.1.0 (2016-05-11)
-------------------------

This 1.1 release brings a lot of interesting features and bug fixes:
### 这个1.1版本带来了很多有趣的功能和错误修正:

- Scrapy 1.1 has beta Python 3 support (requires Twisted >= 15.5). See
### ——Scrapy 1.1 beta Python 3支持(需要扭曲> = 15.5)。看到
  :ref:`news_betapy3` for more details and some limitations.
### 裁判:“news_betapy3”更多的细节和一些限制。
- Hot new features:

  - Item loaders now support nested loaders (:issue:`1467`).
### 项加载器现在支持嵌套装载机(问题:‘1467’)。
  - ``FormRequest.from_response`` improvements (:issue:`1382`, :issue:`1137`).
### ——“FormRequest。from_response“改进(:问题:“1382”,:问题:' 1137 ')。
  - Added setting :setting:`AUTOTHROTTLE_TARGET_CONCURRENCY` and improved
### ——添加设置:设置:“AUTOTHROTTLE_TARGET_CONCURRENCY”和改善
    AutoThrottle docs (:issue:`1324`).
  - Added ``response.text`` to get body as unicode (:issue:`1730`).
### ——添加“响应。文本“让身体unicode(问题:‘1730’)。
  - Anonymous S3 connections (:issue:`1358`).
### ——匿名S3连接(问题:‘1358’)。
  - Deferreds in downloader middlewares (:issue:`1473`). This enables better
### ——延迟下载中间件)(问题:‘1473’)。这使更好的
    robots.txt handling (:issue:`1471`).
  - HTTP caching now follows RFC2616 more closely, added settings
### ——HTTP缓存现在RFC2616更密切,添加设置
    :setting:`HTTPCACHE_ALWAYS_STORE` and
    :setting:`HTTPCACHE_IGNORE_RESPONSE_CACHE_CONTROLS` (:issue:`1151`).
  - Selectors were extracted to the parsel_ library (:issue:`1409`). This means
### ——选择器提取parsel_库(问题:‘1409’)。这意味着
    you can use Scrapy Selectors without Scrapy and also upgrade the
### 您可以使用Scrapy选择器也没有Scrapy和升级
    selectors engine without needing to upgrade Scrapy.
### 选择器引擎Scrapy无需升级。
  - HTTPS downloader now does TLS protocol negotiation by default,
### downloader HTTPS—的现状does TLS protocol中经贸互惠,
    instead of forcing TLS 1.0. You can also set the SSL/TLS method
### 而不是强迫TLS 1.0。你也可以设置SSL / TLS方法
    using the new :setting:`DOWNLOADER_CLIENT_TLS_METHOD`.

- These bug fixes may require your attention:
### ——这些bug修复可能需要您注意:

  - Don't retry bad requests (HTTP 400) by default (:issue:`1289`).
### ——不要重试坏请求(HTTP 400)在默认情况下(问题:‘1289’)。
    If you need the old behavior, add ``400`` to :setting:`RETRY_HTTP_CODES`.
### 如果你需要旧的行为,增加“400”:设置:“RETRY_HTTP_CODES”。
  - Fix shell files argument handling (:issue:`1710`, :issue:`1550`).
### ——修复shell文件参数处理(:问题:“1710”,:问题:' 1550 ')。
    If you try ``scrapy shell index.html`` it will try to load the URL http://index.html,
### 如果你尝试“scrapy壳指数。html ' '它将尝试加载URL http://index.html,
    use ``scrapy shell ./index.html`` to load a local file.
### 使用“scrapy壳。/索引。html的加载本地文件。
  - Robots.txt compliance is now enabled by default for newly-created projects
### ——机器人。txt合规为新创建的项目现在是默认启用
    (:issue:`1724`). Scrapy will also wait for robots.txt to be downloaded
### (问题:‘1724’)。Scrapy还将等待机器人。三种下载
    before proceeding with the crawl (:issue:`1735`). If you want to disable
### 在继续之前的爬行(问题:‘1735’)。如果你想禁用
    this behavior, update :setting:`ROBOTSTXT_OBEY` in ``settings.py`` file
### 这种行为,更新:设置:“ROBOTSTXT_OBEY”“设置。py“文件
    after creating a new project.
### 在创建一个新项目。
  - Exporters now work on unicode, instead of bytes by default (:issue:`1080`).
### ——出口商现在工作在unicode,而不是默认的字节(问题:‘1080’)。
    If you use ``PythonItemExporter``, you may want to update your code to
### 如果你使用“PythonItemExporter ' ',你可能想要更新你的代码
    disable binary mode which is now deprecated.
### 禁用二进制模式现在已经弃用。
  - Accept XML node names containing dots as valid (:issue:`1533`).
### ——接受XML节点名称包含点有效(问题:‘1533’)。
  - When uploading files or images to S3 (with ``FilesPipeline`` or
### ——当S3上传文件或图像(“FilesPipeline ' '
    ``ImagesPipeline``), the default ACL policy is now "private" instead
### “ImagesPipeline ' '),默认ACL策略现在是“私人”代替
    of "public" **Warning: backwards incompatible!**.
### “公共”* *警告:向后兼容! * *。
    You can use :setting:`FILES_STORE_S3_ACL` to change it.
### 您可以使用:设置:“FILES_STORE_S3_ACL”来改变它。
  - We've reimplemented ``canonicalize_url()`` for more correct output,
### ——我们已经重新实现“canonicalize_url()“正确的输出,
    especially for URLs with non-ASCII characters (:issue:`1947`).
### 尤其是对非ascii字符的url(问题:‘1947’)。
    This could change link extractors output compared to previous scrapy versions.
### 这个可以改变链接萃取器输出相比以前scrapy版本。
    This may also invalidate some cache entries you could still have from pre-1.1 runs.
### 
    **Warning: backwards incompatible!**.

Keep reading for more details on other improvements and bug fixes.
### 

.. _news_betapy3:

Beta Python 3 Support
~~~~~~~~~~~~~~~~~~~~~

We have been `hard at work to make Scrapy run on Python 3
### 我们一直在努力使Scrapy Python 3上运行
<https://github.com/scrapy/scrapy/wiki/Python-3-Porting>`_. As a result, now
### 
you can run spiders on Python 3.3, 3.4 and 3.5 (Twisted >= 15.5 required). Some
### 
features are still missing (and some may never be ported).
### 


Almost all builtin extensions/middlewares are expected to work.
### 几乎所有的内装式扩展/中间件)预计的工作。
However, we are aware of some limitations in Python 3:
### 然而,我们知道一些限制在Python 3:

- Scrapy does not work on Windows with Python 3
### ——Scrapy并不与Python 3在Windows上工作
- Sending emails is not supported
### 
- FTP download handler is not supported
### 
- Telnet console is not supported
### ——不支持远程登录控制台

Additional New Features and Enhancements
### 额外的新特性和增强功能
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Scrapy now has a `Code of Conduct`_ (:issue:`1681`).
### 
- Command line tool now has completion for zsh (:issue:`934`).
### 
- Improvements to ``scrapy shell``:
### ——改进“scrapy壳”:

  - Support for bpython and configure preferred Python shell via
### 
    ``SCRAPY_PYTHON_SHELL`` (:issue:`1100`, :issue:`1444`).
  - Support URLs without scheme (:issue:`1498`)
### 没有计划支持的url(:问题:‘1498’)
    **Warning: backwards incompatible!**
  - Bring back support for relative file path (:issue:`1710`, :issue:`1550`).
### 带回支持相对文件路径(:问题:“1710”,:问题:' 1550 ')。

- Added :setting:`MEMUSAGE_CHECK_INTERVAL_SECONDS` setting to change default check
### ——补充道:设置:“MEMUSAGE_CHECK_INTERVAL_SECONDS”设置来改变默认的检查
  interval (:issue:`1282`).
- Download handlers are now lazy-loaded on first request using their
### ——下载处理程序正在使用他们的延迟加载在第一次请求
  scheme (:issue:`1390`, :issue:`1421`).
- HTTPS download handlers do not force TLS 1.0 anymore; instead,
### ——HTTPS下载处理程序不要强迫TLS 1.0了;相反,
  OpenSSL's ``SSLv23_method()/TLS_method()`` is used allowing to try
### OpenSSL的‘SSLv23_method()/ TLS_method()“允许尝试使用
  negotiating with the remote hosts the highest TLS protocol version
### 
  it can (:issue:`1794`, :issue:`1629`).
- ``RedirectMiddleware`` now skips the status codes from
### 
  ``handle_httpstatus_list`` on spider attribute
  or in ``Request``'s ``meta`` key (:issue:`1334`, :issue:`1364`,
### 或在“请求”年代“元”键(:问题:“1334”,:问题:“1364”,
  :issue:`1447`).
- Form submission:

  - now works with ``<button>`` elements too (:issue:`1469`).
### ——现在使用“<按钮>“元素(问题:‘1469’)。
  - an empty string is now used for submit buttons without a value
### ——一个空字符串是现在用于提交按钮没有价值
    (:issue:`1472`)

- Dict-like settings now have per-key priorities
### ——现在Dict-like设置每个键的优先事项
  (:issue:`1135`, :issue:`1149` and :issue:`1586`).
- Sending non-ASCII emails (:issue:`1662`)
### 
- ``CloseSpider`` and ``SpiderState`` extensions now get disabled if no relevant
### ”——“CloseSpider“”和“”SpiderState“扩展现在禁用如果没有相关
  setting is set (:issue:`1723`, :issue:`1725`).
### 设置被设置(问题:‘1723’,:问题:' 1725 ')。
- Added method ``ExecutionEngine.close`` (:issue:`1423`).
### ——“ExecutionEngine添加方法。关闭“(问题:‘1423’)。
- Added method ``CrawlerRunner.create_crawler`` (:issue:`1528`).
### ——“CrawlerRunner添加方法。create_crawler ' '(:问题:‘1528’)。
- Scheduler priority queue can now be customized via
### ——调度器优先队列现在可以通过定制
  :setting:`SCHEDULER_PRIORITY_QUEUE` (:issue:`1822`).
- ``.pps`` links are now ignored by default in link extractors (:issue:`1835`).
### ——“。pps的链接现在忽略默认链接提取器(问题:‘1835’)。
- temporary data folder for FTP and S3 feed storages can be customized
### ——为FTP和S3存储临时数据文件夹可以定制
  using a new :setting:`FEED_TEMPDIR` setting (:issue:`1847`).
### 使用新的设置:“FEED_TEMPDIR”设置(问题:‘1847’)。
- ``FilesPipeline`` and ``ImagesPipeline`` settings are now instance attributes
### ”——“FilesPipeline“”和“”ImagesPipeline ' '现在设置实例属性
  instead of class attributes, enabling spider-specific behaviors (:issue:`1891`).
### 而不是类属性,使spider-specific行为(问题:‘1891’)。
- ``JsonItemExporter`` now formats opening and closing square brackets
### ”——“JsonItemExporter”“现在格式打开和关闭方括号
  on their own line (first and last lines of output file) (:issue:`1950`).
### 在自己的线(第一个和最后一个行输出文件)(问题:‘1950’)。
- If available, ``botocore`` is used for ``S3FeedStorage``, ``S3DownloadHandler``
### ——如果可用”、“botocore“用于“S3FeedStorage ' ',' ' S3DownloadHandler ' '
  and ``S3FilesStore`` (:issue:`1761`, :issue:`1883`).
- Tons of documentation updates and related fixes (:issue:`1291`, :issue:`1302`,
### 
  :issue:`1335`, :issue:`1683`, :issue:`1660`, :issue:`1642`, :issue:`1721`,
### 问题:“1335”,问题:“1683”,:问题:“1660”,问题:“1642”,:问题:“1721”,
  :issue:`1727`, :issue:`1879`).
- Other refactoring, optimizations and cleanup (:issue:`1476`, :issue:`1481`,
### -其他重构,优化和清理(:问题:“1476”,:问题:“1481”,
  :issue:`1477`, :issue:`1315`, :issue:`1290`, :issue:`1750`, :issue:`1881`).
### 

.. _`Code of Conduct`: https://github.com/scrapy/scrapy/blob/master/CODE_OF_CONDUCT.md
### . ._“行为准则”:https://github.com/scrapy/scrapy/blob/master/CODE_OF_CONDUCT.md


Deprecations and Removals
~~~~~~~~~~~~~~~~~~~~~~~~~

- Added ``to_bytes`` and ``to_unicode``, deprecated ``str_to_unicode`` and
### ——还说‘to_bytes’和‘to_unicode ' ',弃用“str_to_unicode ' '
  ``unicode_to_str`` functions (:issue:`778`).
- ``binary_is_text`` is introduced, to replace use of ``isbinarytext``
### ”——“binary_is_text”的介绍,来取代使用“isbinarytext ' '
  (but with inverse return value) (:issue:`1851`)
### (但与逆返回值)(问题:' 1851 ')
- The ``optional_features`` set has been removed (:issue:`1359`).
### ——“optional_features“设置已被删除(问题:‘1359’)。
- The ``--lsprof`` command line option has been removed (:issue:`1689`).
### ——”“——lsprof“命令行选项已被删除(问题:‘1689’)。
  **Warning: backward incompatible**, but doesn't break user code.
### 
- The following datatypes were deprecated (:issue:`1720`):
### 已弃用以下数据类型(:问题:‘1720’):

  + ``scrapy.utils.datatypes.MultiValueDictKeyError``
  + ``scrapy.utils.datatypes.MultiValueDict``
  + ``scrapy.utils.datatypes.SiteNode``

- The previously bundled ``scrapy.xlib.pydispatch`` library was deprecated and
### ——以前“scrapy.xlib捆绑。图书馆被弃用,pydispatch ' '
  replaced by `pydispatcher <https://pypi.python.org/pypi/PyDispatcher>`_.


Relocations
~~~~~~~~~~~

- ``telnetconsole`` was relocated to ``extensions/`` (:issue:`1524`).
### ——“telnetconsole“迁至“扩展/ ' '(:问题:‘1524’)。

  + Note: telnet is not enabled on Python 3
### 
    (https://github.com/scrapy/scrapy/pull/1524#issuecomment-146985595)

.. _parsel: https://github.com/scrapy/parsel


Bugfixes
~~~~~~~~

- Scrapy does not retry requests that got a ``HTTP 400 Bad Request``
### ——Scrapy不重试请求得到“HTTP 400错误请求' '
  response anymore (:issue:`1289`). **Warning: backwards incompatible!**
### 反应了:问题:‘1289’)。* *警告:向后不兼容! * *
- Support empty password for http_proxy config (:issue:`1274`).
### -支持password空http_proxy for config(结果:! ! ! ! 1274)。
- Interpret ``application/x-json`` as ``TextResponse`` (:issue:`1333`).
### ——解读“应用程序/ x-json ' ',' ' TextResponse ' '(:问题:‘1333’)。
- Support link rel attribute with multiple values (:issue:`1201`).
### 
- Fixed ``scrapy.http.FormRequest.from_response`` when there is a ``<base>``
### 
  tag (:issue:`1564`).
- Fixed :setting:`TEMPLATES_DIR` handling (:issue:`1575`).
### ——固定:设置:“TEMPLATES_DIR”处理(问题:‘1575’)。
- Various ``FormRequest`` fixes (:issue:`1595`, :issue:`1596`, :issue:`1597`).
### ——各种“FormRequest“修复(:问题:“1595”,:问题:“1596”,:问题:' 1597 ')。
- Makes ``_monkeypatches`` more robust (:issue:`1634`).
### ——让“_monkeypatches‘更健壮(问题:‘1634’)。
- Fixed bug on ``XMLItemExporter`` with non-string fields in
### ——固定错误“XMLItemExporter non-string字段' '
  items (:issue:`1738`).
- Fixed startproject command in OS X (:issue:`1635`).
### 在OS X -固定startproject命令(问题:‘1635’)。
- Fixed PythonItemExporter and CSVExporter for non-string item
### ——固定PythonItemExporter和CSVExporter non-string项目
  types (:issue:`1737`).
- Various logging related fixes (:issue:`1294`, :issue:`1419`, :issue:`1263`,
### -修复相关的各种日志(:问题:“1294”,:问题:“1419”,:问题:“1263”,
  :issue:`1624`, :issue:`1654`, :issue:`1722`, :issue:`1726` and :issue:`1303`).
### 问题:“1624”,:问题:“1654”,问题:“1722”,:问题:“1726”和:问题:' 1303 ')。
- Fixed bug in ``utils.template.render_templatefile()`` (:issue:`1212`).
### ——在“utils.template.render_templatefile固定错误()' '(:问题:‘1212’)。
- sitemaps extraction from ``robots.txt`` is now case-insensitive (:issue:`1902`).
### 从“机器人——sitemaps提取。txt ' '现在不区分大小写(问题:‘1902’)。
- HTTPS+CONNECT tunnels could get mixed up when using multiple proxies
### - HTTPS +连接隧道可以混在使用多个代理
  to same remote host (:issue:`1912`).
### 同一远程主机(问题:‘1912’)。


Scrapy 1.0.7 (2017-03-03)
-------------------------

- Packaging fix: disallow unsupported Twisted versions in setup.py
### -包装修复:不允许不受支持的扭曲版本在setup . py


Scrapy 1.0.6 (2016-05-04)
-------------------------

- FIX: RetryMiddleware is now robust to non-standard HTTP status codes (:issue:`1857`)
### 
- FIX: Filestorage HTTP cache was checking wrong modified time (:issue:`1875`)
### -修复:Filestorage HTTP缓存是检查错误的修改时间(问题:‘1875’)
- DOC: Support for Sphinx 1.4+ (:issue:`1893`)
### - DOC:支持斯芬克斯1.4 +(:问题:‘1893’)
- DOC: Consistency in selectors examples (:issue:`1869`)
### 在选择器的例子- DOC:一致性(:问题:‘1869’)


Scrapy 1.0.5 (2016-02-04)
-------------------------

- FIX: [Backport] Ignore bogus links in LinkExtractors (fixes :issue:`907`, :commit:`108195e`)
### ——修复(补丁):忽略虚假链接LinkExtractors(修复:问题:“907”,:提交:108195 e)
- TST: Changed buildbot makefile to use 'pytest' (:commit:`1f3d90a`)
### -测试:改变buildbot makefile使用“pytest”(提交:1 f3d90a)
- DOC: Fixed typos in tutorial and media-pipeline (:commit:`808a9ea` and :commit:`803bd87`)
### - DOC:固定错误教程和媒体管道(:提交:“808 a9ea”和:提交:“803 bd87”)
- DOC: Add AjaxCrawlMiddleware to DOWNLOADER_MIDDLEWARES_BASE in settings docs (:commit:`aa94121`)
### - DOC:添加AjaxCrawlMiddleware DOWNLOADER_MIDDLEWARES_BASE在设置文档(承诺:“aa94121”)


Scrapy 1.0.4 (2015-12-30)
-------------------------

- Ignoring xlib/tx folder, depending on Twisted version. (:commit:`7dfa979`)
### -忽略xlib / tx文件夹,根据扭曲的版本。(承诺:“7 dfa979”)
- Run on new travis-ci infra (:commit:`6e42f0b`)
### ——运行在新的travis-ci下文(承诺:“6 e42f0b”)
- Spelling fixes (:commit:`823a1cc`)
- escape nodename in xmliter regex (:commit:`da3c155`)
### ——逃避nodename xmliter regex(承诺:“da3c155”)
- test xml nodename with dots (:commit:`4418fc3`)
### -测试xml节点名用点(提交:4418一个fc3的文件)
- TST don't use broken Pillow version in tests (:commit:`a55078c`)
### ——测试不使用破枕头版本在测试中(承诺:“a55078c”)
- disable log on version command. closes #1426 (:commit:`86fc330`)
### ——命令禁用登录版本。关闭# 1426(:提交:“86 fc330”)
- disable log on startproject command (:commit:`db4c9fe`)
### ——禁用登录startproject命令(承诺:“db4c9fe”)
- Add PyPI download stats badge (:commit:`df2b944`)
### ——添加PyPI下载统计徽章(承诺:“df2b944”)
- don't run tests twice on Travis if a PR is made from a scrapy/scrapy branch (:commit:`a83ab41`)
### ——不要运行测试两次在特拉维斯如果公关是由scrapy / scrapy分支(承诺:“a83ab41”)
- Add Python 3 porting status badge to the README (:commit:`73ac80d`)
### ——添加Python 3移植状态徽章README(提交:“73 ac80d”)
- fixed RFPDupeFilter persistence (:commit:`97d080e`)
### ——固定RFPDupeFilter持久性(提交:“97 d080e”)
- TST a test to show that dupefilter persistence is not working (:commit:`97f2fb3`)
### ——结核菌素试验表明dupefilter持久性不工作(提交:“97 f2fb3”)
- explicit close file on file:// scheme handler (:commit:`d9b4850`)
### ——显式关闭文件文件:/ /计划处理程序(承诺:“d9b4850”)
- Disable dupefilter in shell (:commit:`c0d0734`)
### ——禁用dupefilter shell(承诺:“c0d0734”)
- DOC: Add captions to toctrees which appear in sidebar (:commit:`aa239ad`)
### - DOC:添加字幕toctrees出现在侧边栏(承诺:“aa239ad”)
- DOC Removed pywin32 from install instructions as it's already declared as dependency. (:commit:`10eb400`)
### ——医生移除pywin32从安装说明它已经声明为依赖。(承诺:“10 eb400”)
- Added installation notes about using Conda for Windows and other OSes. (:commit:`1c3600a`)
### ——添加安装notes使用Conda为Windows和其他操作系统。(提交:1 c3600a)
- Fixed minor grammar issues. (:commit:`7f4ddd5`)
### ——固定小语法问题。(承诺:“7 f4ddd5”)
- fixed a typo in the documentation. (:commit:`b71f677`)
### -修正了一个错误的文档。(承诺:“b71f677”)
- Version 1 now exists (:commit:`5456c0e`)
### 现在版本1的存在(提交:“5456 c0e”)
- fix another invalid xpath error (:commit:`0a1366e`)
### ——解决另一个无效的xpath错误(承诺:“0 a1366e”)
- fix ValueError: Invalid XPath: //div/[id="not-exists"]/text() on selectors.rst (:commit:`ca8d60f`)
### -修复ValueError:无效的XPath:/ / div[id = "不存在"]/ text()选择器。rst(承诺:“ca8d60f”)
- Typos corrections (:commit:`7067117`)
- fix typos in downloader-middleware.rst and exceptions.rst, middlware -> middleware (:commit:`32f115c`)
### ——在downloader-middleware修复拼写错误。rst和异常。rst服务所- >中间件(:承诺:“32 f115c”)
- Add note to ubuntu install section about debian compatibility (:commit:`23fda69`)
### ——注意添加到ubuntu安装部分debian兼容(承诺:“23 fda69”)
- Replace alternative OSX install workaround with virtualenv (:commit:`98b63ee`)
### 用virtualenv代替替代OSX安装解决方案(提交:“98 b63ee”)
- Reference Homebrew's homepage for installation instructions (:commit:`1925db1`)
### 安装说明参考自制程序的主页(提交:“1925 db1”)
- Add oldest supported tox version to contributing docs (:commit:`5d10d6d`)
### 托克斯最大的支持版本添加到贡献文档(承诺:“5 d10d6d”)
- Note in install docs about pip being already included in python>=2.7.9 (:commit:`85c980e`)
### ——注意在安装文档关于皮普已经包含在python > = 2.7.9(提交:“85 c980e”)
- Add non-python dependencies to Ubuntu install section in the docs (:commit:`fbd010d`)
### ——在文档中添加非python依赖性Ubuntu安装部分(承诺:“fbd010d”)
- Add OS X installation section to docs (:commit:`d8f4cba`)
### - OS X安装部分添加到文档(承诺:“d8f4cba”)
- DOC(ENH): specify path to rtd theme explicitly (:commit:`de73b1a`)
### - DOC(掺):指定路径rtd主题明确(承诺:“de73b1a”)
- minor: scrapy.Spider docs grammar (:commit:`1ddcc7b`)
### -小:scrapy。蜘蛛文档语法(提交:1 ddcc7b)
- Make common practices sample code match the comments (:commit:`1b85bcf`)
### 让公共实践示例代码匹配的评论(提交:1 b85bcf)
- nextcall repetitive calls (heartbeats). (:commit:`55f7104`)
### ——nextcall重复调用(心跳)。(承诺:“55 f7104”)
- Backport fix compatibility with Twisted 15.4.0 (:commit:`b262411`)
### 补丁修复兼容扭曲15.4.0(承诺:“b262411”)
- pin pytest to 2.7.3 (:commit:`a6535c2`)
### ——销pytest 2.7.3(承诺:“a6535c2”)
- Merge pull request #1512 from mgedmin/patch-1 (:commit:`8876111`)
### ——合并将请求从mgedmin # 1512 /补丁1(提交:' 8876111 ')
- Merge pull request #1513 from mgedmin/patch-2 (:commit:`5d4daf8`)
### ——合并将请求从mgedmin # 1513 / patch-2(承诺:“5 d4daf8”)
- Typo (:commit:`f8d0682`)
- Fix list formatting (:commit:`5f83a93`)
### -修复列表格式(承诺:“5 f83a93”)
- fix scrapy squeue tests after recent changes to queuelib (:commit:`3365c01`)
### ——修复scrapy squeue测试后最近更改queuelib(提交:3365 c01的)
- Merge pull request #1475 from rweindl/patch-1 (:commit:`2d688cd`)
### ——合并将请求从rweindl # 1475 /补丁1(承诺:“2 d688cd”)
- Update tutorial.rst (:commit:`fbc1f25`)
- Merge pull request #1449 from rhoekman/patch-1 (:commit:`7d6538c`)
### ——合并将请求从rhoekman # 1449 /补丁1(承诺:“7 d6538c”)
- Small grammatical change (:commit:`8752294`)
### ——小语法变化:提交:' 8752294 ')
- Add openssl version to version command (:commit:`13c45ac`)
### ——添加openssl版本命令(承诺:“13 c45ac”)

Scrapy 1.0.3 (2015-08-11)
-------------------------

- add service_identity to scrapy install_requires (:commit:`cbc2501`)
### ——添加service_identity scrapy install_requires(承诺:“cbc2501”)
- Workaround for travis#296 (:commit:`66af9cd`)
### 特拉维斯# 296 -解决方案(:提交:“66 af9cd”)

Scrapy 1.0.2 (2015-08-06)
-------------------------

- Twisted 15.3.0 does not raises PicklingError serializing lambda functions (:commit:`b04dd7d`)
### 
- Minor method name fix (:commit:`6f85c7f`)
### ——小方法名修复(承诺:“6 f85c7f”)
- minor: scrapy.Spider grammar and clarity (:commit:`9c9d2e0`)
### -小:scrapy。蜘蛛语法和清晰(承诺:“9 c9d2e0”)
- Put a blurb about support channels in CONTRIBUTING (:commit:`c63882b`)
### 
- Fixed typos (:commit:`a9ae7b0`)
- Fix doc reference. (:commit:`7c8a4fe`)
### ——修复医生参考。(承诺:“7 c8a4fe”)

Scrapy 1.0.1 (2015-07-01)
-------------------------

- Unquote request path before passing to FTPClient, it already escape paths (:commit:`cc00ad2`)
### ——“请求路径传递FTPClient之前,它已经逃生路径(承诺:“cc00ad2”)
- include tests/ to source distribution in MANIFEST.in (:commit:`eca227e`)
### ——包括测试/源分布清单。(承诺:“eca227e”)
- DOC Fix SelectJmes documentation (:commit:`b8567bc`)
### ——医生修复SelectJmes文档(承诺:“b8567bc”)
- DOC Bring Ubuntu and Archlinux outside of Windows subsection (:commit:`392233f`)
### ——医生把Ubuntu和Archlinux Windows之外的分段(提交:392233 f)
- DOC remove version suffix from ubuntu package (:commit:`5303c66`)
### 医生从ubuntu包删除版本后缀(提交:“5303 c66”)
- DOC Update release date for 1.0 (:commit:`c89fa29`)
### ——文档更新发布日期为1.0(承诺:“c89fa29”)

Scrapy 1.0.0 (2015-06-19)
-------------------------

You will find a lot of new features and bugfixes in this major release.  Make
### 你会发现很多新特性和修正主要版本。使
sure to check our updated :ref:`overview <intro-overview>` to get a glance of
### 确保检查我们的更新:裁判:“< intro-overview >概述”一眼
some of the changes, along with our brushed :ref:`tutorial <intro-tutorial>`.
### 的一些变化,以及我们的刷:裁判:“教程< intro-tutorial >”。

Support for returning dictionaries in spiders
### 支持返回词典蜘蛛
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Declaring and returning Scrapy Items is no longer necessary to collect the
### 
scraped data from your spider, you can now return explicit dictionaries
### 刮数据从你的蜘蛛,你现在可以返回明确的字典
instead.

*Classic version*

::

    class MyItem(scrapy.Item):
        url = scrapy.Field()

    class MySpider(scrapy.Spider):
        def parse(self, response):
            return MyItem(url=response.url)

*New version*

::

    class MySpider(scrapy.Spider):
        def parse(self, response):
            return {'url': response.url}

Per-spider settings (GSoC 2014)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Last Google Summer of Code project accomplished an important redesign of the
### 去年Google代码之夏”项目的一个重要设计完成
mechanism used for populating settings, introducing explicit priorities to
### 机制用于填充设置,引入显式优先级
override any given setting. As an extension of that goal, we included a new
### 覆盖任何设置。这一目标为一个扩展,我们包括一个新的
level of priority for settings that act exclusively for a single spider,
### 的优先级级别设置,专门为一个蜘蛛,
allowing them to redefine project settings.
### 让他们重新定义项目设置。

Start using it by defining a :attr:`~scrapy.spiders.Spider.custom_settings`
### 开始使用它通过定义:attr:“~ scrapy.spiders.Spider.custom_settings”
class variable in your spider::
### 在你的蜘蛛:类变量:

    class MySpider(scrapy.Spider):
        custom_settings = {
            "DOWNLOAD_DELAY": 5.0,
            "RETRY_ENABLED": False,
        }

Read more about settings population: :ref:`topics-settings`
### 阅读更多关于设置人口::裁判:“topics-settings”

Python Logging
~~~~~~~~~~~~~~

Scrapy 1.0 has moved away from Twisted logging to support Python built in’s
### Scrapy 1.0已经远离扭曲日志支持Python内建的
as default logging system. We’re maintaining backward compatibility for most
### 默认的日志系统。我们维持对大多数的向后兼容性
of the old custom interface to call logging functions, but you’ll get
### 旧的自定义接口调用日志记录功能,但你会得到
warnings to switch to the Python logging API entirely.
### 警告完全切换到Python日志API。

*Old version*

::

    from scrapy import log
    log.msg('MESSAGE', log.INFO)

*New version*

::

    import logging
    logging.info('MESSAGE')

Logging with spiders remains the same, but on top of the
### 日志记录与蜘蛛是相同的,但上
:meth:`~scrapy.spiders.Spider.log` method you’ll have access to a custom
### :甲:“~ scrapy.spiders.Spider。日志的方法你会获得一个定制的
:attr:`~scrapy.spiders.Spider.logger` created for the spider to issue log
### :attr:~ scrapy.spiders.Spider。蜘蛛问题日志记录器的创建
events:

::

    class MySpider(scrapy.Spider):
        def parse(self, response):
            self.logger.info('Response received')

Read more in the logging documentation: :ref:`topics-logging`
### 阅读更多的日志文档::裁判:“topics-logging”

Crawler API refactoring (GSoC 2014)
### 履带API重构(GSoC 2014)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another milestone for last Google Summer of Code was a refactoring of the
### 去年Google代码之夏”的另一个里程碑的重构
internal API, seeking a simpler and easier usage. Check new core interface
### 内部API,寻求一种更简单和更容易使用。检查新的核心接口
in: :ref:`topics-api`

A common situation where you will face these changes is while running Scrapy
### 
from scripts. Here’s a quick example of how to run a Spider manually with the
### 从脚本。这里有一个快速的例子如何运行蜘蛛手动的
new API:

::

    from scrapy.crawler import CrawlerProcess

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
### “USER_AGENT”:“Mozilla / 4.0(compatible;MSIE 7.0;Windows NT 5.1)”
    })
    process.crawl(MySpider)
    process.start()

Bear in mind this feature is still under development and its API may change
### 记住这个特性仍在发展和它的API可能会改变
until it reaches a stable status.
### ,直到达到一个稳定状态。

See more examples for scripts running Scrapy: :ref:`topics-practices`
### 看到更多的示例脚本运行Scrapy:裁判:“topics-practices”

Module Relocations
~~~~~~~~~~~~~~~~~~

There’s been a large rearrangement of modules trying to improve the general
### 有一个大的重排的模块试图改善一般
structure of Scrapy. Main changes were separating various subpackages into
### Scrapy结构。主要变化是分开不同的子包
new projects and dissolving both `scrapy.contrib` and `scrapy.contrib_exp`
### 新项目和溶解的scrapy。普通发布版”和“scrapy.contrib_exp”
into top level packages. Backward compatibility was kept among internal
### 到顶层的包。一直在内部的向后兼容性
relocations, while importing deprecated modules expect warnings indicating
### 搬迁,而进口弃用模块预计警告指示
their new place.

Full list of relocations
************************

Outsourced packages

.. note::
    These extensions went through some minor changes, e.g. some setting names
### 这些扩展经历了一些小的改变,例如一些设置的名字
    were changed. Please check the documentation in each new repository to
### 被改变了。请检查每一个新的存储库中的文档
    get familiar with the new usage.
### 熟悉新的用法。

+-------------------------------------+-------------------------------------+
| Old location                        | New location                        |
### | | |位置新老位置
+=====================================+=====================================+
| scrapy.commands.deploy              | `scrapyd-client <https://github.com |
### | scrapy.commands.deploy scrapyd-client < https://github.com | |”
|                                     | /scrapy/scrapyd-client>`_           |
### | | / scrapy / scrapyd-client > _ |
|                                     | (See other alternatives here:       |
### | |(见其他选择:|
|                                     | :ref:`topics-deploy`)               |
### | |:裁判:“topics-deploy”)|
+-------------------------------------+-------------------------------------+
| scrapy.contrib.djangoitem           | `scrapy-djangoitem <https://github. |
### | scrapy.contrib。djangoitem |“scrapy-djangoitem < https://github。|
|                                     | com/scrapy-plugins/scrapy-djangoite |
### | | com/scrapy-plugins/scrapy-djangoite |
|                                     | m>`_                                |
### m > ' _ | | |
+-------------------------------------+-------------------------------------+
| scrapy.webservice                   | `scrapy-jsonrpc <https://github.com |
### 
|                                     | /scrapy-plugins/scrapy-jsonrpc>`_   |
### | | / scrapy-plugins / scrapy-jsonrpc > _ |
+-------------------------------------+-------------------------------------+

`scrapy.contrib_exp` and `scrapy.contrib` dissolutions

+-------------------------------------+-------------------------------------+
| Old location                        | New location                        |
### | | |位置新老位置
+=====================================+=====================================+
| scrapy.contrib\_exp.downloadermidd\ | scrapy.downloadermiddlewares.decom\ |
### | scrapy.contrib \ _exp。downloadermidd \ | scrapy.downloadermiddlewares。decom \ |
| leware.decompression                | pression                            |
### leware |。decompression | |压力
+-------------------------------------+-------------------------------------+
| scrapy.contrib\_exp.iterators       | scrapy.utils.iterators              |
### | scrapy.contrib \ _exp。迭代器| scrapy.utils。迭代器|
+-------------------------------------+-------------------------------------+
| scrapy.contrib.downloadermiddleware | scrapy.downloadermiddlewares        |
### | scrapy.contrib。downloadermiddleware | scrapy。downloadermiddlewares |
+-------------------------------------+-------------------------------------+
| scrapy.contrib.exporter             | scrapy.exporters                    |
### 
+-------------------------------------+-------------------------------------+
| scrapy.contrib.linkextractors       | scrapy.linkextractors               |
### | scrapy.contrib。linkextractors | scrapy。linkextractors |
+-------------------------------------+-------------------------------------+
| scrapy.contrib.loader               | scrapy.loader                       |
### | scrapy.contrib。装载机| scrapy。加载器|
+-------------------------------------+-------------------------------------+
| scrapy.contrib.loader.processor     | scrapy.loader.processors            |
### | scrapy.contrib.loader。处理器| scrapy.loader。处理器|
+-------------------------------------+-------------------------------------+
| scrapy.contrib.pipeline             | scrapy.pipelines                    |
### | scrapy.contrib。管道| scrapy。管道|
+-------------------------------------+-------------------------------------+
| scrapy.contrib.spidermiddleware     | scrapy.spidermiddlewares            |
### | scrapy.contrib。spidermiddleware | scrapy。spidermiddlewares |
+-------------------------------------+-------------------------------------+
| scrapy.contrib.spiders              | scrapy.spiders                      |
### | scrapy.contrib。蜘蛛| scrapy。蜘蛛|
+-------------------------------------+-------------------------------------+
| * scrapy.contrib.closespider        | scrapy.extensions.\*                |
### 
| * scrapy.contrib.corestats          |                                     |
### | * scrapy.contrib。corestats | |
| * scrapy.contrib.debug              |                                     |
### | * scrapy.contrib。调试| |
| * scrapy.contrib.feedexport         |                                     |
### | * scrapy.contrib。feedexport | |
| * scrapy.contrib.httpcache          |                                     |
### | scrapy.contrib *。httpcache | |
| * scrapy.contrib.logstats           |                                     |
### | * scrapy.contrib。logstats | |
| * scrapy.contrib.memdebug           |                                     |
### | * scrapy.contrib。memdebug | |
| * scrapy.contrib.memusage           |                                     |
### | * scrapy.contrib。memusage | |
| * scrapy.contrib.spiderstate        |                                     |
### | * scrapy.contrib。spiderstate | |
| * scrapy.contrib.statsmailer        |                                     |
### | * scrapy.contrib。statsmailer | |
| * scrapy.contrib.throttle           |                                     |
### | * scrapy.contrib。节流| |
+-------------------------------------+-------------------------------------+

Plural renames and Modules unification
### 复数重命名和模块统一

+-------------------------------------+-------------------------------------+
| Old location                        | New location                        |
### | | |位置新老位置
+=====================================+=====================================+
| scrapy.command                      | scrapy.commands                     |
### | scrapy.command | scrapy.commands |
+-------------------------------------+-------------------------------------+
| scrapy.dupefilter                   | scrapy.dupefilters                  |
### | scrapy。dupefilter | scrapy。dupefilters |
+-------------------------------------+-------------------------------------+
| scrapy.linkextractor                | scrapy.linkextractors               |
### | scrapy。linkextractor | scrapy。linkextractors |
+-------------------------------------+-------------------------------------+
| scrapy.spider                       | scrapy.spiders                      |
### | scrapy。蜘蛛| scrapy。蜘蛛|
+-------------------------------------+-------------------------------------+
| scrapy.squeue                       | scrapy.squeues                      |
### | scrapy。squeue | scrapy。squeues |
+-------------------------------------+-------------------------------------+
| scrapy.statscol                     | scrapy.statscollectors              |
### | scrapy。statscol | scrapy。statscollectors |
+-------------------------------------+-------------------------------------+
| scrapy.utils.decorator              | scrapy.utils.decorators             |
### | scrapy.utils。装饰| scrapy.utils。decorator |
+-------------------------------------+-------------------------------------+

Class renames

+-------------------------------------+-------------------------------------+
| Old location                        | New location                        |
### | | |位置新老位置
+=====================================+=====================================+
| scrapy.spidermanager.SpiderManager  | scrapy.spiderloader.SpiderLoader    |
### | scrapy.spidermanager。SpiderManager | scrapy.spiderloader。SpiderLoader |
+-------------------------------------+-------------------------------------+

Settings renames

+-------------------------------------+-------------------------------------+
| Old location                        | New location                        |
### | | |位置新老位置
+=====================================+=====================================+
| SPIDER\_MANAGER\_CLASS              | SPIDER\_LOADER\_CLASS               |
### |蜘蛛\ _MANAGER \ _CLASS蜘蛛\ _load \ _CLASS | |
+-------------------------------------+-------------------------------------+

Changelog
~~~~~~~~~

New Features and Enhancements

- Python logging (:issue:`1060`, :issue:`1235`, :issue:`1236`, :issue:`1240`,
### - Python日志(:问题:‘1060’,:问题:“1235”,:问题:“1236”,:问题:“1240”,
  :issue:`1259`, :issue:`1278`, :issue:`1286`)
- FEED_EXPORT_FIELDS option (:issue:`1159`, :issue:`1224`)
### ——FEED_EXPORT_FIELDS选项(问题:‘1159’,:问题:' 1224 ')
- Dns cache size and timeout options (:issue:`1132`)
### Dns缓存大小和超时选项(:问题:‘1132’)
- support namespace prefix in xmliter_lxml (:issue:`963`)
### -支持名称空间前缀xmliter_lxml(:问题:‘963’)
- Reactor threadpool max size setting (:issue:`1123`)
### ——反应堆threadpool最大大小设置(:问题:‘1123’)
- Allow spiders to return dicts. (:issue:`1081`)
### ——让蜘蛛返回字典。(问题:‘1081’)
- Add Response.urljoin() helper (:issue:`1086`)
### ——添加Response.urljoin()辅助(:问题:‘1086’)
- look in ~/.config/scrapy.cfg for user config (:issue:`1098`)
### ——在~ / . config / scrapy看。cfg为用户配置(:问题:‘1098’)
- handle TLS SNI (:issue:`1101`)
### -处理TLS SNI(:问题:‘1101’)
- Selectorlist extract first (:issue:`624`, :issue:`1145`)
### ——Selectorlist提取第一(:问题:“624”,:问题:' 1145 ')
- Added JmesSelect (:issue:`1016`)
- add gzip compression to filesystem http cache backend (:issue:`1020`)
### gzip压缩添加到http缓存文件系统后端(:问题:‘1020’)
- CSS support in link extractors (:issue:`983`)
### CSS支持链接提取器(:问题:‘983’)
- httpcache dont_cache meta #19 #689 (:issue:`821`)
### dont_cache meta httpcache - 689(# #:19:! ! ! ! 821)
- add signal to be sent when request is dropped by the scheduler
### ——添加信号发送请求时下降了调度器
  (:issue:`961`)
- avoid download large response (:issue:`946`)
### -避免下载大响应(:问题:‘946’)
- Allow to specify the quotechar in CSVFeedSpider (:issue:`882`)
### 允许指定quotechar CSVFeedSpider(:问题:‘882’)
- Add referer to "Spider error processing" log message (:issue:`795`)
### ——添加推荐人“蜘蛛错误处理”日志消息(问题:‘795’)
- process robots.txt once (:issue:`896`)
### ——过程的机器人。一旦(txt:问题:' 896 ')
- GSoC Per-spider settings (:issue:`854`)
### ——GSoC Per-spider设置(:问题:‘854’)
- Add project name validation (:issue:`817`)
### 添加项目名称验证(:问题:‘817’)
- GSoC API cleanup (:issue:`816`, :issue:`1128`, :issue:`1147`,
### ——GSoC API清理(:问题:“816”,:问题:“1128”,:问题:“1147”,
  :issue:`1148`, :issue:`1156`, :issue:`1185`, :issue:`1187`, :issue:`1258`,
### 问题:“1148”,问题:“1156”,:问题:“1185”,问题:“1187”,:问题:“1258”,
  :issue:`1268`, :issue:`1276`, :issue:`1285`, :issue:`1284`)
- Be more responsive with IO operations (:issue:`1074` and :issue:`1075`)
### -与IO操作的响应(问题:“1074”和:问题:' 1075 ')
- Do leveldb compaction for httpcache on closing (:issue:`1297`)
### ——为httpcache做压实并且关闭(问题:‘1297’)

Deprecations and Removals

- Deprecate htmlparser link extractor (:issue:`1205`)
### ——反对htmlparser链接器(:问题:‘1205’)
- remove deprecated code from FeedExporter (:issue:`1155`)
### -移除过时的代码从FeedExporter(:问题:‘1155’)
- a leftover for.15 compatibility (:issue:`925`)
### ——剩下的。15兼容性(问题:‘925’)
- drop support for CONCURRENT_REQUESTS_PER_SPIDER (:issue:`895`)
### -支持CONCURRENT_REQUESTS_PER_SPIDER下降(:问题:‘895’)
- Drop old engine code (:issue:`911`)
### 放弃旧的引擎代码(:问题:‘911’)
- Deprecate SgmlLinkExtractor (:issue:`777`)

Relocations

- Move exporters/__init__.py to exporters.py (:issue:`1242`)
### ——出口商/ __init__移动。py出口商。py(问题:‘1242’)
- Move base classes to their packages (:issue:`1218`, :issue:`1233`)
### ——基类移动到他们的包(:问题:“1218”,:问题:' 1233 ')
- Module relocation (:issue:`1181`, :issue:`1210`)
### ——模块搬迁(问题:‘1181’,:问题:' 1210 ')
- rename SpiderManager to SpiderLoader (:issue:`1166`)
### ——重命名SpiderManager SpiderLoader(问题:‘1166’)
- Remove djangoitem (:issue:`1177`)
- remove scrapy deploy command (:issue:`1102`)
### ——删除scrapy部署命令(:问题:‘1102’)
- dissolve contrib_exp (:issue:`1134`)
- Deleted bin folder from root, fixes #913 (:issue:`914`)
### ——删除本从根文件夹,修复# 913(问题:‘914’)
- Remove jsonrpc based webservice (:issue:`859`)
### ——删除jsonrpc基础网络服务(问题:‘859’)
- Move Test cases under project root dir (:issue:`827`, :issue:`841`)
### ——移动测试用例项目根目录下dir(:问题:“827”,:问题:' 841 ')
- Fix backward incompatibility for relocated paths in settings
### ——修复向后不兼容的迁移路径设置
  (:issue:`1267`)

Documentation

- CrawlerProcess documentation (:issue:`1190`)
- Favoring web scraping over screen scraping in the descriptions
### -支持网页抓取屏幕抓取的描述
  (:issue:`1188`)
- Some improvements for Scrapy tutorial (:issue:`1180`)
### ——一些改进Scrapy教程(:问题:‘1180’)
- Documenting Files Pipeline together with Images Pipeline (:issue:`1150`)
### 管道与管道图像,记录文件(:问题:‘1150’)
- deployment docs tweaks (:issue:`1164`)
### 部署文档调整(:问题:‘1164’)
- Added deployment section covering scrapyd-deploy and shub (:issue:`1124`)
### ——添加部署部分覆盖scrapyd-deploy和shub(:问题:‘1124’)
- Adding more settings to project template (:issue:`1073`)
### 添加更多的设置项目模板(:问题:‘1073’)
- some improvements to overview page (:issue:`1106`)
### ——一些改进概述页面(问题:‘1106’)
- Updated link in docs/topics/architecture.rst (:issue:`647`)
### ——更新链接文档/主题/架构。rst(问题:‘647’)
- DOC reorder topics (:issue:`1022`)
### 医生重新排序的话题(:问题:‘1022’)
- updating list of Request.meta special keys (:issue:`1071`)
### ——更新请求列表。元特殊键(:问题:‘1071’)
- DOC document download_timeout (:issue:`898`)
### - DOC文档download_timeout(:问题:‘898’)
- DOC simplify extension docs (:issue:`893`)
### ——文档简化扩展文档(:问题:‘893’)
- Leaks docs (:issue:`894`)
- DOC document from_crawler method for item pipelines (:issue:`904`)
### - DOC文档from_crawler方法项目管道(:问题:‘904’)
- Spider_error doesn't support deferreds (:issue:`1292`)
### Spider_error不支持延迟(:问题:‘1292’)
- Corrections & Sphinx related fixes (:issue:`1220`, :issue:`1219`,
### ——修正&斯芬克斯相关修复(:问题:“1220”,:问题:“1219”,
  :issue:`1196`, :issue:`1172`, :issue:`1171`, :issue:`1169`, :issue:`1160`,
### 问题:“1196”,问题:“1172”,:问题:“1171”,问题:“1169”,:问题:“1160”,
  :issue:`1154`, :issue:`1127`, :issue:`1112`, :issue:`1105`, :issue:`1041`,
### 问题:“1154”,问题:“1127”,:问题:“1112”,问题:“1105”,:问题:“1041”,
  :issue:`1082`, :issue:`1033`, :issue:`944`, :issue:`866`, :issue:`864`,
### 问题:“1082”,问题:“1033”,:问题:“944”,问题:“866”,:问题:“864”,
  :issue:`796`, :issue:`1260`, :issue:`1271`, :issue:`1293`, :issue:`1298`)
### 问题:“796”,问题:“1260”,:问题:“1271”,问题:“1293”,:问题:' 1298 ')

Bugfixes

- Item multi inheritance fix (:issue:`353`, :issue:`1228`)
### 项目多继承修复(:问题:“353”,:问题:' 1228 ')
- ItemLoader.load_item: iterate over copy of fields (:issue:`722`)
### ——ItemLoader。load_item:遍历的字段(:问题:‘722’)
- Fix Unhandled error in Deferred (RobotsTxtMiddleware) (:issue:`1131`,
### ——修复延迟(RobotsTxtMiddleware)(未处理的错误:问题:“1131”,
  :issue:`1197`)
- Force to read DOWNLOAD_TIMEOUT as int (:issue:`954`)
### 力DOWNLOAD_TIMEOUT读int(:问题:‘954’)
- scrapy.utils.misc.load_object should print full traceback (:issue:`902`)
### ——scrapy.utils.misc。load_object应该打印完整回溯(:问题:‘902’)
- Fix bug for ".local" host name (:issue:`878`)
### ——修复bug”。当地的“主机名(:问题:‘878’)
- Fix for Enabled extensions, middlewares, pipelines info not printed
### ——修复启用扩展,中间件(管道信息不打印
  anymore (:issue:`879`)
- fix dont_merge_cookies bad behaviour when set to false on meta
### ——修复dont_merge_cookies元不良行为时设置为false
  (:issue:`846`)

Python 3 In Progress Support
### Python 3进行支持

- disable scrapy.telnet if twisted.conch is not available (:issue:`1161`)
### ——禁用scrapy。如果扭曲telnet。海螺不可用(问题:‘1161’)
- fix Python 3 syntax errors in ajaxcrawl.py (:issue:`1162`)
### ——修复ajaxcrawl Python 3语法错误。py(问题:‘1162’)
- more python3 compatibility changes for urllib (:issue:`1121`)
### 更多的urllib python3兼容性变更(:问题:‘1121’)
- assertItemsEqual was renamed to assertCountEqual in Python 3.
### ——assertItemsEqual改名为assertCountEqual Python 3。
  (:issue:`1070`)
- Import unittest.mock if available. (:issue:`1066`)
### - - - - - -进口unittest。模拟如果可用。(问题:‘1066’)
- updated deprecated cgi.parse_qsl to use six's parse_qsl (:issue:`909`)
### ——更新弃用cgi。parse_qsl使用六parse_qsl(:问题:‘909’)
- Prevent Python 3 port regressions (:issue:`830`)
### ——防止Python 3端口回归(:问题:‘830’)
- PY3: use MutableMapping for python 3 (:issue:`810`)
### python 3 - PY3:使用MutableMapping(:问题:‘810’)
- PY3: use six.BytesIO and six.moves.cStringIO (:issue:`803`)
### - PY3:使用6。BytesIO six.moves。cStringIO(问题:‘803’)
- PY3: fix xmlrpclib and email imports (:issue:`801`)
### 进口- PY3:修复xmlrpclib和电子邮件(:问题:‘801’)
- PY3: use six for robotparser and urlparse (:issue:`800`)
### - PY3:使用6 robotparser和urlparse(问题:‘800’)
- PY3: use six.iterkeys, six.iteritems, and tempfile (:issue:`799`)
### - PY3:使用6。iterkeys 6。iteritems和tempfile(:问题:‘799’)
- PY3: fix has_key and use six.moves.configparser (:issue:`798`)
### - PY3:修复six.moves has_key和使用。configparser(问题:‘798’)
- PY3: use six.moves.cPickle (:issue:`797`)
### - PY3:six.moves使用。cPickle(问题:‘797’)
- PY3 make it possible to run some tests in Python3 (:issue:`776`)
### ——PY3可以运行一些测试Python3(问题:‘776’)

Tests

- remove unnecessary lines from py3-ignores (:issue:`1243`)
### ——删除不必要的台词py3-ignores(问题:‘1243’)
- Fix remaining warnings from pytest while collecting tests (:issue:`1206`)
### ——解决剩余的警告来自pytest而收集测试(:问题:‘1206’)
- Add docs build to travis (:issue:`1234`)
### ——添加文档构建特拉维斯(:问题:‘1234’)
- TST don't collect tests from deprecated modules. (:issue:`1165`)
### ——结核菌素不收集废弃的测试模块。(问题:‘1165’)
- install service_identity package in tests to prevent warnings
### ——安装service_identity包测试,以防止警告
  (:issue:`1168`)
- Fix deprecated settings API in tests (:issue:`1152`)
### ——解决弃用设置API测试(:问题:‘1152’)
- Add test for webclient with POST method and no body given (:issue:`1089`)
### ——添加测试webclient POST方法和没有人给(问题:‘1089’)
- py3-ignores.txt supports comments (:issue:`1044`)
### ——py3-ignores。三种支持评论(:问题:‘1044’)
- modernize some of the asserts (:issue:`835`)
### 现代化的一些断言(:问题:‘835’)
- selector.__repr__ test (:issue:`779`)

Code refactoring

- CSVFeedSpider cleanup: use iterate_spider_output (:issue:`1079`)
### - CSVFeedSpider清理:使用iterate_spider_output(:问题:‘1079’)
- remove unnecessary check from scrapy.utils.spider.iter_spider_output
### ——从scrapy.utils.spider.iter_spider_output删除不必要的检查
  (:issue:`1078`)
- Pydispatch pep8 (:issue:`992`)
- Removed unused 'load=False' parameter from walk_modules() (:issue:`871`)
### -删除未使用的负荷= False参数从walk_modules()(问题:‘871’)
- For consistency, use `job_dir` helper in `SpiderState` extension.
### ——为了一致性,使用“job_dir”辅助“SpiderState”扩展。
  (:issue:`805`)
- rename "sflo" local variables to less cryptic "log_observer" (:issue:`775`)
### ——重命名“sflo”局部变量少神秘“log_observer”(问题:‘775’)

Scrapy 0.24.6 (2015-04-20)
--------------------------

- encode invalid xpath with unicode_escape under PY2 (:commit:`07cb3e5`)
### ——编码无效的xpath与unicode_escape PY2(提交:' 07 cb3e5 ')
- fix IPython shell scope issue and load IPython user config (:commit:`2c8e573`)
### ——修复IPython shell范围问题和负载IPython用户配置(承诺:“2 c8e573”)
- Fix small typo in the docs (:commit:`d694019`)
### 修复小错误文档(承诺:“d694019”)
- Fix small typo (:commit:`f92fa83`)
### ——修复小错误(承诺:“f92fa83”)
- Converted sel.xpath() calls to response.xpath() in Extracting the data (:commit:`c2c6d15`)
### ——转换sel.xpath()调用response.xpath()提取数据(提交:“c2c6d15”)


Scrapy 0.24.5 (2015-02-25)
--------------------------

- Support new _getEndpoint Agent signatures on Twisted 15.0.0 (:commit:`540b9bc`)
### 
- DOC a couple more references are fixed (:commit:`b4c454b`)
### 医生两个引用是固定的(承诺:“b4c454b”)
- DOC fix a reference (:commit:`e3c1260`)
### ——医生修复一个引用(承诺:“e3c1260”)
- t.i.b.ThreadedResolver is now a new-style class (:commit:`9e13f42`)
### ——t.i.b。ThreadedResolver现在是一个新型的类(承诺:“9 e13f42”)
- S3DownloadHandler: fix auth for requests with quoted paths/query params (:commit:`cdb9a0b`)
### - S3DownloadHandler:解决身份验证请求引用路径/查询参数(承诺:“cdb9a0b”)
- fixed the variable types in mailsender documentation (:commit:`bb3a848`)
### ——固定的变量类型mailsender文档(承诺:“bb3a848”)
- Reset items_scraped instead of item_count (:commit:`edb07a4`)
### 重置items_scraped代替item_count(承诺:“edb07a4”)
- Tentative attention message about what document to read for contributions (:commit:`7ee6f7a`)
### ——初步关注信息文档阅读什么贡献(承诺:“7 ee6f7a”)
- mitmproxy 0.10.1 needs netlib 0.10.1 too (:commit:`874fcdd`)
### ——mitmproxy 0.10.1需要netlib 0.10.1(提交:“874 fcdd”)
- pin mitmproxy 0.10.1 as >0.11 does not work with tests (:commit:`c6b21f0`)
### ——销mitmproxy 0.10.1 > 0.11不使用测试(承诺:“c6b21f0”)
- Test the parse command locally instead of against an external url (:commit:`c3a6628`)
### ——在本地测试解析命令而不是反对外部url(承诺:“c3a6628”)
- Patches Twisted issue while closing the connection pool on HTTPDownloadHandler (:commit:`d0bf957`)
### ——补丁扭曲问题而关闭连接池HTTPDownloadHandler(承诺:“d0bf957”)
- Updates documentation on dynamic item classes. (:commit:`eeb589a`)
### ——更新文档动态项目类。(承诺:“eeb589a”)
- Merge pull request #943 from Lazar-T/patch-3 (:commit:`5fdab02`)
### ——合并将请求从Lazar-T # 943 / patch-3(承诺:“5 fdab02”)
- typo (:commit:`b0ae199`)
- pywin32 is required by Twisted. closes #937 (:commit:`5cb0cfb`)
### ——pywin32所需的扭曲。关闭# 937(:提交:“5 cb0cfb”)
- Update install.rst (:commit:`781286b`)
- Merge pull request #928 from Lazar-T/patch-1 (:commit:`b415d04`)
### ——合并将请求从Lazar-T # 928 /补丁1(承诺:“b415d04”)
- comma instead of fullstop (:commit:`627b9ba`)
### 逗号代替fullstop(提交:“627 b9ba”)
- Merge pull request #885 from jsma/patch-1 (:commit:`de909ad`)
### ——合并将请求从jsma # 885 /补丁1(承诺:“de909ad”)
- Update request-response.rst (:commit:`3f3263d`)
- SgmlLinkExtractor - fix for parsing <area> tag with Unicode present (:commit:`49b40f0`)
### - SgmlLinkExtractor解决Unicode解析<区>标记礼物(承诺:“49 b40f0”)

Scrapy 0.24.4 (2014-08-09)
--------------------------

- pem file is used by mockserver and required by scrapy bench (:commit:`5eddc68`)
### ——mockserver使用pem文件和所需的scrapy板凳(承诺:“5 eddc68”)
- scrapy bench needs scrapy.tests* (:commit:`d6cb999`)
### ——scrapy scrapy长椅上需求。测试*(承诺:“d6cb999”)

Scrapy 0.24.3 (2014-08-09)
--------------------------

- no need to waste travis-ci time on py3 for 0.24 (:commit:`8e080c1`)
### ——不需要浪费时间travis-ci py3对0.24(承诺:“8 e080c1”)
- Update installation docs (:commit:`1d0c096`)
### 更新安装文档(提交:1 d0c096)
- There is a trove classifier for Scrapy framework! (:commit:`4c701d7`)
### ——有一个宝库Scrapy框架分类器!(承诺:“4 c701d7”)
- update other places where w3lib version is mentioned (:commit:`d109c13`)
### ——更新其他地方w3lib版本提到(提交:“d109c13”)
- Update w3lib requirement to 1.8.0 (:commit:`39d2ce5`)
### -更新1.8.0 w3lib要求(承诺:“39 d2ce5”)
- Use w3lib.html.replace_entities() (remove_entities() is deprecated) (:commit:`180d3ad`)
### ——使用w3lib.html.replace_entities()(remove_entities(弃用))(:提交:“180 d3ad”)
- set zip_safe=False (:commit:`a51ee8b`)
- do not ship tests package (:commit:`ee3b371`)
### ——不要船测试包(承诺:“ee3b371”)
- scrapy.bat is not needed anymore (:commit:`c3861cf`)
### ——scrapy。蝙蝠不需要了(承诺:“c3861cf”)
- Modernize setup.py (:commit:`362e322`)
- headers can not handle non-string values (:commit:`94a5c65`)
### ——标题不能处理non-string值(提交:“94 a5c65”)
- fix ftp test cases (:commit:`a274a7f`)
### -修复ftp测试用例(承诺:“a274a7f”)
- The sum up of travis-ci builds are taking like 50min to complete (:commit:`ae1e2cc`)
### ——总结travis-ci构建正在50分钟完成(承诺:“ae1e2cc”)
- Update shell.rst typo (:commit:`e49c96a`)
### ——更新壳。rst错误(承诺:“e49c96a”)
- removes weird indentation in the shell results (:commit:`1ca489d`)
### ——删除奇怪的缩进壳结果(提交:1 ca489d)
- improved explanations, clarified blog post as source, added link for XPath string functions in the spec (:commit:`65c8f05`)
### ——改进的解释,澄清了博客作为源,添加链接XPath字符串函数的规范(提交:“65 c8f05”)
- renamed UserTimeoutError and ServerTimeouterror #583 (:commit:`037f6ab`)
### ——重命名UserTimeoutError和ServerTimeouterror # 583(:提交:“037 f6ab”)
- adding some xpath tips to selectors docs (:commit:`2d103e0`)
### 选择器添加一些xpath建议文档(承诺:“2 d103e0”)
- fix tests to account for https://github.com/scrapy/w3lib/pull/23 (:commit:`f8d366a`)
### ——修复测试占https://github.com/scrapy/w3lib/pull/23(提交:“f8d366a”)
- get_func_args maximum recursion fix #728 (:commit:`81344ea`)
### ——get_func_args最大递归解决# 728(:提交:81344 ea)
- Updated input/ouput processor example according to #560. (:commit:`f7c4ea8`)
### ——更新输入/输出根据# 560处理器的例子。(承诺:“f7c4ea8”)
- Fixed Python syntax in tutorial. (:commit:`db59ed9`)
### ——固定Python语法教程。(承诺:“db59ed9”)
- Add test case for tunneling proxy (:commit:`f090260`)
### 为隧道代理添加测试用例(承诺:“f090260”)
- Bugfix for leaking Proxy-Authorization header to remote host when using tunneling (:commit:`d8793af`)
### ——错误修复泄漏Proxy-Authorization头远程主机使用时隧道(承诺:“d8793af”)
- Extract links from XHTML documents with MIME-Type "application/xml" (:commit:`ed1f376`)
### ——从XHTML文档中提取链接mime类型“application / xml”(承诺:“ed1f376”)
- Merge pull request #793 from roysc/patch-1 (:commit:`91a1106`)
### ——合并将请求从roysc # 793 /补丁1(提交:“91 a1106”)
- Fix typo in commands.rst (:commit:`743e1e2`)
### ——修复错误的命令。rst(提交:“743 e1e2”)
- better testcase for settings.overrides.setdefault (:commit:`e22daaf`)
### ——更好的settings.overrides testcase。setdefault(承诺:“e22daaf”)
- Using CRLF as line marker according to http 1.1 definition (:commit:`5ec430b`)
### ——使用CRLF线标记根据http 1.1定义(承诺:“5 ec430b”)

Scrapy 0.24.2 (2014-07-08)
--------------------------

- Use a mutable mapping to proxy deprecated settings.overrides and settings.defaults attribute (:commit:`e5e8133`)
### ——使用一个可变映射代理弃用的设置。覆盖和设置。默认属性(承诺:“e5e8133”)
- there is not support for python3 yet (:commit:`3cd6146`)
### ——还没有支持python3(承诺:“3 cd6146”)
- Update python compatible version set to debian packages (:commit:`fa5d76b`)
### ——更新python兼容版本设置为debian软件包(承诺:“fa5d76b”)
- DOC fix formatting in release notes (:commit:`c6a9e20`)
### 医生修正版本注释的格式(承诺:“c6a9e20”)

Scrapy 0.24.1 (2014-06-27)
--------------------------

- Fix deprecated CrawlerSettings and increase backwards compatibility with
### ——修复弃用CrawlerSettings和增加向后兼容
  .defaults attribute (:commit:`8e3f20a`)


Scrapy 0.24.0 (2014-06-26)
--------------------------

Enhancements
~~~~~~~~~~~~

- Improve Scrapy top-level namespace (:issue:`494`, :issue:`684`)
### ——提高Scrapy顶级名称空间(:问题:“494”,:问题:' 684 ')
- Add selector shortcuts to responses (:issue:`554`, :issue:`690`)
### 选择快捷方式添加到反应(:问题:“554”,:问题:' 690 ')
- Add new lxml based LinkExtractor to replace unmantained SgmlLinkExtractor
### ——添加新lxml LinkExtractor取代unmantained SgmlLinkExtractor
  (:issue:`559`, :issue:`761`, :issue:`763`)
- Cleanup settings API - part of per-spider settings **GSoC project** (:issue:`737`)
### -清理设置API的一部分per-spider设置* * GSoC项目* *(问题:‘737’)
- Add UTF8 encoding header to templates (:issue:`688`, :issue:`762`)
### - use UTF8编码头添加到模板(:问题:“688”,:问题:' 762 ')
- Telnet console now binds to 127.0.0.1 by default (:issue:`699`)
### 
- Update debian/ubuntu install instructions (:issue:`509`, :issue:`549`)
### ——更新debian / ubuntu安装说明(:问题:“509”,:问题:' 549 ')
- Disable smart strings in lxml XPath evaluations (:issue:`535`)
### 在lxml禁用智能字符串XPath评估(:问题:‘535’)
- Restore filesystem based cache as default for http
### http -恢复文件系统缓存为默认为基础
  cache middleware (:issue:`541`, :issue:`500`, :issue:`571`)
### 缓存的中间件(问题:“541”:问题:“500”,:问题:' 571 ')
- Expose current crawler in Scrapy shell (:issue:`557`)
### ——揭露当前履带Scrapy shell(:问题:‘557’)
- Improve testsuite comparing CSV and XML exporters (:issue:`570`)
### ——提高testsuite比较CSV,XML出口商(问题:‘570’)
- New `offsite/filtered` and `offsite/domains` stats (:issue:`566`)
### ——新的“离线/过滤”和“离线/域的统计数据(问题:‘566’)
- Support process_links as generator in CrawlSpider (:issue:`555`)
### ——支持process_links发生器CrawlSpider(问题:‘555’)
- Verbose logging and new stats counters for DupeFilter (:issue:`553`)
### 详细日志记录和新的DupeFilter统计计数器(:问题:‘553’)
- Add a mimetype parameter to `MailSender.send()` (:issue:`602`)
### ——添加一个mimetype参数“MailSender.send()(问题:‘602’)
- Generalize file pipeline log messages (:issue:`622`)
### ——概括文件管道日志消息(:问题:‘622’)
- Replace unencodeable codepoints with html entities in SGMLLinkExtractor (:issue:`565`)
### 与html实体——取代unencodeable codepoints SGMLLinkExtractor(问题:‘565’)
- Converted SEP documents to rst format (:issue:`629`, :issue:`630`,
### ——9月文件转化成rst格式(:问题:“629”,:问题:“630”,
  :issue:`638`, :issue:`632`, :issue:`636`, :issue:`640`, :issue:`635`,
### 问题:“638”,问题:“632”,:问题:“636”,问题:“640”,:问题:“635”,
  :issue:`634`, :issue:`639`, :issue:`637`, :issue:`631`, :issue:`633`,
### 问题:“634”,问题:“639”,:问题:“637”,问题:“631”,:问题:“633”,
  :issue:`641`, :issue:`642`)
- Tests and docs for clickdata's nr index in FormRequest (:issue:`646`, :issue:`645`)
### ——测试和文档在FormRequest clickdata nr指数(:问题:“646”,:问题:' 645 ')
- Allow to disable a downloader handler just like any other component (:issue:`650`)
### ——允许禁用下载处理程序就像任何其他组件(问题:‘650’)
- Log when a request is discarded after too many redirections (:issue:`654`)
### ——日志当请求被丢弃后太多的重定向(问题:‘654’)
- Log error responses if they are not handled by spider callbacks
### - Log the error responses if they are not handled by spiders callbacks
  (:issue:`612`, :issue:`656`)
- Add content-type check to http compression mw (:issue:`193`, :issue:`660`)
### ——添加内容类型检查http压缩兆瓦(:问题:“193”,:问题:' 660 ')
- Run pypy tests using latest pypi from ppa (:issue:`674`)
### 使用最新pypi ppa -运行pypy测试(:问题:‘674’)
- Run test suite using pytest instead of trial (:issue:`679`)
### 运行测试套件使用pytest代替审判(:问题:‘679’)
- Build docs and check for dead links in tox environment (:issue:`687`)
### ——构建文档和检查托克斯死链接环境(问题:‘687’)
- Make scrapy.version_info a tuple of integers (:issue:`681`, :issue:`692`)
### ——让scrapy。version_info tuple的整数(:问题:“681”,:问题:' 692 ')
- Infer exporter's output format from filename extensions
### 从文件名扩展——推断出口国的输出格式
  (:issue:`546`, :issue:`659`, :issue:`760`)
- Support case-insensitive domains in `url_is_from_any_domain()` (:issue:`693`)
### ——支持区分大小写域url_is_from_any_domain()(问题:‘693’)
- Remove pep8 warnings in project and spider templates (:issue:`698`)
### ——删除pep8警告项目和蜘蛛模板(:问题:‘698’)
- Tests and docs for `request_fingerprint` function (:issue:`597`)
### “request_fingerprint”功能,测试和文档(:问题:‘597’)
- Update SEP-19 for GSoC project `per-spider settings` (:issue:`705`)
### ——更新SEP-19 GSoC项目“per-spider设置”(问题:‘705’)
- Set exit code to non-zero when contracts fails (:issue:`727`)
### —退出代码设置为非零当合同失败(问题:‘727’)
- Add a setting to control what class is instanciated as Downloader component
### ——添加一个设置控制类是instanciated下载器组件
  (:issue:`738`)
- Pass response in `item_dropped` signal (:issue:`724`)
### ——通过反应“item_dropped”信号(:问题:‘724’)
- Improve `scrapy check` contracts command (:issue:`733`, :issue:`752`)
### 提高合同“scrapy检查”命令(:问题:“733”,:问题:' 752 ')
- Document `spider.closed()` shortcut (:issue:`719`)
### ——文档spider.closed()“快捷方式(:问题:‘719’)
- Document `request_scheduled` signal (:issue:`746`)
### ——文档“request_scheduled”信号(:问题:‘746’)
- Add a note about reporting security issues (:issue:`697`)
### 添加一个注意报告安全问题(问题:' 697 ')
- Add LevelDB http cache storage backend (:issue:`626`, :issue:`500`)
### ——添加LevelDB http缓存存储后端(:问题:“626”,:问题:' 500 ')
- Sort spider list output of `scrapy list` command (:issue:`742`)
### ——这种蜘蛛scrapy列表的命令的输出列表(:问题:‘742’)
- Multiple documentation enhancemens and fixes
### ——多个文档enhancemens和修复
  (:issue:`575`, :issue:`587`, :issue:`590`, :issue:`596`, :issue:`610`,
### (问题:“575”,:问题:“587”,:问题:“590”,:问题:“596”,:问题:“610”,
  :issue:`617`, :issue:`618`, :issue:`627`, :issue:`613`, :issue:`643`,
### 问题:“617”,问题:“618”,:问题:“627”,问题:“613”,:问题:“643”,
  :issue:`654`, :issue:`675`, :issue:`663`, :issue:`711`, :issue:`714`)
### 问题:“654”,问题:“675”,:问题:“663”,问题:“711”,:问题:' 714 ')

Bugfixes
~~~~~~~~

- Encode unicode URL value when creating Links in RegexLinkExtractor (:issue:`561`)
### - unicode编码的URL值在创建链接RegexLinkExtractor(问题:‘561’)
- Ignore None values in ItemLoader processors (:issue:`556`)
### 忽略这些值在ItemLoader处理器(:问题:‘556’)
- Fix link text when there is an inner tag in SGMLLinkExtractor and
### ——修复链接文本有一个内在SGMLLinkExtractor和标签
  HtmlParserLinkExtractor (:issue:`485`, :issue:`574`)
- Fix wrong checks on subclassing of deprecated classes
### ——修复错误检查弃用类的子类化
  (:issue:`581`, :issue:`584`)
- Handle errors caused by inspect.stack() failures (:issue:`582`)
### ——处理错误造成inspect.stack()失败(:问题:‘582’)
- Fix a reference to unexistent engine attribute (:issue:`593`, :issue:`594`)
### ——修复的引用不存在引擎属性(:问题:“593”,:问题:' 594 ')
- Fix dynamic itemclass example usage of type() (:issue:`603`)
### —dynamic itemclass / 243号决议确定了使用示范of()(结果! ! ! ! 603):
- Use lucasdemarchi/codespell to fix typos (:issue:`628`)
### -使用lucasdemarchi / codespell修复拼写错误(:问题:‘628’)
- Fix default value of attrs argument in SgmlLinkExtractor to be tuple (:issue:`661`)
### ——修复SgmlLinkExtractor attrs参数的默认值是元组(问题:‘661’)
- Fix XXE flaw in sitemap reader (:issue:`676`)
### 站点地图读者解决XXE缺陷(:问题:‘676’)
- Fix engine to support filtered start requests (:issue:`707`)
### ——修复引擎支持过滤开始请求(:问题:‘707’)
- Fix offsite middleware case on urls with no hostnames (:issue:`745`)
### ——解决离线中间件案件url没有主机名(问题:‘745’)
- Testsuite doesn't require PIL anymore (:issue:`585`)
### Testsuite不再需要公益诉讼(:问题:‘585’)


Scrapy 0.22.2 (released 2014-02-14)
-----------------------------------

- fix a reference to unexistent engine.slots. closes #593 (:commit:`13c099a`)
### ——修复的引用不存在engine.slots。关闭# 593(:提交:“13 c099a”)
- downloaderMW doc typo (spiderMW doc copy remnant) (:commit:`8ae11bf`)
### - downloaderMW医生错误(spiderMW doc副本遗迹)(:提交:“8 ae11bf”)
- Correct typos (:commit:`1346037`)

Scrapy 0.22.1 (released 2014-02-08)
-----------------------------------

- localhost666 can resolve under certain circumstances (:commit:`2ec2279`)
### ——localhost666可以解决在某些情况下(承诺:“2 ec2279”)
- test inspect.stack failure (:commit:`cc3eda3`)
### ——测试检查。堆栈失败(承诺:“cc3eda3”)
- Handle cases when inspect.stack() fails (:commit:`8cb44f9`)
### ——处理情况下当inspect.stack()失败(承诺:“8 cb44f9”)
- Fix wrong checks on subclassing of deprecated classes. closes #581 (:commit:`46d98d6`)
### ——修复错误检查弃用类的子类化。关闭# 581(:提交:46 d98d6)
- Docs: 4-space indent for final spider example (:commit:`13846de`)
### 最后蜘蛛的例子- Docs:4空间缩进(提交:13846 de)
- Fix HtmlParserLinkExtractor and tests after #485 merge (:commit:`368a946`)
### - # 485合并后修复HtmlParserLinkExtractor和测试(提交:“368 a946”)
- BaseSgmlLinkExtractor: Fixed the missing space when the link has an inner tag (:commit:`b566388`)
### - BaseSgmlLinkExtractor:固定链接时丢失的空间有一个内在的标签(承诺:“b566388”)
- BaseSgmlLinkExtractor: Added unit test of a link with an inner tag (:commit:`c1cb418`)
### - BaseSgmlLinkExtractor:添加单元测试的链接内标签(承诺:“c1cb418”)
- BaseSgmlLinkExtractor: Fixed unknown_endtag() so that it only set current_link=None when the end tag match the opening tag (:commit:`7e4d627`)
### - BaseSgmlLinkExtractor:固定unknown_endtag(),这样它只设置current_link =没有结束标记时,匹配的开始标记(承诺:“7 e4d627”)
- Fix tests for Travis-CI build (:commit:`76c7e20`)
### ——修复测试Travis-CI构建(提交:“76 c7e20”)
- replace unencodeable codepoints with html entities. fixes #562 and #285 (:commit:`5f87b17`)
### ——取代unencodeable codepoints html实体。修复# 562和# 562(:承诺:“5 f87b17”)
- RegexLinkExtractor: encode URL unicode value when creating Links (:commit:`d0ee545`)
### - RegexLinkExtractor:unicode编码URL值在创建链接(承诺:“d0ee545”)
- Updated the tutorial crawl output with latest output. (:commit:`8da65de`)
### ——更新最新教程爬输出与输出。(承诺:“8 da65de”)
- Updated shell docs with the crawler reference and fixed the actual shell output. (:commit:`875b9ab`)
### ——更新壳与履带引用文档和固定实际壳的输出。(提交:“875 b9ab”)
- PEP8 minor edits. (:commit:`f89efaf`)
### ——PEP8小编辑。(承诺:“f89efaf”)
- Expose current crawler in the scrapy shell. (:commit:`5349cec`)
### ——揭露当前履带scrapy壳。(提交:5349 cec)
- Unused re import and PEP8 minor edits. (:commit:`387f414`)
### ——未使用的导入和PEP8小编辑。(提交:“387 f414”)
- Ignore None's values when using the ItemLoader. (:commit:`0632546`)
### 当使用ItemLoader——忽略这些值。(提交:' 0632546 ')
- DOC Fixed HTTPCACHE_STORAGE typo in the default value which is now Filesystem instead Dbm. (:commit:`cde9a8c`)
### ——医生固定HTTPCACHE_STORAGE错误现在文件系统,而不是Dbm的默认值。(承诺:“cde9a8c”)
- show ubuntu setup instructions as literal code (:commit:`fb5c9c5`)
### ——显示ubuntu设置说明文字代码(承诺:“fb5c9c5”)
- Update Ubuntu installation instructions (:commit:`70fb105`)
### ——更新Ubuntu安装说明(提交:“70 fb105”)
- Merge pull request #550 from stray-leone/patch-1 (:commit:`6f70b6a`)
### ——合并将请求从stray-leone # 550 /补丁1(承诺:“6 f70b6a”)
- modify the version of scrapy ubuntu package (:commit:`725900d`)
### ——修改的版本scrapy ubuntu包(提交:“725900 d”)
- fix 0.22.0 release date (:commit:`af0219a`)
### -修复0.22.0发布日期(:承诺:“af0219a”)
- fix typos in news.rst and remove (not released yet) header (:commit:`b7f58f4`)
### ——修复拼写错误消息。rst和删除(未发布)头(承诺:“b7f58f4”)

Scrapy 0.22.0 (released 2014-01-17)
-----------------------------------

Enhancements
~~~~~~~~~~~~

- [**Backwards incompatible**] Switched HTTPCacheMiddleware backend to filesystem (:issue:`541`)
### -[* *向后不兼容的* *]HTTPCacheMiddleware端转向文件系统(问题:‘541’)
  To restore old backend set `HTTPCACHE_STORAGE` to `scrapy.contrib.httpcache.DbmCacheStorage`
### 恢复旧的后端设置“HTTPCACHE_STORAGE”“scrapy.contrib.httpcache.DbmCacheStorage”
- Proxy \https:// urls using CONNECT method (:issue:`392`, :issue:`397`)
### ——代理\ https:// url使用连接方法(:问题:“392”,:问题:' 397 ')
- Add a middleware to crawl ajax crawleable pages as defined by google (:issue:`343`)
### ——添加一个中间件爬ajax crawleable页面定义的谷歌(问题:‘343’)
- Rename scrapy.spider.BaseSpider to scrapy.spider.Spider (:issue:`510`, :issue:`519`)
### ——重命名scrapy.spider。BaseSpider scrapy.spider。蜘蛛(问题:“510”:问题:' 519 ')
- Selectors register EXSLT namespaces by default (:issue:`472`)
### 选择器注册EXSLT默认名称空间(:问题:‘472’)
- Unify item loaders similar to selectors renaming (:issue:`461`)
### 统一项目加载器类似于选择重命名(:问题:‘461’)
- Make `RFPDupeFilter` class easily subclassable (:issue:`533`)
### ——让“RFPDupeFilter”类容易subclassable(:问题:‘533’)
- Improve test coverage and forthcoming Python 3 support (:issue:`525`)
### 提高测试覆盖率和即将到来的Python 3支持(:问题:‘525’)
- Promote startup info on settings and middleware to INFO level (:issue:`520`)
### ——促进创业信息设置和中间件信息水平(问题:‘520’)
- Support partials in `get_func_args` util (:issue:`506`, issue:`504`)
### -支持泛音的get_func_args util:问题:“506”,问题:' 504 ')
- Allow running indiviual tests via tox (:issue:`503`)
### 托克斯——允许运行indiviual测试通过(问题:‘503’)
- Update extensions ignored by link extractors (:issue:`498`)
### ——更新扩展被链接提取器(:问题:‘498’)
- Add middleware methods to get files/images/thumbs paths (:issue:`490`)
### ——添加中间件方法得到文件/图像/拇指路径(问题:‘490’)
- Improve offsite middleware tests (:issue:`478`)
### ——提高离线中间件测试(:问题:‘478’)
- Add a way to skip default Referer header set by RefererMiddleware (:issue:`475`)
### ——添加一个跳过RefererMiddleware设定的默认引用页头(问题:‘475’)
- Do not send `x-gzip` in default `Accept-Encoding` header (:issue:`469`)
### ——不发送“x-gzip”默认接受编码的头(问题:‘469’)
- Support defining http error handling using settings (:issue:`466`)
### ——支持定义http错误处理使用设置(:问题:‘466’)
- Use modern python idioms wherever you find legacies (:issue:`497`)
### 利用现代python习语无论你找到遗产(:问题:‘497’)
- Improve and correct documentation
### ——完善和正确的文档
  (:issue:`527`, :issue:`524`, :issue:`521`, :issue:`517`, :issue:`512`, :issue:`505`,
### (问题:“527”,:问题:“524”,:问题:“521”,:问题:“517”,:问题:“512”,:问题:“505”,
  :issue:`502`, :issue:`489`, :issue:`465`, :issue:`460`, :issue:`425`, :issue:`536`)
### :问题:“502”:问题:“489”,问题:“465”,:问题:“460”,问题:“425”,:问题:' 536 ')

Fixes
~~~~~

- Update Selector class imports in CrawlSpider template (:issue:`484`)
### ——更新选择器类进口CrawlSpider模板(:问题:‘484’)
- Fix unexistent reference to `engine.slots` (:issue:`464`)
### ——修复不存在引用的引擎。槽”(问题:' 464 ')
- Do not try to call `body_as_unicode()` on a non-TextResponse instance (:issue:`462`)
### ——不要试图调用“body_as_unicode()“non-TextResponse实例(:问题:‘462’)
- Warn when subclassing XPathItemLoader, previously it only warned on
### ——警告当子类化XPathItemLoader,以前只是警告
  instantiation. (:issue:`523`)
- Warn when subclassing XPathSelector, previously it only warned on
### ——警告当子类化XPathSelector,以前只是警告
  instantiation. (:issue:`537`)
- Multiple fixes to memory stats (:issue:`531`, :issue:`530`, :issue:`529`)
### 多个修复内存统计数据(:问题:“531”,:问题:“530”,:问题:' 529 ')
- Fix overriding url in `FormRequest.from_response()` (:issue:`507`)
### -修复”FormRequest.from_response重写url()(问题:‘507’)
- Fix tests runner under pip 1.5 (:issue:`513`)
### ——修复测试运动员在pip 1.5(:问题:‘513’)
- Fix logging error when spider name is unicode (:issue:`479`)
### ——解决日志错误当蜘蛛的名字是unicode(:问题:‘479’)

Scrapy 0.20.2 (released 2013-12-09)
-----------------------------------

- Update CrawlSpider Template with Selector changes (:commit:`6d1457d`)
### ——更新CrawlSpider模板与选择器的变化(承诺:“6 d1457d”)
- fix method name in tutorial. closes GH-480 (:commit:`b4fc359`
### 在教程-修复方法的名字。关闭gh - 480(:承诺:“b4fc359”

Scrapy 0.20.1 (released 2013-11-28)
-----------------------------------

- include_package_data is required to build wheels from published sources (:commit:`5ba1ad5`)
### ——include_package_data需要建立车轮出版来源(承诺:“5 ba1ad5”)
- process_parallel was leaking the failures on its internal deferreds.  closes #458 (:commit:`419a780`)
### ——process_parallel泄漏失败在其内部延迟。关闭# 458(:提交:“419 a780”)

Scrapy 0.20.0 (released 2013-11-08)
-----------------------------------

Enhancements
~~~~~~~~~~~~

- New Selector's API including CSS selectors (:issue:`395` and :issue:`426`),
### 新的选择器的API包括CSS选择器(问题:“395”和:问题:' 426 '),
- Request/Response url/body attributes are now immutable
### ——请求/响应url /身体属性现在不可变的
  (modifying them had been deprecated for a long time)
### (修改已经弃用了很长一段时间)
- :setting:`ITEM_PIPELINES` is now defined as a dict (instead of a list)
### -:设置:“ITEM_PIPELINES”现在是定义为一个dict(而不是列表)
- Sitemap spider can fetch alternate URLs (:issue:`360`)
### -网站地图的蜘蛛能取回备用url(:问题:‘360’)
- `Selector.remove_namespaces()` now remove namespaces from element's attributes. (:issue:`416`)
### ——“Selector.remove_namespaces()“现在删除名称空间元素的属性。(问题:‘416’)
- Paved the road for Python 3.3+ (:issue:`435`, :issue:`436`, :issue:`431`, :issue:`452`)
### ——铺平了道路Python 3.3 +(:问题:“435”,:问题:“436”,:问题:“431”,:问题:' 452 ')
- New item exporter using native python types with nesting support (:issue:`366`)
### ——新产品出口国使用本机python类型,并支持嵌套(问题:‘366’)
- Tune HTTP1.1 pool size so it matches concurrency defined by settings (:commit:`b43b5f575`)
### ——优化HTTP1.1池大小所以匹配并发性定义为设置(承诺:“b43b5f575”)
- scrapy.mail.MailSender now can connect over TLS or upgrade using STARTTLS (:issue:`327`)
### ——scrapy.mail。MailSender现在可以连接在TLS或升级使用STARTTLS(问题:‘327’)
- New FilesPipeline with functionality factored out from ImagesPipeline (:issue:`370`, :issue:`409`)
### ——新FilesPipeline功能分解从ImagesPipeline(:问题:“370”,:问题:' 409 ')
- Recommend Pillow instead of PIL for image handling (:issue:`317`)
### ——推荐枕头而不是公益诉讼为图像处理(问题:' 317 ')
- Added debian packages for Ubuntu quantal and raring (:commit:`86230c0`)
### 增加了对Ubuntu量子和渴望的debian软件包(承诺:“86230 c0”)
- Mock server (used for tests) can listen for HTTPS requests (:issue:`410`)
### 模拟服务器(用于测试)可以监听HTTPS请求(问题:‘410’)
- Remove multi spider support from multiple core components
### ——删除多蜘蛛从多个核心组件的支持
  (:issue:`422`, :issue:`421`, :issue:`420`, :issue:`419`, :issue:`423`, :issue:`418`)
### (问题:“422”,:问题:“421”,:问题:“420”,:问题:“419”,:问题:“423”,:问题:' 418 ')
- Travis-CI now tests Scrapy changes against development versions of `w3lib` and `queuelib` python packages.
### ——Travis-CI现在测试Scrapy变化对开发版本的“w3lib”和“queuelib”python包。
- Add pypy 2.1 to continuous integration tests (:commit:`ecfa7431`)
### ——添加pypy 2.1持续集成测试(承诺:“ecfa7431”)
- Pylinted, pep8 and removed old-style exceptions from source (:issue:`430`, :issue:`432`)
### ——Pylinted pep8和移除旧式异常从源(:问题:“430”,:问题:' 432 ')
- Use importlib for parametric imports (:issue:`445`)
### -使用importlib进口参数(:问题:‘445’)
- Handle a regression introduced in Python 2.7.5 that affects XmlItemExporter (:issue:`372`)
### ——处理回归了Python 2.7.5影响XmlItemExporter(问题:‘372’)
- Bugfix crawling shutdown on SIGINT (:issue:`450`)
### ——错误修复爬行关闭信号情报(:问题:‘450’)
- Do not submit `reset` type inputs in FormRequest.from_response (:commit:`b326b87`)
### ——不要在FormRequest提交“重置”类型的输入。from_response(承诺:“b326b87”)
- Do not silence download errors when request errback raises an exception (:commit:`684cfc0`)
### ——不沉默下载错误当请求errback引发了异常(提交:“684 cfc0”)

Bugfixes
~~~~~~~~

- Fix tests under Django 1.6 (:commit:`b6bed44c`)
### ——修复测试在Django 1.6(承诺:“b6bed44c”)
- Lot of bugfixes to retry middleware under disconnections using HTTP 1.1 download handler
### ——许多修正重试中间件在断开连接使用HTTP 1.1处理程序下载
- Fix inconsistencies among Twisted releases (:issue:`406`)
### ——解决之间的矛盾扭曲版本(:问题:‘406’)
- Fix scrapy shell bugs (:issue:`418`, :issue:`407`)
### 修复bug scrapy壳(:问题:“418”,:问题:' 407 ')
- Fix invalid variable name in setup.py (:issue:`429`)
### ——修复无效的设置变量名。py(问题:‘429’)
- Fix tutorial references (:issue:`387`)
### ——修复教程引用(:问题:‘387’)
- Improve request-response docs (:issue:`391`)
### -改善请求-响应文档(:问题:‘391’)
- Improve best practices docs (:issue:`399`, :issue:`400`, :issue:`401`, :issue:`402`)
### -改善最佳实践文档(:问题:“399”,:问题:“400”,:问题:“401”,:问题:' 402 ')
- Improve django integration docs (:issue:`404`)
### ——提高django集成文档(:问题:‘404’)
- Document `bindaddress` request meta (:commit:`37c24e01d7`)
### ——文档“bindaddress”请求元(承诺:“37 c24e01d7”)
- Improve `Request` class documentation (:issue:`226`)
### ——提高“请求”类文档(:问题:‘226’)

Other
~~~~~

- Dropped Python 2.6 support (:issue:`448`)
### Python 2.6支持下降(:问题:‘448’)
- Add `cssselect`_ python package as install dependency
### ——添加“cssselect”_ python安装依赖包
- Drop libxml2 and multi selector's backend support, `lxml`_ is required from now on.
### ——下降libxml2和多选择器的后端支持,lxml的_是必需的。
- Minimum Twisted version increased to 10.0.0, dropped Twisted 8.0 support.
### 最低版本增加10.0.0扭曲,扭曲的8.0支持下降。
- Running test suite now requires `mock` python library (:issue:`390`)
### ——运行测试套件现在要求“模拟”python库(问题:‘390’)


Thanks
~~~~~~

Thanks to everyone who contribute to this release!
### 感谢每一位为这个版本!

List of contributors sorted by number of commits::
### 列表排序的贡献者的数量提交:

     69 Daniel Graña <dangra@...>
     37 Pablo Hoffman <pablo@...>
     13 Mikhail Korobov <kmike84@...>
      9 Alex Cepoi <alex.cepoi@...>
      9 alexanderlukanin13 <alexander.lukanin.13@...>
      8 Rolando Espinoza La fuente <darkrho@...>
### 8除了Espinoza源darkrho@…> <
      8 Lukasz Biedrycki <lukasz.biedrycki@...>
      6 Nicolas Ramirez <nramirez.uy@...>
      3 Paul Tremberth <paul.tremberth@...>
      2 Martin Olveyra <molveyra@...>
      2 Stefan <misc@...>
      2 Rolando Espinoza <darkrho@...>
      2 Loren Davie <loren@...>
      2 irgmedeiros <irgmedeiros@...>
      1 Stefan Koch <taikano@...>
      1 Stefan <cct@...>
      1 scraperdragon <dragon@...>
      1 Kumara Tharmalingam <ktharmal@...>
      1 Francesco Piccinno <stack.box@...>
      1 Marcos Campal <duendex@...>
      1 Dragon Dave <dragon@...>
      1 Capi Etheriel <barraponto@...>
      1 cacovsky <amarquesferraz@...>
      1 Berend Iwema <berend@...>

Scrapy 0.18.4 (released 2013-10-10)
-----------------------------------

- IPython refuses to update the namespace. fix #396 (:commit:`3d32c4f`)
### ——IPython拒绝更新名称空间。解决# 396(:提交:“3 d32c4f”)
- Fix AlreadyCalledError replacing a request in shell command. closes #407 (:commit:`b1d8919`)
### ——修复AlreadyCalledError取代在shell命令请求。关闭# 407(:提交:“b1d8919”)
- Fix start_requests laziness and early hangs (:commit:`89faf52`)
### ——修复start_requests懒惰和早期挂(提交:“89 faf52”)

Scrapy 0.18.3 (released 2013-10-03)
-----------------------------------

- fix regression on lazy evaluation of start requests (:commit:`12693a5`)
### ——修复回归懒惰开始评估请求(提交:12693 a5)
- forms: do not submit reset inputs (:commit:`e429f63`)
### ——形式:不提交复位输入(承诺:“e429f63”)
- increase unittest timeouts to decrease travis false positive failures (:commit:`912202e`)
### ——增加unittest超时减少特拉维斯假阳性失败(提交:912202 e)
- backport master fixes to json exporter (:commit:`cfc2d46`)
### 补丁修复大师json出口国(承诺:“cfc2d46”)
- Fix permission and set umask before generating sdist tarball (:commit:`06149e0`)
### ——修复权限和设置umask之前生成sdist tarball(提交:06149 e0)

Scrapy 0.18.2 (released 2013-09-03)
-----------------------------------

- Backport `scrapy check` command fixes and backward compatible multi
### ——补丁“scrapy检查”命令修复和向后兼容的多
  crawler process(:issue:`339`)

Scrapy 0.18.1 (released 2013-08-27)
-----------------------------------

- remove extra import added by cherry picked changes (:commit:`d20304e`)
### ——删除添加的额外进口樱桃采摘的变化(承诺:“d20304e”)
- fix crawling tests under twisted pre 11.0.0 (:commit:`1994f38`)
### ——修复爬行测试下扭曲pre 11.0.0(提交:“1994 f38”)
- py26 can not format zero length fields {} (:commit:`abf756f`)
### ——py26不能零长度字段格式{ }(承诺:“abf756f”)
- test PotentiaDataLoss errors on unbound responses (:commit:`b15470d`)
### ——测试PotentiaDataLoss错误的反应(承诺:“b15470d”)
- Treat responses without content-length or Transfer-Encoding as good responses (:commit:`c4bf324`)
### ——治疗反应没有内容长度或传输编码好的反应(承诺:“c4bf324”)
- do no include ResponseFailed if http11 handler is not enabled (:commit:`6cbe684`)
### ——不包括ResponseFailed如果http11处理器不启用(承诺:“6 cbe684”)
- New HTTP client wraps connection losts in ResponseFailed exception. fix #373 (:commit:`1a20bba`)
### ——新的HTTP客户端封装连接丢失ResponseFailed例外。解决# 373(:提交:1 a20bba)
- limit travis-ci build matrix (:commit:`3b01bb8`)
### ——限制travis-ci构建矩阵(承诺:“3 b01bb8”)
- Merge pull request #375 from peterarenot/patch-1 (:commit:`fa766d7`)
### ——合并将请求从peterarenot # 375 /补丁1(承诺:“fa766d7”)
- Fixed so it refers to the correct folder (:commit:`3283809`)
### ——固定所以它是指正确的文件夹(提交:' 3283809 ')
- added quantal & raring to support ubuntu releases (:commit:`1411923`)
### ——增加了量子&渴望支持ubuntu版本(提交:' 1411923 ')
- fix retry middleware which didn't retry certain connection errors after the upgrade to http1 client, closes GH-373 (:commit:`bb35ed0`)
### ——修复重试中间件不重试一定升级到http1后端连接错误,关闭gh - 373(:提交:“bb35ed0”)
- fix XmlItemExporter in Python 2.7.4 and 2.7.5 (:commit:`de3e451`)
### -修复第2.7.4 XmlItemExporter在Python和2.7.5(承诺:“de3e451”)
- minor updates to 0.18 release notes (:commit:`c45e5f1`)
### ——小更新0.18发行说明(承诺:“c45e5f1”)
- fix contributters list format (:commit:`0b60031`)
### ——修复contributters列表格式(承诺:“0 b60031”)

Scrapy 0.18.0 (released 2013-08-09)
-----------------------------------

- Lot of improvements to testsuite run using Tox, including a way to test on pypi
### 托克斯——很多改进testsuite运行使用,包括在pypi上测试的一种方法
- Handle GET parameters for AJAX crawleable urls (:commit:`3fe2a32`)
### ——处理参数对AJAX crawleable url(承诺:“3 fe2a32”)
- Use lxml recover option to parse sitemaps (:issue:`347`)
### -使用lxml恢复选项解析站点地图(:问题:‘347’)
- Bugfix cookie merging by hostname and not by netloc (:issue:`352`)
### ——错误修复饼干合并由主机名和不是netloc(问题:‘352’)
- Support disabling `HttpCompressionMiddleware` using a flag setting (:issue:`359`)
### ——支持禁用“HttpCompressionMiddleware”使用国旗设置(问题:‘359’)
- Support xml namespaces using `iternodes` parser in `XMLFeedSpider` (:issue:`12`)
### ——支持xml名称空间使用“iternodes”解析器在“XMLFeedSpider”(问题:“12”)
- Support `dont_cache` request meta flag (:issue:`19`)
### ——支持“dont_cache”请求meta标记(问题:“19”)
- Bugfix `scrapy.utils.gz.gunzip` broken by changes in python 2.7.4 (:commit:`4dc76e`)
### ——错误修复”scrapy.utils.gz。(第2.7.4 gunzip”打破了python的变化:提交:“4 dc76e”)
- Bugfix url encoding on `SgmlLinkExtractor` (:issue:`24`)
### ——修复bug url编码“SgmlLinkExtractor”(问题:“24”)
- Bugfix `TakeFirst` processor shouldn't discard zero (0) value (:issue:`59`)
### ——错误修复“TakeFirst”处理器不应该丢弃零(0)值(问题:“59”)
- Support nested items in xml exporter (:issue:`66`)
### -支持嵌套在xml出口国(:问题:‘66’)
- Improve cookies handling performance (:issue:`77`)
### -提高饼干处理性能(:问题:‘77’)
- Log dupe filtered requests once (:issue:`105`)
### ——记录欺骗过滤请求一次(:问题:‘105’)
- Split redirection middleware into status and meta based middlewares (:issue:`78`)
### ——重定向中间件分割成地位和元基础中间件)(问题:‘78’)
- Use HTTP1.1 as default downloader handler (:issue:`109` and :issue:`318`)
### ——使用HTTP1.1作为默认下载工具处理程序(问题:“109”和:问题:' 318 ')
- Support xpath form selection on `FormRequest.from_response` (:issue:`185`)
### ——支持xpath选择“FormRequest形式。from_response '(:问题:‘185’)
- Bugfix unicode decoding error on `SgmlLinkExtractor` (:issue:`199`)
### ——错误修复unicode解码错误“SgmlLinkExtractor”(问题:' 199 ')
- Bugfix signal dispatching on pypi interpreter (:issue:`205`)
### ——错误修复信号调度在pypi解释器(问题:‘205’)
- Improve request delay and concurrency handling (:issue:`206`)
### -改进请求延迟和并发处理(问题:' 206 ')
- Add RFC2616 cache policy to `HttpCacheMiddleware` (:issue:`212`)
### ——添加RFC2616缓存策略“HttpCacheMiddleware”(问题:' 212 ')
- Allow customization of messages logged by engine (:issue:`214`)
### 由发动机——允许定制的消息记录(问题:' 214 ')
- Multiples improvements to `DjangoItem` (:issue:`217`, :issue:`218`, :issue:`221`)
### -改善DjangoItem的倍数(:问题:“217”,:问题:“218”,:问题:' 221 ')
- Extend Scrapy commands using setuptools entry points (:issue:`260`)
### ——扩展Scrapy命令使用setuptools入口点(:问题:‘260’)
- Allow spider `allowed_domains` value to be set/tuple (:issue:`261`)
### ——允许蜘蛛“allowed_domains”值设置/元组(问题:‘261’)
- Support `settings.getdict` (:issue:`269`)
- Simplify internal `scrapy.core.scraper` slot handling (:issue:`271`)
### ——简化内部scrapy.core。刮板的槽处理(问题:' 271 ')
- Added `Item.copy` (:issue:`290`)
- Collect idle downloader slots (:issue:`297`)
### -收集闲置下载插槽(:问题:‘297’)
- Add `ftp://` scheme downloader handler (:issue:`329`)
### 添加“ftp://”方案下载处理程序(:问题:‘329’)
- Added downloader benchmark webserver and spider tools :ref:`benchmarking`
### ——添加下载基准网络服务器和蜘蛛工具:裁判:“基准”
- Moved persistent (on disk) queues to a separate project (queuelib_) which scrapy now depends on
### ——持续的(在磁盘上)队列转移到一个单独的项目(queuelib_)scrapy现在取决于
- Add scrapy commands using external libraries (:issue:`260`)
### 使用外部库添加scrapy命令(:问题:‘260’)
- Added ``--pdb`` option to ``scrapy`` command line tool
### ——“——pdb ' '选项添加到“scrapy“命令行工具
- Added :meth:`XPathSelector.remove_namespaces` which allows to remove all namespaces from XML documents for convenience (to work with namespace-less XPaths). Documented in :ref:`topics-selectors`.
### ——补充道:冰毒:“XPathSelector。remove_namespaces”,允许从XML文档删除所有名称空间为了方便(与namespace-less xpath)。记录在:裁判:“topics-selectors”。
- Several improvements to spider contracts
### ——改进蜘蛛合同
- New default middleware named MetaRefreshMiddldeware that handles meta-refresh html tag redirections,
### ——新的默认名为MetaRefreshMiddldeware的中间件,处理元刷新html标签重定向,
- MetaRefreshMiddldeware and RedirectMiddleware have different priorities to address #62
### ——MetaRefreshMiddldeware和RedirectMiddleware解决# 62有不同的优先级
- added from_crawler method to spiders
### ——添加from_crawler蜘蛛的方法
- added system tests with mock server
### ——添加系统测试与模拟服务器
- more improvements to Mac OS compatibility (thanks Alex Cepoi)
### ——更多的改进Mac OS兼容性(感谢亚历克斯Cepoi)
- several more cleanups to singletons and multi-spider support (thanks Nicolas Ramirez)
### ——几个清理单件和multi-spider支持(感谢尼古拉斯·拉米雷斯)
- support custom download slots
### ——支持自定义下载插槽
- added --spider option to "shell" command.
### ————蜘蛛选项添加到“壳”命令。
- log overridden settings when scrapy starts
### ——日志scrapy启动时设置覆盖

Thanks to everyone who contribute to this release. Here is a list of
### 感谢每一位为这个版本。这是一个列表
contributors sorted by number of commits::
### 贡献者排序的数量提交:

    130 Pablo Hoffman <pablo@...>
     97 Daniel Graña <dangra@...>
     20 Nicolás Ramírez <nramirez.uy@...>
     13 Mikhail Korobov <kmike84@...>
     12 Pedro Faustino <pedrobandim@...>
     11 Steven Almeroth <sroth77@...>
      5 Rolando Espinoza La fuente <darkrho@...>
### 5人darkrho@ Espinoza源< >……
      4 Michal Danilak <mimino.coder@...>
      4 Alex Cepoi <alex.cepoi@...>
      4 Alexandr N Zamaraev (aka tonal) <tonal@...>
### 4 Alexandr Zamaraev N)< tonal@(aka调性的... >
      3 paul <paul.tremberth@...>
      3 Martin Olveyra <molveyra@...>
      3 Jordi Llonch <llonchj@...>
      3 arijitchakraborty <myself.arijit@...>
      2 Shane Evans <shane.evans@...>
      2 joehillen <joehillen@...>
      2 Hart <HartSimha@...>
      2 Dan <ellisd23@...>
      1 Zuhao Wan <wanzuhao@...>
      1 whodatninja <blake@...>
      1 vkrest <v.krestiannykov@...>
      1 tpeng <pengtaoo@...>
      1 Tom Mortimer-Jones <tom@...>
      1 Rocio Aramberri <roschegel@...>
      1 Pedro <pedro@...>
      1 notsobad <wangxiaohugg@...>
      1 Natan L <kuyanatan.nlao@...>
      1 Mark Grey <mark.grey@...>
      1 Luan <luanpab@...>
      1 Libor Nenadál <libor.nenadal@...>
      1 Juan M Uys <opyate@...>
### 1 Uys < opyate@胡安·M ... >
      1 Jonas Brunsgaard <jonas.brunsgaard@...>
      1 Ilya Baryshev <baryshev@...>
      1 Hasnain Lakhani <m.hasnain.lakhani@...>
      1 Emanuel Schorsch <emschorsch@...>
      1 Chris Tilden <chris.tilden@...>
      1 Capi Etheriel <barraponto@...>
      1 cacovsky <amarquesferraz@...>
      1 Berend Iwema <berend@...>


Scrapy 0.16.5 (released 2013-05-30)
-----------------------------------

- obey request method when scrapy deploy is redirected to a new endpoint (:commit:`8c4fcee`)
### ——遵守请求方法当scrapy部署被重定向到一个新的端点(承诺:“8 c4fcee”)
- fix inaccurate downloader middleware documentation. refs #280 (:commit:`40667cb`)
### ——修复不准确的中间件文档下载器。参考文献# 280(:提交:40667 cb)
- doc: remove links to diveintopython.org, which is no longer available. closes #246 (:commit:`bd58bfa`)
### - doc:删除链接diveintopython.org,这是不再可用。关闭# 246(:提交:“bd58bfa”)
- Find form nodes in invalid html5 documents (:commit:`e3d6945`)
### ——找到表单无效的html5文档中的节点(承诺:“e3d6945”)
- Fix typo labeling attrs type bool instead of list (:commit:`a274276`)
### ——修复错误标签attrs bool类型而不是列表(承诺:“a274276”)

Scrapy 0.16.4 (released 2013-01-23)
-----------------------------------

- fixes spelling errors in documentation (:commit:`6d2b3aa`)
### ——修复拼写错误文档(承诺:“6 d2b3aa”)
- add doc about disabling an extension. refs #132 (:commit:`c90de33`)
### ——添加文档禁用一个扩展。参考文献# 132(:提交:“c90de33”)
- Fixed error message formatting. log.err() doesn't support cool formatting and when error occurred, the message was:    "ERROR: Error processing %(item)s" (:commit:`c16150c`)
### ——固定错误消息格式。log.err()不支持酷格式化错误发生时,该消息是:“错误:错误处理%(项)”(承诺:“c16150c”)
- lint and improve images pipeline error logging (:commit:`56b45fc`)
### 线头和改善图像管道错误日志(承诺:“56 b45fc”)
- fixed doc typos (:commit:`243be84`)
### 固定的医生输入错误(提交:“243 be84”)
- add documentation topics: Broad Crawls & Common Practies (:commit:`1fbb715`)
### ——添加文档主题:广泛的爬行和常见Practies(提交:1 fbb715)
- fix bug in scrapy parse command when spider is not specified explicitly. closes #209 (:commit:`c72e682`)
### ——修复bug scrapy解析命令当蜘蛛没有显式地指定。关闭# 209(:提交:“c72e682”)
- Update docs/topics/commands.rst (:commit:`28eac7a`)

Scrapy 0.16.3 (released 2012-12-07)
-----------------------------------

- Remove concurrency limitation when using download delays and still ensure inter-request delays are enforced (:commit:`487b9b5`)
### ——删除并发限制仍在使用下载延迟和确保inter-request延迟执行(提交:“487 b9b5”)
- add error details when image pipeline fails (:commit:`8232569`)
### ——添加错误细节图像管道失败时(提交:' 8232569 ')
- improve mac os compatibility (:commit:`8dcf8aa`)
### -提高mac os兼容性(承诺:“8 dcf8aa”)
- setup.py: use README.rst to populate long_description (:commit:`7b5310d`)
### ——设置。py:使用README。rst填充long_description(承诺:“7 b5310d”)
- doc: removed obsolete references to ClientForm (:commit:`80f9bb6`)
### - doc:删除过时的引用ClientForm(提交:“80 f9bb6”)
- correct docs for default storage backend (:commit:`2aa491b`)
### ——正确的文档默认存储后端(承诺:“2 aa491b”)
- doc: removed broken proxyhub link from FAQ (:commit:`bdf61c4`)
### - doc:删除打破proxyhub链接从FAQ(承诺:“bdf61c4”)
- Fixed docs typo in SpiderOpenCloseLogging example (:commit:`7184094`)
### ——固定文档错误SpiderOpenCloseLogging(例子:提交:' 7184094 ')


Scrapy 0.16.2 (released 2012-11-09)
-----------------------------------

- scrapy contracts: python2.6 compat (:commit:`a4a9199`)
### - scrapy合同:python2.6兼容(承诺:“a4a9199”)
- scrapy contracts verbose option (:commit:`ec41673`)
### ——scrapy合同详细选项(承诺:“ec41673”)
- proper unittest-like output for scrapy contracts (:commit:`86635e4`)
### ——适当unittest-like输出scrapy合同(提交:86635 e4的)
- added open_in_browser to debugging doc (:commit:`c9b690d`)
### ——添加open_in_browser调试文档(承诺:“c9b690d”)
- removed reference to global scrapy stats from settings doc (:commit:`dd55067`)
### -删除引用全球scrapy统计设置doc(承诺:“dd55067”)
- Fix SpiderState bug in Windows platforms (:commit:`58998f4`)
### ——修复SpiderState bug在Windows平台(提交:58998 f4)


Scrapy 0.16.1 (released 2012-10-26)
-----------------------------------

- fixed LogStats extension, which got broken after a wrong merge before the 0.16 release (:commit:`8c780fd`)
### -固定LogStats扩展,弄错了破碎后合并前的0.16版(承诺:“8 c780fd”)
- better backwards compatibility for scrapy.conf.settings (:commit:`3403089`)
### ——scrapy.conf更好的向后兼容性。设置(提交:' 3403089 ')
- extended documentation on how to access crawler stats from extensions (:commit:`c4da0b5`)
### ——扩展文档如何从扩展访问履带统计数据(提交:“c4da0b5”)
- removed .hgtags (no longer needed now that scrapy uses git) (:commit:`d52c188`)
### ——删除。hgtags(现在不再需要scrapy使用git)(:提交:“d52c188”)
- fix dashes under rst headers (:commit:`fa4f7f9`)
### - rst头下修复破折号(承诺:“fa4f7f9”)
- set release date for 0.16.0 in news (:commit:`e292246`)
### -制定0.16.0新闻发布日期(承诺:“e292246”)


Scrapy 0.16.0 (released 2012-10-18)
-----------------------------------

Scrapy changes:

- added :ref:`topics-contracts`, a mechanism for testing spiders in a formal/reproducible way
### ——补充说:裁判:“topics-contracts”,测试蜘蛛在一个正式的/可再生的机制
- added options ``-o`` and ``-t`` to the :command:`runspider` command
### ——添加选项“- o ' '和' ' - t ' ':命令:“runspider”命令
- documented :doc:`topics/autothrottle` and added to extensions installed by default. You still need to enable it with :setting:`AUTOTHROTTLE_ENABLED`
### ——记录:医生:“主题/自动油门”和添加到扩展默认安装。你仍然需要启用:设置:“AUTOTHROTTLE_ENABLED”
- major Stats Collection refactoring: removed separation of global/per-spider stats, removed stats-related signals (``stats_spider_opened``, etc). Stats are much simpler now, backwards compatibility is kept on the Stats Collector API and signals.
### ——主要统计数据收集重构:全球/ per-spider分离数据,删除stats-related信号(“stats_spider_opened ' ',等等)。统计现在简单多了,向后兼容性是保存在数据收集器API和信号。
- added :meth:`~scrapy.contrib.spidermiddleware.SpiderMiddleware.process_start_requests` method to spider middlewares
### ——补充道:甲:“~ scrapy.contrib.spidermiddleware.SpiderMiddleware。process_start_requests蜘蛛中间件)的方法
- dropped Signals singleton. Signals should now be accesed through the Crawler.signals attribute. See the signals documentation for more info.
### ——单例下降信号。现在应该通过履带accesed信号。信号属性。看到信号文档了解更多信息。
- dropped Signals singleton. Signals should now be accesed through the Crawler.signals attribute. See the signals documentation for more info.
### ——单例下降信号。现在应该通过履带accesed信号。信号属性。看到信号文档了解更多信息。
- dropped Stats Collector singleton. Stats can now be accessed through the Crawler.stats attribute. See the stats collection documentation for more info.
### ——数据收集器singleton下降。数据现在可以通过爬虫访问。统计属性。看到统计数据收集文档了解更多信息。
- documented :ref:`topics-api`
- `lxml` is now the default selectors backend instead of `libxml2`
### ——“lxml”现在是默认选择器的后端,而不是“libxml2”
- ported FormRequest.from_response() to use `lxml`_ instead of `ClientForm`_
### -移植FormRequest.from_response()使用lxml的_而不是ClientForm _
- removed modules: ``scrapy.xlib.BeautifulSoup`` and ``scrapy.xlib.ClientForm``
### -删除模块:“scrapy.xlib。BeautifulSoup‘’和‘’scrapy.xlib.ClientForm ' '
- SitemapSpider: added support for sitemap urls ending in .xml and .xml.gz, even if they advertise a wrong content type (:commit:`10ed28b`)
### - SitemapSpider:添加支持站点url的结局。xml和xml。广州,即使他们宣传一个错误的内容类型(承诺:“10 ed28b”)
- StackTraceDump extension: also dump trackref live references (:commit:`fe2ce93`)
### - StackTraceDump扩展:还转储trackref住引用(承诺:“fe2ce93”)
- nested items now fully supported in JSON and JSONLines exporters
### ——嵌套物品现在完全支持JSON和JSONLines出口商
- added :reqmeta:`cookiejar` Request meta key to support multiple cookie sessions per spider
### ——补充道:reqmeta:“cookiejar”请求支持多个meta关键cookie会话/蜘蛛
- decoupled encoding detection code to `w3lib.encoding`_, and ported Scrapy code to use that module
### “w3lib -解耦编码检测代码。编码的_,移植Scrapy代码使用这个模块
- dropped support for Python 2.5. See https://blog.scrapinghub.com/2012/02/27/scrapy-0-15-dropping-support-for-python-2-5/
### ——支持Python 2.5下降。参见https://blog.scrapinghub.com/2012/02/27/scrapy-0-15-dropping-support-for-python-2-5/
- dropped support for Twisted 2.5
### ——支持扭曲的2.5下降
- added :setting:`REFERER_ENABLED` setting, to control referer middleware
### ——补充道:设置:“REFERER_ENABLED”设置,控制推荐人中间件
- changed default user agent to: ``Scrapy/VERSION (+http://scrapy.org)``
### ——默认用户代理改为:“Scrapy /版本(+ http://scrapy.org)'
- removed (undocumented) ``HTMLImageLinkExtractor`` class from ``scrapy.contrib.linkextractors.image``
### -删除(无证)“HTMLImageLinkExtractor从' ' ' '类scrapy.contrib.linkextractors.image ' '
- removed per-spider settings (to be replaced by instantiating multiple crawler objects)
### -删除per-spider设置(取而代之的是实例化多个爬虫对象)
- ``USER_AGENT`` spider attribute will no longer work, use ``user_agent`` attribute instead
### ——“USER_AGENT“蜘蛛属性将不再工作,使用“USER_AGENT“属性
- ``DOWNLOAD_TIMEOUT`` spider attribute will no longer work, use ``download_timeout`` attribute instead
### ——“DOWNLOAD_TIMEOUT“蜘蛛属性将不再工作,使用“DOWNLOAD_TIMEOUT“属性
- removed ``ENCODING_ALIASES`` setting, as encoding auto-detection has been moved to the `w3lib`_ library
### -删除“ENCODING_ALIASES“设置,如编码自动识别已搬到w3lib _图书馆
- promoted :ref:`topics-djangoitem` to main contrib
### -提升:裁判:“topics-djangoitem”主要普通发布版
- LogFormatter method now return dicts(instead of strings) to support lazy formatting (:issue:`164`, :commit:`dcef7b0`)
### ——LogFormatter方法现在返回字典(而不是字符串)来支持懒惰格式化(:问题:“164”,:提交:“dcef7b0”)
- downloader handlers (:setting:`DOWNLOAD_HANDLERS` setting) now receive settings as the first argument of the constructor
### ——下载处理程序(设置:“DOWNLOAD_HANDLERS”设置)现在接收设置作为构造函数的第一个参数
- replaced memory usage acounting with (more portable) `resource`_ module, removed ``scrapy.utils.memory`` module
### ——更换内存使用情况进行统计(便携式)_“资源”模块,“scrapy.utils删除。记忆的模块
- removed signal: ``scrapy.mail.mail_sent``
- removed ``TRACK_REFS`` setting, now :ref:`trackrefs <topics-leaks-trackrefs>` is always enabled
### -删除“TRACK_REFS“设置,现在:裁判:“trackrefs < topics-leaks-trackrefs >”总是启用
- DBM is now the default storage backend for HTTP cache middleware
### - DBM现在HTTP缓存的默认存储后端的中间件
- number of log messages (per level) are now tracked through Scrapy stats (stat name: ``log_count/LEVEL``)
### 日志消息的数量(每级)现在跟踪通过Scrapy统计(统计的名字:“log_count /级别' ')
- number received responses are now tracked through Scrapy stats (stat name: ``response_received_count``)
### ——通过Scrapy现在收到响应跟踪数量统计(统计的名字:“response_received_count ' ')
- removed ``scrapy.log.started`` attribute

Scrapy 0.14.4
-------------

- added precise to supported ubuntu distros (:commit:`b7e46df`)
### ——添加精确支持ubuntu发行版(承诺:“b7e46df”)
- fixed bug in json-rpc webservice reported in https://groups.google.com/forum/#!topic/scrapy-users/qgVBmFybNAQ/discussion. also removed no longer supported 'run' command from extras/scrapy-ws.py (:commit:`340fbdb`)
### json - rpc webservice -固定错误报告在https://groups.google.com/forum/ # ! / scrapy-users / qgVBmFybNAQ /讨论主题。也将不再支持“运行”命令从临时演员/ scrapy-ws。py(提交:“340 fbdb”)
- meta tag attributes for content-type http equiv can be in any order. #123 (:commit:`0cb68af`)
### - meta标签属性内容类型的http枚可以以任何顺序。# 123(:提交:“0 cb68af”)
- replace "import Image" by more standard "from PIL import Image". closes #88 (:commit:`4d17048`)
### ——取代“导入形象”“从公益诉讼导入形象”的标准。关闭# 88(:提交:“4 d17048”)
- return trial status as bin/runtests.sh exit value. #118 (:commit:`b7b2e7f`)
### - bin / runtests返回试验状态。上海出口的价值。# 118(:提交:“b7b2e7f”)

Scrapy 0.14.3
-------------

- forgot to include pydispatch license. #118 (:commit:`fd85f9c`)
### ——忘了包括pydispatch许可证。# 118(:提交:“fd85f9c”)
- include egg files used by testsuite in source distribution. #118 (:commit:`c897793`)
### —包括testsuite in彩蛋files说明来源加以分发。第118(#:c897793 ! ! ! !)双赢的:
- update docstring in project template to avoid confusion with genspider command, which may be considered as an advanced feature. refs #107 (:commit:`2548dcc`)
### ——docstring更新项目模板与genspider命令避免混淆,这可能被认为是一个先进的特性。参考文献# 107(:提交:2548年大同)
- added note to docs/topics/firebug.rst about google directory being shut down (:commit:`668e352`)
### ——注意添加到文档/主题/ firebug。rst关于谷歌目录被关闭(提交:“668 e352”)
- dont discard slot when empty, just save in another dict in order to recycle if needed again. (:commit:`8e9f607`)
### ——不该丢弃时槽空,只是保存在另一个东西如果需要为了回收了。(承诺:“8 e9f607”)
- do not fail handling unicode xpaths in libxml2 backed selectors (:commit:`b830e95`)
### ——不失败处理unicode xpath libxml2支持选择器(承诺:“b830e95”)
- fixed minor mistake in Request objects documentation (:commit:`bf3c9ee`)
### ——请求对象中的固定小错误文档(承诺:“bf3c9ee”)
- fixed minor defect in link extractors documentation (:commit:`ba14f38`)
### :固定小瑕疵链接提取文档(承诺:“ba14f38”)
- removed some obsolete remaining code related to sqlite support in scrapy (:commit:`0665175`)
### sqlite -删除一些过时的剩余代码相关的支持scrapy(提交:' 0665175 ')

Scrapy 0.14.2
-------------

- move buffer pointing to start of file before computing checksum. refs #92 (:commit:`6a5bef2`)
### ——移动缓冲指向之前开始的文件计算校验和。参考文献# 92(:提交:“6 a5bef2”)
- Compute image checksum before persisting images. closes #92 (:commit:`9817df1`)
### ——计算校验和持久化之前图片形象。关闭# 92(:提交:9817 df1)
- remove leaking references in cached failures (:commit:`673a120`)
### ——删除缓存中的泄漏引用故障(提交:“673 a120”)
- fixed bug in MemoryUsage extension: get_engine_status() takes exactly 1 argument (0 given) (:commit:`11133e9`)
### ——固定错误MemoryUsage扩展:get_engine_status()接受完全1参数(0)(:提交:“11133 e9”)
- fixed struct.error on http compression middleware. closes #87 (:commit:`1423140`)
### ——固定结构。误差在http压缩中间件。关闭# 87(:提交:' 1423140 ')
- ajax crawling wasn't expanding for unicode urls (:commit:`0de3fb4`)
### ajax不是膨胀的抓取unicode url(提交:“0 de3fb4”)
- Catch start_requests iterator errors. refs #83 (:commit:`454a21d`)
### ——抓住start_requests迭代器错误。参考文献# 83(:提交:“454 a21d”)
- Speed-up libxml2 XPathSelector (:commit:`2fbd662`)
### 加速libxml2 XPathSelector(承诺:“2 fbd662”)
- updated versioning doc according to recent changes (:commit:`0a070f5`)
### ——根据最近的变化更新版本文档(承诺:“0 a070f5”)
- scrapyd: fixed documentation link (:commit:`2b4e4c3`)
### - scrapyd:固定文档链接(承诺:“2 b4e4c3”)
- extras/makedeb.py: no longer obtaining version from git (:commit:`caffe0e`)
### -附加/ makedeb。py:不再从git获取版本(承诺:“caffe0e”)

Scrapy 0.14.1
-------------

- extras/makedeb.py: no longer obtaining version from git (:commit:`caffe0e`)
### -附加/ makedeb。py:不再从git获取版本(承诺:“caffe0e”)
- bumped version to 0.14.1 (:commit:`6cb9e1c`)
### ——撞版0.14.1(承诺:“6 cb9e1c”)
- fixed reference to tutorial directory (:commit:`4b86bd6`)
### 固定参考教程目录(承诺:“4 b86bd6”)
- doc: removed duplicated callback argument from Request.replace() (:commit:`1aeccdd`)
### - doc:删除重复调Request.replace论证()(:提交:1 aeccdd)
- fixed formatting of scrapyd doc (:commit:`8bf19e6`)
### 固定格式的scrapyd doc(承诺:“8 bf19e6”)
- Dump stacks for all running threads and fix engine status dumped by StackTraceDump extension (:commit:`14a8e6e`)
### ——转储所有正在运行的线程的堆栈和修复发动机状态StackTraceDump甩了扩展(承诺:“14 a8e6e”)
- added comment about why we disable ssl on boto images upload (:commit:`5223575`)
### ——添加评论为什么我们宝途上禁用ssl图片上传(提交:' 5223575 ')
- SSL handshaking hangs when doing too many parallel connections to S3 (:commit:`63d583d`)
### - SSL握手挂在太多的并行连接S3(提交:“63 d583d”)
- change tutorial to follow changes on dmoz site (:commit:`bcb3198`)
### -改变教程跟着变化dmoz网站(承诺:“bcb3198”)
- Avoid _disconnectedDeferred AttributeError exception in Twisted>=11.1.0 (:commit:`98f3f87`)
### -避免_disconnectedDeferred AttributeError异常扭曲> = 11.1.0(提交:“98 f3f87”)
- allow spider to set autothrottle max concurrency (:commit:`175a4b5`)
### ——允许蜘蛛设置自动油门最大并发(提交:“175 a4b5”)

Scrapy 0.14
-----------

New features and settings
~~~~~~~~~~~~~~~~~~~~~~~~~

- Support for `AJAX crawleable urls`_
### ——支持AJAX crawleable url _
- New persistent scheduler that stores requests on disk, allowing to suspend and resume crawls (:rev:`2737`)
### ——新的持久调度程序存储在磁盘上的请求,允许暂停和恢复爬(牧师:‘2737’)
- added ``-o`` option to ``scrapy crawl``, a shortcut for dumping scraped items into a file (or standard output using ``-``)
### ——添加“- o ' '选项' ' scrapy爬' ',一个倾倒的快捷方式物品刮到一个文件中(或标准输出使用' ',' ')
- Added support for passing custom settings to Scrapyd ``schedule.json`` api (:rev:`2779`, :rev:`2783`)
### ——添加支持通过自定义设置Scrapyd“时间表。json的api(牧师:“2779”,牧师:' 2783 ')
- New ``ChunkedTransferMiddleware`` (enabled by default) to support `chunked transfer encoding`_ (:rev:`2769`)
### ——新“ChunkedTransferMiddleware“(默认启用)支持“分块传输编码”_(:牧师:‘2769’)
- Add boto 2.0 support for S3 downloader handler (:rev:`2763`)
### ——添加宝途S3支持下载器2.0处理程序(:牧师:‘2763’)
- Added `marshal`_ to formats supported by feed exports (:rev:`2744`)
### ——添加“元帅”_格式支持的饲料出口(牧师:‘2744’)
- In request errbacks, offending requests are now received in `failure.request` attribute (:rev:`2738`)
### ——请求errback冒犯请求现在收到的失败。请求的属性(:牧师:‘2738’)
- Big downloader refactoring to support per domain/ip concurrency limits (:rev:`2732`)
### ——大下载每个域重构支持/ ip并发限制(牧师:‘2732’)
   - ``CONCURRENT_REQUESTS_PER_SPIDER`` setting has been deprecated and replaced by:
### ——“CONCURRENT_REQUESTS_PER_SPIDER“设置已经弃用,取而代之的是:
      - :setting:`CONCURRENT_REQUESTS`, :setting:`CONCURRENT_REQUESTS_PER_DOMAIN`, :setting:`CONCURRENT_REQUESTS_PER_IP`
   - check the documentation for more details
### ——检查文档的更多细节
- Added builtin caching DNS resolver (:rev:`2728`)
### ——增加了内装式缓存DNS解析器(牧师:‘2728’)
- Moved Amazon AWS-related components/extensions (SQS spider queue, SimpleDB stats collector) to a separate project: [scaws](https://github.com/scrapinghub/scaws) (:rev:`2706`, :rev:`2714`)
### ——搬到亚马逊AWS-related组件/扩展(SQS队列蜘蛛,SimpleDB数据收集器)到一个单独的项目:[海角](https://github.com/scrapinghub/scaws)(牧师:“2706”,牧师:' 2714 ')
- Moved spider queues to scrapyd: `scrapy.spiderqueue` -> `scrapyd.spiderqueue` (:rev:`2708`)
### ——蜘蛛队列转移到scrapyd:“scrapy。spiderqueue scrapyd“- >”。spiderqueue '(:牧师:‘2708’)
- Moved sqlite utils to scrapyd: `scrapy.utils.sqlite` -> `scrapyd.sqlite` (:rev:`2781`)
### ——将sqlite跑龙套scrapyd:“scrapy.utils。sqlite scrapyd“- >”。sqlite”(牧师:‘2781’)
- Real support for returning iterators on `start_requests()` method. The iterator is now consumed during the crawl when the spider is getting idle (:rev:`2704`)
### ——真正的支持返回迭代器start_requests()的方法。迭代器现在消耗在蜘蛛的爬行是空闲的(启示录:‘2704’)
- Added :setting:`REDIRECT_ENABLED` setting to quickly enable/disable the redirect middleware (:rev:`2697`)
### ——补充道:设置:“REDIRECT_ENABLED”设置快速启用/禁用重定向中间件(牧师:‘2697’)
- Added :setting:`RETRY_ENABLED` setting to quickly enable/disable the retry middleware (:rev:`2694`)
### ——补充道:设置:“RETRY_ENABLED”设置快速启用/禁用重试中间件(牧师:‘2694’)
- Added ``CloseSpider`` exception to manually close spiders (:rev:`2691`)
### ——添加“CloseSpider“例外手动关闭蜘蛛(牧师:‘2691’)
- Improved encoding detection by adding support for HTML5 meta charset declaration (:rev:`2690`)
### -改善编码检测通过添加支持HTML5元字符集宣言(牧师:‘2690’)
- Refactored close spider behavior to wait for all downloads to finish and be processed by spiders, before closing the spider (:rev:`2688`)
### ——重构密切蜘蛛行为等所有下载完成和处理蜘蛛,收盘蜘蛛(牧师:‘2688’)
- Added ``SitemapSpider`` (see documentation in Spiders page) (:rev:`2658`)
### ——添加“SitemapSpider ' '(参见文档在页面蜘蛛)(牧师:‘2658’)
- Added ``LogStats`` extension for periodically logging basic stats (like crawled pages and scraped items) (:rev:`2657`)
### ——添加“LogStats定期“扩展日志基本数据(如爬页面和刮项目)(牧师:‘2657’)
- Make handling of gzipped responses more robust (#319, :rev:`2643`). Now Scrapy will try and decompress as much as possible from a gzipped response, instead of failing with an `IOError`.
### 使处理gzip反应更健壮(# 319:牧师:' 2643 ')。现在Scrapy将试着从gzip压缩尽可能的反应,而不是以一个“IOError的那么失败。
- Simplified !MemoryDebugger extension to use stats for dumping memory debugging info (:rev:`2639`)
### ——简化!MemoryDebugger扩展为倾销内存调试使用统计信息(牧师:‘2639’)
- Added new command to edit spiders: ``scrapy edit`` (:rev:`2636`) and `-e` flag to `genspider` command that uses it (:rev:`2653`)
### -添加新命令编辑蜘蛛:“scrapy编辑' '(:牧师:“2636”)和“e”旗帜的genspider命令使用它(牧师:‘2653’)
- Changed default representation of items to pretty-printed dicts. (:rev:`2631`). This improves default logging by making log more readable in the default case, for both Scraped and Dropped lines.
### ——改变了默认的表示形式打印字典条目。(牧师:‘2631’)。这提高了默认日志记录通过日志更具可读性在默认情况下,刮和直线下降。
- Added :signal:`spider_error` signal (:rev:`2628`)
### ——补充道:信号:“spider_error”信号(牧师:‘2628’)
- Added :setting:`COOKIES_ENABLED` setting (:rev:`2625`)
### ——补充道:设置:“COOKIES_ENABLED”设置(牧师:‘2625’)
- Stats are now dumped to Scrapy log (default value of :setting:`STATS_DUMP` setting has been changed to `True`). This is to make Scrapy users more aware of Scrapy stats and the data that is collected there.
### ——统计现在倾倒Scrapy日志(默认值:设置:“STATS_DUMP”设置被更改为“真正的”)。这是使Scrapy用户更清楚Scrapy统计数据和收集的数据。
- Added support for dynamically adjusting download delay and maximum concurrent requests (:rev:`2599`)
### ——增加了支持动态调整下载延迟和最大并发请求(牧师:‘2599’)
- Added new DBM HTTP cache storage backend (:rev:`2576`)
### ——添加新DBM HTTP缓存存储后端(:牧师:‘2576’)
- Added ``listjobs.json`` API to Scrapyd (:rev:`2571`)
### ——“listjobs补充道。json的API Scrapyd(:牧师:‘2571’)
- ``CsvItemExporter``: added ``join_multivalued`` parameter (:rev:`2578`)
### :还说”——“CsvItemExporter”“join_multivalued“参数(转速:‘2578’)
- Added namespace support to ``xmliter_lxml`` (:rev:`2552`)
### ——添加名称空间支持“xmliter_lxml ' '(:牧师:‘2552’)
- Improved cookies middleware by making `COOKIES_DEBUG` nicer and documenting it (:rev:`2579`)
### ——改善饼干中间件更好地通过“COOKIES_DEBUG”和记录(牧师:‘2579’)
- Several improvements to Scrapyd and Link extractors
### ——改进Scrapyd和链接提取器

Code rearranged and removed
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Merged item passed and item scraped concepts, as they have often proved confusing in the past. This means: (:rev:`2630`)
### ——合并项目,项目刮的概念,因为他们常常证明过去令人困惑。这意味着:(:牧师:‘2630’)
   - original item_scraped signal was removed
### ——原始item_scraped信号被移除
   - original item_passed signal was renamed to item_scraped
### ——原始item_passed信号是item_scraped重命名
   - old log lines ``Scraped Item...`` were removed
### 历史日志行“刮项…“被移除
   - old log lines ``Passed Item...`` were renamed to ``Scraped Item...`` lines and downgraded to ``DEBUG`` level
### 历史日志行“通过项目……“被改名为“刮项……“行,降级为“调试”水平
- Reduced Scrapy codebase by striping part of Scrapy code into two new libraries:
### Scrapy代码库,减少了分段Scrapy代码分成两个新库的一部分:
   - `w3lib`_ (several functions from ``scrapy.utils.{http,markup,multipart,response,url}``, done in :rev:`2584`)
### ——“w3lib”从“scrapy.utils _(几个函数。{ http、标记、扇形、响应url } ' ',在:牧师:‘2584’)
   - `scrapely`_ (was ``scrapy.contrib.ibl``, done in :rev:`2586`)
### “刮”_(“scrapy.contrib。ibl ' ',在牧师:' 2586 ')
- Removed unused function: `scrapy.utils.request.request_info()` (:rev:`2577`)
### -删除未使用的功能:“scrapy.utils.request.request_info()(牧师:‘2577’)
- Removed googledir project from `examples/googledir`. There's now a new example project called `dirbot` available on github: https://github.com/scrapy/dirbot
### -删除从的例子/ googledir googledir项目。现在有一个新的例子项目名为“dirbot”可以在github:https://github.com/scrapy/dirbot
- Removed support for default field values in Scrapy items (:rev:`2616`)
### -删除支持缺省字段值Scrapy物品(牧师:‘2616’)
- Removed experimental crawlspider v2 (:rev:`2632`)
### -删除实验crawlspider v2(:牧师:‘2632’)
- Removed scheduler middleware to simplify architecture. Duplicates filter is now done in the scheduler itself, using the same dupe fltering class as before (`DUPEFILTER_CLASS` setting) (:rev:`2640`)
### -删除调度器中间件来简化架构。重复的过滤器是现在做的调度器本身,使用相同的欺骗fltering类之前(“DUPEFILTER_CLASS”设置)(牧师:‘2640’)
- Removed support for passing urls to ``scrapy crawl`` command (use ``scrapy parse`` instead) (:rev:`2704`)
### -删除支持url传递给“scrapy爬“命令(使用“scrapy解析“)(牧师:‘2704’)
- Removed deprecated Execution Queue (:rev:`2704`)
### -删除弃用执行队列(:牧师:‘2704’)
- Removed (undocumented) spider context extension (from scrapy.contrib.spidercontext) (:rev:`2780`)
### -删除(非法)蜘蛛上下文扩展(从scrapy.contrib.spidercontext)(牧师:‘2780’)
- removed ``CONCURRENT_SPIDERS`` setting (use scrapyd maxproc instead) (:rev:`2789`)
### -删除“CONCURRENT_SPIDERS“设置(使用scrapyd maxproc)(牧师:‘2789’)
- Renamed attributes of core components: downloader.sites -> downloader.slots, scraper.sites -> scraper.slots (:rev:`2717`, :rev:`2718`)
### -更名为核心组件的属性:下载工具。网站- >下载器。槽,刮板。网站- >刮刀。槽(牧师:“2717”,:牧师:' 2718 ')
- Renamed setting ``CLOSESPIDER_ITEMPASSED`` to :setting:`CLOSESPIDER_ITEMCOUNT` (:rev:`2655`). Backwards compatibility kept.
### ”,改名为“CLOSESPIDER_ITEMPASSED””:设置:“CLOSESPIDER_ITEMCOUNT”(启示录:‘2655’)。向后兼容性。

Scrapy 0.12
-----------

The numbers like #NNN reference tickets in the old issue tracker (Trac) which is no longer available.
### 数字# NNN参考门票在旧的问题跟踪器(Trac)这是不再可用。

New features and improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Passed item is now sent in the ``item`` argument of the :signal:`item_passed` (#273)
### ——通过项目是“现在发送项目的“参数:信号:“item_passed”(# 273)
- Added verbose option to ``scrapy version`` command, useful for bug reports (#298)
### ——verbose选项添加到“scrapy版本“命令,用于错误报告(# 298)
- HTTP cache now stored by default in the project data dir (#279)
### ——HTTP缓存现在默认存储在项目数据dir(# 279)
- Added project data storage directory (#276, #277)
### ——添加项目数据存储目录(# 276,# 277)
- Documented file structure of Scrapy projects (see command-line tool doc)
### ——记录文件结构Scrapy项目(见命令行工具文档)
- New lxml backend for XPath selectors (#147)
### ——新lxml端XPath选择器(# 147)
- Per-spider settings (#245)
- Support exit codes to signal errors in Scrapy commands (#248)
### ——支持退出码信号错误Scrapy命令(# 248)
- Added ``-c`` argument to ``scrapy shell`` command
### ”,添加“c”的论点“scrapy shell的命令
- Made ``libxml2`` optional (#260)
### ——“libxml2“可选(# 260)
- New ``deploy`` command (#261)
### ——新的“部署”命令(# 261)
- Added :setting:`CLOSESPIDER_PAGECOUNT` setting (#253)
### ——补充道:设置:“CLOSESPIDER_PAGECOUNT”设置(# 253)
- Added :setting:`CLOSESPIDER_ERRORCOUNT` setting (#254)
### ——补充道:设置:“CLOSESPIDER_ERRORCOUNT”设置(# 254)

Scrapyd changes
~~~~~~~~~~~~~~~

- Scrapyd now uses one process per spider
### ——Scrapyd现在使用一个进程/蜘蛛
- It stores one log file per spider run, and rotate them keeping the lastest 5 logs per spider (by default)
### ——它存储日志文件/蜘蛛跑,和旋转它们保持最新的5日志/蜘蛛(默认)
- A minimal web ui was added, available at http://localhost:6800 by default
### ——增加了最小的web ui,默认情况下可以在http://localhost:6800
- There is now a `scrapy server` command to start a Scrapyd server of the current project
### ——现在有一个“scrapy服务器”命令来启动Scrapyd服务器当前的项目

Changes to settings
~~~~~~~~~~~~~~~~~~~

- added `HTTPCACHE_ENABLED` setting (False by default) to enable HTTP cache middleware
### ——添加“HTTPCACHE_ENABLED”设置(默认错误)启用HTTP缓存中间件
- changed `HTTPCACHE_EXPIRATION_SECS` semantics: now zero means "never expire".
### ——改变“HTTPCACHE_EXPIRATION_SECS”语义:现在零意味着“永不过期”。

Deprecated/obsoleted functionality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Deprecated ``runserver`` command in favor of ``server`` command which starts a Scrapyd server. See also: Scrapyd changes
### ——弃用“runserver '命令的“服务器的命令开始Scrapyd服务器。参见:Scrapyd变化
- Deprecated ``queue`` command in favor of using Scrapyd ``schedule.json`` API. See also: Scrapyd changes
### ——弃用“队列”命令的使用Scrapyd“时间表。json的API。参见:Scrapyd变化
- Removed the !LxmlItemLoader (experimental contrib which never graduated to main contrib)
### ——删除了!LxmlItemLoader(实验contrib从未毕业主要contrib)

Scrapy 0.10
-----------

The numbers like #NNN reference tickets in the old issue tracker (Trac) which is no longer available.
### 数字# NNN参考门票在旧的问题跟踪器(Trac)这是不再可用。

New features and improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- New Scrapy service called ``scrapyd`` for deploying Scrapy crawlers in production (#218) (documentation available)
### ——新Scrapy服务称为“scrapyd“部署Scrapy爬虫在生产(# 218)(文档)
- Simplified Images pipeline usage which doesn't require subclassing your own images pipeline now (#217)
### ——管道使用简化的图像不需要子类化自己的图片现在管道(# 217)
- Scrapy shell now shows the Scrapy log by default (#206)
### ——Scrapy壳牌现在显示默认Scrapy日志(# 206)
- Refactored execution queue in a common base code and pluggable backends called "spider queues" (#220)
### -重构执行队列中一个共同的基础代码和可插拔后端称为“蜘蛛队列”(# 220)
- New persistent spider queue (based on SQLite) (#198), available by default, which allows to start Scrapy in server mode and then schedule spiders to run.
### ——新的持久蜘蛛队列(基于SQLite)(# 198),可用在默认情况下,它允许在服务器模式开始Scrapy然后安排蜘蛛。
- Added documentation for Scrapy command-line tool and all its available sub-commands. (documentation available)
### ——添加文档Scrapy sub-commands命令行工具及其所有可用。(文档)
- Feed exporters with pluggable backends (#197) (documentation available)
### ——饲料出口商可插拔后端(# 197)(文档)
- Deferred signals (#193)
- Added two new methods to item pipeline open_spider(), close_spider() with deferred support (#195)
### ——添加了两个新的方法项目管道open_spider(),close_spider()与递延支持(# 195)
- Support for overriding default request headers per spider (#181)
### ——支持覆盖默认请求头/蜘蛛(# 181)
- Replaced default Spider Manager with one with similar functionality but not depending on Twisted Plugins (#186)
### ——取代默认的蜘蛛经理与一个类似的功能,但不是根据扭曲的插件(# 186)
- Splitted Debian package into two packages - the library and the service (#187)
### -分裂Debian包分成两包库和服务(# 187)
- Scrapy log refactoring (#188)
### ——Scrapy日志重构(# 188)
- New extension for keeping persistent spider contexts among different runs (#203)
### 保持持久的蜘蛛——新的扩展上下文在不同运行(# 203)
- Added `dont_redirect` request.meta key for avoiding redirects (#233)
### ——添加“dont_redirect”请求。meta关键避免重定向(# 233)
- Added `dont_retry` request.meta key for avoiding retries (#234)
### ——添加“dont_retry”请求。meta关键避免重试(# 234)

Command-line tool changes
~~~~~~~~~~~~~~~~~~~~~~~~~

- New `scrapy` command which replaces the old `scrapy-ctl.py` (#199)
### ——新' scrapy '命令替换旧的scrapy-ctl。py’(# 199)
  - there is only one global `scrapy` command now, instead of one `scrapy-ctl.py` per project
### ——只有一个全球现在' scrapy '命令,而不是一个“scrapy-ctl。py的每个项目
  - Added `scrapy.bat` script for running more conveniently from Windows
### ——“scrapy补充道。蝙蝠的脚本运行得更加方便地从Windows
- Added bash completion to command-line tool (#210)
### ——完成添加bash命令行工具(# 210)
- Renamed command `start` to `runserver` (#209)
### ——重命名命令“开始”“runserver”(# 209)

API changes
~~~~~~~~~~~

- ``url`` and ``body`` attributes of Request objects are now read-only (#230)
### ”——“url”和“身体”“现在请求对象的属性是只读的(# 230)
- ``Request.copy()`` and ``Request.replace()`` now also copies their ``callback`` and ``errback`` attributes (#231)
### -“Request.copy()' '和' ' Request.replace()' '现在也拷贝他们的“回调”和“errback“属性(# 231)
- Removed ``UrlFilterMiddleware`` from ``scrapy.contrib`` (already disabled by default)
### -删除“UrlFilterMiddleware从“scrapy ' '。contrib“(默认已经禁用)
- Offsite middelware doesn't filter out any request coming from a spider that doesn't have a allowed_domains attribute (#225)
### ——离线middelware不过滤掉任何请求来自一只蜘蛛没有allowed_domains属性(# 225)
- Removed Spider Manager ``load()`` method. Now spiders are loaded in the constructor itself.
### -删除蜘蛛经理“load()“方法。蜘蛛是加载在构造函数本身。
- Changes to Scrapy Manager (now called "Crawler"):
### ——改变Scrapy经理(现在称为“爬虫”):
   - ``scrapy.core.manager.ScrapyManager`` class renamed to ``scrapy.crawler.Crawler``
### ——“scrapy.core.manager。ScrapyManager“类重新命名为“scrapy.crawler.Crawler ' '
   - ``scrapy.core.manager.scrapymanager`` singleton moved to ``scrapy.project.crawler``
### ——“scrapy.core.manager。scrapymanager“单例搬到“scrapy.project.crawler ' '
- Moved module: ``scrapy.contrib.spidermanager`` to ``scrapy.spidermanager``
### -移动模块:“scrapy.contrib。spidermanager ' ',' ' scrapy.spidermanager ' '
- Spider Manager singleton moved from ``scrapy.spider.spiders`` to the ``spiders` attribute of ``scrapy.project.crawler`` singleton.
### 单从“scrapy.spider——蜘蛛经理。蜘蛛的“的”“蜘蛛”属性的“scrapy.project。履带的单例。
- moved Stats Collector classes: (#204)
### ——移动数据收集器类:(# 204)
   - ``scrapy.stats.collector.StatsCollector`` to ``scrapy.statscol.StatsCollector``
   - ``scrapy.stats.collector.SimpledbStatsCollector`` to ``scrapy.contrib.statscol.SimpledbStatsCollector``
- default per-command settings are now specified in the ``default_settings`` attribute of command object class (#201)
### ——现在各命令的默认设置中指定的“default_settings '命令对象类的属性(# 201)
- changed arguments of Item pipeline ``process_item()`` method from ``(spider, item)`` to ``(item, spider)``
### ——改变参数项管道“process_item()从' ' ' '方法(蜘蛛、项目)' ' ' '(项目,蜘蛛)'
   - backwards compatibility kept (with deprecation warning)
### 向后兼容性保持(弃用警告)
- moved ``scrapy.core.signals`` module to ``scrapy.signals``
### ——“scrapy.core移动。信号的“模块”“scrapy.signals ' '
   - backwards compatibility kept (with deprecation warning)
### 向后兼容性保持(弃用警告)
- moved ``scrapy.core.exceptions`` module to ``scrapy.exceptions``
### ——“scrapy.core移动。异常“模块”“scrapy.exceptions ' '
   - backwards compatibility kept (with deprecation warning)
### 向后兼容性保持(弃用警告)
- added ``handles_request()`` class method to ``BaseSpider``
### -添加“handles_request()“类方法“BaseSpider ' '
- dropped ``scrapy.log.exc()`` function (use ``scrapy.log.err()`` instead)
### -“scrapy.log.exc下降()“功能(使用“scrapy.log.err()“相反)
- dropped ``component`` argument of ``scrapy.log.msg()`` function
### ——把“组件”的论点“scrapy.log.msg()“函数
- dropped ``scrapy.log.log_level`` attribute
- Added ``from_settings()`` class methods to Spider Manager, and Item Pipeline Manager
### -添加“from_settings()“类方法蜘蛛经理,项目管道经理

Changes to settings
~~~~~~~~~~~~~~~~~~~

- Added ``HTTPCACHE_IGNORE_SCHEMES`` setting to ignore certain schemes on !HttpCacheMiddleware (#225)
### ——添加“HTTPCACHE_IGNORE_SCHEMES“设置忽略某些计划!HttpCacheMiddleware(# 225)
- Added ``SPIDER_QUEUE_CLASS`` setting which defines the spider queue to use (#220)
### ——添加“SPIDER_QUEUE_CLASS“设置它定义了蜘蛛队列使用(# 220)
- Added ``KEEP_ALIVE`` setting (#220)
### ——添加“KEEP_ALIVE“设置(# 220)
- Removed ``SERVICE_QUEUE`` setting (#220)
### -删除“SERVICE_QUEUE“设置(# 220)
- Removed ``COMMANDS_SETTINGS_MODULE`` setting (#201)
### -删除“COMMANDS_SETTINGS_MODULE“设置(# 201)
- Renamed ``REQUEST_HANDLERS`` to ``DOWNLOAD_HANDLERS`` and make download handlers classes (instead of functions)
### ”,改名为“REQUEST_HANDLERS”’“DOWNLOAD_HANDLERS ' ',使下载处理程序类(而不是功能)

Scrapy 0.9
----------

The numbers like #NNN reference tickets in the old issue tracker (Trac) which is no longer available.
### 数字# NNN参考门票在旧的问题跟踪器(Trac)这是不再可用。

New features and improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Added SMTP-AUTH support to scrapy.mail
### ——添加scrapy.mail SMTP-AUTH支持
- New settings added: ``MAIL_USER``, ``MAIL_PASS`` (:rev:`2065` | #149)
### ——新设置补充道:“MAIL_USER ' ',' ' MAIL_PASS ' '(:牧师:“2065”| # 149)
- Added new scrapy-ctl view command - To view URL in the browser, as seen by Scrapy (:rev:`2039`)
### -添加新的scrapy-ctl视图命令查看URL在浏览器中,所看到的Scrapy(牧师:‘2039’)
- Added web service for controlling Scrapy process (this also deprecates the web console. (:rev:`2053` | #167)
### 添加web服务控制Scrapy流程(这也不赞成web控制台。(牧师:' 2053 ' | # 167)
- Support for running Scrapy as a service, for production systems (:rev:`1988`, :rev:`2054`, :rev:`2055`, :rev:`2056`, :rev:`2057` | #168)
### ——支持Scrapy作为服务运行,生产系统(牧师:“1988”,牧师:“2054”,:牧师:“2055”,:牧师:“2056”,:牧师:“2057”| # 168)
- Added wrapper induction library (documentation only available in source code for now). (:rev:`2011`)
### ——添加包装器归纳库(文档现在只能在源代码)。(牧师:‘2011’)
- Simplified and improved response encoding support (:rev:`1961`, :rev:`1969`)
### -简化和改进的响应编码支持(牧师:“1961”,牧师:' 1969 ')
- Added ``LOG_ENCODING`` setting (:rev:`1956`, documentation available)
### ——添加“LOG_ENCODING“设置(牧师:“1956”,文档可用)
- Added ``RANDOMIZE_DOWNLOAD_DELAY`` setting (enabled by default) (:rev:`1923`, doc available)
### ——添加“RANDOMIZE_DOWNLOAD_DELAY“设置(默认启用)(牧师:“1923”,医生可用)
- ``MailSender`` is no longer IO-blocking (:rev:`1955` | #146)
### ——“MailSender“不再是IO-blocking(牧师:“1955”| # 146)
- Linkextractors and new Crawlspider now handle relative base tag urls (:rev:`1960` | #148)
### ——新Linkextractors Crawlspider现在处理相对基础标记的url(牧师:“1960”| # 148)
- Several improvements to Item Loaders and processors (:rev:`2022`, :rev:`2023`, :rev:`2024`, :rev:`2025`, :rev:`2026`, :rev:`2027`, :rev:`2028`, :rev:`2029`, :rev:`2030`)
### 一些改进项加载器和处理器(牧师:“2022”,牧师:“2023”,:牧师:“2024”,:牧师:“2025”,:牧师:“2026”,:牧师:“2027”,:牧师:“2028”,:牧师:“2029”,:牧师:' 2030 ')
- Added support for adding variables to telnet console (:rev:`2047` | #165)
### ——支持添加变量添加到远程登录控制台(牧师:“2047”| # 165)
- Support for requests without callbacks (:rev:`2050` | #166)
### ——支持请求没有回调(牧师:“2050”| # 166)

API changes
~~~~~~~~~~~

- Change ``Spider.domain_name`` to ``Spider.name`` (SEP-012, :rev:`1975`)
### -改变“蜘蛛。domain_name ' ',' ' Spider.name”(——012年9月,牧师:' 1975 ')
- ``Response.encoding`` is now the detected encoding (:rev:`1961`)
### ——“响应。编码”“现在发现编码(:牧师:‘1961’)
- ``HttpErrorMiddleware`` now returns None or raises an exception (:rev:`2006` | #157)
### ——“HttpErrorMiddleware ' '现在返回没有或引发一个异常(牧师:“2006”| # 157)
- ``scrapy.command`` modules relocation (:rev:`2035`, :rev:`2036`, :rev:`2037`)
### ”——“scrapy.command”模块搬迁(牧师:“2035”,牧师:“2036”,:牧师:' 2037 ')
- Added ``ExecutionQueue`` for feeding spiders to scrape (:rev:`2034`)
### ——还说‘ExecutionQueue”喂蜘蛛刮(牧师:‘2034’)
- Removed ``ExecutionEngine`` singleton (:rev:`2039`)
### -删除“ExecutionEngine“单例(牧师:‘2039’)
- Ported ``S3ImagesStore`` (images pipeline) to use boto and threads (:rev:`2033`)
### ——移植' ' S3ImagesStore ' '(图片管道)使用宝途和线程(牧师:‘2033’)
- Moved module: ``scrapy.management.telnet`` to ``scrapy.telnet`` (:rev:`2047`)
### -移动模块:“scrapy.management。“scrapy telnet ' '。telnet ' '(:牧师:‘2047’)

Changes to default settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Changed default ``SCHEDULER_ORDER`` to ``DFO`` (:rev:`1939`)
### ——改变默认' ' SCHEDULER_ORDER '”“柴油”(启示录:‘1939’)

Scrapy 0.8
----------

The numbers like #NNN reference tickets in the old issue tracker (Trac) which is no longer available.
### 数字# NNN参考门票在旧的问题跟踪器(Trac)这是不再可用。

New features
~~~~~~~~~~~~

- Added DEFAULT_RESPONSE_ENCODING setting (:rev:`1809`)
### ——添加DEFAULT_RESPONSE_ENCODING设置(牧师:‘1809’)
- Added ``dont_click`` argument to ``FormRequest.from_response()`` method (:rev:`1813`, :rev:`1816`)
### ——添加“dont_click“参数“FormRequest.from_response()“方法(牧师:“1813”,牧师:' 1816 ')
- Added ``clickdata`` argument to ``FormRequest.from_response()`` method (:rev:`1802`, :rev:`1803`)
### ——添加“clickdata“参数“FormRequest.from_response()“方法(牧师:“1802”,牧师:' 1803 ')
- Added support for HTTP proxies (``HttpProxyMiddleware``) (:rev:`1781`, :rev:`1785`)
### ——增加了对HTTP代理的支持(“HttpProxyMiddleware“)(牧师:“1781”,牧师:' 1785 ')
- Offsite spider middleware now logs messages when filtering out requests (:rev:`1841`)
### ——离线蜘蛛中间件现在日志消息当过滤请求(牧师:‘1841’)

Backwards-incompatible changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Changed ``scrapy.utils.response.get_meta_refresh()`` signature (:rev:`1804`)
### -改变“scrapy.utils.response.get_meta_refresh()“签名(牧师:‘1804’)
- Removed deprecated ``scrapy.item.ScrapedItem`` class - use ``scrapy.item.Item instead`` (:rev:`1838`)
### -删除弃用“scrapy.item。ScrapedItem“类-使用“scrapy.item。项相反' '(:牧师:‘1838’)
- Removed deprecated ``scrapy.xpath`` module - use ``scrapy.selector`` instead. (:rev:`1836`)
### -删除弃用“scrapy。——使用“scrapy xpath的模块。选择器”。(牧师:‘1836’)
- Removed deprecated ``core.signals.domain_open`` signal - use ``core.signals.domain_opened`` instead (:rev:`1822`)
### -删除弃用“core.signals。——使用“core.signals domain_open“信号。domain_opened ' '(:牧师:‘1822’)
- ``log.msg()`` now receives a ``spider`` argument (:rev:`1822`)
### -“log.msg()“现在收到一个“蜘蛛”“参数(转速:‘1822’)
   - Old domain argument has been deprecated and will be removed in 0.9. For spiders, you should always use the ``spider`` argument and pass spider references. If you really want to pass a string, use the ``component`` argument instead.
### 岁域参数在0.9被废弃,将被删除。对于蜘蛛,你应该总是使用“蜘蛛”参数,通过蜘蛛引用。如果你真的想传递一个字符串,使用“组件”的论点。
- Changed core signals ``domain_opened``, ``domain_closed``, ``domain_idle``
### ——改变核心信号' ' domain_opened ' ',' ' domain_closed ' ',' ' domain_idle ' '
- Changed Item pipeline to use spiders instead of domains
### ——改变项目管道使用蜘蛛而不是域
   -  The ``domain`` argument of  ``process_item()`` item pipeline method was changed to  ``spider``, the new signature is: ``process_item(spider, item)`` (:rev:`1827` | #105)
### ——“域”的论点“process_item()“项目管道方法更改为“蜘蛛”,新的签名:“process_item(蜘蛛、项目)' '(:牧师:‘1827’| # 105)
   - To quickly port your code (to work with Scrapy 0.8) just use ``spider.domain_name`` where you previously used ``domain``.
### ——快速端口代码(使用Scrapy 0.8)只使用“蜘蛛。domain_name ' '你在哪里之前使用“域”。
- Changed Stats API to use spiders instead of domains (:rev:`1849` | #113)
### ——改变数据API使用蜘蛛而不是域(牧师:“1849”| # 113)
   - ``StatsCollector`` was changed to receive spider references (instead of domains) in its methods (``set_value``, ``inc_value``, etc).
### ”——“StatsCollector””是改变接收蜘蛛引用(而不是域)的方法(“set_value ' ',' ' inc_value ' ',等等)。
   - added ``StatsCollector.iter_spider_stats()`` method
   - removed ``StatsCollector.list_domains()`` method
   - Also, Stats signals were renamed and now pass around spider references (instead of domains). Here's a summary of the changes:
### ——同时,统计数据的信号被重命名,现在通过蜘蛛(而不是域)的引用。这是一个变化的总结:
   - To quickly port your code (to work with Scrapy 0.8) just use ``spider.domain_name`` where you previously used ``domain``. ``spider_stats`` contains exactly the same data as ``domain_stats``.
### ——快速端口代码(使用Scrapy 0.8)只使用“蜘蛛。domain_name ' '你在哪里之前使用“域”。“spider_stats“包含完全相同的数据作为“domain_stats’”。
- ``CloseDomain`` extension moved to ``scrapy.contrib.closespider.CloseSpider`` (:rev:`1833`)
### ——“CloseDomain搬到“scrapy.contrib.closespider“扩展。CloseSpider ' '(:牧师:‘1833’)
   - Its settings were also renamed:
### ——它的设置也更名为:
      - ``CLOSEDOMAIN_TIMEOUT`` to ``CLOSESPIDER_TIMEOUT``
      - ``CLOSEDOMAIN_ITEMCOUNT`` to ``CLOSESPIDER_ITEMCOUNT``
- Removed deprecated ``SCRAPYSETTINGS_MODULE`` environment variable - use ``SCRAPY_SETTINGS_MODULE`` instead (:rev:`1840`)
### -删除弃用“SCRAPYSETTINGS_MODULE“环境变量,使用“SCRAPY_SETTINGS_MODULE ' '相反(牧师:‘1840’)
- Renamed setting: ``REQUESTS_PER_DOMAIN`` to ``CONCURRENT_REQUESTS_PER_SPIDER`` (:rev:`1830`, :rev:`1844`)
### -重命名设置:' ' REQUESTS_PER_DOMAIN '”“CONCURRENT_REQUESTS_PER_SPIDER ' '(:牧师:“1830”,牧师:' 1844 ')
- Renamed setting: ``CONCURRENT_DOMAINS`` to ``CONCURRENT_SPIDERS`` (:rev:`1830`)
### -重命名设置:' ' CONCURRENT_DOMAINS '”“CONCURRENT_SPIDERS ' '(:牧师:‘1830’)
- Refactored HTTP Cache middleware
### ——重构HTTP缓存中间件
- HTTP Cache middleware has been heavilty refactored, retaining the same functionality except for the domain sectorization which was removed. (:rev:`1843` )
### —HTTP缓存中间件heavilty重构,保留相同的功能除了域功能分区被删除。(牧师:‘1843’)
- Renamed exception: ``DontCloseDomain`` to ``DontCloseSpider`` (:rev:`1859` | #120)
### ”——重命名例外:“DontCloseDomain”’“DontCloseSpider ' '(:牧师:“1859”| # 120)
- Renamed extension: ``DelayedCloseDomain`` to ``SpiderCloseDelay`` (:rev:`1861` | #121)
### -重命名扩展:' ' DelayedCloseDomain '”“SpiderCloseDelay ' '(:牧师:“1861”| # 121)
- Removed obsolete ``scrapy.utils.markup.remove_escape_chars`` function - use ``scrapy.utils.markup.replace_escape_chars`` instead (:rev:`1865`)
### -删除过时的“scrapy.utils.markup。——使用“scrapy.utils.markup remove_escape_chars ' '功能。replace_escape_chars ' '(:牧师:‘1865’)

Scrapy 0.7
----------

First release of Scrapy.


.. _AJAX crawleable urls: https://developers.google.com/webmasters/ajax-crawling/docs/getting-started?csw=1
### . ._AJAX crawleable url:https://developers.google.com/webmasters/ajax-crawling/docs/getting-started?csw=1
.. _chunked transfer encoding: https://en.wikipedia.org/wiki/Chunked_transfer_encoding
### . ._chunked传输编码:https://en.wikipedia.org/wiki/Chunked_transfer_encoding
.. _w3lib: https://github.com/scrapy/w3lib
.. _scrapely: https://github.com/scrapy/scrapely
.. _marshal: https://docs.python.org/2/library/marshal.html
.. _w3lib.encoding: https://github.com/scrapy/w3lib/blob/master/w3lib/encoding.py
.. _lxml: http://lxml.de/
.. _ClientForm: http://wwwsearch.sourceforge.net/old/ClientForm/
.. _resource: https://docs.python.org/2/library/resource.html
.. _queuelib: https://github.com/scrapy/queuelib
.. _cssselect: https://github.com/SimonSapin/cssselect
