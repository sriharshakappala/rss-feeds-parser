import feedparser

d = feedparser.parse('http://www.symantec.com/xml/rss/listings.jsp?lid=advisories')

print d['feed']['title']            # Print the title of the feed
 
print d.feed.link                   # Resolves relative links
 
print d.feed.subtitle               # Parse escaped html
 
print len(d['entries'])             # See number of entries
 
print d['entries'][0]['title']      # Each entry is a dictionary. Print the first entry
 
print d.entries[0]['link']          # Print the first entry and its link
             
for i in range(len(d['entries'])):  # Print all entries using a for loop
    print d.entries[1]
 
print d.entries[0].updated_parsed   # Parse all date formats
 
print d.version                     # Reports feed type and version
 
print d.headers                     # Full access to all HTTP headers
 
print d.headers.get('content-type') # Get just the content-type
