from gdata.youtube import service
import codecs

USERNAME = 'amar.kris@gmail.com'
PASSWORD = '*************'
VIDEO_ID = '6qmj5mhDwJQ'

def comments_generator(client, video_id):
    comment_feed = client.GetYouTubeVideoCommentFeed(video_id=video_id)
    while comment_feed is not None:
        for comment in comment_feed.entry:
             yield comment
        next_link = comment_feed.GetNextLink()
        if next_link is None:
             comment_feed = None
        else:
             comment_feed = client.GetYouTubeVideoCommentFeed(next_link.href)

client = service.YouTubeService()
client.ClientLogin(USERNAME, PASSWORD)


outfile = codecs.open('FINAL_noah.txt',"w", encoding='utf-8',)
comment_feed = comments_generator(client, VIDEO_ID)

for comment in comment_feed:
	comment_text = comment.content.text
	comment_text = comment_text.replace('\n', ' ')
	post_date = comment.published.text.split("T")[0]
	outstring = post_date + '$' +' '+ comment_text.decode('utf-8') + '\n'
	outfile.write(outstring)
  	
