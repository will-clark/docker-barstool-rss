One of my favorite websites, Barstool Sports, no longer has an RSS feed, :-(

When I was viewing the source, I noticed the page calls out to an API to retrieve its list of blog posts in JSON, ;-)

I built a little python application to fetch the JSON every 15 minutes, converts it to an RSS format, and exposes it to the web so Feedly can access it;

The application is compiled into Docker image so I drop it onto my Rancher node hosted with Digital Ocean;

Other Notes:

Category 97 is Boston;
The template does some filtering to remove "Barstool Original" video content which I do not enjoy at all;

URL: https://union.barstoolsports.com/v2/stories/category/97?limit=100&page=1

<rss version="2.0">
	<channel>
		<title>Barstool Sports - Boston</title>
		<link>https://www.barstoolsports.com/category/boston</link>
		<description>By The Common Man, For The Common Man</description>
		<image></image>
		<item>
			<title>Really early morning no-coffee notes</title>
			<link>http://scriptingnews.userland.com/backissues/2002/09/29#reallyEarlyMorningNocoffeeNotes</link>
			<description></description>
			<pubDate>Sun, 29 Sep 2002 11:13:10 GMT</pubDate>
			<guid>http://scriptingnews.userland.com/backissues/2002/09/29#reallyEarlyMorningNocoffeeNotes</guid>
		</item>
	</channel>
</rss>