import scrapy

# run spider => scrapy runspider EveryManSpider.py -o movies.json

# this script nevigates to everyman kings cross and return all the movie names and screening times for the movies currently playing at the kings cross cinema,
# in a form of a list of nested dictionaries where the key is the movie name and value is a a dictionary with keys for metadata of the movies starting with a
# list of screening times, the next script will add to it more metadata such as synopsis, rating, genre, etc...


class CinemaSpider(scrapy.Spider):
    name = "movieSpider"
    allowed_domains = ['everymancinema.com']
    start_urls = [
        'https://www.everymancinema.com/kings-cross/film-listings'
    ]

    def parse(self, response):
        moviesContainer = response.css("ul.gridRow.films-1") 
        for movie in moviesContainer:
            # movie data located at li.gridRow.filmItem --> HTML location of the data
            for movie_data in movie.css('div.clearfix'):
                descData = movie_data.css('div.gridCol-s-12.gridCol-m-5.gridCol-l-5.p_rel')
                screening = movie.css('ul.filmTimes')
                    
                if descData.css("h2.filmItemTitle a::text").extract():

                    yield{

                        descData.css("h2.filmItemTitle a::text").extract()[0] : {
                            'screening' : screening.css('a::text').extract()
                        }

                    }
                       

# next step create adiotional script to process the json file making a single dictionary with movies names as keys mapping to another dictionary with
# metadata about the movie.
# Then have the script return more info about each movie, updating the dictionary to add more metadata about the movie;
# genre, rating, synopsis, directors starring actors etc...
               





