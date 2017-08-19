import hashlib
from urllib import request

md5 = hashlib.md5()
md5.update('lwq'.encode('utf-8'))
# print(md5.hexdigest())

# for item in request.__all__:
#     print(item)
# print(dir(urllib.request))
# print(help(request.urlretrieve))

# url = "http://img.blog.csdn.net/20160316171847321?watermark/2/text/" \
#       "aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast"
# md5.update('lwq'.encode('utf-8'))
# filename = "images/" + md5.hexdigest() + ".png"

# request.urlretrieve(url, filename=filename)


html = """
<p>1,点击Create New Project.</p>
<p><img alt="" src="http://img.blog.csdn.net/20130718114827500?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvY2hlbmdnb25nMmRt/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast"/></p>
<p><br>
</br></p>

"""
url = "http://img.blog.csdn.net/20130718114827500?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvY2hlbmdnb25nMmRt/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast"
filename = "output/images/" + md5.hexdigest() + ".jpg"
print(html.replace(url, filename))
