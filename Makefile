all:

clean:

install:
	mkdir -p $(DESTDIR)/usr/bin
	mkdir -p $(DESTDIR)/usr/share/spiderfoot
	
	cp -r dyn ext modules static setup.py sf.py sfdb.py sflib.py sfscan.py sfwebui.py Dockerfile LICENSE LICENSE.tp README.md Makefile THANKYOU VERSION $(DESTDIR)/usr/share/spiderfoot/
	cp spiderfoot spiderfoot-gui spiderfoot-server $(DESTDIR)/usr/bin/
	
	chown root:root $(DESTDIR)/usr/share/spiderfoot -R
	chown root:root $(DESTDIR)/usr/bin/spiderfoot*
	chmod 755 $(DESTDIR)/usr/share/spiderfoot -R
	chmod 755 $(DESTDIR)/usr/bin/spiderfoot*
