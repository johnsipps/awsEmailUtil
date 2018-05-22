# -*- coding: utf-8 -*-
"""
Created on Wed May 23 03:56:10 2018

@author: John
"""

def lambda_handler(event,context):
    import jemail
    jcall=jemail.Jemail()
    jcall.main()   
