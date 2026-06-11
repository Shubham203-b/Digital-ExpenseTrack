[app]
title = Digital Expense Tracker
package.name = digitalexpensetracker
package.domain = org.digitalexpensetracker
source.dir = ./app
source.include_exts = py,png,jpg,kv,atlas,ttf,db,ini,spec
presplash.filename = %(source.dir)s/data/images/icon.png
icon.filename = %(source.dir)s/data/images/icon.png
version = 1.0

requirements = python3,kivy==2.3.1,sqlalchemy,python-dateutil,typing_extensions

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True

# Copy db file to app
android.add_src = app

log_level = 2
warn_on_root = 1

[buildozer]
log_level = 2
