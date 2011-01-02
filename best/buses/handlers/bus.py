#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4


from rapidsms.contrib.handlers.handlers.keyword import KeywordHandler
from buses.models import *

class BestHandler(KeywordHandler):
    keyword = "route"

    def help(self):
        self.respond("Send route <bus_no>")

    def handle(self, text):
        bus_no = text.strip()
        a = Atlas.objects.filter(route__iexact=bus_no)
        if len(a) < 1:
            self.respond("Did not find that bus number. Sorry.")
        else:
            a = a[0]
            src = a.src
            first_src = a.first_src
            last_src = a.last_src
            dest = a.dest
            first_dest = a.first_dest
            last_dest = a.last_dest
            schedule = a.schedule
            ret = "%s(%s-%s) to %s(%s-%s) from %s" % (src, str(first_src), str(last_src), dest, str(first_dest), str(last_dest), schedule) 
            self.respond(ret)


