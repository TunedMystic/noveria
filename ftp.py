#!/usr/bin/env python
import os
import sys
import re
import pysftp
import dotenv


if __name__ == "__main__":
  dotenv.read_dotenv()
  
  dirname = os.path.abspath(os.path.dirname(__file__))
  
  host = os.environ.get("SFTP_HOST")
  print "host:", host
  user = os.environ.get("SFTP_USER")
  print "user:", user
  pswd = os.environ.get("SFTP_PASSWORD")
  print "password:", pswd
  source_dir = os.environ.get("SOURCE_DIR")
  print "source_dir:", source_dir
  output_dir = os.environ.get("OUTPUT_DIR")
  print "output_dir:", output_dir
  
  with pysftp.Connection(host, username = user, password = pswd) as sftp:
    with sftp.cd(source_dir):
      try:
        sftp.mkdir(output_dir)
      except:
        pass
      sftp.put_r(localpath = os.path.join(dirname, "output"), remotepath = output_dir)
