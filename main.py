#!/usr/bin/env python


from modules import cli
from modules import model
from modules import storage

def main():
    cli.hello() # печатает cli
    model.hello() # model
    storage.hello() # storage
    
 

if __name__ == "__main__":
    main()