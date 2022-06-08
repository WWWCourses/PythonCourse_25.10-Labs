import string
from bs4 import BeautifulSoup as bs
import re


html = '''
<title>Test</title>
<div class="c1 c2" itemprop title='MouvieTitle'>
	<ul>
		<li><a href="/page1.html">page1</a></li>
		<li id="vip"><a href="/page2.html">page2</a></li>
	</ul>
</div>
<div>
	<ul>
		<li>Item1</li>
	</ul>
	<p class="c1">paragraph 1</p>
</div>
<div>
	author: <span>Ahutor Name</span>
</div>
'''
# create BeautifulSoup object, which represents the document as a nested data structure:
soup = bs(html, 'html.parser')

# # find first DIV
# div = soup.div
# # print( dir(div))

# # get title attribute content:
# print(div['title'])

## get all DIVs:
# divs = soup.find_all('div')
# print(divs)

# # get all LI and P elements:
# elements = soup.find_all(re.compile(r'li|p'))
# print(elements)

# # get all elements with class="c1":
# elements = soup.find_all(class_='c1')
# print(elements)

# # get all elements which have 'author' in their contents.
# TODO: why not works
# elements = soup.find_all('div', string=re.compile(r'author'))
# print(elements)

# # find_all works on object scope:
# soup_lis = soup.find_all('li')
# # print(soup_lis)
# first_div_lis = soup.div.find_all('li')
# print(first_div_lis)


second_li = soup.find('li',id='vip')
# # get parent element:
# ul = second_li.parent.parent
# print(ul)


# print(second_li)
# # get previous sibling:
# # TODO: not working
# first_li = second_li.previous_elements

# next(first_li)

# print(f'>{first_li}<')


