#!/usr/bin/python3

from urllib.parse import urlsplit
import re, itertools
from glob import glob 

def urls():
    with open('externallinks_en.csv') as fp:
        for i, line in enumerate(fp.readlines()):
            try:


                url = urlsplit(line.split()[2].strip())
                if url:
                    yield url#.split('/')[0]
            except Exception as ex:
                print(ex)

# www = re.compile('^www[^\.]*\.')

def main():
    for url in urls(): #itertools.islice(urls(), 1000):
        print(url.netloc)

		
def profiling():
	import profile, pstats
	profile.run('main()', 'stats')
	p = pstats.Stats('stats')
	p.sort_stats(pstats.SortKey.TIME, pstats.SortKey.CUMULATIVE).print_stats(20)
	

if __name__ == '__main__':
    main()

