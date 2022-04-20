#!/usr/bin/env python

import sys
sys.path.append('modules')
sys.path.append('..')

import config

import boost
import cef
import icu
import openssl
import curl
import websocket
import v8
import html2
import hunspell
import glew

def make():
  boost.make()
  cef.make()
  icu.make()
  openssl.make()
  v8.make()
  html2.make()
  hunspell.make()
  glew.make()
  if config.check_option("module", "mobile"):
    curl.make()
    websocket.make()
  return
