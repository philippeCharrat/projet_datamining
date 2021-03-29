#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:13:36 2021
@authors: Philippe CHARRAT & Clement CORNU
@version: 1.1
Usage : Script pour lancer un serveur
Remarque : Faire attention aux autres services pouvant l'utiliser (ex : Apache). Si tel est le cas, stopper le processus (ex : Apache) en cours
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