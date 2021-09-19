# GPU-HUNTER

## Overview
GPU Hunter is a example project for scraping data and messaging via SMS.

## Description
GPU-hunter scrapes links from bestbuy.com to check specific graphics cards (GPU's) to see if they are sold out. If it finds one of the links is in stock, it will text a phone number using Twillo's API.


## Planed Development
As of september 2021, GPU hunter only looks at spefic links. It may be more beneficial to have it go through either a list of specific links or a whole search result on bestbuy.com for links. It would then filter out only ones I want to find.


## Hosted on Heroku
Curently set up to run once an hour on heroku using an addon.