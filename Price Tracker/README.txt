1. Find a product that we want to track and get the product URL.
2. Use the BeautifulSoup to Scrape the Product Price
3. Use the requests library to request the HTML page of the product using the URL
4. We need to pass along some headers in order for  the request to return the actual website HTML At minimum we'll need to give our "User-Agent" and "Accept-Language" values in the request header (http://myhttpheader.com)
5. We want to get an email when the price of our product is below a certain value I use smtp module to send an email to myself. The email include the title of the product, the current price and a link to buy the product.