#!/usr/bin/env python3

from pytm.pytm import TM, Server, Database, Dataflow


tm = TM("my test tm")
tm.description = "another test tm"


web = Server("web server")
web.OS = "CloudOS"
web.hardened = True

db = Database("database server")
web.OS = "CentOS"
web.hardened = False

web_and_db = Dataflow(web, db, "web and db")
web_and_db.protocol = "HTTP"

tm.resolve()  
tm.report('Intro', 'Diagram', 'Threats')