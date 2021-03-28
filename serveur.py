#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:39:48 2021

@author: philippe
"""

"Démarrage du serveur web pour la partie frontend du projet"

import http.server 
port = 80
address = ("",port)
server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]
httpd = server(address,handler)

print("Serveur démarré")
httpd.serve_forever()