<rss version="2.0">
    <channel>
        <title>Barstool Sports - Boston</title>
        <link>https://www.barstoolsports.com/category/boston</link>
        <description>By The Common Man, For The Common Man</description>
        <image></image>
        %for blog in blogs:
            %if blog['type'] in ['standard_post','gallery']:
                <item>
                    <title>${blog['title']}</title>
                    <link>${blog['url']}</link>
                    <pubDate>${blog['date']}</pubDate>
                    <guid>${blog['url']}</guid>
                </item>
            %endif
        %endfor
    </channel>
</rss>
