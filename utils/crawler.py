from icrawler.builtin import GoogleImageCrawler

request_word = "скан чека"
num_pic = 300

google = GoogleImageCrawler(storage={'root_dir': r'C:\Users\misha\Desktop\Python\pythonProject1\train\images'},
                            feeder_threads=4, parser_threads=4, downloader_threads=4)
google.crawl(keyword=request_word)