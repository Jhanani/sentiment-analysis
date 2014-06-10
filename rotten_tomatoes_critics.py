from rottentomatoes import RT
import time

rt = RT()
#movies = ['fight club','gravity','toy story 3','american hustle','skyfall','jack and jill','basic instinct 2','white out','lost souls','babylon','argo','bears','her','up','a beautiful mind','braveheart','the hurt locker','gambit','paranoia','getaway']
movies =[line.strip('\n') for line in open('movies.txt')]
f = open('reviews-date.txt','w')
count = 0
for u in movies:
	movlst = rt.search(u, page_limit=1)
	if movlst:
		if movlst[0][u'id'] != '':
			review = rt.info(movlst[0][u'id'],'reviews')
			review.viewkeys() 
			rlt = review[u'reviews'] #review is a dict, value of each key is list, each list element is a dict
			for a in rlt:
				f.write(a[u'quote']+'\t'+a[u'date']+'\n')
				f2.write(a[u'date']+'\n')
				count = count+1
				#print a[u'quote']
			if len(rlt)==0: 
				print u 
			else: 
				print count
		else:
			print u
	else:
		print u
	time.sleep(5)
f.close()