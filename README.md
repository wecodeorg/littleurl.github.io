
# [LITTLE URL](https://littleurl.tech) &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/littleurl/littleurl.github.io/blob/master/LICENSE) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/littleurl/littleurl.github.io/) ![Little url shotner](https://github.com/littleurl/littleurl.github.io/workflows/Little%20url%20shotner/badge.svg) <img alt="github actions" src="https://img.shields.io/badge/-Github_Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white" />
**(Makes your URL Short)**

The first url shortner for personal use build with (python+Github Actions) 

## How it work's ?
It works as a url redirector the default domain is set inside the [short.py](https://github.com/littleurl/littleurl.github.io/blob/master/short.py) ie.littleurl.tech and CNAME File. The custom short url are to be placed in [urls.json](https://github.com/littleurl/littleurl.github.io/blob/master/urls.json) file which could be generated with our [custom JSON Generator](https://littleurl.netlify.app/#jsongenrator). As soon as the JSON file is edited with New url, github Actions does its job [little url shortner workflow](https://github.com/littleurl/littleurl.github.io/actions?query=workflow%3A%22Little+url+shotner%22) starts running and a new html file is generated in [gh-pages branch](https://github.com/littleurl/littleurl.github.io/tree/gh-pages) with the url redirect. 

## Requirments (To set Your own)
* 1)Github Account.
* 2)Custom domain name.

## Examples
* Original url:-https://drive.google.com/file/d/1coDzFd1liCH4CUSs0GPv7UiBpSEVcxhk/view?usp=sharing
* Shorten url:- https://littleurl.tech/comvis
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
* Original url:-https://www.huffpost.com/entry/jiff-the-dog-wins-halloween_n_56327e41e4b00aa54a4d7a89?ncid=fcbklnkushpmg00000022&utm_content=buffer83279&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer&guccounter=1
* Shorten url:-https://littleurl.tech/jiffthedog

## Purpose
The main purpose of this repository is to make use of github actions to make this task automated , making it faster and easier to use.

### License
Littleurl is [MIT licensed](./LICENSE).
