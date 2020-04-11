from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv
my_url='https://www.nytimes.com/'

#opening connection and obtaining url
uClient = uReq(my_url)
page_html=uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html,"html.parser")

#to get each news and the contents on new york times
asset_wrapper = page_soup.findAll("div",{"class":"css-1ee8y2t assetWrapper"})

filename="newyorktimes.csv"
f = csv.writer(open('newyorktimes.csv', 'w'))

f.writerow(['podheader', 'poddescription', 'newsheader', 'multiline-newsdescription', 'singleline-newsdescription'])

for container in asset_wrapper:
#to get the header of podcasts and arguments on new york times
	asset_podh = container.findAll("div",{"class":"css-1064d4e esl82me1"})
	for ast in asset_podh:
		name=ast.text
		print("header of pods: "+name)
		f.writerow([name])
#to get the short description of podcasts and arguments on new york times
	asset_podd=container.findAll("p",{"class":"css-gs67ux e1n8kpyg0"})
	for dsc in asset_podd:
		desc=dsc.text
		print("desciption of pods: "+desc)
		f.writerow(['', desc])
	
#to get header of main news below podcasts
	containerh_mainnews=container.findAll("div",{"class":"css-1ez5fsm esl82me1"})
	for hd in containerh_mainnews:
		desc_mainnews=hd.text
		print("main news header: "+desc_mainnews)
		f.writerow(['', '',desc_mainnews])

#to get header description of main news below podcasts which has multi-line description
	containerd_mainnewsml=container.findAll("ul",{"class":"css-ip5ca7 e1n8kpyg1"})
	for desml in containerd_mainnewsml:
		desc_mainnews_multiline=desml.text
		print("desc of multiline: "+desc_mainnews_multiline)
		f.writerow(['','','',desc_mainnews_multiline])

#to get header description of main news below podcasts which has single-line description
	containerd_mainnewssl=container.findAll("p",{"class":"css-1pfq5u e1n8kpyg0"})
	for descsl in containerd_mainnewssl:
		desc_mainnews_singleline=descsl.text
		print("desc of singleline: "+desc_mainnews_singleline)
		f.writerow(['','','','',desc_mainnews_singleline])
		