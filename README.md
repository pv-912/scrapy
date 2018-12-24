##### Terminal commands for python-scrapy
-  `scray shell <url>` Provide us the response shell we can use to access the data from the page
- `print(response.text)` Print the whole page content
- `response.css(div.author)` Return inside object of that div
- `response.css(div.author).extract()` Return actual html selected data 
- `response.css(div.author::text).extract()` Return array of text only of that element 
- `response.css(div.author::text)[0].extract()` Return string of text only of that element 


#### To run python-scrapy in python file
- `scrapy genspider <spider-name> <domain-name-url>` after running this a file name <spider-name>.py will be created in the same directory
- `scrapy runspider filename.py` To run the file
- `scrapy runspider filename.py -o file-name.json` To save the file as file-name.json
- `more file-name.json` To see file content

#### scraping dynamic javascript webpages
- `sudo apt install docker.io` install docker
- `sudo docker pull scrapyhub/splash` download splash js engine
- `docker run -p 8050:8050 scrapyhub/splash` run splash at port : 8050
- `pip install scrapy-splash` install interactive display plugin
- 