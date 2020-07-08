# async-crawler
## This web crawler will extract all books information asynchronously from books.toscrape.com. Afterwards it will let the user filter it by name, rating, price or topic

### Warning: 
In this project I applied asynchronous python development to make the 50 requests 'simultaneously' that in theory would be SO MUCH FASTER than doing one by one. 
Because we get all the books so fast, we dont need to use a database, just a big python list that gets deleted when the program ends, saving some memory.
But the webpage wouldn´t accept too many requests as a security measure, but on bigger webpages this will totally work.
