#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import argparse
import sys, os, re


def other_type(url):
	other = url.lower()
	#input username & password
	other_value = {
	"paloalto":"user:passwd"
	}
	if other_value[other]:
		return other_value[other]
	else:
		return False