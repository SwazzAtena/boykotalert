[app]

# Uygulamanızın adı (boşluk ve özel karakterler içermemeli)
title = BoykotApp

# Uygulamanızın kullandığı Kivy sürümü
kivy_version = 2.1.0

# Uygulamanızın ana Python dosyası (bu dosyanın adı)
package.name = boykotapp

# Uygulama ana ekranı (Python dosyasının adı, .py uzantısı olmadan)
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = assets/*,images/*.png
source.exclude_patterns = licenses.txt, *.pyc, .gitignore
