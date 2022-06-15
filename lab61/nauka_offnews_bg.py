from bs4 import BeautifulSoup as bs
import re

def get_max_page(div):
	# get all children (including text, commetnt, HTML elements)
	# print(len(list(div.children)))
	# print(len(list(div.contents)))
	# last_child = list(div.children)[-1]

	# # get 2nd a element: using CSS Selectors:
	# second_a = div.select('a:nth-of-type(2)')
	# print(second_a)

	# get last HTML child - variant 1
	last_a_child = div.find_all('a')[-1]
	# print(last_a_child)

	href = last_a_child['href']
	print(href)

	# get all digits from href:
	rx = re.compile(r'(\d+)')
	m = rx.search(href)
	if m:
		return m.group(1)
	else:
		return 0

	# print(href[-1:-4:-1])



html = """

	<div class="pageBox bb3y">
				<a href="?page_which=0" title="« Първа страница"> « Първа </a>
				<span class="extend"> ... </span>
				<span class="extend"> ... </span>
				<span class="extend"> ... </span>
				<span class="extend"> ... </span>
				<span class="extend"> ... </span>
				<a class="prev" href="?page_which=10" title="Предишна страница">«</a>                                                                <a href="?page_which=0" title="Списък с новини от &quot;Космология&quot; страница 01 ">01</a><a href="?page_which=20" title="Списък с новини от &quot;Космология&quot; страница 02 ">02</a><a href="?page_which=40" title="Списък с новини от &quot;Космология&quot; страница 03 ">03</a><a href="?page_which=60" title="Списък с новини от &quot;Космология&quot; страница 04 ">04</a><a href="?page_which=80" title="Списък с новини от &quot;Космология&quot; страница 05 ">05</a><a href="?page_which=100" title="Списък с новини от &quot;Космология&quot; страница 06 ">06</a>
				<a class="next" href="?page_which=50" title="Следваща страница">»</a>                                                         <span class="extend"> ... </span>
				<a href="?page_which=234" title="Последна страница »"> Последна » </a>
	</div>
"""
soup = bs(html, 'html.parser')
div = soup.find(class_="pageBox")

# print(div)

max_page = get_max_page(div)
print(max_page)